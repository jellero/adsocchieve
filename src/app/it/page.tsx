import type { Metadata } from "next";
import Link from "next/link";
import { BookingLink } from "@/components/BookingLink";
import { Card, Shell } from "@/components/UI";
import { BASE, photos, SLOPE, stays } from "@/lib/data";

export const metadata: Metadata = {
  title: "Dormire in Carnia | Appartamenti Albergo Diffuso Col Gentile",
  description: "Case e appartamenti nei borghi di Socchieve, in Carnia. Scopri gli alloggi di Col Gentile e prenota il tuo soggiorno nel Friuli montano.",
  alternates: { canonical: "/it", languages: { "it-IT": "/it", "en-GB": "/en" } },
  openGraph: { title: "Col Gentile — Albergo Diffuso Socchieve", images: [photos.hero] }
};

export default function Home() {
  const structured = {
    "@context": "https://schema.org",
    "@type": "LodgingBusiness",
    name: "Albergo Diffuso Socchieve Col Gentile",
    url: BASE + "/it",
    telephone: "+39 0433 819934",
    email: "info@albergodiffusosocchieve.it",
    address: { "@type": "PostalAddress", streetAddress: "Via Roma 20", addressLocality: "Mediis, Socchieve", addressRegion: "UD", addressCountry: "IT" }
  };
  return <Shell>
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(structured) }}/>
    <section className="hero">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={photos.hero} alt="Casa tradizionale con ballatoi in legno a Socchieve, in Carnia" className="bg"/>
      <div className="container hero-content">
        <div className="eyebrow light">Socchieve · Carnia · Friuli Venezia Giulia</div>
        <h1>In Carnia, la tua casa è dentro il borgo.</h1>
        <p>Case e appartamenti nei borghi di Socchieve. Scopri l'autenticità della montagna, scegli il tuo alloggio e organizza il soggiorno.</p>
        <div className="hero-actions"><Link className="button light" href="/it/alloggi">Esplora gli alloggi ↗</Link><BookingLink href={SLOPE} placement="homepage_hero" className="button outline">Verifica disponibilità ↗</BookingLink></div>
        <div className="hero-tags"><span>Case nei borghi</span><span>Montagna e natura</span><span>Gestione locale</span></div>
      </div>
    </section>
    <div className="container search-strip">
      <div><strong>Trova dove dormire in Carnia</strong><p>Scegli l'alloggio adatto e controlla date, ospiti e disponibilità sul motore ufficiale.</p></div>
      <BookingLink href={SLOPE} placement="homepage_search" className="button">Verifica date e disponibilità ↗</BookingLink>
    </div>
    <section className="section"><div className="container">
      <div className="section-head"><div><span className="eyebrow">Scegli il tuo soggiorno</span><h2>Le nostre case in Carnia</h2></div><p>Appartamenti e residenze distribuiti tra i borghi di Feltrone, Viaso, Lungis e Mediis.</p></div>
      <div className="cards">{[stays[0], stays[2], stays[8]].map((stay) => <Card key={stay.slug} stay={stay}/>)}</div>
      <p style={{marginTop:32}}><Link href="/it/alloggi" className="text-link">Scopri tutti gli alloggi ↗</Link></p>
    </div></section>
    <section className="section" style={{background:"var(--paper)"}}><div className="container two-col">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="story-photo" src={photos.lungis} alt="Paesaggio montano e case del borgo di Lungis"/>
      <div className="story-copy"><span className="eyebrow">Ospitalità diffusa</span><h2>Non solo una camera. Un luogo da vivere.</h2>
        <p>L'albergo diffuso permette di soggiornare nelle case dei paesi, scoprendo il territorio, le persone e i ritmi della Carnia. Con Col Gentile puoi abitare un borgo anziché limitarti a visitarlo.</p>
        <div className="perks"><span>Borghi autentici</span><span>Libertà del soggiorno</span><span>Territorio da scoprire</span></div>
        <p style={{marginTop:32}}><Link href="/it/territorio" className="text-link">Scopri Socchieve ↗</Link></p>
      </div>
    </div></section>
    <section className="section farie-teaser"><div className="container two-col">
      <div><span className="eyebrow">Due identità, un territorio</span><h2 className="serif">La Farie. Un'altra atmosfera.</h2>
        <p>Una dimora a Lungis, con un'identità propria. Scopri gli ambienti di La Farie e il suo percorso di soggiorno, separato da quello degli appartamenti Col Gentile.</p>
        <Link className="button light" href="/la-farie">Scopri La Farie ↗</Link>
      </div>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="farie-photo" src={photos.farie} alt="Edificio in pietra e legno della struttura La Farie a Lungis" loading="lazy"/>
    </div></section>
    <section className="section"><div className="container">
      <div className="section-head"><div><span className="eyebrow">Esperienze nel territorio</span><h2>La Carnia da scoprire</h2></div><p>Sentieri, paesi, natura e cultura sono parte del soggiorno a Socchieve.</p></div>
      <div className="topics">
        <Link className="topic" href="/it/trekking">{/* eslint-disable-next-line @next/next/no-img-element */}<img src={photos.lungis} alt="Panorama delle montagne della Carnia"/><strong>Trekking ↗</strong></Link>
        <Link className="topic" href="/it/cicloturismo">{/* eslint-disable-next-line @next/next/no-img-element */}<img src={photos.rosuline} alt="Panorama dai ballatoi di Lungis"/><strong>Cicloturismo ↗</strong></Link>
        <Link className="topic" href="/it/territorio">{/* eslint-disable-next-line @next/next/no-img-element */}<img src={photos.hero} alt="Architettura tradizionale di Socchieve"/><strong>Borghi e territorio ↗</strong></Link>
      </div>
    </div></section>
    <section className="cta"><div className="container"><span className="eyebrow light">Il tuo prossimo soggiorno</span><h2>Ci vediamo in Carnia?</h2><p>Esplora le case, scegli il periodo e verifica le disponibilità direttamente con Col Gentile.</p><BookingLink href={SLOPE} placement="homepage_bottom" className="button light">Verifica la disponibilità ↗</BookingLink></div></section>
  </Shell>;
}
