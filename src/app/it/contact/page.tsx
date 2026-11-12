import type { Metadata } from "next";
import Link from "next/link";
import { BookingLink } from "@/components/BookingLink";
import { Shell } from "@/components/UI";
import { EMAIL, SLOPE, TEL } from "@/lib/data";
export const metadata: Metadata = { title: "Contatti Albergo Diffuso Col Gentile Socchieve", description: "Contatti della reception Col Gentile a Mediis, Socchieve: indirizzo, email e telefono. Prenotazioni online tramite Slope.", alternates: {canonical:"/it/contact"} };
export default function Contact() { return <Shell>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/it">Home</Link> / Contatti</p><span className="eyebrow">Siamo a Socchieve</span><h1>Contatta Col Gentile.</h1><p>Per informazioni sugli appartamenti e per organizzare il tuo soggiorno in Carnia.</p></section>
  <section className="container two-col" style={{alignItems:"start",paddingBottom:90}}>
    <div className="alt-panel"><h2>Reception</h2><p><strong>Indirizzo:</strong> Via Roma 20, 33020 Mediis, Socchieve (UD), Italia</p><p><strong>Email:</strong> <a className="text-link" href={"mailto:" + EMAIL}>{EMAIL}</a></p><p><strong>Telefono:</strong> <a className="text-link" href={"tel:" + TEL}>+39 0433 819934</a></p><p><strong>Cellulare:</strong> <a className="text-link" href="tel:+393668948584">+39 366 894 8584</a></p><p className="fine">Orari della reception da riallineare con la gestione: le pagine del sito precedente riportano informazioni differenti.</p></div>
    <div><h2>Verifica disponibilità</h2><p>Puoi consultare date e sistemazioni disponibili sul motore di prenotazione Col Gentile. La Farie ha un percorso separato.</p><BookingLink href={SLOPE} placement="contacts">Vai alle prenotazioni ↗</BookingLink><p style={{marginTop:25}}><Link className="text-link" href="/la-farie/contatti">Cerchi La Farie? ↗</Link></p></div>
  </section>
  </Shell>; }
