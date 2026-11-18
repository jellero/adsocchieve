"""Traduzioni del sito: inglese (en) e tedesco (de).

UI      testi dell'interfaccia usati in build.py: chiave = testo italiano, valore = (inglese, tedesco).
        I segnaposto tra graffe ({n}, {b}...) vanno lasciati uguali.
CONTENT contenuti di data.py tradotti, per id: si sovrascrivono solo i campi indicati.

Se si cambia un testo italiano in build.py o se ne aggiunge uno, build.py elenca alla fine
quelli rimasti senza traduzione."""

UI = {
    # ------------------------------------------------------------ homepage: La Farie
    "Scopri La Farie, affittacamere a Lungis": ("Discover La Farie, guesthouse in Lungis", "La Farie entdecken, Gästehaus in Lungis"),
    "Affittacamere · Lungis": ("Guesthouse · Lungis", "Gästehaus · Lungis"),
    "Camere con bagno privato e giardino": ("Rooms with private bathrooms and a garden", "Zimmer mit eigenem Bad und Garten"),
    "Scopri le camere": ("Explore the rooms", "Zimmer entdecken"),
    "Case e appartamenti vacanza nei borghi di Socchieve e La Farie, affittacamere a Lungis. Ospitalità autentica in Carnia, vicino alle Dolomiti Friulane.": (
        "Holiday houses and apartments in the villages of Socchieve, plus La Farie, a guesthouse in Lungis. Authentic stays in Carnia, near the Friulian Dolomites.",
        "Ferienhäuser und Ferienwohnungen in den Dörfern von Socchieve sowie La Farie, ein Gästehaus in Lungis. Authentisch übernachten in Karnien, nahe den Friauler Dolomiten."),
    "La Farie a Lungis: casa in pietra con balconi in legno": (
        "La Farie in Lungis: stone house with wooden balconies",
        "La Farie in Lungis: Steinhaus mit Holzbalkonen"),
    "Un'altra ospitalità in Carnia": ("Another way to stay in Carnia", "Eine andere Art, in Karnien zu wohnen"),
    "La Farie, <em>affittacamere a Lungis.</em>": (
        "La Farie, <em>guesthouse in Lungis.</em>",
        "La Farie, <em>Gästehaus in Lungis.</em>"),
    "A Lungis, nel comune di Socchieve, La Farie è un affittacamere in una casa carnica ristrutturata. Camere con bagno privato, giardino e colazione disponibile: un'alternativa alle case vacanza Col Gentile, gestita dallo stesso Albergo Diffuso Socchieve.": (
        "In Lungis, near Socchieve, La Farie is a guesthouse in a restored traditional Carnic house. Rooms with private bathrooms, a garden and breakfast available: a different way to stay from the Col Gentile holiday homes, run by the same Albergo Diffuso Socchieve.",
        "In Lungis bei Socchieve ist La Farie ein Gästehaus in einem restaurierten karnischen Haus. Zimmer mit eigenem Bad, Garten und Frühstücksangebot: eine Alternative zu den Ferienwohnungen von Col Gentile, geführt vom selben Albergo Diffuso Socchieve."),
    "Colazione disponibile": ("Breakfast available", "Frühstück verfügbar"),
    "Giardino": ("Garden", "Garten"),
    "Parcheggio privato gratuito": ("Free private parking", "Kostenlose Privatparkplätze"),
    "Scopri camere e servizi": ("Explore rooms and amenities", "Zimmer und Ausstattung entdecken"),
    "Disponibilità La Farie": ("La Farie availability", "Verfügbarkeit La Farie"),
    "Case e appartamenti vacanza a Socchieve, in Carnia: {n} alloggi nei borghi e La Farie, affittacamere a Lungis. Prenotazione diretta.": (
        "Holiday homes and apartments in Socchieve, Carnia: {n} places to stay across the villages, plus La Farie guesthouse in Lungis. Book direct.",
        "Ferienhäuser und Ferienwohnungen in Socchieve, Karnien: {n} Unterkünfte in den Dörfern und La Farie Gästehaus in Lungis. Direkt buchen."),

    # ------------------------------------------------------------ navigazione e layout
    "Le case": ("The houses", "Die Häuser"),
    "I borghi": ("The villages", "Die Dörfer"),
    "Esperienze": ("Experiences", "Erlebnisse"),
    "Benessere": ("Wellness", "Wellness"),
    "Contatti": ("Contact", "Kontakt"),
    "Lingua": ("Language", "Sprache"),
    "Vai al contenuto": ("Skip to content", "Zum Inhalt"),
    "Albergo Diffuso Socchieve Col Gentile, home": ("Albergo Diffuso Socchieve Col Gentile, home", "Albergo Diffuso Socchieve Col Gentile, Startseite"),
    "Principale": ("Main", "Hauptmenü"),
    "Prenota": ("Book", "Buchen"),
    "Apri menu": ("Open menu", "Menü öffnen"),
    "Chiudi menu": ("Close menu", "Menü schließen"),
    "Menu mobile": ("Mobile menu", "Mobiles Menü"),
    "Verifica disponibilità": ("Check availability", "Verfügbarkeit prüfen"),
    "Sito realizzato da": ("Website by", "Website von"),
    "La porta delle Dolomiti Friulane.": ("The gateway to the Friulian Dolomites.", "Das Tor zu den Friauler Dolomiten."),
    "Tutte le case": ("All houses", "Alle Häuser"),
    "Benessere: sauna e bagno di bosco": ("Wellness: sauna and forest bathing", "Wellness: Sauna und Waldbaden"),
    "Il territorio": ("The area", "Die Umgebung"),
    "Contatti e come arrivare": ("Contact and getting here", "Kontakt und Anreise"),
    "P.I.": ("VAT no.", "USt-IdNr."),
    "Cookie": ("Cookies", "Cookies"),
    "Preferenze cookie": ("Cookie preferences", "Cookie-Einstellungen"),
    "Condizioni di prenotazione": ("Booking terms", "Buchungsbedingungen"),
    "Galleria fotografica": ("Photo gallery", "Fotogalerie"),
    "Chiudi galleria": ("Close gallery", "Galerie schließen"),
    "Foto precedente": ("Previous photo", "Vorheriges Foto"),
    "Foto successiva": ("Next photo", "Nächstes Foto"),
    "Chiama": ("Call", "Anrufen"),
    "Percorso": ("Breadcrumb", "Brotkrümelnavigation"),
    "Prenota online": ("Book online", "Online buchen"),
    "Prenota La Farie": ("Book La Farie", "La Farie buchen"),
    "Chiedi disponibilità": ("Ask about availability", "Verfügbarkeit anfragen"),

    # ------------------------------------------------------------ modulo contatti
    "Scrivi a <em>La Farie.</em>": ("Write to <em>La Farie.</em>", "Schreiben Sie <em>La Farie.</em>"),
    "Il messaggio sarà identificato come richiesta per La Farie e non per gli appartamenti Col Gentile.": (
        "Your message will be marked as an enquiry for La Farie, not for the Col Gentile apartments.",
        "Ihre Nachricht wird als Anfrage für La Farie gekennzeichnet, nicht für die Ferienwohnungen von Col Gentile."),
    "Richiedi informazioni <em>sul soggiorno.</em>": ("Ask us <em>about your stay.</em>", "Fragen Sie uns <em>zu Ihrem Aufenthalt.</em>"),
    "Per informazioni su case, periodi e soggiorni a Socchieve, inviaci un messaggio. Per la disponibilità aggiornata utilizza sempre il motore di prenotazione.": (
        "For information about the houses, dates and stays in Socchieve, send us a message. For up-to-date availability, always use the booking engine.",
        "Für Informationen zu Häusern, Reisezeiten und Aufenthalten in Socchieve schreiben Sie uns. Die aktuelle Verfügbarkeit sehen Sie immer im Buchungssystem."),
    "I campi contrassegnati con * sono obbligatori. La richiesta non costituisce una prenotazione.": (
        "Fields marked with * are required. Sending an enquiry is not a booking.",
        "Mit * gekennzeichnete Felder sind Pflichtfelder. Eine Anfrage ist keine Buchung."),
    "Lascia vuoto questo campo": ("Leave this field empty", "Dieses Feld leer lassen"),
    "Nome e cognome": ("Full name", "Vor- und Nachname"),
    "Il tuo nome": ("Your name", "Ihr Name"),
    "nome@esempio.it": ("name@example.com", "name@beispiel.de"),
    "Telefono (facoltativo)": ("Phone (optional)", "Telefon (optional)"),
    "Messaggio": ("Message", "Nachricht"),
    "Raccontaci la tua richiesta...": ("Tell us what you need...", "Wie können wir helfen?"),
    "Ho letto l'<a href=\"{href}\" target=\"_blank\" rel=\"noopener noreferrer\">informativa sulla privacy</a> e acconsento al trattamento dei dati per rispondere alla mia richiesta.": (
        "I have read the <a href=\"{href}\" target=\"_blank\" rel=\"noopener noreferrer\">privacy policy</a> and agree to my data being processed to answer my enquiry.",
        "Ich habe die <a href=\"{href}\" target=\"_blank\" rel=\"noopener noreferrer\">Datenschutzerklärung</a> gelesen und bin mit der Verarbeitung meiner Daten zur Beantwortung meiner Anfrage einverstanden."),
    "Invia il messaggio": ("Send message", "Nachricht senden"),
    "Risposta visibile qui dopo l'invio": ("The result will appear here", "Das Ergebnis erscheint hier"),

    # ------------------------------------------------------------ blocchi comuni
    "Fino a {n} ospiti": ("Up to {n} guests", "Bis zu {n} Gäste"),
    "{n} stelle": ("{n} stars", "{n} Sterne"),
    "{n} stelle, ": ("{n} stars, ", "{n} Sterne, "),
    "circa {t}": ("about {t}", "ca. {t}"),
    "{n}, {label} a {b}, Carnia": ("{n}, {label} in {b}, Carnia", "{n}, {label} in {b}, Karnien"),
    "Filtra le residenze": ("Filter the houses", "Häuser filtern"),
    "Tutti i borghi": ("All villages", "Alle Dörfer"),
    "Ogni capienza": ("Any size", "Jede Größe"),
    "2–8 posti": ("2–8 guests", "2–8 Gäste"),
    "9–16 posti": ("9–16 guests", "9–16 Gäste"),
    "Oltre 16": ("Over 16", "Über 16"),
    "Scorri per vedere tutte le case": ("Swipe to see all the houses", "Wischen, um alle Häuser zu sehen"),
    "Nessuna casa con questi filtri. Prova un altro borgo o un'altra capienza.": (
        "No houses match these filters. Try another village or group size.",
        "Kein Haus passt zu diesen Filtern. Versuchen Sie ein anderes Dorf oder eine andere Gruppengröße."),
    "Date, prezzi e disponibilità in tempo reale": ("Live dates, prices and availability", "Termine, Preise und Verfügbarkeit in Echtzeit"),
    "Prenoti direttamente sul sistema ufficiale Col Gentile, senza intermediari.": (
        "Book directly on the official Col Gentile system, with no middlemen.",
        "Sie buchen direkt im offiziellen Buchungssystem von Col Gentile, ohne Vermittler."),
    "Date, prezzi e disponibilità in tempo reale sul sistema ufficiale di prenotazione Col Gentile.": (
        "Live dates, prices and availability on the official Col Gentile booking system.",
        "Termine, Preise und Verfügbarkeit in Echtzeit im offiziellen Buchungssystem von Col Gentile."),
    "Richiesta informazioni: ": ("Enquiry: ", "Anfrage: "),
    "Scrivici": ("Write to us", "Schreiben Sie uns"),
    "Apri foto {i} di {n}": ("Open photo {i} of {n}", "Foto {i} von {n} öffnen"),
    "{label}, foto {i}": ("{label}, photo {i}", "{label}, Foto {i}"),
    "Ambiente {i}": ("Room {i}", "Raum {i}"),
    "Tour virtuale": ("Virtual tour", "Virtueller Rundgang"),
    "Entra in casa, a 360°": ("Step inside, in 360°", "Treten Sie ein – in 360°"),
    "Anteprima del tour virtuale di {n}": ("Preview of the virtual tour of {n}", "Vorschau des virtuellen Rundgangs durch {n}"),
    "Avvia il tour virtuale a 360 gradi": ("Start the 360-degree virtual tour", "Virtuellen 360-Grad-Rundgang starten"),
    "Avvia il tour": ("Start the tour", "Rundgang starten"),
    "{n} ambienti da esplorare · trascina per guardarti intorno": ("{n} rooms to explore · drag to look around", "{n} Räume zum Entdecken · ziehen, um sich umzusehen"),
    "Il borgo di {n}": ("The village of {n}", "Das Dorf {n}"),
    "m s.l.m.": ("m a.s.l.", "m ü. M."),
    "Frazione di Socchieve": ("Hamlet of Socchieve", "Ortsteil von Socchieve"),

    # ------------------------------------------------------------ pagina casa
    "Tour 360°": ("360° tour", "360°-Rundgang"),
    "Gli appartamenti": ("The apartments", "Die Wohnungen"),
    "Prenota tutta la casa o un solo appartamento": ("Book the whole house or a single apartment", "Buchen Sie das ganze Haus oder eine einzelne Wohnung"),
    "Planimetria": ("Floor plan", "Grundriss"),
    "Planimetria di {n}": ("Floor plan of {n}", "Grundriss von {n}"),
    "Servizi": ("Amenities", "Ausstattung"),
    "Appartamenti": ("Apartments", "Wohnungen"),
    "Ambiente unico": ("Single open space", "Einraum"),
    "Camere": ("Bedrooms", "Schlafzimmer"),
    "Camera": ("Bedroom", "Schlafzimmer"),
    "{n} a {b}, Carnia": ("{n} in {b}, Carnia", "{n} in {b}, Karnien"),
    "{label} a {b} · Carnia": ("{label} in {b} · Carnia", "{label} in {b} · Karnien"),
    "Posti letto": ("Beds", "Betten"),
    "Classificazione": ("Rating", "Klassifizierung"),
    "Tipologia": ("Type", "Art"),
    "Foto": ("Photos", "Fotos"),
    "{c} foto di {n}": ("{c} photos of {n}", "{c} Fotos von {n}"),
    "Il borgo": ("The village", "Das Dorf"),
    "{b}, frazione di Socchieve": ("{b}, a hamlet of Socchieve", "{b}, ein Ortsteil von Socchieve"),
    "Scopri {b}: sentieri, locali e cosa fare": ("Discover {b}: trails, places to eat and things to do", "{b} entdecken: Wanderwege, Lokale und Aktivitäten"),
    "Codice identificativo nazionale (CIN)": ("National identification code (CIN)", "Nationaler Identifikationscode (CIN)"),
    "Indirizzo": ("Address", "Adresse"),
    "Comune": ("Municipality", "Gemeinde"),
    "Ospiti": ("Guests", "Gäste"),
    "fino a {n}": ("up to {n}", "bis zu {n}"),
    "Categoria": ("Category", "Kategorie"),
    "Nella stessa casa": ("In the same house", "Im selben Haus"),
    "Potrebbero piacerti": ("You might also like", "Das könnte Ihnen auch gefallen"),
    "Altre case dell'albergo diffuso": ("More houses of the albergo diffuso", "Weitere Häuser des Albergo Diffuso"),
    "{n} a {b} · {label} fino a {beds} ospiti in Carnia": ("{n} in {b} · {label} for up to {beds} guests in Carnia", "{n} in {b} · {label} für bis zu {beds} Gäste in Karnien"),
    ", tour virtuale 360°": (", 360° virtual tour", ", virtueller 360°-Rundgang"),
    "{short} {stars}{b} (Socchieve, Carnia). {c} foto{tour} e prenotazione diretta.": (
        "{short} {stars}{b} (Socchieve, Carnia). {c} photos{tour} and direct booking.",
        "{short} {stars}{b} (Socchieve, Karnien). {c} Fotos{tour} und Direktbuchung."),
    # tipologie e servizi delle case (data.py)
    "Villa storica": ("Historic villa", "Historische Villa"),
    "Casa per gruppi": ("Group house", "Gruppenhaus"),
    "Casa vacanze": ("Holiday home", "Ferienhaus"),
    "Appartamento": ("Apartment", "Ferienwohnung"),
    "Monolocale": ("Studio", "Studio"),
    "Casa con giardino": ("House with garden", "Haus mit Garten"),
    "TV": ("TV", "TV"),
    "Riscaldamento": ("Heating", "Heizung"),
    "Posto auto": ("Parking space", "Parkplatz"),
    "Giardino comune": ("Shared garden", "Gemeinschaftsgarten"),
    "Wi-Fi": ("Wi-Fi", "WLAN"),
    "Animali ammessi": ("Pets allowed", "Haustiere erlaubt"),
    "Lavastoviglie": ("Dishwasher", "Geschirrspüler"),
    "Microonde": ("Microwave", "Mikrowelle"),
    "Vasca da bagno": ("Bathtub", "Badewanne"),
    "Cucina": ("Kitchen", "Küche"),
    "Lavatrice": ("Washing machine", "Waschmaschine"),
    "Bagno privato con doccia": ("Private bathroom with shower", "Eigenes Bad mit Dusche"),
    "Asciugacapelli": ("Hairdryer", "Haartrockner"),
    "Giardino privato": ("Private garden", "Privatgarten"),
    "Terrazze panoramiche": ("Panoramic terraces", "Panoramaterrassen"),
    "Terrazzo": ("Terrace", "Terrasse"),
    "Parcheggio": ("Parking", "Parkplatz"),
    "Parcheggio condiviso (posti limitati)": ("Shared parking (limited spaces)", "Gemeinsamer Parkplatz (begrenzte Plätze)"),
    "Giardino": ("Garden", "Garten"),

    # ------------------------------------------------------------ pagina borgo
    "Sentieri dal paese": ("Trails from the village", "Wanderwege ab dem Dorf"),
    "Dove mangiare e bere": ("Where to eat and drink", "Essen und Trinken"),
    "Servizi in paese": ("Facilities in the village", "Einrichtungen im Dorf"),
    "Dove dormire a {n}": ("Where to stay in {n}", "Übernachten in {n}"),
    "Le case più vicine, a {n}": ("The nearest houses, in {n}", "Die nächsten Häuser, in {n}"),
    "Le case dell'albergo diffuso": ("The houses of the albergo diffuso", "Die Häuser des Albergo Diffuso"),
    "Abitanti": ("Inhabitants", "Einwohner"),
    "Sentieri": ("Trails", "Wanderwege"),
    "Locali": ("Places to eat", "Lokale"),
    "{n} abitanti": ("{n} inhabitants", "{n} Einwohner"),
    "Panorama di {n}, Socchieve, Carnia": ("View of {n}, Socchieve, Carnia", "Blick auf {n}, Socchieve, Karnien"),
    "Capoluogo del comune, in Carnia": ("The main village of the municipality, in Carnia", "Hauptort der Gemeinde, in Karnien"),
    "Frazione di Socchieve, in Carnia": ("A hamlet of Socchieve, in Carnia", "Ein Ortsteil von Socchieve, in Karnien"),
    "Cosa vedere e cosa fare a {n}": ("What to see and do in {n}", "Sehenswertes und Aktivitäten in {n}"),
    "Panorami": ("Views", "Ausblicke"),
    "{n} in foto": ("{n} in pictures", "{n} in Bildern"),
    "Dormire a {n}": ("Stay in {n}", "Übernachten in {n}"),
    "Soggiorna a Socchieve": ("Stay in Socchieve", "Urlaub in Socchieve"),
    "Socchieve e i suoi paesi": ("Socchieve and its villages", "Socchieve und seine Dörfer"),
    "Gli altri borghi": ("The other villages", "Die anderen Dörfer"),
    "{n}, Socchieve: cosa vedere, sentieri e dove dormire": ("{n}, Socchieve: what to see, trails and where to stay", "{n}, Socchieve: Sehenswertes, Wanderwege und Unterkünfte"),
    ", a {q} m": (", at {q} m", ", auf {q} m"),
    "{n}, frazione di Socchieve in Carnia{alt}: {t}": ("{n}, a hamlet of Socchieve in Carnia{alt}: {t}", "{n}, Ortsteil von Socchieve in Karnien{alt}: {t}"),

    # ------------------------------------------------------------ pagine esperienze
    "Gli itinerari": ("The routes", "Die Touren"),
    "Borghi": ("Villages", "Dörfer"),
    "Mappa del percorso {n}": ("Map of the {n} route", "Karte der Tour {n}"),
    "Altri itinerari in zona": ("More routes nearby", "Weitere Touren in der Gegend"),
    "{n} a Socchieve, Carnia": ("{n} in Socchieve, Carnia", "{n} in Socchieve, Karnien"),
    "Parti da Socchieve": ("Start from Socchieve", "Starten Sie in Socchieve"),
    "Cosa fare a Socchieve": ("Things to do in Socchieve", "Aktivitäten in Socchieve"),
    "Altre esperienze": ("More experiences", "Weitere Erlebnisse"),
    "Benessere a Socchieve": ("Wellness in Socchieve", "Wellness in Socchieve"),
    "Sauna e bagno di bosco": ("Sauna and forest bathing", "Sauna und Waldbaden"),
    "{n} a Socchieve": ("{n} in Socchieve", "{n} in Socchieve"),
    "Escursionisti": ("Hikers", "Wanderer"),
    "Ciclisti": ("Cyclists", "Radfahrer"),

    # ------------------------------------------------------------ home
    "Albergo diffuso con case e appartamenti vacanza nei borghi di Socchieve, in Carnia (Friuli Venezia Giulia), alla porta delle Dolomiti Friulane.": (
        "Albergo diffuso (scattered hotel) with holiday houses and apartments in the villages of Socchieve, Carnia (Friuli Venezia Giulia), at the gateway to the Friulian Dolomites.",
        "Albergo Diffuso (verstreutes Hotel) mit Ferienhäusern und Ferienwohnungen in den Dörfern von Socchieve, Karnien (Friaul-Julisch Venetien), am Tor zu den Friauler Dolomiten."),
    "Strada tra i prati verso le montagne della Carnia, a Socchieve": ("Road through the meadows towards the mountains of Carnia, in Socchieve", "Straße durch die Wiesen in Richtung der Berge Karniens, in Socchieve"),
    "Albergo diffuso a Socchieve · Carnia": ("Albergo diffuso in Socchieve · Carnia", "Albergo Diffuso in Socchieve · Karnien"),
    "Vivi la Carnia <em>da paesano.</em>": ("Live Carnia <em>like a local.</em>", "Karnien erleben <em>wie ein Einheimischer.</em>"),
    "Case e appartamenti vacanza nei borghi di Socchieve, con i servizi di un albergo. A 18 km da Sauris e mezz'ora dalle Dolomiti Friulane.": (
        "Holiday houses and apartments in the villages of Socchieve, with the services of a hotel. 18 km from Sauris and half an hour from the Friulian Dolomites.",
        "Ferienhäuser und Ferienwohnungen in den Dörfern von Socchieve, mit dem Service eines Hotels. 18 km von Sauris und eine halbe Stunde von den Friauler Dolomiten entfernt."),
    "Scopri le case": ("Discover the houses", "Die Häuser entdecken"),
    "alloggi": ("places to stay", "Unterkünfte"),
    "borghi": ("villages", "Dörfer"),
    "Dolomiti Friulane · <b>Patrimonio UNESCO</b>": ("Friulian Dolomites · <b>UNESCO World Heritage</b>", "Friauler Dolomiten · <b>UNESCO-Welterbe</b>"),
    "Scorri": ("Scroll", "Scrollen"),
    "Cos'è un albergo diffuso": ("What is an albergo diffuso", "Was ist ein Albergo Diffuso"),
    "Non un hotel con tante stanze. <em>Un paese intero</em> che ti apre le sue case.": (
        "Not a hotel with many rooms. <em>A whole village</em> that opens its homes to you.",
        "Kein Hotel mit vielen Zimmern. <em>Ein ganzes Dorf,</em> das Ihnen seine Häuser öffnet."),
    "L'albergo diffuso offre i servizi di una struttura alberghiera dentro un territorio abitato. A Socchieve dormi in una casa vera del borgo, prendi il caffè con chi ci vive ed esci a piedi sui sentieri della Carnia. Turista e paesano, nello stesso viaggio.": (
        "An albergo diffuso – literally a “scattered hotel” – offers hotel services spread across a lived-in village. In Socchieve you sleep in a real village house, have your coffee with the people who live here and walk straight out onto the trails of Carnia. Tourist and local, on the same trip.",
        "Ein Albergo Diffuso – wörtlich ein „verstreutes Hotel“ – bietet den Service eines Hotels mitten in einem bewohnten Ort. In Socchieve schlafen Sie in einem echten Dorfhaus, trinken Ihren Kaffee mit den Menschen, die hier leben, und starten zu Fuß direkt auf die Wanderwege Karniens. Gast und Dorfbewohner zugleich."),
    "case e appartamenti": ("houses and apartments", "Häuser und Wohnungen"),
    "borghi del comune": ("villages in the municipality", "Dörfer der Gemeinde"),
    "posti letto per casa": ("beds per house", "Betten pro Haus"),
    "Albero e panchina in un prato di montagna a Socchieve": ("Tree and bench in a mountain meadow in Socchieve", "Baum und Bank auf einer Bergwiese in Socchieve"),
    "Casa Vanda a Viaso, villa settecentesca con ballatoi in legno": ("Casa Vanda in Viaso, an 18th-century villa with wooden balconies", "Casa Vanda in Viaso, eine Villa aus dem 18. Jahrhundert mit Holzbalkonen"),
    "OSPITI DELLA NATURA · OSPITI DELLA NATURA · ": ("GUESTS OF NATURE · GUESTS OF NATURE · ", "GÄSTE DER NATUR · GÄSTE DER NATUR · "),
    "Dove dormire in Carnia": ("Where to stay in Carnia", "Übernachten in Karnien"),
    "Scegli la tua <em>casa nel borgo.</em>": ("Choose your <em>village home.</em>", "Wählen Sie Ihr <em>Haus im Dorf.</em>"),
    "Dal monolocale per due alla villa per gruppi fino a 21 persone. Filtra per borgo o per numero di posti letto.": (
        "From a studio for two to a villa for groups of up to 21. Filter by village or number of beds.",
        "Vom Studio für zwei bis zur Villa für Gruppen bis 21 Personen. Filtern Sie nach Dorf oder Bettenzahl."),
    "Otto borghi, <em>un'unica valle.</em>": ("Eight villages, <em>one valley.</em>", "Acht Dörfer, <em>ein Tal.</em>"),
    "Borghi precedenti": ("Previous villages", "Vorherige Dörfer"),
    "Borghi successivi": ("Next villages", "Nächste Dörfer"),
    "Prenditi <em>il tempo.</em>": ("Take <em>your time.</em>", "Nehmen Sie sich <em>Zeit.</em>"),
    "Passeggiate ed escursioni, bici, arte romanica e i grandi classici della Carnia. Si parte direttamente dalle nostre case.": (
        "Walks and hikes, cycling, Romanesque art and the great classics of Carnia. You set off straight from our houses.",
        "Spaziergänge und Wanderungen, Radtouren, romanische Kunst und die großen Klassiker Karniens. Los geht es direkt vor unseren Häusern."),
    "Sentiero tra prati e boschi in Carnia": ("Trail through meadows and woods in Carnia", "Wanderweg durch Wiesen und Wälder in Karnien"),
    "Quattro anelli che partono dai borghi e la traversata del Col Gentile sul sentiero CAI 235.": (
        "Four loops starting from the villages, plus the Col Gentile crossing on CAI trail 235.",
        "Vier Rundwege ab den Dörfern und die Überschreitung des Col Gentile auf dem CAI-Weg 235."),
    "Scopri i percorsi": ("See the routes", "Zu den Touren"),
    "La pista MTB di Mediis e l'anello del Passo Rest, con lo Zoncolan a 24 km.": (
        "The Mediis MTB trail and the Passo Rest loop, with the Zoncolan 24 km away.",
        "Die MTB-Strecke von Mediis und die Runde über den Passo Rest – der Zoncolan ist nur 24 km entfernt."),
    "Approfondisci": ("Find out more", "Mehr erfahren"),
    "Antica meridiana dipinta su un muro in pietra a Socchieve": ("Old sundial painted on a stone wall in Socchieve", "Alte Sonnenuhr auf einer Steinmauer in Socchieve"),
    "Sauris e il suo prosciutto, la Forra del Lumiei, Forni di Sopra e la Val Pesarina: tutto a meno di un'ora.": (
        "Sauris and its ham, the Lumiei gorge, Forni di Sopra and Val Pesarina: all less than an hour away.",
        "Sauris und sein Schinken, die Lumiei-Schlucht, Forni di Sopra und das Val Pesarina: alles in weniger als einer Stunde erreichbar."),
    "Benessere in Carnia": ("Wellness in Carnia", "Wellness in Karnien"),
    "Sauna e <em>bagno di bosco</em> a Socchieve.": ("Sauna and <em>forest bathing</em> in Socchieve.", "Sauna und <em>Waldbaden</em> in Socchieve."),
    "Dopo una giornata sui sentieri o in bici, la sauna scioglie i muscoli; nei boschi intorno ai borghi lo Shinrin-yoku con Petra ti insegna a rallentare. Si prenotano online con conferma immediata: serve una carta di credito a garanzia.": (
        "After a day on the trails or in the saddle, the sauna loosens tired muscles; in the woods around the villages, Shinrin-yoku with Petra teaches you to slow down. Book online with instant confirmation: a credit card is required as a guarantee.",
        "Nach einem Tag auf den Wanderwegen oder auf dem Rad lockert die Sauna die Muskeln; in den Wäldern rund um die Dörfer lehrt Sie Petra beim Shinrin-yoku, langsamer zu werden. Online buchbar mit sofortiger Bestätigung; eine Kreditkarte dient als Garantie."),
    "Sauna in Carnia": ("Sauna in Carnia", "Sauna in Karnien"),
    "Sauna a ore per tutto il gruppo, {p} € l'ora a prezzo unico, da due ore in su: il modo migliore per chiudere un'escursione, un'uscita in mountain bike o una giornata sulle piste di Forni di Sopra.": (
        "Sauna by the hour for your whole group, a flat {p} € per hour, two hours minimum: the best way to end a hike, a mountain-bike ride or a day on the slopes of Forni di Sopra.",
        "Sauna stundenweise für die ganze Gruppe, pauschal {p} € pro Stunde, ab zwei Stunden: der beste Abschluss nach einer Wanderung, einer Mountainbike-Tour oder einem Tag auf den Pisten von Forni di Sopra."),
    "Prezzi e orari": ("Prices and times", "Preise und Zeiten"),
    "Bagno di bosco (Shinrin-yoku)": ("Forest bathing (Shinrin-yoku)", "Waldbaden (Shinrin-yoku)"),
    "Forest bathing guidato da Petra nei boschi di Socchieve: circa due ore di immersione lenta e sensoriale nella natura, gruppi fino a 6 persone, {p} € a persona, ritrovo alla reception di Mediis.": (
        "Forest bathing guided by Petra in the woods of Socchieve: about two hours of slow, sensory immersion in nature, groups of up to 6, {p} € per person, meeting at the Mediis reception.",
        "Waldbaden mit Petra in den Wäldern von Socchieve: rund zwei Stunden langsames, sinnliches Eintauchen in die Natur, Gruppen bis 6 Personen, {p} € pro Person, Treffpunkt an der Rezeption in Mediis."),
    "Come funziona": ("How it works", "So funktioniert es"),
    "Prenota il tuo momento di benessere": ("Book your wellness time", "Buchen Sie Ihre Auszeit"),
    "Dov'è Socchieve": ("Where is Socchieve", "Wo liegt Socchieve"),
    "Al centro della Carnia, <em>vicino a tutto.</em>": ("In the heart of Carnia, <em>close to everything.</em>", "Im Herzen Karniens, <em>nah an allem.</em>"),
    "Tra le Dolomiti Friulane e le Pesarine, lungo la SS52 che unisce Tolmezzo a Forni di Sopra. Distanze in auto dalla reception di Mediis.": (
        "Between the Friulian and Pesarina Dolomites, along the SS52 road from Tolmezzo to Forni di Sopra. Driving distances from the Mediis reception.",
        "Zwischen den Friauler und den Pesariner Dolomiten, an der SS52 von Tolmezzo nach Forni di Sopra. Fahrstrecken ab der Rezeption in Mediis."),
    "Come arrivare e contatti": ("Getting here and contact", "Anreise und Kontakt"),
    "Affittacamere a Lungis · gestito dall'Albergo Diffuso": ("Guesthouse in Lungis · run by the Albergo Diffuso", "Gästehaus in Lungis · geführt vom Albergo Diffuso"),
    "Un affittacamere in una casa carnica ristrutturata nel borgo di Lungis, gestito direttamente dall'Albergo Diffuso Socchieve.": (
        "A guesthouse in a restored Carnic house in the village of Lungis, run directly by the Albergo Diffuso Socchieve.",
        "Ein Gästehaus in einem restaurierten karnischen Haus im Dorf Lungis, direkt vom Albergo Diffuso Socchieve geführt."),
    "Scopri La Farie": ("Discover La Farie", "La Farie entdecken"),
    "Domande frequenti": ("Frequently asked questions", "Häufige Fragen"),
    "Prima di <em>partire.</em>": ("Before <em>you go.</em>", "Vor der <em>Abreise.</em>"),
    "Una vacanza diversa": ("A different kind of holiday", "Ein anderer Urlaub"),
    "La montagna, <em>tra le persone.</em>": ("The mountains, <em>among people.</em>", "Die Berge, <em>unter Menschen.</em>"),
    "Lasciati affascinare dal vivere in montagna tra la gente e la natura della Carnia.": (
        "Let yourself be charmed by mountain life among the people and nature of Carnia.",
        "Lassen Sie sich vom Leben in den Bergen begeistern, mitten unter den Menschen und in der Natur Karniens."),
    "Prenota il soggiorno": ("Book your stay", "Aufenthalt buchen"),
    "Albergo Diffuso Socchieve · Case vacanza in Carnia e Dolomiti": ("Albergo Diffuso Socchieve · Holiday homes in Carnia and the Dolomites", "Albergo Diffuso Socchieve · Ferienhäuser in Karnien und den Dolomiten"),
    "Case e appartamenti vacanza nei borghi di Socchieve, in Carnia: {n} alloggi da 2 a 21 posti, a 18 km da Sauris e 30 minuti dalle Dolomiti Friulane. Prenotazione diretta.": (
        "Holiday houses and apartments in the villages of Socchieve, Carnia: {n} places to stay for 2 to 21 guests, 18 km from Sauris and 30 minutes from the Friulian Dolomites. Book direct.",
        "Ferienhäuser und Ferienwohnungen in den Dörfern von Socchieve, Karnien: {n} Unterkünfte für 2 bis 21 Gäste, 18 km von Sauris und 30 Minuten von den Friauler Dolomiten. Direkt buchen."),

    # ------------------------------------------------------------ elenco case
    "Case vacanza dell'albergo diffuso di Socchieve": ("Holiday homes of the Socchieve albergo diffuso", "Ferienhäuser des Albergo Diffuso Socchieve"),
    "Case vacanza <em>in Carnia</em>": ("Holiday homes <em>in Carnia</em>", "Ferienhäuser <em>in Karnien</em>"),
    "{n} case e appartamenti nei borghi di Socchieve, dal monolocale per due alla villa per gruppi. Prenotazione diretta, senza intermediari.": (
        "{n} houses and apartments in the villages of Socchieve, from a studio for two to a villa for groups. Direct booking, no middlemen.",
        "{n} Häuser und Wohnungen in den Dörfern von Socchieve, vom Studio für zwei bis zur Villa für Gruppen. Direktbuchung ohne Vermittler."),
    "Tutti gli alloggi": ("All places to stay", "Alle Unterkünfte"),
    "Trova la casa <em>giusta per te.</em>": ("Find the <em>right house for you.</em>", "Finden Sie <em>Ihr passendes Haus.</em>"),
    "Appartamenti per coppie e famiglie, case intere per gruppi: tutte arredate, con cucina, e a pochi passi dai sentieri.": (
        "Apartments for couples and families, whole houses for groups: all furnished, all with a kitchen, and all a few steps from the trails.",
        "Wohnungen für Paare und Familien, ganze Häuser für Gruppen: alle möbliert, mit Küche und nur wenige Schritte von den Wanderwegen entfernt."),
    "Case vacanza dell'Albergo Diffuso Socchieve": ("Holiday homes of the Albergo Diffuso Socchieve", "Ferienhäuser des Albergo Diffuso Socchieve"),
    "Case vacanza e appartamenti in Carnia · {n} alloggi a Socchieve": ("Holiday homes and apartments in Carnia · {n} places to stay in Socchieve", "Ferienhäuser und Ferienwohnungen in Karnien · {n} Unterkünfte in Socchieve"),
    "{n} case vacanza e appartamenti nei borghi di Socchieve, in Carnia: da 2 a 21 posti letto, 3 e 4 stelle, alcuni con tour 360° e animali ammessi. Prenota direttamente.": (
        "{n} holiday homes and apartments in the villages of Socchieve, Carnia: 2 to 21 beds, 3 and 4 stars, some with a 360° tour and pets allowed. Book direct.",
        "{n} Ferienhäuser und Ferienwohnungen in den Dörfern von Socchieve, Karnien: 2 bis 21 Betten, 3 und 4 Sterne, teils mit 360°-Rundgang und Haustieren erlaubt. Direkt buchen."),

    # ------------------------------------------------------------ territorio
    "Montagne della Carnia sopra Feltrone": ("Mountains of Carnia above Feltrone", "Berge Karniens oberhalb von Feltrone"),
    "Socchieve <em>e la Carnia</em>": ("Socchieve <em>and Carnia</em>", "Socchieve <em>und Karnien</em>"),
    "Otto borghi tra le Dolomiti Friulane e le Pesarine, sentieri fuori dalla porta e i grandi classici della Carnia a meno di un'ora.": (
        "Eight villages between the Friulian and Pesarina Dolomites, trails right outside the door and the great classics of Carnia less than an hour away.",
        "Acht Dörfer zwischen den Friauler und den Pesariner Dolomiten, Wanderwege direkt vor der Tür und die großen Klassiker Karniens in weniger als einer Stunde."),
    "Ogni frazione ha il suo carattere, i suoi sentieri e le sue osterie. Scopri dove dormire e cosa fare in ciascuna.": (
        "Each hamlet has its own character, trails and inns. Find out where to stay and what to do in each.",
        "Jeder Ortsteil hat seinen eigenen Charakter, seine Wege und Gasthäuser. Entdecken Sie, wo Sie übernachten und was Sie unternehmen können."),
    "Distanze": ("Distances", "Entfernungen"),
    "Il campo base <em>per la Carnia.</em>": ("Your base camp <em>for Carnia.</em>", "Ihr Basislager <em>für Karnien.</em>"),
    "Socchieve e i suoi borghi: cosa fare in Carnia": ("Socchieve and its villages: things to do in Carnia", "Socchieve und seine Dörfer: Aktivitäten in Karnien"),
    "Gli otto borghi di Socchieve, i sentieri, la mountain bike, l'arte romanica e le mete della Carnia vicine: Sauris, Forni di Sopra, Ampezzo e la Val Pesarina.": (
        "The eight villages of Socchieve, hiking trails, mountain biking, Romanesque art and nearby places in Carnia: Sauris, Forni di Sopra, Ampezzo and Val Pesarina.",
        "Die acht Dörfer von Socchieve, Wanderwege, Mountainbiken, romanische Kunst und Ausflugsziele in Karnien: Sauris, Forni di Sopra, Ampezzo und das Val Pesarina."),
    # distanze (data.py)
    "Ampezzo": ("Ampezzo", "Ampezzo"),
    "Tolmezzo": ("Tolmezzo", "Tolmezzo"),
    "Sauris e il suo lago": ("Sauris and its lake", "Sauris und sein See"),
    "Forni di Sopra": ("Forni di Sopra", "Forni di Sopra"),
    "Val Pesarina (Pesariis)": ("Val Pesarina (Pesariis)", "Val Pesarina (Pesariis)"),
    "Monte Zoncolan": ("Monte Zoncolan", "Monte Zoncolan"),
    "Casello A23 Carnia": ("A23 motorway exit Carnia", "Autobahnausfahrt A23 Carnia"),
    "Udine": ("Udine", "Udine"),
    "Aeroporto di Trieste": ("Trieste airport", "Flughafen Triest"),
    "Lignano Sabbiadoro": ("Lignano Sabbiadoro", "Lignano Sabbiadoro"),

    # ------------------------------------------------------------ contatti
    "Panorama di Mediis, sede della reception": ("View of Mediis, home of the reception", "Blick auf Mediis, Sitz der Rezeption"),
    "Contatti <em>e come arrivare</em>": ("Contact <em>and getting here</em>", "Kontakt <em>und Anreise</em>"),
    "La reception è a Mediis, in Via Roma 20. Scrivici o chiamaci per qualsiasi informazione sul soggiorno.": (
        "The reception is in Mediis, at Via Roma 20. Write or call us with any question about your stay.",
        "Die Rezeption befindet sich in Mediis, Via Roma 20. Schreiben oder rufen Sie uns bei allen Fragen zu Ihrem Aufenthalt an."),
    "Telefono": ("Phone", "Telefon"),
    "Cellulare": ("Mobile", "Mobil"),
    "Come arrivare": ("Getting here", "Anreise"),
    "Tra le Dolomiti Friulane <em>e le Pesarine.</em>": ("Between the Friulian <em>and Pesarina Dolomites.</em>", "Zwischen den Friauler <em>und den Pesariner Dolomiten.</em>"),
    "Socchieve è nell'Alto Friuli, in Carnia, lungo la valle che unisce Villa Santina a Forni di Sotto.": (
        "Socchieve is in Upper Friuli, in Carnia, along the valley that runs from Villa Santina to Forni di Sotto.",
        "Socchieve liegt im oberen Friaul, in Karnien, im Tal zwischen Villa Santina und Forni di Sotto."),
    "Autostrada A23": ("A23 motorway", "Autobahn A23"),
    "Uscita Carnia, poi SS52 verso Tolmezzo e Forni di Sopra (27 km dal casello)": (
        "Exit Carnia, then the SS52 towards Tolmezzo and Forni di Sopra (27 km from the exit)",
        "Ausfahrt Carnia, dann SS52 Richtung Tolmezzo und Forni di Sopra (27 km ab der Ausfahrt)"),
    "Dal Cadore": ("From Cadore", "Aus dem Cadore"),
    "SS52 da Forni di Sopra (26 km)": ("SS52 from Forni di Sopra (26 km)", "SS52 ab Forni di Sopra (26 km)"),
    "Da Pordenone": ("From Pordenone", "Aus Pordenone"),
    "SS552 del Monte Rest da Tramonti di Sopra": ("SS552 over Monte Rest from Tramonti di Sopra", "SS552 über den Monte Rest ab Tramonti di Sopra"),
    "Dalla Val d'Arzino": ("From Val d'Arzino", "Aus dem Val d'Arzino"),
    "Strada comunale di Preone": ("Preone municipal road", "Gemeindestraße von Preone"),
    "In aereo": ("By plane", "Mit dem Flugzeug"),
    "Aeroporto di Trieste (103 km), Venezia Marco Polo (circa 2 h 30)": ("Trieste airport (103 km), Venice Marco Polo (about 2 h 30)", "Flughafen Triest (103 km), Venedig Marco Polo (ca. 2 Std. 30)"),
    "In treno": ("By train", "Mit dem Zug"),
    "Stazione Carnia, poi autobus SAF (fermata a Mediis, Bar alla Posta)": ("Carnia station, then SAF bus (stop in Mediis, Bar alla Posta)", "Bahnhof Carnia, dann SAF-Bus (Haltestelle in Mediis, Bar alla Posta)"),
    "Indicazioni stradali": ("Directions", "Route planen"),
    "Mappa della reception a Mediis, Socchieve": ("Map of the reception in Mediis, Socchieve", "Karte der Rezeption in Mediis, Socchieve"),
    "Chiama la reception": ("Call the reception", "Rezeption anrufen"),
    "Distanze dalla reception": ("Distances from the reception", "Entfernungen ab der Rezeption"),
    "Contatti e come arrivare · Albergo Diffuso Socchieve": ("Contact and getting here · Albergo Diffuso Socchieve", "Kontakt und Anreise · Albergo Diffuso Socchieve"),
    "Reception a Mediis (Socchieve, UD), tel. +39 0433 819934, info@albergodiffusosocchieve.it. Come arrivare in Carnia da A23, Cadore, Pordenone e aeroporto di Trieste.": (
        "Reception in Mediis (Socchieve, UD), tel. +39 0433 819934, info@albergodiffusosocchieve.it. How to reach Carnia from the A23, Cadore, Pordenone and Trieste airport.",
        "Rezeption in Mediis (Socchieve, UD), Tel. +39 0433 819934, info@albergodiffusosocchieve.it. Anreise nach Karnien über die A23, aus dem Cadore, aus Pordenone und vom Flughafen Triest."),

    # ------------------------------------------------------------ La Farie
    "Prenotazione diretta · conferma via email": ("Direct booking · confirmation by email", "Direktbuchung · Bestätigung per E-Mail"),
    "La casa": ("The house", "Das Haus"),
    "Info utili": ("Useful info", "Gut zu wissen"),
    "La Farie, affittacamere a Lungis": ("La Farie, guesthouse in Lungis", "La Farie, Gästehaus in Lungis"),
    "Affittacamere · Lungis, Carnia": ("Guesthouse · Lungis, Carnia", "Gästehaus · Lungis, Karnien"),
    "La Farie, affittacamere in una casa carnica a Lungis": ("La Farie, guesthouse in a Carnic house in Lungis", "La Farie, Gästehaus in einem karnischen Haus in Lungis"),
    "Affittacamere a Lungis · Carnia": ("Guesthouse in Lungis · Carnia", "Gästehaus in Lungis · Karnien"),
    "La Farie. <em>Sentirsi a casa.</em>": ("La Farie. <em>Feel at home.</em>", "La Farie. <em>Wie zu Hause.</em>"),
    "Una casa tipica carnica ristrutturata nel borgo di Lungis, con camere con terrazza o balcone, giardino e la quiete delle montagne. Gestita dall'Albergo Diffuso Socchieve.": (
        "A restored traditional Carnic house in the village of Lungis, with rooms with a terrace or balcony, a garden and the peace of the mountains. Run by the Albergo Diffuso Socchieve.",
        "Ein restauriertes, typisch karnisches Haus im Dorf Lungis, mit Zimmern mit Terrasse oder Balkon, Garten und der Ruhe der Berge. Geführt vom Albergo Diffuso Socchieve."),
    "Le camere": ("The rooms", "Die Zimmer"),
    "Parcheggio gratuito": ("Free parking", "Kostenloses Parken"),
    "Gestione <b>Albergo Diffuso Socchieve</b>": ("Run by <b>Albergo Diffuso Socchieve</b>", "Geführt vom <b>Albergo Diffuso Socchieve</b>"),
    "Una casa carnica, <em>la quiete di Lungis.</em>": ("A Carnic house, <em>the peace of Lungis.</em>", "Ein karnisches Haus, <em>die Ruhe von Lungis.</em>"),
    "{c} foto di <em>La Farie</em>": ("{c} photos of <em>La Farie</em>", "{c} Fotos von <em>La Farie</em>"),
    "Cinque camere, <em>un appartamento.</em>": ("Four rooms, <em>one apartment.</em>", "Vier Zimmer, <em>eine Wohnung.</em>"),
    "fino a {m} ospite": ("up to {m} guest", "bis zu {m} Gast"),
    "fino a {m} ospiti": ("up to {m} guests", "bis zu {m} Gäste"),
    " o ": (" or ", " oder "),
    " e ": (" and ", " und "),
    "Tariffe: {plans}.": ("Rates: {plans}.", "Tarife: {plans}."),
    "Tutto quello <em>che serve.</em>": ("Everything <em>you need.</em>", "Alles, <em>was Sie brauchen.</em>"),
    "Prima di <em>arrivare.</em>": ("Before <em>you arrive.</em>", "Vor der <em>Ankunft.</em>"),
    "Dove siamo": ("Where we are", "Lage"),
    "A Lungis, nella <em>Carnia più vera.</em>": ("In Lungis, in the <em>real Carnia.</em>", "In Lungis, im <em>echten Karnien.</em>"),
    "{addr}, frazione di Lungis, comune di Socchieve (UD), a 554 metri di quota. A due passi l'agriturismo In Già, il bar e ristorante Al Cervo e i sentieri dell'Anello delle Frazioni.": (
        "{addr}, in the hamlet of Lungis, municipality of Socchieve (UD), at 554 metres above sea level. A short walk to the In Già farm restaurant, the Al Cervo bar and restaurant, and the trails of the Anello delle Frazioni.",
        "{addr}, Ortsteil Lungis, Gemeinde Socchieve (UD), auf 554 Metern Höhe. Nur ein paar Schritte zum Agriturismo In Già, zur Bar und zum Restaurant Al Cervo und zu den Wegen des Anello delle Frazioni."),
    "Scopri il borgo di Lungis": ("Discover the village of Lungis", "Das Dorf Lungis entdecken"),
    "Il tuo affittacamere <em>in Carnia.</em>": ("Your guesthouse <em>in Carnia.</em>", "Ihr Gästehaus <em>in Karnien.</em>"),
    "Scegli le date e prenota direttamente: conferma immediata via email. Hai domande? Scrivici.": (
        "Pick your dates and book direct: instant confirmation by email. Questions? Write to us.",
        "Wählen Sie Ihre Daten und buchen Sie direkt: sofortige Bestätigung per E-Mail. Fragen? Schreiben Sie uns."),
    "Scopri anche Col Gentile": ("Discover Col Gentile too", "Auch Col Gentile entdecken"),
    "La Farie · affittacamere a Lungis, Socchieve (Carnia)": ("La Farie · guesthouse in Lungis, Socchieve (Carnia)", "La Farie · Gästehaus in Lungis, Socchieve (Karnien)"),
    "Affittacamere in una casa carnica ristrutturata a Lungis, Socchieve (Carnia), gestito dall'Albergo Diffuso Socchieve: camere con terrazza, giardino, Wi-Fi e parcheggio gratuito.": (
        "Guesthouse in a restored Carnic house in Lungis, Socchieve (Carnia), run by the Albergo Diffuso Socchieve: rooms with a terrace, garden, Wi-Fi and free parking.",
        "Gästehaus in einem restaurierten karnischen Haus in Lungis, Socchieve (Karnien), geführt vom Albergo Diffuso Socchieve: Zimmer mit Terrasse, Garten, WLAN und kostenlosem Parkplatz."),
    "Prenota <em>La Farie</em>": ("Book <em>La Farie</em>", "<em>La Farie</em> buchen"),
    "Prenota La Farie · affittacamere a Lungis": ("Book La Farie · guesthouse in Lungis", "La Farie buchen · Gästehaus in Lungis"),
    "Disponibilità e prenotazione diretta delle camere di La Farie, affittacamere a Lungis (Socchieve).": ("Availability and direct booking for the rooms of La Farie, a guesthouse in Lungis (Socchieve).", "Verfügbarkeit und Direktbuchung der Zimmer von La Farie, Gästehaus in Lungis (Socchieve)."),
    "La prenotazione online sarà disponibile a breve.": ("Online booking will be available soon.", "Die Online-Buchung ist bald verfügbar."),
    "Scrivici a": ("Write to us at", "Schreiben Sie uns an"),
    "o chiama il": ("or call", "oder rufen Sie an:"),
    "Condizioni di soggiorno": ("Terms of stay", "Aufenthaltsbedingungen"),
    "Valgono per le prenotazioni delle camere di La Farie, {addr}, Lungis, Socchieve (UD), gestita da {legal}, {street}, {locality}, P.I. {vat}.": (
        "These apply to bookings of rooms at La Farie, {addr}, Lungis, Socchieve (UD), run by {legal}, {street}, {locality}, VAT no. {vat}.",
        "Sie gelten für Zimmerbuchungen bei La Farie, {addr}, Lungis, Socchieve (UD), geführt von {legal}, {street}, {locality}, USt-IdNr. {vat}."),
    "Tariffe": ("Rates", "Tarife"),
    "Sono disponibili le tariffe {plans}. Il prezzo è quello indicato al momento della prenotazione per le date, la camera e il numero di ospiti scelti.": (
        "The available rates are {plans}. The price is the one shown at the time of booking for the chosen dates, room and number of guests.",
        "Verfügbar sind die Tarife {plans}. Es gilt der bei der Buchung angezeigte Preis für die gewählten Daten, das Zimmer und die Anzahl der Gäste."),
    "Cancellazione": ("Cancellation", "Stornierung"),
    "Dopo questo termine contatta la struttura.": ("After this deadline, please contact the property.", "Nach dieser Frist wenden Sie sich bitte an die Unterkunft."),
    "Arrivo e partenza": ("Arrival and departure", "Anreise und Abreise"),
    "Dati personali": ("Personal data", "Personenbezogene Daten"),
    "I dati della prenotazione sono trattati come descritto nell'<a href=\"{href}\">informativa privacy</a>.": (
        "Booking data is processed as described in the <a href=\"{href}\">privacy policy</a>.",
        "Die Buchungsdaten werden wie in der <a href=\"{href}\">Datenschutzerklärung</a> beschrieben verarbeitet."),
    "Condizioni di soggiorno · La Farie, Lungis": ("Terms of stay · La Farie, Lungis", "Aufenthaltsbedingungen · La Farie, Lungis"),
    "Condizioni di prenotazione e cancellazione delle camere di La Farie, affittacamere a Lungis gestito dall'Albergo Diffuso Socchieve.": (
        "Booking and cancellation terms for the rooms of La Farie, a guesthouse in Lungis run by the Albergo Diffuso Socchieve.",
        "Buchungs- und Stornierungsbedingungen für die Zimmer von La Farie, Gästehaus in Lungis, geführt vom Albergo Diffuso Socchieve."),

    # ------------------------------------------------------------ benessere
    "Conferma immediata via email · carta di credito richiesta a garanzia · preferisci parlarci?": (
        "Instant confirmation by email · credit card required as a guarantee · prefer to talk to us?",
        "Sofortige Bestätigung per E-Mail · Kreditkarte als Garantie erforderlich · lieber persönlich?"),
    "Prenotazione ": ("Booking: ", "Buchung: "),
    "Scegli giorno, orario e numero di persone: la conferma arriva via email.": ("Choose the day, time and number of people: confirmation arrives by email.", "Wählen Sie Tag, Uhrzeit und Personenzahl: Die Bestätigung kommt per E-Mail."),
    "Scrivici o chiamaci con giorno, orario e numero di persone: ti confermiamo la disponibilità.": ("Write or call us with the day, time and number of people and we will confirm availability.", "Schreiben oder rufen Sie uns mit Tag, Uhrzeit und Personenzahl an – wir bestätigen die Verfügbarkeit."),
    "Prenota via email": ("Book by email", "Per E-Mail buchen"),
    "Per prenotare online serve una carta di credito a garanzia.": ("Online booking requires a credit card as a guarantee.", "Für die Online-Buchung ist eine Kreditkarte als Garantie nötig."),
    "Scopri e prenota": ("Discover and book", "Entdecken und buchen"),
    "Cosa portare": ("What to bring", "Was mitbringen"),
    "Come prepararsi": ("How to prepare", "Gut vorbereitet"),
    "Ritrovo": ("Meeting point", "Treffpunkt"),
    "Dove ci si incontra": ("Where we meet", "Wo wir uns treffen"),
    "Cos'è il bagno di bosco": ("What is forest bathing", "Was ist Waldbaden"),
    "Come funziona la sauna": ("How the sauna works", "So funktioniert die Sauna"),
    "Benessere a Socchieve · Carnia": ("Wellness in Socchieve · Carnia", "Wellness in Socchieve · Karnien"),
    "Prenota {n}": ("Book {n}", "{n} buchen"),
    "Benessere e natura": ("Wellness and nature", "Wellness und Natur"),
    "Da abbinare": ("Pair it with", "Passt dazu"),
    "Prati al tramonto a Nonta, Socchieve": ("Meadows at sunset in Nonta, Socchieve", "Wiesen bei Sonnenuntergang in Nonta, Socchieve"),
    "Benessere <em>in Carnia</em>": ("Wellness <em>in Carnia</em>", "Wellness <em>in Karnien</em>"),
    "Sauna e bagno di bosco all'Albergo Diffuso di Socchieve: il modo giusto per chiudere una giornata in montagna.": (
        "Sauna and forest bathing at the Albergo Diffuso in Socchieve: the right way to end a day in the mountains.",
        "Sauna und Waldbaden im Albergo Diffuso in Socchieve: der richtige Abschluss für einen Tag in den Bergen."),
    "I servizi": ("The experiences", "Die Angebote"),
    "Rallenta, <em>respira.</em>": ("Slow down, <em>breathe.</em>", "Langsamer werden, <em>durchatmen.</em>"),
    "Prezzi chiari e conferma immediata. Per prenotare online serve una carta di credito a garanzia. Scrivici per sapere se si possono prenotare anche senza soggiornare da noi.": (
        "Clear prices and instant confirmation. Online booking requires a credit card as a guarantee. Write to us to ask whether you can book them without staying with us.",
        "Klare Preise und sofortige Bestätigung. Für die Online-Buchung ist eine Kreditkarte als Garantie nötig. Fragen Sie uns, ob Sie auch ohne Übernachtung bei uns buchen können."),
    "Prenota sauna o bagno di bosco": ("Book the sauna or forest bathing", "Sauna oder Waldbaden buchen"),
    "Benessere all'Albergo Diffuso Socchieve": ("Wellness at the Albergo Diffuso Socchieve", "Wellness im Albergo Diffuso Socchieve"),
    "Benessere in Carnia: sauna e bagno di bosco a Socchieve": ("Wellness in Carnia: sauna and forest bathing in Socchieve", "Wellness in Karnien: Sauna und Waldbaden in Socchieve"),
    "Sauna (20 € l'ora per il gruppo) e bagno di bosco Shinrin-yoku con guida (15 € a persona) all'Albergo Diffuso di Socchieve, in Carnia. Prenota direttamente.": (
        "Sauna (20 € per hour for the group) and guided Shinrin-yoku forest bathing (15 € per person) at the Albergo Diffuso in Socchieve, Carnia. Book direct.",
        "Sauna (20 € pro Stunde für die Gruppe) und geführtes Waldbaden – Shinrin-yoku – (15 € pro Person) im Albergo Diffuso in Socchieve, Karnien. Direkt buchen."),
    "Prenota servizi": ("Book wellness", "Wellness buchen"),
    "La prenotazione online sarà disponibile a breve. Nel frattempo scrivici a": ("Online booking will be available soon. In the meantime, write to us at", "Die Online-Buchung ist bald verfügbar. Bis dahin schreiben Sie uns an"),
    "Prenota <em>sauna e bagno di bosco</em>": ("Book the <em>sauna and forest bathing</em>", "<em>Sauna und Waldbaden</em> buchen"),
    "Prenota sauna e bagno di bosco · Albergo Diffuso Socchieve": ("Book the sauna and forest bathing · Albergo Diffuso Socchieve", "Sauna und Waldbaden buchen · Albergo Diffuso Socchieve"),
    "Prenota online sauna e bagno di bosco all'Albergo Diffuso di Socchieve, in Carnia.": ("Book the sauna and forest bathing online at the Albergo Diffuso in Socchieve, Carnia.", "Sauna und Waldbaden online buchen im Albergo Diffuso in Socchieve, Karnien."),

}


