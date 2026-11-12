import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
import { photos } from "@/lib/data";
export const metadata: Metadata = { title: "Cicloturismo in Carnia | Alloggi a Socchieve", description: "Esplora i dintorni di Socchieve in bicicletta e scegli un appartamento per il tuo soggiorno in Carnia.", alternates: {canonical:"/it/cicloturismo"} };
export default function Cicloturismo() { return <Shell>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/it">Home</Link> / <Link href="/it/territorio">Territorio</Link> / Cicloturismo</p>
  <span className="eyebrow">La Carnia su due ruote</span><h1>Cicloturismo nei dintorni di Socchieve.</h1><p>Tra paesi e paesaggi montani, una base per scoprire la Carnia pedalando. Esplora le case dell'albergo diffuso e organizza il tuo itinerario.</p></section>
  <section className="container two-col" style={{paddingBottom:90}}>{/* eslint-disable-next-line @next/next/no-img-element */}<img className="story-photo" src={photos.rosuline} alt="Vista del territorio di Lungis"/><div><h2>Scegli il borgo da cui partire.</h2><p>Gli appartamenti di Col Gentile si trovano in diverse località del comune di Socchieve.</p><p className="fine">Servizi dedicati ai ciclisti e percorsi specifici vanno confermati prima di promuoverli.</p><Link className="button" href="/it/alloggi">Trova il tuo alloggio ↗</Link></div></section>
  </Shell>; }
