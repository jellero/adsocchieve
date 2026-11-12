# adsocchieve — demo HTML statica

**Nessun Node.js, npm, Next.js, server o processo di build richiesto.**

## Come aprire
Scarica il file index.html e aprilo nel browser con doppio clic. La demo è responsive e include HTML, CSS e JavaScript nello stesso file.

## Due identità
- Col Gentile: homepage, catalogo di sei alloggi dimostrativi, filtri per località e ospiti, link al booking Slope.
- La Farie: navigazione e identità grafica distinte. Seleziona "La Farie" nel menu: la demo mostra la seconda homepage senza richiedere un secondo file.
- I due percorsi commerciali restano separati.
- La Farie non è ancora prenotabile nella scheda Booking.com pubblica: la demo lo indica e non inventa disponibilità.

## Importante
La demo utilizza immagini pubblicate sul sito attuale e fotografie provvisorie come segnaposto; alcune immagini non sono delle specifiche case presenti nella scheda e vanno sostituite. Foto, diritti, CIN, capienze, descrizioni, traduzioni, prezzi, contatti, identità e privacy vanno verificati prima della messa online.

I dati del catalogo non sono completi: questa è una **demo del layout e del percorso di conversione**, non una migrazione finita. I link alle schede portano al sito attuale, e quelli di prenotazione Col Gentile al motore Slope.

## Pubblicazione futura
Per una release statica vera, separare le pagine con URL indicizzabili e gestire redirect dalle pagine storiche: l'uso degli hash nella demo serve solo a mostrare le due esperienze in un file. Aggiungere file ottimizzati locali, sitemap, metadati per pagina, hreflang e tracciamento GA4 prima del lancio.

La cronologia Git conserva l'esperimento Next.js precedente, ma il branch principale contiene ora solo la demo HTML statica e questo README.
