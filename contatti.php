<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=UTF-8');
header('Cache-Control: no-store, no-cache, must-revalidate');
header('X-Content-Type-Options: nosniff');

// Lingua delle risposte: quella della pagina da cui arriva il modulo (campo nascosto "lang").
$lang = in_array($_POST['lang'] ?? '', ['it', 'en', 'de'], true) ? $_POST['lang'] : 'it';
const MESSAGES = [
    'method'    => ['it' => 'Metodo non consentito.', 'en' => 'Method not allowed.', 'de' => 'Methode nicht erlaubt.'],
    'too_long'  => ['it' => 'Messaggio troppo lungo.', 'en' => 'Message too long.', 'de' => 'Nachricht zu lang.'],
    'forbidden' => ['it' => 'Richiesta non autorizzata.', 'en' => 'Request not authorised.', 'de' => 'Anfrage nicht erlaubt.'],
    'received'  => ['it' => 'Messaggio ricevuto.', 'en' => 'Message received.', 'de' => 'Nachricht erhalten.'],
    'brand'     => ['it' => 'Struttura non valida.', 'en' => 'Invalid property.', 'de' => 'Ungültige Unterkunft.'],
    'name'      => ['it' => 'Inserisci un nome valido (2–100 caratteri).', 'en' => 'Please enter a valid name (2–100 characters).', 'de' => 'Bitte geben Sie einen gültigen Namen ein (2–100 Zeichen).'],
    'email'     => ['it' => 'Inserisci un indirizzo email valido.', 'en' => 'Please enter a valid email address.', 'de' => 'Bitte geben Sie eine gültige E-Mail-Adresse ein.'],
    'phone'     => ['it' => 'Inserisci un telefono valido.', 'en' => 'Please enter a valid phone number.', 'de' => 'Bitte geben Sie eine gültige Telefonnummer ein.'],
    'message'   => ['it' => 'Il messaggio deve contenere tra 10 e 5000 caratteri.', 'en' => 'The message must be between 10 and 5000 characters.', 'de' => 'Die Nachricht muss zwischen 10 und 5000 Zeichen lang sein.'],
    'privacy'   => ['it' => 'Devi accettare l’informativa sulla privacy.', 'en' => 'You must accept the privacy policy.', 'de' => 'Bitte akzeptieren Sie die Datenschutzerklärung.'],
    'wait'      => ['it' => 'Hai già inviato un messaggio. Riprova tra pochi secondi.', 'en' => 'You have just sent a message. Please try again in a few seconds.', 'de' => 'Sie haben gerade eine Nachricht gesendet. Bitte versuchen Sie es in ein paar Sekunden erneut.'],
    'down'      => ['it' => 'Servizio non disponibile. Contattaci telefonicamente.', 'en' => 'Service unavailable. Please contact us by phone.', 'de' => 'Dienst nicht verfügbar. Bitte kontaktieren Sie uns telefonisch.'],
    'failed'    => ['it' => 'Invio non riuscito. Riprova o contattaci telefonicamente.', 'en' => 'Sending failed. Please try again or contact us by phone.', 'de' => 'Senden fehlgeschlagen. Bitte erneut versuchen oder uns telefonisch kontaktieren.'],
    'sent'      => ['it' => 'Messaggio inviato correttamente. Ti risponderemo appena possibile.', 'en' => 'Message sent. We will reply as soon as possible.', 'de' => 'Nachricht gesendet. Wir antworten Ihnen so bald wie möglich.'],
];

function respond(int $status, bool $success, string $key): void {
    global $lang;
    http_response_code($status);
    echo json_encode(['success' => $success, 'message' => MESSAGES[$key][$lang]], JSON_UNESCAPED_UNICODE);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, false, 'method');
}
if ((int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 16000) {
    respond(413, false, 'too_long');
}

// Il form si può inviare solo dalla stessa origine; l'header Origin può essere assente.
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '') {
    $originHost = parse_url($origin, PHP_URL_HOST);
    $siteHost = explode(':', $_SERVER['HTTP_HOST'] ?? '')[0];
    if (!is_string($originHost) || !hash_equals(strtolower($siteHost), strtolower($originHost))) {
        respond(403, false, 'forbidden');
    }
}

$brand = trim((string)($_POST['brand'] ?? ''));
$nome = trim((string)($_POST['nome'] ?? ''));
$email = trim((string)($_POST['email'] ?? ''));
$telefono = trim((string)($_POST['telefono'] ?? ''));
$messaggio = trim((string)($_POST['messaggio'] ?? ''));
$privacy = (string)($_POST['privacy'] ?? '');
$website = trim((string)($_POST['website'] ?? ''));

// Il campo nascosto compilato è un segnale di spam: non spediamo.
if ($website !== '') {
    respond(200, true, 'received');
}
if (!in_array($brand, ['col-gentile', 'la-farie'], true)) {
    respond(422, false, 'brand');
}
if (strlen($nome) < 2 || strlen($nome) > 100 || preg_match('/[\r\n]/', $nome)) {
    respond(422, false, 'name');
}
if (strlen($email) > 254 || !filter_var($email, FILTER_VALIDATE_EMAIL) || preg_match('/[\r\n]/', $email)) {
    respond(422, false, 'email');
}
if (strlen($telefono) > 40 || preg_match('/[\r\n]/', $telefono)) {
    respond(422, false, 'phone');
}
if (strlen($messaggio) < 10 || strlen($messaggio) > 5000) {
    respond(422, false, 'message');
}
if ($privacy !== '1') {
    respond(422, false, 'privacy');
}

// Limitazione semplice per sessione (non sostituisce la protezione antispam del server).
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
$lastSent = (int)($_SESSION['last_contact_sent'] ?? 0);
if ($lastSent > 0 && time() - $lastSent < 30) {
    respond(429, false, 'wait');
}

$recipient = $brand === 'la-farie'
    ? (getenv('FARIE_CONTACT_EMAIL') ?: 'info@albergodiffusosocchieve.it')
    : 'info@albergodiffusosocchieve.it';
if (!filter_var($recipient, FILTER_VALIDATE_EMAIL)) {
    error_log('Contatti: destinatario non valido');
    respond(500, false, 'down');
}
$subject = $brand === 'la-farie'
    ? 'Richiesta dal sito - La Farie'
    : 'Richiesta dal sito - Col Gentile';
$clean = static function (string $value): string {
    return strip_tags(str_replace("\0", '', $value));
};

$body = "Nuova richiesta dal sito web\n"
    . "Struttura: " . ($brand === 'la-farie' ? 'La Farie' : 'Col Gentile') . "\n"
    . "Nome: " . $clean($nome) . "\n"
    . "Email: " . $email . "\n"
    . "Telefono: " . $clean($telefono) . "\n"
    . "Lingua del sito: " . strtoupper($lang) . "\n"
    . "Privacy: accettata\n\n"
    . "Messaggio:\n" . $clean($messaggio) . "\n";
$headers = [
    'From' => 'Sito Albergo Diffuso <noreply@albergodiffusosocchieve.it>',
    'Reply-To' => $email,
    'Content-Type' => 'text/plain; charset=UTF-8',
    'MIME-Version' => '1.0',
    'X-Mailer' => 'PHP'
];

// mail() deve essere configurato sul server PHP: il successo non garantisce la consegna.
if (!@mail($recipient, $subject, $body, $headers)) {
    error_log('Contatti: mail() non riuscita per ' . $brand);
    respond(500, false, 'failed');
}

$_SESSION['last_contact_sent'] = time();
respond(200, true, 'sent');
