import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
import { photos } from "@/lib/data";

export const metadata: Metadata = {
  title: "Socchieve e la Carnia | Borghi e territorio",
  description: "Scopri Socchieve e le frazioni di Lungis, Viaso, Feltrone e Mediis, tra borghi, sentieri e paesaggi della Carnia.",
  alternates: { canonical: "/it/territorio" }
};
export default function Territorio() { return <Shell>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/it">Home</Link> / Territorio</p>
    <span className="eyebrow">Vivi il territorio</span><h1>Socchieve, i borghi e la Carnia.</h1>
    <p>Un territorio di montagna attraversato dall'Alto Tagliamento e dal Lumiei, tra architetture tradizionali, natura e piccoli paesi.</p>
  </section>
  <section className="container two-col" style={{paddingBottom:75}}>
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img src={photos.lungis} className="story-photo" alt="Paesaggio di Lungis, nel comune di Socchieve"/>
    <div className="story-copy"><span className="eyebrow">Otto paesi</span><h2>Un territorio da abitare, non solo da visitare.</h2>
      <p>Il Comune di Socchieve comprende Socchieve, Nonta, Mediis, Priuso, Lungis, Dilignidis, Feltrone e Viaso. Le case dell'albergo diffuso si trovano in diverse frazioni, ciascuna con il suo carattere.</p>
      <p>Scopri gli alloggi prima di scegliere il punto di partenza per il tuo soggiorno.</p>
      <Link className="button" href="/it/alloggi">Esplora gli alloggi ↗</Link>
    </div>
  </section>
  <section className="section" style={{background:"var(--paper)"}}><div className="container">
    <h2>Esperienze e dintorni</h2>
    <div className="topics">
      <Link className="topic" href="/it/trekking">{/* eslint-disable-next-line @next/next/no-img-element */}<img src={photos.lungis} alt="Montagne della Carnia"/><strong>Trekking ↗</strong></Link>
      <Link className="topic" href="/it/cicloturismo">{/* eslint-disable-next-line @next/next/no-img-element */}<img src={photos.rosuline} alt="Panorama del borgo"/><strong>Cicloturismo ↗</strong></Link>
      <Link className="topic" href="/it/alloggi">{/* eslint-disable-next-line @next/next/no-img-element */}<img src={photos.hero} alt="Casa tradizionale di Socchieve"/><strong>Dove dormire ↗</strong></Link>
    </div>
  </div></section>
  </Shell>; }
