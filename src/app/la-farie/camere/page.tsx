import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
import { photos } from "@/lib/data";

export const metadata: Metadata = {
  title: "Le camere di La Farie | Lungis, Socchieve",
  description: "Le camere di La Farie a Lungis: una pagina dedicata alla nuova gestione, distinta dal catalogo appartamenti Col Gentile.",
  alternates: { canonical: "/la-farie/camere" },
  robots: { index: false, follow: true }
};
export default function Camere() { return <Shell farie>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/la-farie">La Farie</Link> / Camere</p>
    <span className="eyebrow">La Farie · Lungis</span><h1>Le camere della dimora.</h1>
    <p>Questa sezione sarà dedicata esclusivamente alle sistemazioni di La Farie, con fotografie, caratteristiche e informazioni verificate dalla nuova gestione.</p></section>
  <section className="container two-col" style={{paddingBottom:90}}>
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img src={photos.farie} className="story-photo" alt="Facciata della dimora La Farie"/>
    <div><h2>Il soggiorno a La Farie.</h2><p>Stiamo predisponendo il catalogo delle camere. Tipologie, capienza, servizi e prezzi saranno pubblicati solo dopo la conferma delle informazioni e l'attivazione del canale Booking.com.</p>
      <div className="farie-banner"><strong>Prenotazione non ancora attiva sul nuovo sito.</strong><p className="booking-note">Nessuna camera o disponibilità fittizia è mostrata.</p></div>
      <p style={{marginTop:25}}><Link href="/la-farie/contatti" className="text-link">Scopri dove siamo ↗</Link></p>
    </div>
  </section>
  </Shell>; }