# ---------------------------------------------------------------- contenuti (data.py)
VILLA_EN = ("Villa Vanda, recognised by the Municipality of Socchieve as a building of historic value, dates from the second half of "
            "the 18th century: typical Carnic architecture, stone arches and wooden galleries (linde) that open onto a beautiful view. "
            "It stands in Viaso, a quiet, sunny hamlet surrounded by greenery, where life follows the slow rhythm of nature. Guests "
            "have a small courtyard with a garden. Three parking spaces are shared by the five apartments and are not reserved.")
VILLA_DE = ("Die Villa Vanda, von der Gemeinde Socchieve als historisch wertvolles Gebäude anerkannt, stammt aus der zweiten Hälfte des "
            "18. Jahrhunderts: typisch karnische Architektur, Steinbögen und hölzerne Laubengänge (linde), von denen sich ein herrlicher "
            "Blick öffnet. Sie liegt in Viaso, einem ruhigen, sonnigen Ortsteil im Grünen, wo das Leben im langsamen Takt der Natur "
            "verläuft. Den Gästen steht ein kleiner Innenhof mit Garten zur Verfügung. Drei Parkplätze werden von den fünf Wohnungen gemeinsam genutzt und sind nicht reserviert.")

STAYS_EN = {
    "casa-vanda": dict(
        short="The whole 18th-century villa in Viaso, in stone with wooden balconies: five apartments for large families and groups of up to 18.",
        text=[VILLA_EN, "Booking the whole residence gives you all the apartments in the villa – Iris, Genziana, Bucaneve, Papavero and Ortensia – each carefully furnished around the colour that gives it its name. The ideal choice for extended families, groups of friends, associations and retreats."]),
    "casa-ernesto-da-rosuline": dict(
        short="The whole house in Lungis with its four units: the solution for large groups in Carnia.",
        text=["The house in Lungis brings together four units furnished in a simple, practical style: the ground-floor studio and three apartments on the upper floors, with terraces overlooking the village and the mountains.", "Booked as a whole, it is ideal for large groups, extended families, sports teams and associations. The Anello delle Frazioni trail starts from the village, and the bar-grocery and the farm restaurant are a short walk away."]),
    "casa-pradin": dict(
        short="The old village inn of Feltrone, on three floors with wooden terraces: four double bedrooms for groups and large families.",
        text=["Casa Pradin is in Feltrone, the highest hamlet of Socchieve (769 m), just below the village chapel. It was once the village inn: today it is a renovated building on three floors, with wooden terraces on every floor – the first and second connected – and a shady porch on the ground floor.", "It has four double bedrooms, a living room with kitchen and a bathroom, furnished in a simple, practical style. CAI trail 235 to the Col Gentile starts right here."]),
    "casa-ai-pascoli": dict(
        short="Bright, spacious apartment surrounded by the greenery of Priuso, with two bedrooms and a bathroom with a tub.",
        text=["Casa Ai Pascoli is a first-floor apartment, all on one level with generous spaces, surrounded by the greenery of the hamlet of Priuso: a few steps from the walk to the sports ground and close to the small village centre.", "It has a double bedroom and a twin room, a small sitting room, a kitchen and a bathroom with a tub. Peace and views are guaranteed, and the Monte Rest road, much loved by cyclists, starts from Priuso."]),
    "casa-vanda-iris": dict(
        short="Three bedrooms and a large, convivial kitchen in the 18th-century villa in Viaso, for up to 6 guests.",
        text=["Iris has a double bedroom with an extra single bed, a twin room with balcony access and a single room. The large kitchen is made for time together; the living room opens onto the wooden terrace, with a touch of red in the linen and curtains. TV in every room.", VILLA_EN]),
    "casa-vanda-bucaneve": dict(
        short="4-star apartment in green and white with a large wooden terrace, in the historic villa in Viaso.",
        text=["Bucaneve has a bedroom, a bathroom and a large living room with kitchen opening onto the big wooden terrace. Green and white tie the furnishings together and give the apartment a fresh, springtime feel.", VILLA_EN]),
    "casa-vanda-papavero": dict(
        short="4-star apartment in warm red tones, with a living room opening onto the wooden terrace, in Viaso.",
        text=["Papavero has a bedroom, a bathroom, a kitchen and a large living room that opens onto the wooden terrace. The red of the linen and curtains brings a joyful summer feeling.", VILLA_EN]),
    "casa-vanda-genziana": dict(
        short="Two bedrooms and a large living room on the wooden terrace: a 4-star family apartment in Viaso.",
        text=["Genziana has two bedrooms, a bathroom, a kitchen with dining table and a large living room with access to the wooden terrace. Blue and grey throughout the furnishings give it a warm, homely feel.", VILLA_EN]),
    "casa-vanda-ortensia": dict(
        short="Ground-floor apartment in the villa in Viaso, with kitchen, small sitting room, a double and a single bedroom, for up to 4 guests.",
        text=["Ortensia is on the ground floor of Casa Vanda, in the quiet hamlet of Viaso: a welcoming, comfortable space for a relaxing stay, immersed in the authentic atmosphere of the area.",
              "It has a kitchen with living area – a practical, pleasant space to cook and spend time together – a double bedroom, a single bedroom and a charming little sitting room for reading or resting. The house's original beams and stone frame the rooms, and the door opens onto the cobbled courtyard with its garden.",
              "Its layout makes it ideal for couples, small families or anyone who wants to feel at home away from home.", VILLA_EN]),
    "ernesto-da-rosuline-1": dict(
        short="First-floor apartment with two bedrooms and a large terrace, in the village of Lungis.",
        text=["On the first floor: two bedrooms, a living room with kitchenette, the bathroom and a large terrace. Furnished in a simple, practical style, with a shared garden."]),
    "ernesto-da-rosuline-2": dict(
        short="Second-floor apartment with a panoramic terrace over the mountains of Carnia, in Lungis.",
        text=["On the second floor: a bedroom, a living room with kitchenette, the bathroom and a large panoramic terrace. Furnished in a simple, practical style, with a shared garden."]),
    "ernesto-da-rosuline-3": dict(
        short="Top-floor apartment looking over the rooftops of Lungis, for families of up to 5.",
        text=["On the top floor: a bedroom, an open sleeping area, a living room with kitchenette and the bathroom, looking over the village rooftops. Furnished in a simple, practical style, with a shared garden."]),
    "ernesto-da-rosuline-terra-0": dict(
        short="Ground-floor studio for two with access to the garden: a romantic hideaway in the village of Lungis.",
        text=["On the ground floor, a studio for two: a single room with kitchenette and bathroom, furnished in a simple, practical style, with access to the shared garden. Perfect for a couple looking for silence with trails right outside the door."]),
    "casa-rovedo": dict(
        short="Detached three-storey house with a large private garden and terraces over the valley, in Feltrone.",
        text=["Casa Rovedo is in Feltrone, the highest hamlet of Socchieve, at the end of an old row of houses. Recently renovated, it spreads over three floors and sits in a large private garden; each floor has its own terrace overlooking the valley.", "Two bedrooms, a kitchen and a bathroom, furnished in a simple, practical style. The property has two separate entrances."]),
    "casa-dal-miedi": dict(
        short="Apartment with a large terrace in the centre of Mediis, next to the reception and the village services.",
        text=["On the first floor of a recently built block, next to the Mediis town hall and above the village pharmacy: very convenient, with a bar, petrol station and bus stop close by and the albergo diffuso reception on the same street.", "Two bedrooms, one with bunk beds, a living room with kitchenette, the bathroom and a large terrace with a view over the valley."]),
}

