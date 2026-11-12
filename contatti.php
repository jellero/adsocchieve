<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=UTF-8');
header('Cache-Control: no-store, no-cache, must-revalidate');
header('X-Content-Type-Options: nosniff');

function respond(int $status, bool $success, string $message): void {
    http_response_code($status);
    echo json_encode(['success' => $success, 'message' => $message], JSON_UNESCAPED_UNICODE);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, false, 'Metodo non consentito.');
}
if ((int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 16000) {
    respond(413, false, 'Messaggio troppo lungo.');
}

// Il form si può inviare solo dalla stessa origine; l'header Origin può essere assente.
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '') {
    $originHost = parse_url($origin, PHP_URL_HOST);
    $siteHost = explode(':', $_SERVER['HTTP_HOST'] ?? '')[0];
    if (!is_string($originHost) || !hash_equals(strtolower($siteHost), strtolower($originHost))) {
        respond(403, false, 'Richiesta non autorizzata.');
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
    respond(200, true, 'Messaggio ricevuto.');
}
if (!in_array($brand, ['col-gentile', 'la-farie'], true)) {
    respond(422, false, 'Struttura non valida.');
}
if (strlen($nome) < 2 || strlen($nome) > 100 || preg_match('/[\r\n]/', $nome)) {
    respond(422, false, 'Inserisci un nome valido (2–100 caratteri).');
}
if (strlen($email) > 254 || !filter_var($email, FILTER_VALIDATE_EMAIL) || preg_match('/[\r\n]/', $email)) {
    respond(422, false, 'Inserisci un indirizzo email valido.');
}
if (strlen($telefono) > 40 || preg_match('/[\r\n]/', $telefono)) {
    respond(422, false, 'Inserisci un telefono valido.');
}
if (strlen($messaggio) < 10 || strlen($messaggio) > 5000) {
    respond(422, false, 'Il messaggio deve contenere tra 10 e 5000 caratteri.');
}
if ($privacy !== '1') {
    respond(422, false, 'Devi accettare l’informativa sulla privacy.');
}

// Limitazione semplice per sessione (non sostituisce la protezione antispam del server).
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
$lastSent = (int)($_SESSION['last_contact_sent'] ?? 0);
if ($lastSent > 0 && time() - $lastSent < 30) {
    respond(429, false, 'Hai già inviato un messaggio. Riprova tra pochi secondi.');
}

$recipient = $brand === 'la-farie'
    ? (getenv('FARIE_CONTACT_EMAIL') ?: 'info@albergodiffusosocchieve.it')
    : 'info@albergodiffusosocchieve.it';
if (!filter_var($recipient, FILTER_VALIDATE_EMAIL)) {
    error_log('Contatti: destinatario non valido');
    respond(500, false, 'Servizio non disponibile. Contattaci telefonicamente.');
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
    respond(500, false, 'Invio non riuscito. Riprova o contattaci telefonicamente.');
}

$_SESSION['last_contact_sent'] = time();
respond(200, true, 'Messaggio inviato correttamente. Ti risponderemo appena possibile.');
