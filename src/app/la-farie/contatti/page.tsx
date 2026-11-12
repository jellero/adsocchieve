import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
export const metadata: Metadata = {
  title: "La Farie: posizione e contatti | Lungis, Carnia",
  description: "La Farie si trova a Lungis, nel comune di Socchieve, in Carnia. Informazioni sulla posizione della dimora.",
  alternates: { canonical: "/la-farie/contatti" }, robots: { index: false, follow: true }
};
export default function Contatti() { return <Shell farie>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/la-farie">La Farie</Link> / Contatti</p><span className="eyebrow">Lungis · Socchieve</span><h1>Dove trovare La Farie.</h1><p>La dimora si trova nel borgo di Lungis, nel comune di Socchieve, in provincia di Udine.</p></section>
  <section className="container two-col" style={{alignItems:"start",paddingBottom:90}}>
    <div className="alt-panel"><h2>Posizione</h2><p><strong>La Farie</strong></p><p>Via Bellini 8A, Lungis, 33020 Socchieve (UD), Italia</p><p className="fine">Indirizzo riportato nella scheda pubblica di Google Hotels: verificare con la nuova gestione prima della pubblicazione.</p><a className="text-link" href="https://www.google.com/maps/search/?api=1&query=La+Farie+Lungis+Socchieve" target="_blank" rel="noopener noreferrer">Apri la mappa ↗</a></div>
    <div><h2>Prenotazioni indipendenti.</h2><p>La Farie utilizzerà un proprio percorso di prenotazione Booking.com, distinto da Col Gentile. I contatti commerciali e il collegamento definitivo saranno pubblicati dopo la configurazione della nuova gestione.</p><div className="farie-banner">La configurazione delle prenotazioni è da completare.</div></div>
  </section>
  </Shell>; }