STAYS_DE = {
    "casa-vanda": dict(
        short="Die ganze Villa aus dem 18. Jahrhundert in Viaso, aus Stein mit Holzbalkonen: fünf Wohnungen für große Familien und Gruppen bis 18 Personen.",
        text=[VILLA_DE, "Wer die ganze Residenz bucht, hat alle Wohnungen der Villa für sich – Iris, Genziana, Bucaneve, Papavero und Ortensia –, jede liebevoll rund um die Farbe eingerichtet, die ihr den Namen gibt. Ideal für Großfamilien, Freundesgruppen, Vereine und Seminare."]),
    "casa-ernesto-da-rosuline": dict(
        short="Das ganze Haus in Lungis mit seinen vier Wohneinheiten: die Lösung für große Gruppen in Karnien.",
        text=["Das Haus in Lungis vereint vier schlicht und zweckmäßig eingerichtete Wohneinheiten: das Studio im Erdgeschoss und drei Wohnungen in den oberen Stockwerken, mit Terrassen mit Blick auf das Dorf und die Berge.", "Als Ganzes gebucht ist es ideal für große Gruppen, Großfamilien, Sportmannschaften und Vereine. Im Dorf beginnt der Rundweg Anello delle Frazioni, und Bar mit Lebensmittelladen und Agriturismo sind nur ein paar Schritte entfernt."]),
    "casa-pradin": dict(
        short="Das alte Dorfgasthaus von Feltrone, auf drei Etagen mit Holzterrassen: vier Doppelzimmer für Gruppen und große Familien.",
        text=["Casa Pradin liegt in Feltrone, dem höchsten Ortsteil von Socchieve (769 m), knapp unterhalb der Dorfkirche. Früher war es das Gasthaus des Dorfes; heute ist es ein renoviertes Gebäude auf drei Etagen mit Holzterrassen auf jedem Stockwerk – die im ersten und zweiten sind verbunden – und einem schattigen Laubengang im Erdgeschoss.", "Die Einheit hat vier Doppelzimmer, einen Wohnraum mit Küche und ein Bad, schlicht und zweckmäßig eingerichtet. Von hier führt der CAI-Weg 235 auf den Col Gentile."]),
    "casa-ai-pascoli": dict(
        short="Helle, geräumige Wohnung im Grünen von Priuso, mit zwei Schlafzimmern und Bad mit Badewanne.",
        text=["Casa Ai Pascoli ist eine Wohnung im ersten Stock, großzügig auf einer Ebene, im Grünen des Ortsteils Priuso: nur ein paar Schritte vom Spazierweg zum Sportplatz und nah am kleinen Ortskern.", "Sie hat ein Doppelzimmer und ein Zweibettzimmer, ein kleines Wohnzimmer, eine Küche und ein Bad mit Badewanne. Ruhe und Aussicht sind garantiert, und in Priuso beginnt die bei Radfahrern beliebte Straße auf den Monte Rest."]),
    "casa-vanda-iris": dict(
        short="Drei Schlafzimmer und eine große, gesellige Küche in der Villa aus dem 18. Jahrhundert in Viaso, für bis zu 6 Gäste.",
        text=["Iris hat ein Doppelzimmer mit zusätzlichem Einzelbett, ein Zweibettzimmer mit Zugang zum Balkon und ein Einzelzimmer. Die große Küche ist wie gemacht für gesellige Stunden; das Wohnzimmer öffnet sich zur Holzterrasse, mit roten Akzenten bei Wäsche und Vorhängen. TV in allen Zimmern.", VILLA_DE]),
    "casa-vanda-bucaneve": dict(
        short="4-Sterne-Wohnung in Grün und Weiß mit großer Holzterrasse, in der historischen Villa in Viaso.",
        text=["Bucaneve hat ein Schlafzimmer, ein Bad und einen großen Wohnraum mit Küche, von dem man auf die große Holzterrasse tritt. Grün und Weiß verbinden die Einrichtung und verleihen der Wohnung eine frühlingshafte Frische.", VILLA_DE]),
    "casa-vanda-papavero": dict(
        short="4-Sterne-Wohnung in warmen Rottönen, mit Wohnzimmer zur Holzterrasse, in Viaso.",
        text=["Papavero hat ein Schlafzimmer, ein Bad, eine Küche und einen großen Wohnraum, der sich zur Holzterrasse öffnet. Das Rot von Wäsche und Vorhängen sorgt für fröhliches Sommergefühl.", VILLA_DE]),
    "casa-vanda-genziana": dict(
        short="Zwei Schlafzimmer und ein großes Wohnzimmer mit Holzterrasse: 4-Sterne-Familienwohnung in Viaso.",
        text=["Genziana hat zwei Schlafzimmer, ein Bad, eine Küche mit Esstisch und einen großen Wohnraum mit Zugang zur Holzterrasse. Blau und Grau in der Einrichtung schaffen eine familiäre, einladende Atmosphäre.", VILLA_DE]),
    "casa-vanda-ortensia": dict(
        short="Wohnung im Erdgeschoss der Villa in Viaso, mit Küche, kleinem Wohnzimmer, einem Doppel- und einem Einzelzimmer, für bis zu 4 Gäste.",
        text=["Ortensia liegt im Erdgeschoss von Casa Vanda, im ruhigen Ortsteil Viaso: eine einladende, gemütliche Wohnung für einen erholsamen Aufenthalt in der authentischen Atmosphäre der Gegend.",
              "Sie hat eine Küche mit Wohnbereich – praktisch und angenehm zum Kochen und Beisammensein –, ein Doppelzimmer, ein Einzelzimmer und ein hübsches kleines Wohnzimmer zum Lesen oder Ausruhen. Die originalen Balken und Steinmauern des Hauses rahmen die Räume, und durch die Tür gelangt man in den gepflasterten Innenhof mit Garten.",
              "Durch ihre Aufteilung ist sie ideal für Paare, kleine Familien und alle, die sich auch fern von zu Hause wie daheim fühlen möchten.", VILLA_DE]),
    "ernesto-da-rosuline-1": dict(
        short="Wohnung im ersten Stock mit zwei Schlafzimmern und großer Terrasse, im Dorf Lungis.",
        text=["Im ersten Stock: zwei Schlafzimmer, ein Wohnraum mit Kochnische, das Bad und eine große Terrasse. Schlicht und zweckmäßig eingerichtet, mit Gemeinschaftsgarten."]),
    "ernesto-da-rosuline-2": dict(
        short="Wohnung im zweiten Stock mit Panoramaterrasse über den Bergen Karniens, in Lungis.",
        text=["Im zweiten Stock: ein Schlafzimmer, ein Wohnraum mit Kochnische, das Bad und eine große Panoramaterrasse. Schlicht und zweckmäßig eingerichtet, mit Gemeinschaftsgarten."]),
    "ernesto-da-rosuline-3": dict(
        short="Wohnung im obersten Stock mit Blick über die Dächer von Lungis, für Familien bis 5 Personen.",
        text=["Im obersten Stock: ein Schlafzimmer, ein offener Schlafbereich, ein Wohnraum mit Kochnische und das Bad, mit Blick über die Dächer des Dorfes. Schlicht und zweckmäßig eingerichtet, mit Gemeinschaftsgarten."]),
    "ernesto-da-rosuline-terra-0": dict(
        short="Studio für zwei im Erdgeschoss mit Zugang zum Garten: das romantische Refugium im Dorf Lungis.",
        text=["Im Erdgeschoss ein Studio für zwei: ein einziger Raum mit Kochnische und Bad, schlicht und zweckmäßig eingerichtet, mit Zugang zum Gemeinschaftsgarten. Perfekt für ein Paar, das Stille sucht und die Wanderwege direkt vor der Tür hat."]),
    "casa-rovedo": dict(
        short="Freistehendes Haus auf drei Etagen mit großem Privatgarten und Terrassen mit Talblick, in Feltrone.",
        text=["Casa Rovedo liegt in Feltrone, dem höchsten Ortsteil von Socchieve, am Ende einer alten Häuserzeile. Vor Kurzem renoviert, erstreckt es sich über drei Etagen inmitten eines großen Privatgartens; jedes Stockwerk hat seine eigene Terrasse mit Blick ins Tal.", "Zwei Schlafzimmer, eine Küche und ein Bad, schlicht und zweckmäßig eingerichtet. Das Haus hat zwei getrennte Eingänge."]),
    "casa-dal-miedi": dict(
        short="Wohnung mit großer Terrasse im Zentrum von Mediis, neben der Rezeption und den Einrichtungen des Dorfes.",
        text=["Im ersten Stock eines neueren Gebäudes, neben dem Rathaus von Mediis und über der Dorfapotheke: sehr praktisch, mit Bar, Tankstelle und Bushaltestelle ganz in der Nähe und der Rezeption des Albergo Diffuso in derselben Straße.", "Zwei Schlafzimmer, eines davon mit Etagenbetten, ein Wohnraum mit Kochnische, das Bad und eine große Terrasse mit Blick ins Tal."]),
}

