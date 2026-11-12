import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
import { photos } from "@/lib/data";

export const metadata: Metadata = {
  title: "La Farie | Dimora a Lungis, Carnia",
  description: "Scopri La Farie a Lungis, Socchieve: una dimora in pietra e legno nel cuore della Carnia, con un'identità ricettiva distinta.",
  alternates: { canonical: "/la-farie" },
  robots: { index: false, follow: true }
};
export default function Farie() { return <Shell farie>
  <section className="hero">
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img className="bg" src={photos.farie} alt="La Farie, edificio in pietra e legno a Lungis"/>
    <div className="container hero-content">
      <span className="eyebrow light">Lungis · Socchieve · Carnia</span>
      <h1>La Farie. Una dimora, un'altra atmosfera.</h1>
      <p>Una casa in pietra e legno nel borgo di Lungis, con la propria identità e un soggiorno distinto da quello degli appartamenti Col Gentile.</p>
      <div className="hero-actions"><Link className="button light" href="/la-farie/camere">Scopri le camere ↗</Link><Link className="button outline" href="/la-farie/contatti">Dove siamo ↗</Link></div>
    </div>
  </section>
  <section className="section" style={{background:"var(--paper)"}}><div className="container" style={{maxWidth:900,textAlign:"center"}}>
    <span className="eyebrow">Un'altra esperienza di ospitalità</span>
    <h2>Il carattere di una dimora carnica.</h2>
    <p>La Farie si trova a Lungis, nel comune di Socchieve. La sua architettura combina pietra e legno e dialoga con il paesaggio della Carnia.</p>
  </div></section>
  <section className="section"><div className="container two-col">
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img className="story-photo" src={photos.farie} alt="Esterno di La Farie a Lungis" loading="lazy"/>
    <div><span className="eyebrow">La struttura</span><h2>Una presenza distinta nel gruppo AD.</h2>
      <p>Qui trovi informazioni e aggiornamenti dedicati esclusivamente a La Farie, senza mescolare disponibilità e prenotazioni con gli alloggi dell'Albergo Diffuso.</p>
      <Link className="button" href="/la-farie/camere">Esplora le camere ↗</Link>
    </div>
  </div></section>
  <section className="section" style={{background:"var(--paper)"}}><div className="container two-col">
    <div><span className="eyebrow">La posizione</span><h2>A Lungis, nel cuore della Carnia.</h2><p>Una base per conoscere i piccoli borghi di Socchieve e la montagna friulana.</p><Link className="text-link" href="/la-farie/contatti">Posizione e contatti ↗</Link></div>
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img src={photos.lungis} className="story-photo" alt="Panorama del borgo di Lungis" loading="lazy"/>
  </div></section>
  <section className="container" style={{paddingTop:55,paddingBottom:75}}><div className="farie-banner">
    <strong>Prenotazioni La Farie</strong><p style={{margin:"8px 0 0"}}>La configurazione Booking.com per la nuova gestione è in corso di verifica. Questa pagina non presenta disponibilità né prezzi fino alla conferma dell'attivazione.</p>
  </div></section>
  </Shell>; }
