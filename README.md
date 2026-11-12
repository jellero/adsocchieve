# Albergo Diffuso Socchieve · sito statico

Sito statico ottimizzato per la SEO, generato da un piccolo script Python. Le pagine HTML
risultanti sono nel repository e si pubblicano su qualsiasi hosting statico
(GitHub Pages, Netlify, Cloudflare Pages, un server Apache/Nginx).

## Struttura

| Percorso | Cosa contiene |
|---|---|
| `_src/data.py` | **Tutti i contenuti**: case, borghi, esperienze, FAQ, distanze, contatti |
| `_src/site.css`, `_src/site.js` | Stile e comportamento (filtri, galleria, tour 360°, menu) |
| `_src/build.py` | Genera le pagine HTML, `sitemap.xml`, `robots.txt`, `_redirects`, icone |
| `_src/fetch_assets.py` | Scarica le foto dal vecchio sito, le ottimizza in WebP e scarica i font |
| `_src/serve.py` | Anteprima locale con URL senza `.html`, come sull'hosting |
| `index.html`, `it/…`, `img/`, `assets/` | **Sito generato**: da pubblicare così com'è |

## Modificare un testo o aggiungere una casa

```bash
python _src/fetch_assets.py   # solo se hai aggiunto foto nuove (serve Pillow)
python _src/build.py
python _src/serve.py          # anteprima su http://localhost:8000
```

## SEO: cosa è già fatto

- **Stessi URL del vecchio sito** (`/it/alloggi/casa-vanda`, `/it/viaso`, `/it/trekking`…): il posizionamento attuale non si perde e non servono redirect.
- Pagina dedicata per ognuna delle 14 case, degli 8 borghi e delle 4 esperienze, con `title`, `meta description`, canonical e Open Graph unici.
- Dati strutturati schema.org: `LodgingBusiness`, `House`/`Apartment` (posti letto, camere, servizi, animali, CIN), `TouristDestination`, `TouristTrip`, `FAQPage`, `BreadcrumbList`.
- `sitemap.xml` con le immagini, `robots.txt`, pagina 404, favicon e manifest.
- Foto in WebP ottimizzate con `srcset`, dimensioni esplicite (niente salti di layout), hero precaricata, font in locale (anche per il GDPR), nessun JavaScript necessario per leggere i contenuti.
- Tour virtuali 360° di Casa Vanda, Casa Ernesto da Rosuline e Casa dal Miedi (Pannellum, caricato solo al clic).
- `_redirects` (Netlify/Cloudflare Pages) che porta le vecchie pagine `/en/…` e `/fr/…` alle pagine italiane finché non ci sono le traduzioni.

## Da fare prima della messa online

1. **Pubblicare sul dominio `albergodiffusosocchieve.it`** (senza www, come oggi) e far puntare `www` con redirect 301.
2. **Google Search Console**: verificare il dominio e inviare `https://albergodiffusosocchieve.it/sitemap.xml`.
3. **Profilo dell'attività su Google** (Google Business Profile): stesso nome, indirizzo e telefono del sito, foto, link al sito e al booking. È la leva più forte per le ricerche “dove dormire in Carnia”.
4. Far verificare i testi di **privacy e cookie**.
5. Verificare i dati: posti letto di Casa Ernesto da Rosuline (21 sulla casa intera, 17 sommando le unità), “animali ammessi” (dedotto dall'icona del vecchio sito), CIN di Casa Ai Pascoli (mancante).
6. **Traduzioni EN/DE/FR**: il vecchio sito aveva inglese e francese; il tedesco è il mercato estero principale della Carnia.