VILLAGES_EN = {
    "viaso": dict(
        t="Viaso sits where the trails linking the hamlets of the municipality meet, and it surprises with how well it stays hidden while being so close to Socchieve. The mountain-bike route runs through it and, with the La Baita restaurant, it is a safe harbour for lovers of food and wine tourism.",
        locali=["La Baita restaurant"]),
    "lungis": dict(
        t="Like nearby Feltrone, Lungis is crossed by many trails, including the mountain-bike route that links all the hamlets of the municipality. The village has the In Già farm restaurant and the Al Cervo bar and restaurant, and it is the starting point of the Anello delle Frazioni.",
        locali=["In Già farm restaurant (agriturismo)", "Al Cervo bar and restaurant · tel. 0433 80007"]),
    "feltrone-e-dilignidis": dict(
        f=dict(lo="in Lungis"),
        t="The highest hamlet of the municipality. Many trails cross Feltrone, but the most important is the route that climbs to the Col Gentile and continues to Prato Carnico in Val Pesarina: CAI trail 235 passes through unspoilt places of extraordinary beauty such as the Forca di Pani. With 1,350 metres of ascent over 23 km – about 7 hours on foot – it is for fit walkers. The reception can arrange a minibus back.",
        locali=["In Già farm restaurant in Lungis (2 km)", "Al Cervo bar and restaurant in Lungis (2 km)"]),
    "mediis": dict(
        t="The Mediis mountain-bike circuit starts here and the well-known Anello delle Frazioni passes through. The village, which once vied with Socchieve to be the main town, is central to almost all the hamlets and overlooks the Lumiei as it flows into the Tagliamento. This is where the albergo diffuso reception is.",
        locali=["Bar alla Posta · via Roma 10 · tel. 0433 80072 · SAF bus tickets and petrol station"]),
    "dilignidis": dict(
        t="Very close to Feltrone, Dilignidis shares its trails and services: the Anello delle Frazioni and the Mediis mountain-bike route both cross it. There are no albergo diffuso houses here: the nearest are in Feltrone, a few minutes' walk away.",
        locali=["In Già farm restaurant in Lungis (2 km)", "Al Cervo bar and restaurant in Lungis (2 km)"]),
    "nonta": dict(
        t="Nonta is small and elusive, just as its castle must once have been. The road from Mediis to Socchieve only skirts it and, even along via San Maurizio, the village seems impenetrable: like its lake, it is there but you can't see it. On the other hand, the Osteria di Nonta, said to date back to the 17th century, is famous throughout the area for its traditional Carnic cooking.",
        locali=["Osteria di Nonta · tel. 0433 80596"]),
    "priuso": dict(
        t="The SR 552 starts in Priuso and climbs to Monte Rest, linking Socchieve with Tramonti di Sopra: a winding road and a fine cycling route, with steady gradients up to the pass at over a thousand metres. From there you can continue on foot along CAI trail 826 or ride down towards Tramonti and Meduno. The Caprizzi area is full of trails and views, with its lake and, in summer, the Rifugio Grasia and its home cooking.",
        locali=["Osteria Monte Corona", "Gino bar with kitchen and grocery · via G. Marconi 22 · tel. 0433 80009"],
        servizi=["Football pitch", "Roller-skating rink", "Playground"]),
    "socchieve": dict(
        t="The main village of the municipality offers the most services, places to eat and cultural sights, such as the Church of San Martino and, in summer, the Rassegna Carnica Arte Cultura Lavoro. Its two trails branch into lanes and paths spreading across the countryside, where in Roman times, so the story goes, vines and olives were grown.",
        locali=["Bar La Stella"]),
}

VILLAGES_DE = {
    "viaso": dict(
        t="Viaso liegt dort, wo sich die Wege zwischen den Ortsteilen der Gemeinde kreuzen, und überrascht damit, wie gut es verborgen bleibt, obwohl es ganz nah bei Socchieve liegt. Die Mountainbike-Strecke führt hindurch, und mit dem Restaurant La Baita ist es ein sicherer Hafen für Genießer.",
        locali=["Restaurant La Baita"]),
    "lungis": dict(
        t="Wie das benachbarte Feltrone wird Lungis von vielen Wegen durchzogen, darunter die Mountainbike-Strecke, die alle Ortsteile der Gemeinde verbindet. Im Dorf gibt es den Agriturismo In Già und die Bar und Restaurant Al Cervo, und hier beginnt der Rundweg Anello delle Frazioni.",
        locali=["Agriturismo In Già", "Bar und Restaurant Al Cervo · Tel. 0433 80007"]),
    "feltrone-e-dilignidis": dict(
        f=dict(lo="in Lungis"),
        t="Der höchste Ortsteil der Gemeinde. Durch Feltrone führen viele Wege, doch der wichtigste steigt zum Col Gentile auf und führt weiter bis Prato Carnico im Val Pesarina: Der CAI-Weg 235 durchquert unberührte Orte von außergewöhnlicher Schönheit wie die Forca di Pani. Mit 1350 Höhenmetern auf 23 km – rund 7 Stunden Gehzeit – ist er für trainierte Wanderer geeignet. Die Rückfahrt im Kleinbus lässt sich an der Rezeption organisieren.",
        locali=["Agriturismo In Già in Lungis (2 km)", "Bar und Restaurant Al Cervo in Lungis (2 km)"]),
    "mediis": dict(
        t="In Mediis beginnt der gleichnamige Mountainbike-Rundkurs, und auch der bekannte Anello delle Frazioni führt hier vorbei. Das Dorf, das Socchieve einst den Rang als Hauptort streitig machte, liegt zentral zu fast allen Ortsteilen und überblickt den Lauf des Lumiei, der hier in den Tagliamento mündet. Hier befindet sich die Rezeption des Albergo Diffuso.",
        locali=["Bar alla Posta · via Roma 10 · Tel. 0433 80072 · SAF-Busfahrkarten und Tankstelle"]),
    "dilignidis": dict(
        t="Ganz nah bei Feltrone teilt Dilignidis dessen Wege und Einrichtungen: Der Anello delle Frazioni und die Mountainbike-Strecke von Mediis führen hindurch. Häuser des Albergo Diffuso gibt es hier nicht; die nächsten liegen wenige Gehminuten entfernt in Feltrone.",
        locali=["Agriturismo In Già in Lungis (2 km)", "Bar und Restaurant Al Cervo in Lungis (2 km)"]),
    "nonta": dict(
        t="Nonta ist klein und schwer zu fassen, so wie es einst seine Burg gewesen sein muss. Die Straße von Mediis nach Socchieve streift es nur, und selbst auf der via San Maurizio wirkt das Dorf unzugänglich: Wie sein See ist es da, aber man sieht es nicht. Dafür ist die Osteria di Nonta, die angeblich aus dem 17. Jahrhundert stammt, in der ganzen Gegend für ihre traditionelle karnische Küche bekannt.",
        locali=["Osteria di Nonta · Tel. 0433 80596"]),
    "priuso": dict(
        t="In Priuso beginnt die SR 552, die auf den Monte Rest führt und Socchieve mit Tramonti di Sopra verbindet: eine kurvenreiche Straße und eine reizvolle Radtour, mit gleichmäßiger Steigung bis zum Pass auf über tausend Metern. Von dort geht es zu Fuß auf dem CAI-Weg 826 weiter oder mit dem Rad hinunter nach Tramonti und Meduno. Die Gegend um Caprizzi ist reich an Wegen und Ausblicken, mit dem gleichnamigen See und im Sommer dem Rifugio Grasia mit seiner Hausmannskost.",
        locali=["Osteria Monte Corona", "Bar mit Küche und Lebensmitteln Gino · via G. Marconi 22 · Tel. 0433 80009"],
        servizi=["Fußballplatz", "Rollschuhbahn", "Spielplatz"]),
    "socchieve": dict(
        t="Der Hauptort der Gemeinde bietet die meisten Einrichtungen, Lokale und kulturellen Sehenswürdigkeiten, etwa die Kirche San Martino und im Sommer die Rassegna Carnica Arte Cultura Lavoro. Seine zwei Wege verzweigen sich in Straßen und Pfade über das Land, wo zur Römerzeit, so erzählt man, Wein und Oliven angebaut wurden.",
        locali=["Bar La Stella"]),
}

EXPS_EN = {
    "trekking": dict(
        n="Trekking",
        title="Hiking in Socchieve: 4 trails in Carnia from the villages",
        desc="Anello delle Frazioni, Anello di Fondas, Flamias and Lumiei: four loop trails starting from the houses of the Socchieve albergo diffuso, in Carnia.",
        lead="Four loop routes starting right from the villages, through meadows, mule tracks and streams.",
        intro=["Without leaving the villages of the municipality of Socchieve you can enjoy pleasant, healthy walks in a natural and human setting of great tranquillity. We have chosen four routes that can start from the house you are staying in.", "For those who want more, there is the Col Gentile crossing on CAI trail 235 from Feltrone to Prato Carnico: 23 km and 1,350 m of ascent, about 7 hours. The reception can arrange a minibus back."],
        routes=[
            dict(t="From Lungis, follow part of the Nagri trail to the Chialaria meadows and the Frizzon area; along the aqueduct road you reach Feltrone. From the lower part of the village a path leads to Dilignidis; beyond it, just past the church, take the cobbled Pecol path down to Viaso. On the paved road, near a crucifix, turn left onto the Dàs Vàls path and Mediis appears. Heading towards Ampezzo, turn right at the bridge over the Lumiei to the little Borgo Siega and climb back up the Lungjania path to Lungis."),
            dict(t="From Viaso a comfortable mule track descends to the Dusili stream, passes the ruins of the Baldo mill and, heading north, joins the paved road between Feltrone and Enemonzo. You soon reach the terraces of Feltrone; to the east an easy path descends to the Filuvigna stream, beside the farmhouse of the same name. Following MTB route no. 1 you pass a ruined house, and MTB route no. 2 takes you back to Viaso across wide meadows."),
            dict(t="From Viaso a mule track descends south to the SS52 road and the village of Socchieve. Along the main road towards Enemonzo, just before the turn-off for Preone, turn left onto a gravel road and then onto faint paths. You cross a spruce wood and, keeping left, an old lane and a cart track bring you back to the start."),
            dict(t="From Nonta, the smallest hamlet, an easy walk follows the mostly dry bed of the Lumiei. Leaving towards Mediis, a cart track on the left leads to the old summer camp where, in the 1930s and 40s, many children spent their summers. You reach Balòt, where after the war there was a carpentry workshop, a mill, a dance hall and a cinema, and then the sports area with a football pitch and children's games. Towards Socchieve, on the opposite bank, you come across fortifications; near the Puart das boras turn left and follow the riverbed back to the start."),
        ],
        note="The route descriptions come from the tourism website of the Municipality of Socchieve. Trails, mule tracks and cart tracks should be walked with care, and conditions may have changed since. The nature you will see is your friend too: respect it."),
    "cicloturismo": dict(
        n="Cycling",
        title="Cycling in Carnia: MTB in Mediis and the Passo Rest loop",
        desc="From the Mediis MTB trail to the Passo Rest loop (101 km, 2,055 m): road and mountain-bike routes based in Socchieve, close to the Zoncolan and the Crostis.",
        lead="Legendary climbs, technical gravel and quiet roads: Carnia is a paradise on two wheels.",
        intro=["Thanks to the Zoncolan and the Crostis, made famous by the Giro d'Italia, Carnia is well known to anyone who loves the great climbs of the Alps. But the whole area rises and falls through breathtaking views and unspoilt landscapes, on a network of paved and gravel roads that leaves you spoilt for choice.", "From Socchieve, with the Zoncolan about 24 km away, we suggest two routes: one off-road and one on the road."],
        routes=[
            dict(n="The Mediis MTB trail", t="The best-known mountain-bike route in Carnia, home of the Trofeo Carnia MTB. It crosses the hamlets of the municipality on dirt tracks, alternating short, sharp climbs with technical, demanding descents: ride it with care, and it will reward anyone who loves riding off-road."),
            dict(n="The Passo Rest loop", t="A loop linking the upper Pordenone area with Carnia over the Passo del Rest, which can be ridden in either direction: Socchieve, Preone and its valley, San Francesco, Anduins, Vito d'Asio, Clauzetto, Travesio, Meduno, Lake Redona, Tramonti di Sotto and di Sopra, Passo di Monte Rest, Caprizzi, Priuso, Mediis and back to Socchieve. Quiet roads and splendid natural surroundings reward the effort: for experienced cyclists, at least 5 hours.", stats=["101 km", "2,055 m of ascent", "Max gradient 20%"]),
        ],
        more=[("On the road", ["Giro di Carnia", "Giro di Carnia, Sauris variant"]), ("Mountain bike", ["Passo Pura and Monte Jouf", "Monte Pezzeit"]), ("For experts", ["Crostis and Zoncolan", "Carnia Classic Granfondo"])]),
    "arte-e-cultura": dict(
        n="Art and culture",
        title="Art and culture in Socchieve: San Martino and the Rassegna Carnica",
        desc="The Church of San Martino with its Romanesque frescoes, the Pieve di Castoia and the Rassegna Carnica Arte Cultura Lavoro: the artistic heritage of Socchieve in Carnia.",
        lead="Romanesque churches, frescoes and a festival that every summer tells the story of Carnia through the hands of its craftspeople.",
        intro=["The municipality of Socchieve holds some of the most interesting artistic gems of Carnia, such as the Church of San Martino and the Pieve di Castoia. But it is not just about the “immovable” heritage: this is where Carnia's most important festival of Art, Culture and Work takes place, with craftspeople and artists from Carnia and Friuli whose works tell the story of a land that perhaps speaks better with its hands than with words."],
        items=[
            dict(n="Church of San Martino", t=["In the centre of the village, with its back to the Castoia hill, the little church of San Martino is one of the most typically Carnic religious buildings: an entrance porch, a bell gable, a timber-trussed roof and a covering of curved tiles.", "In the sacristy and at the base of the small apse, remains of high-quality Romanesque frescoes have come to light (Christ in a mandorla with the symbols of the Evangelists, fragments of Apostles' heads, decorations), testifying to the building's age."]),
            dict(n="Rassegna Carnica Arte Cultura Lavoro", t=["Organised by the Comitato Gianfrancesco da Tolmezzo, this summer festival gives space to the culture, art and work that Carnia and Friuli have to offer: a chance to meet and share ideas, keeping attention on the small but important things of mountain life."]),
        ]),
    "visita-la-carnia": dict(
        n="Visit Carnia",
        title="What to see in Carnia near Socchieve: Sauris, the Lumiei gorge",
        desc="Sauris 18 km away, Forni di Sopra, the Lumiei gorge, Ampezzo, the Preone valley and Val Pesarina: what to see in Carnia from the Socchieve albergo diffuso.",
        lead="Eight valleys, ancient languages, Sauris ham and the Dolomites on the doorstep: Socchieve is the ideal base camp.",
        intro=["Carnia is an archipelago of small villages spread over four main valleys that open out from Tolmezzo (But, Chiarsò, Degano and Tagliamento) and four smaller ones (Valcalda, Lumiei, Pesarina and Pontaiba). A variety of landscapes and cultures that makes it a rich store of experiences for visitors.", "To the north, about 18 km away, lies Sauris with its lake, the famous Wolf ham-maker, in business since 1862, the Zahre Beer brewery, its Carnival and the Ham Festival in July. Half an hour away are the Friulian Dolomites, a UNESCO World Heritage Site, and the Varmost slope at Forni di Sopra – for walking in summer and skiing in winter – with the Dolomiti Adventure Park and its rope bridges among the trees. To the south, after a stop at the Caseificio Val Tagliamento dairy, you reach Tolmezzo, the capital of Carnia, with the Carnic Museum of Folk Arts.", "Carnia covers just 15.6% of Friuli Venezia Giulia, yet it is full of surprises and magical places where several dialects and minority languages are spoken: a land to discover and, in the end, to love."],
        items=[
            dict(n="The Lumiei gorge", t=["A canyon where the stream plunges deep into the rock, creating spectacular views – a destination for experienced trekkers and canyoning fans. The trail, one of the most striking in Carnia, once linked Ampezzo with Sauris and can be walked thanks in part to a metal bridge suspended between water and stone."]),
            dict(n="Ampezzo, Palazzo Unfer", t=["4 km from Mediis, Ampezzo – proud of the history of the Free Republic of Carnia – houses the Geological Museum of Carnia in Palazzo Unfer: rocks and fossils from one of the few areas in Europe where the paleontological heritage has been preserved so completely, with displays designed for children too. The same building holds the gallery of Marco Davanzo (1872–1955), who painted Carnia in the crystal-clear light of the mountains."]),
            dict(n="Preone and its valley", t=["A few kilometres from Socchieve, Preone sits at the entrance of a valley that seems hidden from the world, quiet and untouched between two mountains. The village itself is worth a visit, and the trails and peaks around it, where many of the fossils on display in Ampezzo were found, complete the picture."]),
            dict(n="Val Pesarina, the valley of time", t=["Bordering Socchieve along the ridge of the Col Gentile, Val Pesarina is home to the clock museum in Pesariis and to the typical architecture of the Friulian mountains, such as the famous haylofts (stavoli) of Orias."]),
        ]),
}

EXPS_DE = {
    "trekking": dict(
        n="Wandern",
        title="Wandern in Socchieve: 4 Wege in Karnien ab den Dörfern",
        desc="Anello delle Frazioni, Anello di Fondas, Flamias und Lumiei: vier Rundwege, die direkt an den Häusern des Albergo Diffuso Socchieve in Karnien beginnen.",
        lead="Vier Rundwege direkt ab den Dörfern, über Wiesen, Saumpfade und an Bächen entlang.",
        intro=["Ohne die Dörfer der Gemeinde Socchieve zu verlassen, kann man angenehme, gesunde Wanderungen in einer natürlichen und menschlichen Umgebung von großer Ruhe unternehmen. Wir haben vier Wege ausgewählt, die direkt an Ihrer Unterkunft beginnen können.", "Wer mehr sucht, wählt die Überschreitung des Col Gentile auf dem CAI-Weg 235 von Feltrone nach Prato Carnico: 23 km und 1350 Höhenmeter, rund 7 Stunden. Die Rückfahrt im Kleinbus lässt sich an der Rezeption organisieren."],
        routes=[
            dict(t="Von Lungis folgt man einem Stück des Nagri-Wegs bis zu den Wiesen von Chialaria und zur Flur Frizzon; über die Straße der Wasserleitung erreicht man Feltrone. Vom unteren Dorfteil führt ein Pfad nach Dilignidis; kurz hinter der Kirche nimmt man den gepflasterten Pecol-Weg hinunter nach Viaso. Auf der asphaltierten Straße biegt man bei einem Wegkreuz links auf den Pfad Dàs Vàls ab, und schon ist man in Mediis. Richtung Ampezzo biegt man an der Brücke über den Lumiei rechts zum kleinen Borgo Siega ab und steigt über den Lungjania-Pfad wieder nach Lungis hinauf."),
            dict(t="Von Viaso führt ein bequemer Saumpfad hinunter zum Bach Dusili, vorbei an den Ruinen der Mühle von Baldo, und trifft nach Norden auf die asphaltierte Straße zwischen Feltrone und Enemonzo. Bald erreicht man die Terrassen von Feltrone; nach Osten führt ein bequemer Pfad hinunter zum Bach Filuvigna, neben dem gleichnamigen Bauernhaus. Auf der MTB-Strecke Nr. 1 kommt man an einem verfallenen Haus vorbei, und über die Strecke Nr. 2 geht es durch weite Wiesen zurück nach Viaso."),
            dict(t="Von Viaso führt ein Saumpfad nach Süden hinunter zur Staatsstraße 52 und in den Ort Socchieve. Entlang der Staatsstraße Richtung Enemonzo biegt man kurz vor der Abzweigung nach Preone links auf einen Schotterweg und dann auf Pfadspuren ab. Man durchquert einen Fichtenwald, und links haltend bringen ein alter Weg und ein Karrenweg zurück zum Ausgangspunkt."),
            dict(t="Von Nonta, dem kleinsten Ortsteil, führt ein ruhiger Spaziergang über das fast immer trockene Bett des Lumiei. Richtung Mediis führt links ein Karrenweg zur ehemaligen Ferienkolonie, in der in den 1930er- und 40er-Jahren viele Kinder den Sommer verbrachten. Man erreicht Balòt, wo es nach dem Krieg eine Schreinerei, eine Mühle, einen Tanzsaal und ein Kino gab, und dann das Sportgelände mit Fußballplatz und Spielplatz. Richtung Socchieve trifft man am gegenüberliegenden Ufer auf Befestigungen; beim Puart das boras biegt man links ab und kehrt am Flussbett entlang zum Ausgangspunkt zurück."),
        ],
        note="Die Wegbeschreibungen stammen von der Tourismus-Website der Gemeinde Socchieve. Wege, Saumpfade und Karrenwege sind mit Vorsicht zu begehen; zwischenzeitliche Änderungen vorbehalten. Die Natur, die Sie hier erleben, ist auch Ihre Freundin: Respektieren Sie sie."),
    "cicloturismo": dict(
        n="Radfahren",
        title="Radfahren in Karnien: MTB in Mediis und die Runde über den Passo Rest",
        desc="Von der MTB-Strecke in Mediis bis zur Runde über den Passo Rest (101 km, 2055 Hm): Rennrad- und Mountainbike-Touren ab Socchieve, nahe Zoncolan und Crostis.",
        lead="Legendäre Anstiege, technische Schotterwege und ruhige Straßen: Karnien ist ein Paradies auf zwei Rädern.",
        intro=["Dank Zoncolan und Crostis, die durch den Giro d'Italia berühmt wurden, kennen alle, die die großen Anstiege der Alpen lieben, Karnien. Doch die ganze Gegend ist ein Auf und Ab zwischen atemberaubenden Ausblicken und unberührter Natur, auf einem Netz aus Asphalt- und Schotterstraßen, das die Wahl schwer macht.", "Von Socchieve aus, mit dem Zoncolan in rund 24 km Entfernung, schlagen wir zwei Touren vor: eine im Gelände und eine auf der Straße."],
        routes=[
            dict(n="Die MTB-Strecke von Mediis", t="Die bekannteste Mountainbike-Strecke Karniens, Austragungsort der Trophäe Trofeo Carnia MTB. Sie führt auf Naturwegen durch die Ortsteile der Gemeinde, mit kurzen, steilen Anstiegen und technischen, anspruchsvollen Abfahrten: Man sollte sie mit Vorsicht fahren, doch wer Gelände liebt, wird reich belohnt."),
            dict(n="Die Runde über den Passo Rest", t="Eine Runde, die das obere Pordenone-Gebiet über den Passo del Rest mit Karnien verbindet und in beide Richtungen gefahren werden kann: Socchieve, Preone und sein Tal, San Francesco, Anduins, Vito d'Asio, Clauzetto, Travesio, Meduno, Lago di Redona, Tramonti di Sotto und di Sopra, Passo di Monte Rest, Caprizzi, Priuso, Mediis und zurück nach Socchieve. Ruhige Straßen und herrliche Natur entschädigen für die Mühe: für erfahrene Radfahrer, mindestens 5 Stunden.", stats=["101 km", "2055 Höhenmeter", "Max. Steigung 20 %"]),
        ],
        more=[("Straße", ["Giro di Carnia", "Giro di Carnia, Variante Sauris"]), ("Mountainbike", ["Passo Pura und Monte Jouf", "Monte Pezzeit"]), ("Für Erfahrene", ["Crostis und Zoncolan", "Carnia Classic Granfondo"])]),
    "arte-e-cultura": dict(
        n="Kunst und Kultur",
        title="Kunst und Kultur in Socchieve: San Martino und die Rassegna Carnica",
        desc="Die Kirche San Martino mit ihren romanischen Fresken, die Pieve di Castoia und die Rassegna Carnica Arte Cultura Lavoro: das künstlerische Erbe von Socchieve in Karnien.",
        lead="Romanische Kirchen, Fresken und eine Ausstellung, die jeden Sommer Karnien durch die Hände seiner Handwerker erzählt.",
        intro=["Die Gemeinde Socchieve bewahrt einige der interessantesten Kunstschätze Karniens, etwa die Kirche San Martino und die Pieve di Castoia. Doch es gibt nicht nur das „unbewegliche“ Erbe: Hier findet die wichtigste Ausstellung für Kunst, Kultur und Arbeit Karniens statt, mit Handwerkern und Künstlern aus Karnien und dem Friaul, die mit ihren Werken von einem Land erzählen, das vielleicht mehr mit den Händen als mit Worten spricht."],
        items=[
            dict(n="Kirche San Martino", t=["Mitten im Ort, mit dem Rücken zum Hügel von Castoia, ist die kleine Kirche San Martino einer der typischsten karnischen Sakralbauten: Eingangsvorhalle, Glockengiebel, offener Dachstuhl und Deckung aus Mönch-und-Nonne-Ziegeln.", "In der Sakristei und am Sockel der kleinen Apsis kamen Reste hochwertiger romanischer Fresken zum Vorschein (Christus in der Mandorla mit den Symbolen der Evangelisten, Fragmente von Apostelköpfen, Verzierungen), die das hohe Alter des Gebäudes belegen."]),
            dict(n="Rassegna Carnica Arte Cultura Lavoro", t=["Die vom Comitato Gianfrancesco da Tolmezzo organisierte Sommerausstellung gibt der Kultur, der Kunst und der Arbeit Raum, die Karnien und das Friaul hervorbringen: ein Ort der Begegnung und des Austauschs, der den Blick auf die kleinen und wichtigen Dinge des Lebens in den Bergen lenkt."]),
        ]),
    "visita-la-carnia": dict(
        n="Karnien entdecken",
        title="Sehenswertes in Karnien bei Socchieve: Sauris, Lumiei-Schlucht",
        desc="Sauris in 18 km, Forni di Sopra, die Lumiei-Schlucht, Ampezzo, das Tal von Preone und das Val Pesarina: Ausflugsziele in Karnien ab dem Albergo Diffuso Socchieve.",
        lead="Acht Täler, alte Sprachen, Schinken aus Sauris und die Dolomiten vor der Tür: Socchieve ist das ideale Basislager.",
        intro=["Karnien ist ein Archipel kleiner Dörfer, verteilt auf vier Haupttäler, die sich von Tolmezzo aus öffnen (But, Chiarsò, Degano und Tagliamento), und vier kleinere Täler (Valcalda, Lumiei, Pesarina und Pontaiba). Eine Vielfalt an Landschaften und Kulturen, die für Besucher zu einer reichen Fundgrube an Erlebnissen wird.", "Im Norden, rund 18 km entfernt, liegt Sauris mit seinem See, dem berühmten Schinkenhersteller Wolf (seit 1862), der Brauerei Zahre Beer, dem Karneval und dem Schinkenfest im Juli. In einer halben Stunde erreicht man die Friauler Dolomiten, UNESCO-Welterbe, und die Varmost-Piste von Forni di Sopra – im Sommer zum Wandern, im Winter zum Skifahren – mit dem Dolomiti Adventure Park und seinen Hängebrücken zwischen den Bäumen. Im Süden erreicht man nach einem Halt in der Käserei Caseificio Val Tagliamento Tolmezzo, die Hauptstadt Karniens, mit dem Karnischen Museum für Volkskunst.", "Karnien macht nur 15,6 % von Friaul-Julisch Venetien aus und steckt doch voller Überraschungen und magischer Orte, an denen verschiedene Dialekte und Minderheitensprachen gesprochen werden: ein Land zum Entdecken und am Ende zum Lieben."],
        items=[
            dict(n="Die Lumiei-Schlucht", t=["Ein Canyon, in dem der Bach tief im Fels verschwindet und spektakuläre Ausblicke schafft – ein Ziel für erfahrene Wanderer und Canyoning-Fans. Der Weg, einer der eindrucksvollsten Karniens, verband einst Ampezzo mit Sauris und ist unter anderem dank einer Metallbrücke zwischen Wasser und Stein begehbar."]),
            dict(n="Ampezzo, Palazzo Unfer", t=["4 km von Mediis entfernt beherbergt Ampezzo – stolz auf die Geschichte der Freien Republik Karnien – im Palazzo Unfer das Geologische Museum Karniens: Gesteine und Fossilien aus einem der wenigen Gebiete Europas, in denen das paläontologische Erbe so vollständig erhalten ist, mit Rundgängen auch für Kinder. Im selben Palast befindet sich die Gemäldesammlung von Marco Davanzo (1872–1955), der Karnien im kristallklaren Licht der Berge malte."]),
            dict(n="Preone und sein Tal", t=["Wenige Kilometer von Socchieve entfernt liegt Preone am Eingang eines Tals, das wie vor der Welt verborgen scheint, ruhig und unberührt zwischen zwei Bergen. Schon das Dorf lohnt einen Besuch, und die Wege und Gipfel ringsum, wo viele der in Ampezzo ausgestellten Fossilien gefunden wurden, runden das Bild ab."]),
            dict(n="Val Pesarina, das Tal der Zeit", t=["Das Val Pesarina grenzt entlang des Col-Gentile-Kamms an Socchieve und bewahrt in Pesariis das Uhrenmuseum sowie die typische Architektur der Friauler Berge, etwa die berühmten Heustadel (stavoli) von Orias."]),
        ]),
}

FAQ_EN = [
    ("What is an albergo diffuso?", "It is a type of accommodation whose rooms are spread across the houses of a village instead of being in a single building. At the Albergo Diffuso Socchieve “Col Gentile” you stay in houses and apartments in the villages of Carnia, with the services of a hotel and a single reception in Mediis."),
    ("Where is Socchieve?", "Socchieve is in Carnia, in Upper Friuli (province of Udine), between the Friulian and Pesarina Dolomites, along the SS52 road from Tolmezzo to Forni di Sopra. Ampezzo is 4 km away, Tolmezzo 17 km, Sauris 18 km and Forni di Sopra 26 km."),
    ("How do I get to the albergo diffuso?", "By car: A23 motorway, exit Carnia, then the SS52 towards Tolmezzo and Forni di Sopra (about 27 km from the exit). From Cadore, take the SS52 from Forni di Sopra; from the Pordenone area, the SS552 over Monte Rest from Tramonti. The nearest airport is Trieste (about 100 km); Udine is 65 km away."),
    ("How many people can the houses sleep?", "From the studio for two at Ernesto da Rosuline Terra to apartments for 4–8 people, up to whole houses for groups: Casa Pradin (9 beds), Casa Vanda (18) and Casa Ernesto da Rosuline (21)."),
    ("Are pets allowed?", "Yes, in several houses: the Casa Vanda apartments (Iris, Genziana, Bucaneve, Papavero), the Casa Ernesto da Rosuline apartments, Casa dal Miedi and Casa Ai Pascoli are pet friendly. Please let us know when you book."),
    ("What is there to do in Socchieve?", "Hiking on trails that start from the villages, mountain biking on the Mediis trail, road cycling over the Passo Rest, Romanesque art in the Church of San Martino. Within half an hour you can reach Sauris, the Friulian Dolomites – a UNESCO World Heritage Site – and Forni di Sopra, also for skiing in winter."),
    ("Is there a sauna and wellness?", "Yes: the sauna is booked by the hour for your whole group (20 € per hour, 2 hours minimum), and forest bathing (Shinrin-yoku) with Petra lasts about two hours, for groups of up to 6 at 15 € per person, meeting at the Mediis reception."),
    ("How do I book?", "Online on the official Col Gentile system, with live availability and prices, or by writing to info@albergodiffusosocchieve.it or calling +39 0433 819934."),
]

FAQ_DE = [
    ("Was ist ein Albergo Diffuso?", "Eine Unterkunft, deren Zimmer und Wohnungen auf die Häuser eines Dorfes verteilt sind, statt in einem einzigen Gebäude zu liegen. Im Albergo Diffuso Socchieve „Col Gentile“ wohnen Sie in Häusern und Wohnungen in den Dörfern Karniens, mit dem Service eines Hotels und einer zentralen Rezeption in Mediis."),
    ("Wo liegt Socchieve?", "Socchieve liegt in Karnien im oberen Friaul (Provinz Udine), zwischen den Friauler und den Pesariner Dolomiten, an der SS52 von Tolmezzo nach Forni di Sopra. Ampezzo ist 4 km entfernt, Tolmezzo 17 km, Sauris 18 km und Forni di Sopra 26 km."),
    ("Wie komme ich zum Albergo Diffuso?", "Mit dem Auto: Autobahn A23, Ausfahrt Carnia, dann die SS52 Richtung Tolmezzo und Forni di Sopra (rund 27 km ab der Ausfahrt). Aus dem Cadore kommt man über die SS52 ab Forni di Sopra, aus dem Gebiet von Pordenone über die SS552 über den Monte Rest ab Tramonti. Der nächste Flughafen ist Triest (rund 100 km), Udine ist 65 km entfernt."),
    ("Wie viele Personen finden in den Häusern Platz?", "Vom Studio für zwei im Ernesto da Rosuline Terra über Wohnungen für 4–8 Personen bis zu ganzen Häusern für Gruppen: Casa Pradin (9 Betten), Casa Vanda (18) und Casa Ernesto da Rosuline (21)."),
    ("Sind Haustiere erlaubt?", "Ja, in mehreren Häusern: Die Wohnungen von Casa Vanda (Iris, Genziana, Bucaneve, Papavero), die von Casa Ernesto da Rosuline, Casa dal Miedi und Casa Ai Pascoli sind haustierfreundlich. Bitte geben Sie es bei der Buchung an."),
    ("Was kann man in Socchieve unternehmen?", "Wandern auf Wegen direkt ab den Dörfern, Mountainbiken auf der Strecke von Mediis, Rennradfahren über den Passo Rest, romanische Kunst in der Kirche San Martino. In einer halben Stunde erreichen Sie Sauris, die Friauler Dolomiten (UNESCO-Welterbe) und Forni di Sopra, im Winter auch zum Skifahren."),
    ("Gibt es Sauna und Wellness?", "Ja: Die Sauna wird stundenweise für die ganze Gruppe gebucht (20 € pro Stunde, mindestens 2 Stunden), und das Waldbaden (Shinrin-yoku) mit Petra dauert rund zwei Stunden, für Gruppen bis 6 Personen zu 15 € pro Person, mit Treffpunkt an der Rezeption in Mediis."),
    ("Wie buche ich?", "Online im offiziellen Buchungssystem von Col Gentile, mit Verfügbarkeit und Preisen in Echtzeit, oder per E-Mail an info@albergodiffusosocchieve.it bzw. telefonisch unter +39 0433 819934."),
]

FARIE_EN = dict(
    intro=["La Farie is a guesthouse in a restored traditional Carnic house in the village of Lungis, at 554 metres: peace and quiet, mountain views and the slow pace of a real village.",
           "The rooms have a terrace or balcony, a private bathroom with bidet, hairdryer, a flat-screen TV and free Wi-Fi. The house has a garden, a shared lounge and free private parking.",
           "La Farie is managed by the Albergo Diffuso Socchieve “Col Gentile”. For information about the property and suggestions on places to visit in Carnia, please contact the reception in Mediis."],
    am=["Italian-style sweet and savoury breakfast", "Free Wi-Fi", "Free private parking", "Terrace or balcony", "Private bathroom", "Flat-screen TV", "Garden", "Shared lounge", "Kettle", "Non-smoking rooms"],
    rules=[("Check-in", "from 15:00 to 18:00"), ("Check-out", "by 10:00"), ("Children", "welcome at any age, free cot up to 2 years"), ("Extra bed", "on request, 40 € per night"), ("Pets", "not allowed"), ("Smoking", "not allowed"), ("Parties and events", "not allowed")],
    rooms=[("Campanula", "Double room with bathroom and terrace", 2), ("Salvia", "Double room with terrace", 2),
           ("Tarassacco", "Double room with bathroom", 2), ("Centaurea", "Double room with bathroom", 4),
           ("Stella Alpina", "Apartment with a double bedroom and a single sofa bed", 3)],
    plans=["Room only", "Bed and breakfast"],
    cancel="Free cancellation through the booking portal up to 7 days before arrival, by 18:00.",
    near=[("Arta Terme spa", "25 km"), ("Roman forum of Zuglio", "23 km"), ("Sauris", "18 km"), ("Trieste airport", "105 km")],
)

FARIE_DE = dict(
    intro=["La Farie ist ein Gästehaus in einem restaurierten, typisch karnischen Haus im Dorf Lungis, auf 554 Metern Höhe: Ruhe, Blick auf die Berge und der langsame Rhythmus eines echten Dorfes.",
           "Die Zimmer haben Terrasse oder Balkon, ein eigenes Bad mit Bidet, Haartrockner, Flachbild-TV und kostenloses WLAN. Zum Haus gehören ein Garten, ein Gemeinschaftsraum und ein kostenloser Privatparkplatz.",
           "La Farie wird vom Albergo Diffuso Socchieve „Col Gentile“ geführt. Für Informationen zur Unterkunft und Tipps zu Ausflugszielen in Karnien wenden Sie sich bitte an die Rezeption in Mediis."],
    am=["Italienisches Frühstück mit süßen und herzhaften Speisen", "Kostenloses WLAN", "Kostenloser Privatparkplatz", "Terrasse oder Balkon", "Eigenes Bad", "Flachbild-TV", "Garten", "Gemeinschaftsraum", "Wasserkocher", "Nichtraucherzimmer"],
    rules=[("Anreise", "von 15:00 bis 18:00 Uhr"), ("Abreise", "bis 10:00 Uhr"), ("Kinder", "in jedem Alter willkommen, Babybett bis 2 Jahre kostenlos"), ("Zustellbett", "auf Anfrage, 40 € pro Nacht"), ("Haustiere", "nicht gestattet"), ("Rauchen", "nicht gestattet"), ("Partys und Veranstaltungen", "nicht gestattet")],
    rooms=[("Campanula", "Doppelzimmer mit Bad und Terrasse", 2), ("Salvia", "Doppelzimmer mit Terrasse", 2),
           ("Tarassacco", "Doppelzimmer mit Bad", 2), ("Centaurea", "Doppelzimmer mit Bad", 4),
           ("Stella Alpina", "Wohnung mit Doppelzimmer und Einzel-Schlafsofa", 3)],
    plans=["Übernachtung", "Übernachtung mit Frühstück"],
    cancel="Kostenlose Stornierung über das Buchungsportal bis 7 Tage vor Anreise, bis 18:00 Uhr.",
    near=[("Therme Arta Terme", "25 km"), ("Römisches Forum von Zuglio", "23 km"), ("Sauris", "18 km"), ("Flughafen Triest", "105 km")],
)

SERVICES_EN = {
    "bagno-di-bosco": dict(
        n="Forest bathing",
        title="Forest bathing in Carnia (Shinrin-yoku) with a guide in Socchieve",
        desc="Forest bathing (Shinrin-yoku) in the woods of Socchieve, Carnia, with Petra: about 2 hours of slow immersion in nature, groups of up to 6, 15 € per person.",
        lead="Shinrin-yoku, or forest bathing: a slow, sensory immersion in the woods of Carnia to restore body and mind.",
        text=["Forest bathing, known in Japanese as Shinrin-yoku, is a wellbeing practice based on slow, mindful and sensory immersion in the forest, to restore body and mind.",
              "With Petra you walk and pause in the woods around the villages of Socchieve: an experience that helps you slow down, step away from the rush and reawaken your senses through deep contact with nature. You spend about two hours together, in small groups."],
        facts=[("2 hours", "approx., together"), ("15 €", "per person"), ("6", "people max."), ("Mediis", "meet at the reception")],
        meeting="Albergo Diffuso Col Gentile reception, Via Roma 20, Mediis di Socchieve",
        bring=[("Layered clothing", "comfortable and breathable, suitable for outdoors"), ("Waterproof or windproof jacket", "for changes in the weather"), ("Hiking boots or trainers", "to walk safely on the forest floor"), ("Water bottle", "to stay hydrated"), ("Blanket or small waterproof mat", "to sit or lie on the ground"), ("Insect repellent", "if you like"), ("A light snack", ""), ("Notebook and pen", "optional, to jot down thoughts and feelings")],
        note="To get the most out of forest bathing, your phone stays on silent or airplane mode during the practice: let anyone who needs to know that you will be unreachable for a couple of hours.",
        unit="per person"),
    "sauna": dict(
        n="Sauna",
        title="Sauna in Socchieve, Carnia · Albergo Diffuso Col Gentile",
        desc="A sauna for your group at the Albergo Diffuso in Socchieve, Carnia: 20 € per hour for the whole booking, from 2 hours, after a day on the trails.",
        lead="Dry heat after a day on the trails, for as long as you choose.",
        text=["After a hike, a day on the bike or on the slopes of Forni di Sopra, the sauna is the best way to loosen your muscles and slow down.",
              "It is booked by the hour for the whole group: the price is for the booking, not per person. Two hours minimum, then you decide how long to stay."],
        facts=[("20 €", "per hour, for the group"), ("2 hours", "minimum"), ("1 hour ahead", "minimum notice to book"), ("Socchieve", "Albergo Diffuso")],
        unit="per hour, total price"),
}

SERVICES_DE = {
    "bagno-di-bosco": dict(
        n="Waldbaden",
        title="Waldbaden in Karnien (Shinrin-yoku) mit Begleitung in Socchieve",
        desc="Waldbaden (Shinrin-yoku) in den Wäldern von Socchieve, Karnien, mit Petra: rund 2 Stunden langsames Eintauchen in die Natur, Gruppen bis 6 Personen, 15 € pro Person.",
        lead="Shinrin-yoku oder Waldbaden: ein langsames, sinnliches Eintauchen in die Wälder Karniens, das Körper und Geist erholt.",
        text=["Waldbaden, auf Japanisch Shinrin-yoku, ist eine Wohlfühlpraxis, die auf dem langsamen, achtsamen und sinnlichen Eintauchen in den Wald beruht und Körper und Geist erholt.",
              "Mit Petra gehen und verweilen Sie in den Wäldern rund um die Dörfer von Socchieve: ein Erlebnis, um langsamer zu werden, Abstand von der Hektik zu gewinnen und die Sinne durch den tiefen Kontakt mit der Natur neu zu wecken. Sie verbringen rund zwei Stunden gemeinsam, in kleinen Gruppen."],
        facts=[("2 Std.", "ca., gemeinsam"), ("15 €", "pro Person"), ("6", "Personen max."), ("Mediis", "Treffpunkt Rezeption")],
        meeting="Rezeption Albergo Diffuso Col Gentile, Via Roma 20, Mediis di Socchieve",
        bring=[("Kleidung im Zwiebellook", "bequem, atmungsaktiv und für draußen geeignet"), ("Regen- oder Windjacke", "für Wetterwechsel"), ("Wander- oder Turnschuhe", "für sicheren Tritt auf dem Waldboden"), ("Trinkflasche", "um genug zu trinken"), ("Decke oder kleine wasserdichte Matte", "zum Sitzen oder Liegen am Boden"), ("Insektenschutz", "nach Wunsch"), ("Ein leichter Snack", ""), ("Notizbuch und Stift", "optional, für Gedanken und Eindrücke")],
        note="Damit Sie das Waldbaden ganz erleben, bleibt das Handy während der Übung stumm oder im Flugmodus: Sagen Sie allen Bescheid, die es wissen müssen, dass Sie ein paar Stunden nicht erreichbar sind.",
        unit="pro Person"),
    "sauna": dict(
        n="Sauna",
        title="Sauna in Socchieve, Karnien · Albergo Diffuso Col Gentile",
        desc="Sauna für Ihre Gruppe im Albergo Diffuso in Socchieve, Karnien: 20 € pro Stunde für die ganze Buchung, ab 2 Stunden, nach einem Tag auf den Wanderwegen.",
        lead="Trockene Wärme nach einem Tag auf den Wanderwegen, so lange Sie möchten.",
        text=["Nach einer Wanderung, einem Tag auf dem Rad oder auf den Pisten von Forni di Sopra ist die Sauna der beste Weg, die Muskeln zu lockern und zur Ruhe zu kommen.",
              "Sie wird stundenweise für die ganze Gruppe gebucht: Der Preis gilt pro Buchung, nicht pro Person. Mindestens zwei Stunden, danach bestimmen Sie, wie lange Sie bleiben."],
        facts=[("20 €", "pro Stunde, für die Gruppe"), ("2 Stunden", "Minimum"), ("1 Std. vorher", "Mindestvorlauf für die Buchung"), ("Socchieve", "Albergo Diffuso")],
        unit="pro Stunde, Gesamtpreis"),
}

CONTENT = {
    "en": dict(stays=STAYS_EN, villages=VILLAGES_EN, exps=EXPS_EN, faq=FAQ_EN, farie=FARIE_EN, services=SERVICES_EN),
    "de": dict(stays=STAYS_DE, villages=VILLAGES_DE, exps=EXPS_DE, faq=FAQ_DE, farie=FARIE_DE, services=SERVICES_DE),
}


# ---------------------------------------------------------------- pagine legali (versione 1.0)
# Traduzioni dei testi legali di build_legal(). Per ogni pagina: (title, description, html).
# Segnaposto per i link: {privacy} {cookies} {booking} {terms} e {original} (la stessa pagina in italiano).
# Se cambia il testo italiano, aggiornare anche qui e il numero di versione.
_H1 = '<h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">'
_OPEN = '<section class="d-body" style="padding-top:140px"><div class="wrap prose">\n'
_CLOSE = "\n</div></section>"
_MAIL = '<a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a>'
_TEL = '<a href="tel:+390433819934">+39 0433 819934</a>'
_NOTE_EN = '<p><em>This is a translation provided for convenience. In case of any discrepancy, the <a href="{original}">Italian version</a> prevails.</em></p>'
_NOTE_DE = '<p><em>Dies ist eine Übersetzung zu Ihrer Information. Bei Abweichungen gilt die <a href="{original}">italienische Fassung</a>.</em></p>'
_VER_EN = "<p><strong>Version 1.0 · 16 November 2026</strong></p>"
_VER_DE = "<p><strong>Version 1.0 · 16. November 2026</strong></p>"

LEGAL = {"en": {}, "de": {}}

LEGAL["en"]["privacy"] = ("Privacy · Albergo Diffuso Socchieve", "GDPR privacy notice for guests, enquiries, bookings and services of the Albergo Diffuso Socchieve.", _OPEN + f"""<span class="eyebrow">Information</span>{_H1}Privacy</h1>
<p><strong>Version 1.1 · 16 November 2026</strong></p>
{_NOTE_EN}
<p>This notice covers the website of the Albergo Diffuso Socchieve “Col Gentile”, its contact forms and enquiries relating to stays and services. It is provided under Regulation (EU) 2016/679 (GDPR).</p>
<h2>1. Data controller</h2>
<p><strong>Zanier Lucio</strong> · Albergo Diffuso Socchieve “Col Gentile” · Via Roma 20, Mediis, 33020 Socchieve (UD), Italy · VAT no. 02790180307. Email: {_MAIL} · Phone: {_TEL}.</p>
<h2>2. Data processed</h2>
<p>The contact forms may ask for your full name, email address, phone number (optional), message and details of the property or service your enquiry refers to. For bookings and stays we may process identification and contact details, dates, number of guests, preferences, and information needed for the booking and for legal obligations. The servers may log technical access data, including IP address, date, time and resources requested.</p>
<h2>3. Purposes and legal bases</h2>
<p>Data is used to answer enquiries and prepare quotes (pre-contractual measures), to manage bookings, stays and purchased services (performance of a contract), to comply with tax, administrative and public-security obligations (legal obligation), and to protect the security of the website and prevent abuse or spam (legitimate interest). The forms described here are not used for marketing, unless you receive separate specific information.</p>
<h2>4. Bookings, payments and guarantee card</h2>
<p>Bookings for the Col Gentile houses go through <strong>Slope</strong>; bookings for La Farie, the sauna and forest bathing go through <strong>Welora</strong>. When you use an external booking or payment system, the data you enter there is also processed by the providers involved, according to their respective roles and privacy notices. The website's contact form does not ask for your credit card number. The terms of the guarantee card and of any charges are shown in the booking process and in the <a href="{{booking}}">booking terms</a>.</p>
<h2>5. Recipients and external tools</h2>
<p>Where necessary, data may be shared with hosting and email providers, booking and payment services, authorised staff, advisers and, where required by law, the authorities. The website may link to OpenStreetMap maps, 360° tours using external libraries and other third-party content or services. When these resources are loaded, their providers may receive technical connection data. Only with the consent given in the cookie banner does the website use Google Analytics 4 (Google Ireland Limited) for aggregate visit statistics; consent can be withdrawn at any time from “Cookie preferences”. Details in the <a href="{{cookies}}">Cookie Policy</a>.</p>
<h2>6. Retention and security</h2>
<p>Enquiries are kept for as long as needed to reply and to manage any subsequent relationship; booking and administrative data for the periods required by applicable law. Appropriate technical and organisational measures are in place to protect personal data.</p>
<h2>7. International transfers</h2>
<p>The use of external services may involve transfers of data outside the European Economic Area. Where they occur, such transfers must take place with the safeguards provided for by the GDPR.</p>
<h2>8. Your rights</h2>
<p>You can request access, rectification, erasure, restriction, portability or object to processing in the cases provided for by law, and you can withdraw any consent without affecting the lawfulness of earlier processing. To exercise your rights, write to {_MAIL}. You can lodge a complaint with the Italian Data Protection Authority (Garante per la protezione dei dati personali).</p>
<h2>9. Cookies and updates</h2>
<p>For information on cookies and integrated services, see the <a href="{{cookies}}">Cookie Policy</a>. This notice may be updated; the current version is published on this page.</p>""" + _CLOSE)

LEGAL["de"]["privacy"] = ("Datenschutz · Albergo Diffuso Socchieve", "Datenschutzerklärung nach DSGVO für Gäste, Anfragen, Buchungen und Angebote des Albergo Diffuso Socchieve.", _OPEN + f"""<span class="eyebrow">Information</span>{_H1}Datenschutz</h1>
<p><strong>Version 1.1 · 16. November 2026</strong></p>
{_NOTE_DE}
<p>Diese Erklärung betrifft die Website des Albergo Diffuso Socchieve „Col Gentile“, die Kontaktformulare und Anfragen zu Aufenthalten und Angeboten. Sie erfolgt gemäß der Verordnung (EU) 2016/679 (DSGVO).</p>
<h2>1. Verantwortlicher</h2>
<p><strong>Zanier Lucio</strong> · Albergo Diffuso Socchieve „Col Gentile“ · Via Roma 20, Mediis, 33020 Socchieve (UD), Italien · USt-IdNr. 02790180307. E-Mail: {_MAIL} · Telefon: {_TEL}.</p>
<h2>2. Verarbeitete Daten</h2>
<p>In den Kontaktformularen können Vor- und Nachname, E-Mail-Adresse, Telefonnummer (optional), Nachricht sowie Angaben zur Unterkunft oder zum Angebot abgefragt werden, auf die sich die Anfrage bezieht. Für Buchungen und Aufenthalte können Identifikations- und Kontaktdaten, Reisedaten, Anzahl der Gäste, Wünsche sowie Angaben verarbeitet werden, die für die Buchung und die gesetzlichen Pflichten nötig sind. Die Server können technische Zugriffsdaten protokollieren, darunter IP-Adresse, Datum, Uhrzeit und abgerufene Ressourcen.</p>
<h2>3. Zwecke und Rechtsgrundlagen</h2>
<p>Die Daten werden verwendet, um Anfragen zu beantworten und Angebote zu erstellen (vorvertragliche Maßnahmen), Buchungen, Aufenthalte und gebuchte Leistungen abzuwickeln (Vertragserfüllung), steuerliche, verwaltungsrechtliche und melderechtliche Pflichten zu erfüllen (rechtliche Verpflichtung) sowie die Sicherheit der Website zu schützen und Missbrauch oder Spam zu verhindern (berechtigtes Interesse). Über die beschriebenen Formulare findet keine Werbung statt, sofern nicht gesondert darüber informiert wird.</p>
<h2>4. Buchungen, Zahlungen und Kreditkarte als Garantie</h2>
<p>Buchungen der Häuser von Col Gentile laufen über <strong>Slope</strong>, Buchungen von La Farie, Sauna und Waldbaden über <strong>Welora</strong>. Wenn Sie ein externes Buchungs- oder Zahlungssystem nutzen, werden die dort eingegebenen Daten auch von den beteiligten Anbietern gemäß ihrer jeweiligen Rolle und Datenschutzhinweise verarbeitet. Das Kontaktformular der Website fragt keine Kreditkartennummer ab. Die Bedingungen der Kreditkartengarantie und möglicher Belastungen werden im Buchungsablauf und in den <a href="{{booking}}">Buchungsbedingungen</a> angegeben.</p>
<h2>5. Empfänger und externe Dienste</h2>
<p>Die Daten können, soweit nötig, an Hosting- und E-Mail-Anbieter, Buchungs- und Zahlungsdienste, befugte Mitarbeitende, Berater sowie in gesetzlich vorgesehenen Fällen an Behörden weitergegeben werden. Die Website kann OpenStreetMap-Karten, 360°-Rundgänge mit externen Bibliotheken und andere Inhalte oder Dienste Dritter einbinden. Wenn diese Ressourcen geladen werden, können deren Anbieter technische Verbindungsdaten erhalten. Nur mit der im Cookie-Banner erteilten Einwilligung nutzt die Website Google Analytics 4 (Google Ireland Limited) für zusammengefasste Besuchsstatistiken; die Einwilligung kann jederzeit über „Cookie-Einstellungen“ widerrufen werden. Einzelheiten in den <a href="{{cookies}}">Cookie-Hinweisen</a>.</p>
<h2>6. Speicherdauer und Sicherheit</h2>
<p>Anfragen werden so lange gespeichert, wie es für die Antwort und eine eventuelle weitere Geschäftsbeziehung nötig ist; Buchungs- und Verwaltungsdaten für die gesetzlich vorgeschriebenen Fristen. Zum Schutz personenbezogener Daten werden angemessene technische und organisatorische Maßnahmen getroffen.</p>
<h2>7. Internationale Übermittlungen</h2>
<p>Die Nutzung externer Dienste kann Datenübermittlungen außerhalb des Europäischen Wirtschaftsraums mit sich bringen. In diesem Fall müssen sie mit den in der DSGVO vorgesehenen Garantien erfolgen.</p>
<h2>8. Ihre Rechte</h2>
<p>Sie können in den gesetzlich vorgesehenen Fällen Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit verlangen oder der Verarbeitung widersprechen und erteilte Einwilligungen widerrufen, ohne dass die Rechtmäßigkeit der bisherigen Verarbeitung berührt wird. Schreiben Sie dazu an {_MAIL}. Sie können Beschwerde bei der italienischen Datenschutzbehörde (Garante per la protezione dei dati personali) einlegen.</p>
<h2>9. Cookies und Aktualisierungen</h2>
<p>Informationen zu Cookies und eingebundenen Diensten finden Sie in den <a href="{{cookies}}">Cookie-Hinweisen</a>. Diese Erklärung kann aktualisiert werden; die gültige Fassung ist auf dieser Seite veröffentlicht.</p>""" + _CLOSE)

LEGAL["en"]["cookies"] = ("Cookies · Albergo Diffuso Socchieve", "Cookie policy for the website and the external booking services.", _OPEN + f"""<span class="eyebrow">Information</span>{_H1}Cookies</h1>
<p><strong>Version 1.1 · 16 November 2026</strong></p>
{_NOTE_EN}
<p>The website uses technical cookies and tools needed to display its pages, handle enquiries and remember your cookie choice. Only with your consent does it also use Google Analytics to measure visits in aggregate form.</p>
<h2>Technical cookies</h2>
<p>They are needed for the website to work and do not require consent. Your cookie choice is stored in your browser's local storage (key <code>adsocchieve-consent-v1</code>) until you change it or clear the site data.</p>
<h2>Google Analytics (statistics, only with consent)</h2>
<p>If you click “Accept” in the banner, the website loads Google Analytics 4, provided by Google Ireland Limited, to count visits and page views and understand how the site is used. The cookies <code>_ga</code> and <code>_ga_*</code> are set, lasting up to 2 years. Google processes the data as a processor and may transfer it to the United States with the safeguards provided for by the GDPR. We do not use Google Analytics for advertising or profiling. If you reject, Google Analytics is not loaded.</p>
<p>You can change your mind at any time from the <a href="#" data-cookie-settings>Cookie preferences</a> link at the bottom of every page.</p>
<h2>External services</h2>
<p>The <strong>Slope</strong> and <strong>Welora</strong> booking systems may use their own cookies and technical tools within their environments or widgets. Other external components, such as the OpenStreetMap map and the virtual tour, may receive technical data when they are loaded. See the notices provided by these providers for the categories, purposes and duration of their cookies and how to manage your preferences.</p>
<h2>Preferences and contact</h2>
<p>You can manage or delete cookies in your browser settings and, where available, through the controls in the external services. For requests about personal data, see the <a href="{{privacy}}">privacy notice</a> or write to {_MAIL}.</p>""" + _CLOSE)

LEGAL["de"]["cookies"] = ("Cookies · Albergo Diffuso Socchieve", "Cookie-Hinweise zur Website und zu den externen Buchungsdiensten.", _OPEN + f"""<span class="eyebrow">Information</span>{_H1}Cookies</h1>
<p><strong>Version 1.1 · 16. November 2026</strong></p>
{_NOTE_DE}
<p>Die Website verwendet technische Cookies und Hilfsmittel, die zur Anzeige der Seiten, zur Bearbeitung von Anfragen und zum Speichern Ihrer Cookie-Auswahl nötig sind. Nur mit Ihrer Einwilligung nutzt sie außerdem Google Analytics, um Besuche in zusammengefasster Form zu messen.</p>
<h2>Technische Cookies</h2>
<p>Sie sind für den Betrieb der Website erforderlich und benötigen keine Einwilligung. Ihre Cookie-Auswahl wird im lokalen Speicher Ihres Browsers gespeichert (Schlüssel <code>adsocchieve-consent-v1</code>), bis Sie sie ändern oder die Website-Daten löschen.</p>
<h2>Google Analytics (Statistik, nur mit Einwilligung)</h2>
<p>Wenn Sie im Banner auf „Akzeptieren“ klicken, lädt die Website Google Analytics 4 von Google Ireland Limited, um Besuche und Seitenaufrufe zu zählen und die Nutzung der Website zu verstehen. Dabei werden die Cookies <code>_ga</code> und <code>_ga_*</code> mit einer Speicherdauer von bis zu 2 Jahren gesetzt. Google verarbeitet die Daten als Auftragsverarbeiter und kann sie mit den in der DSGVO vorgesehenen Garantien in die USA übermitteln. Wir nutzen Google Analytics nicht für Werbung oder Profiling. Wenn Sie ablehnen, wird Google Analytics nicht geladen.</p>
<p>Sie können Ihre Entscheidung jederzeit über den Link <a href="#" data-cookie-settings>Cookie-Einstellungen</a> unten auf jeder Seite ändern.</p>
<h2>Externe Dienste</h2>
<p>Die Buchungssysteme <strong>Slope</strong> und <strong>Welora</strong> können in ihren Umgebungen oder Widgets eigene Cookies und technische Hilfsmittel verwenden. Andere externe Komponenten wie die OpenStreetMap-Karte und der virtuelle Rundgang können beim Laden technische Daten erhalten. Informationen zu Kategorien, Zwecken und Speicherdauer der Cookies sowie zur Verwaltung Ihrer Einstellungen finden Sie in den Hinweisen der jeweiligen Anbieter.</p>
<h2>Einstellungen und Kontakt</h2>
<p>Sie können Cookies in den Einstellungen Ihres Browsers und, sofern verfügbar, über die Steuerelemente der externen Dienste verwalten oder löschen. Für Anfragen zu personenbezogenen Daten lesen Sie die <a href="{{privacy}}">Datenschutzerklärung</a> oder schreiben Sie an {_MAIL}.</p>""" + _CLOSE)

LEGAL["en"]["terms"] = ("Wellness booking terms · Albergo Diffuso Socchieve", "Terms for sauna and forest bathing bookings: price, guarantee card, cancellations and no-shows.", _OPEN + f"""<span class="eyebrow">Wellness</span>{_H1}Booking terms for wellness services</h1>
{_VER_EN}
{_NOTE_EN}
<p>These terms apply to sauna and forest bathing bookings offered by the Albergo Diffuso Socchieve “Col Gentile”, Via Roma 20, Mediis, 33020 Socchieve (UD), Italy, VAT no. 02790180307. They form part of the <a href="{{booking}}">general booking terms</a>.</p>
<h2>Prices and duration</h2>
<p>The sauna costs <strong>20 € per hour for the whole group</strong>, with a minimum of two hours. Forest bathing costs <strong>15 € per person</strong> and lasts about two hours. Actual prices, dates and availability are shown before you confirm; the price accepted in the booking applies.</p>
<h2>Guarantee card</h2>
<p>Online booking may require a guarantee card through Welora. Any charges and applicable financial terms must be shown before you confirm. No additional penalty for late cancellation or no-show is set here unless a specific condition was communicated and accepted in the booking.</p>
<h2>Changes, cancellations and no-shows</h2>
<p>To change or cancel a booking, contact the property promptly at {_MAIL} or on {_TEL}. In the event of a no-show, only the penalty conditions communicated before confirmation and accepted for that specific service apply; the published rules consulted state no standard percentage.</p>
<h2>How the services take place</h2>
<p>Forest bathing takes place outdoors on trails and woodland ground: suitable clothing and footwear are required. For both services, the capacity, times and instructions given in the confirmation apply. For privacy, see the <a href="{{privacy}}">privacy notice</a>.</p>""" + _CLOSE)

LEGAL["de"]["terms"] = ("Buchungsbedingungen Wellness · Albergo Diffuso Socchieve", "Bedingungen für Buchungen von Sauna und Waldbaden: Preis, Kreditkartengarantie, Stornierungen und Nichterscheinen.", _OPEN + f"""<span class="eyebrow">Wellness</span>{_H1}Buchungsbedingungen für die Wellness-Angebote</h1>
{_VER_DE}
{_NOTE_DE}
<p>Diese Bedingungen gelten für Buchungen von Sauna und Waldbaden beim Albergo Diffuso Socchieve „Col Gentile“, Via Roma 20, Mediis, 33020 Socchieve (UD), Italien, USt-IdNr. 02790180307. Sie sind Teil der <a href="{{booking}}">allgemeinen Buchungsbedingungen</a>.</p>
<h2>Preise und Dauer</h2>
<p>Die Sauna kostet <strong>20 € pro Stunde für die ganze Gruppe</strong>, Mindestdauer zwei Stunden. Das Waldbaden kostet <strong>15 € pro Person</strong> und dauert rund zwei Stunden. Tatsächliche Preise, Termine und Verfügbarkeit werden vor der Bestätigung angezeigt; es gilt der bei der Buchung akzeptierte Preis.</p>
<h2>Kreditkarte als Garantie</h2>
<p>Für die Online-Buchung kann über Welora eine Kreditkarte als Garantie verlangt werden. Mögliche Belastungen und die geltenden finanziellen Bedingungen müssen vor der Bestätigung angezeigt werden. Eine zusätzliche Gebühr für späte Stornierung oder Nichterscheinen wird hier nicht festgelegt, sofern keine besondere Bedingung bei der Buchung mitgeteilt und akzeptiert wurde.</p>
<h2>Änderungen, Stornierungen und Nichterscheinen</h2>
<p>Um eine Buchung zu ändern oder zu stornieren, wenden Sie sich bitte umgehend an die Unterkunft unter {_MAIL} oder {_TEL}. Bei Nichterscheinen gelten ausschließlich die vor der Bestätigung mitgeteilten und für dieses Angebot akzeptierten Gebührenbedingungen; in den eingesehenen veröffentlichten Regeln ist kein Standardprozentsatz angegeben.</p>
<h2>Ablauf der Angebote</h2>
<p>Das Waldbaden findet im Freien auf Wegen und Waldboden statt: Geeignete Kleidung und Schuhe sind erforderlich. Für beide Angebote gelten die in der Bestätigung mitgeteilte Höchstteilnehmerzahl, Uhrzeit und Hinweise. Zum Datenschutz lesen Sie die <a href="{{privacy}}">Datenschutzerklärung</a>.</p>""" + _CLOSE)

LEGAL["en"]["booking-terms"] = ("Booking terms · Albergo Diffuso Socchieve", "Booking terms for stays at Col Gentile and La Farie, the sauna and forest bathing: deposit, cancellations, no-shows and guarantee card.", _OPEN + f"""<span class="eyebrow">Contract information</span>{_H1}Booking terms</h1>
{_VER_EN}
{_NOTE_EN}
<p>These terms cover stays at the Albergo Diffuso Socchieve “Col Gentile”, the La Farie Gästehaus and the sauna and forest bathing services. Operator: <strong>Zanier Lucio</strong>, Albergo Diffuso Socchieve “Col Gentile”, Via Roma 20, Mediis, 33020 Socchieve (UD), Italy, VAT no. 02790180307 · {_MAIL}.</p>
<h2>1. Prices, availability and confirmation</h2>
<p>Availability, total price, any supplements, deposit, rate conditions and payment methods are shown before the booking is confirmed or stated in the accepted quote. The booking is confirmed on the terms set out in the confirmation sent to the guest. Specific rate conditions expressly communicated and accepted before confirmation take precedence over the general provisions on this page.</p>
<h2>2. Stays in the Col Gentile houses</h2>
<p>According to the rules on the official website of the Albergo Diffuso Socchieve, the price includes use of the accommodation and bed and bath linen. The accommodation is available from 12:00 and must be vacated by 10:00 on the day of departure, unless otherwise agreed or stated in the confirmation. Payment of the balance is preferably made on arrival; any extras are settled on departure.</p>
<h3>Supplements and reductions for the Col Gentile houses</h3>
<p>The official rules list the following supplements: pets, where allowed, 5 € one-off; baby cot, 5 € one-off; extra cleaning, 10 € for small apartments or 15 € for large apartments; extra bed linen, 4 €; extra towel, 1 € each. For stays of fewer than three nights they state a 30% surcharge, and for single use of an apartment a 50% increase on the rate. The reductions stated are: free up to age 3, 50% from 4 to 6 and 30% from 7 to 10. The actual amounts and conditions of the booking are those confirmed in the quote or rate summary before purchase.</p>
<h2>3. Deposit, cancellation and early departure in the Col Gentile houses</h2>
<p>The published rules state that, in case of cancellation, <strong>any deposit paid is not refunded</strong>; by agreement with the management it may be used for another date on equivalent terms. For early departure, the cost of the accommodation alone is charged for the unused period, unless otherwise agreed. If the booked rate has a different cancellation policy, the one communicated and accepted during booking applies.</p>
<h2>4. La Farie</h2>
<p>For the La Farie Gästehaus, the condition stated on the booking page is: <strong>free cancellation through the portal up to 7 days before arrival, by 18:00</strong>. For later cancellations, no-shows, any deposits or charges, only the amounts and conditions expressly shown and accepted during booking apply; this page introduces no further penalty percentage.</p>
<h2>5. No-shows and guarantee card</h2>
<p>If the guest does not arrive on the agreed date and time and has not cancelled within the deadline, the financial conditions of the specific booking apply. For Col Gentile, the rule on any deposit paid continues to apply, unless a different rate was agreed. <strong>No additional standard percentage penalty for no-shows is published</strong>: further charges to the guarantee card may only be made if the amount or the method of calculating the penalty was communicated before confirmation and accepted by the guest. Where required, the guarantee card is requested and handled within the booking system.</p>
<h2>6. Sauna and forest bathing</h2>
<p>The sauna costs <strong>20 € per hour for the group</strong>; forest bathing <strong>15 € per person</strong>. Online bookings may require a guarantee card through Welora. Changes, cancellations and no-shows are governed by the specific conditions stated and accepted during booking. Unless a penalty is explicitly communicated before confirmation, this page introduces none. See also the <a href="{{terms}}">detailed wellness terms</a>.</p>
<h2>7. House rules</h2>
<p>Every guest, including minors, must present a valid identity document for legal requirements. Unregistered persons may not stay overnight. Smoking is not allowed in the accommodation. Please respect quiet hours from 23:00 to 08:00 and from 14:00 to 16:00. The rules prohibit taking the property's linen outside the apartments and using appliances to cook or heat food in rooms that are not kitchens. Missing linen, damage or lost keys may be charged according to the actual damage and applicable law.</p>
<h2>8. Assistance and privacy</h2>
<p>For cancellations, changes or questions, contact {_MAIL} or {_TEL}. Personal data is processed in accordance with the <a href="{{privacy}}">privacy notice</a>.</p>""" + _CLOSE)

LEGAL["de"]["booking-terms"] = ("Buchungsbedingungen · Albergo Diffuso Socchieve", "Buchungsbedingungen für Aufenthalte in Col Gentile und La Farie, Sauna und Waldbaden: Anzahlung, Stornierungen, Nichterscheinen und Kreditkartengarantie.", _OPEN + f"""<span class="eyebrow">Vertragsinformationen</span>{_H1}Buchungsbedingungen</h1>
{_VER_DE}
{_NOTE_DE}
<p>Diese Bedingungen gelten für Aufenthalte im Albergo Diffuso Socchieve „Col Gentile“, im Gästehaus La Farie sowie für die Angebote Sauna und Waldbaden. Betreiber: <strong>Zanier Lucio</strong>, Albergo Diffuso Socchieve „Col Gentile“, Via Roma 20, Mediis, 33020 Socchieve (UD), Italien, USt-IdNr. 02790180307 · {_MAIL}.</p>
<h2>1. Preise, Verfügbarkeit und Bestätigung</h2>
<p>Verfügbarkeit, Gesamtpreis, eventuelle Zuschläge, Anzahlung, Tarifbedingungen und Zahlungsweise werden vor der Buchungsbestätigung angezeigt oder im angenommenen Angebot mitgeteilt. Die Buchung gilt zu den Bedingungen, die in der an den Gast gesendeten Bestätigung stehen. Besondere Tarifbedingungen, die vor der Bestätigung ausdrücklich mitgeteilt und akzeptiert wurden, haben Vorrang vor den allgemeinen Angaben dieser Seite.</p>
<h2>2. Aufenthalte in den Häusern von Col Gentile</h2>
<p>Laut den Regeln auf der offiziellen Website des Albergo Diffuso Socchieve umfasst der Preis die Nutzung der Unterkunft sowie Bett- und Badwäsche. Die Unterkünfte stehen ab 12:00 Uhr zur Verfügung und müssen am Abreisetag bis 10:00 Uhr geräumt werden, sofern nicht anders vereinbart oder in der Bestätigung angegeben. Die Restzahlung erfolgt vorzugsweise bei Ankunft; Extras werden bei der Abreise abgerechnet.</p>
<h3>Zuschläge und Ermäßigungen für die Häuser von Col Gentile</h3>
<p>Die offiziellen Regeln nennen folgende Zuschläge: Haustiere, wo erlaubt, einmalig 5 €; Babybett einmalig 5 €; Zusatzreinigung 10 € für kleine bzw. 15 € für große Wohnungen; zusätzliche Bettwäsche 4 €; zusätzliches Handtuch 1 € pro Stück. Für Aufenthalte unter drei Nächten wird ein Aufschlag von 30 % angegeben, für die Einzelnutzung einer Wohnung ein Aufschlag von 50 % auf den Tarif. Die angegebenen Ermäßigungen sind: kostenlos bis 3 Jahre, 50 % von 4 bis 6 Jahren und 30 % von 7 bis 10 Jahren. Maßgeblich sind die Beträge und Bedingungen, die im Angebot oder in der Tarifübersicht vor dem Kauf bestätigt werden.</p>
<h2>3. Anzahlung, Stornierung und vorzeitige Abreise in den Häusern von Col Gentile</h2>
<p>Die veröffentlichten Regeln sehen vor, dass bei Stornierung <strong>eine geleistete Anzahlung nicht erstattet wird</strong>; nach Absprache mit der Leitung kann sie zu gleichwertigen Bedingungen für einen anderen Termin genutzt werden. Bei vorzeitiger Abreise werden für den nicht genutzten Zeitraum nur die Kosten der Unterkunft berechnet, sofern nicht anders vereinbart. Hat der gebuchte Tarif andere Stornobedingungen, gelten die bei der Buchung mitgeteilten und akzeptierten.</p>
<h2>4. La Farie</h2>
<p>Für das Gästehaus La Farie gilt laut Buchungsseite: <strong>kostenlose Stornierung über das Portal bis 7 Tage vor Anreise, bis 18:00 Uhr</strong>. Für spätere Stornierungen, Nichterscheinen, eventuelle Anzahlungen oder Belastungen gelten ausschließlich die bei der Buchung ausdrücklich angezeigten und akzeptierten Beträge und Bedingungen; diese Seite legt keinen zusätzlichen Gebührenprozentsatz fest.</p>
<h2>5. Nichterscheinen (No-Show) und Kreditkarte als Garantie</h2>
<p>Erscheint der Gast nicht zum vereinbarten Datum und zur vereinbarten Uhrzeit und hat er nicht fristgerecht storniert, gelten die finanziellen Bedingungen der jeweiligen Buchung. Für Col Gentile bleibt die Regel zur geleisteten Anzahlung anwendbar, sofern kein anderer Tarif vereinbart wurde. <strong>Eine zusätzliche Standard-Prozentgebühr für Nichterscheinen ist nicht veröffentlicht</strong>: Weitere Belastungen der Garantiekarte sind nur möglich, wenn Betrag oder Berechnungsweise der Gebühr vor der Bestätigung mitgeteilt und vom Gast akzeptiert wurden. Sofern vorgesehen, wird die Garantiekarte im Buchungssystem abgefragt und verwaltet.</p>
<h2>6. Sauna und Waldbaden</h2>
<p>Die Sauna kostet <strong>20 € pro Stunde für die Gruppe</strong>, das Waldbaden <strong>15 € pro Person</strong>. Für Online-Buchungen kann über Welora eine Kreditkarte als Garantie verlangt werden. Änderungen, Stornierungen und Nichterscheinen richten sich nach den bei der Buchung angegebenen und akzeptierten besonderen Bedingungen. Wurde vor der Bestätigung keine Gebühr ausdrücklich mitgeteilt, legt diese Seite keine fest. Siehe auch die <a href="{{terms}}">ausführlichen Bedingungen für die Wellness-Angebote</a>.</p>
<h2>7. Hausordnung</h2>
<p>Jeder Gast, auch Minderjährige, muss für die gesetzlichen Meldepflichten ein gültiges Ausweisdokument vorlegen. Nicht angemeldete Personen dürfen nicht übernachten. In den Unterkünften ist Rauchen nicht gestattet. Bitte halten Sie die Ruhezeiten von 23:00 bis 08:00 Uhr und von 14:00 bis 16:00 Uhr ein. Die Hausordnung untersagt, die Wäsche der Unterkunft aus den Wohnungen mitzunehmen und in Räumen ohne Küche Geräte zum Kochen oder Erwärmen von Speisen zu benutzen. Fehlende Wäsche, Schäden oder verlorene Schlüssel können nach dem tatsächlichen Schaden und gemäß geltendem Recht berechnet werden.</p>
<h2>8. Hilfe und Datenschutz</h2>
<p>Für Stornierungen, Änderungen oder Fragen wenden Sie sich an {_MAIL} oder {_TEL}. Personenbezogene Daten werden gemäß der <a href="{{privacy}}">Datenschutzerklärung</a> verarbeitet.</p>""" + _CLOSE)
