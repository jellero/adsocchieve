import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
import { photos } from "@/lib/data";
export const metadata: Metadata = { title: "Trekking a Socchieve e in Carnia | Dove dormire", description: "Scopri la Carnia a piedi partendo dai borghi di Socchieve. Appartamenti e case per un soggiorno dedicato alla natura.", alternates: {canonical:"/it/trekking"} };
export default function Trekking() { return <Shell>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/it">Home</Link> / <Link href="/it/territorio">Territorio</Link> / Trekking</p>
  <span className="eyebrow">La Carnia a piedi</span><h1>Trekking e natura a Socchieve.</h1><p>I borghi di Socchieve sono un punto di partenza per conoscere la Carnia a piedi, tra passeggiate e itinerari montani. Scegli un alloggio e pianifica le escursioni secondo la tua esperienza e le condizioni aggiornate.</p></section>
  <section className="container two-col" style={{paddingBottom:90}}>{/* eslint-disable-next-line @next/next/no-img-element */}<img className="story-photo" src={photos.lungis} alt="Montagne attorno al borgo di Lungis"/><div><h2>Cammina, poi torna a casa nel borgo.</h2><p>Col Gentile offre alloggi in diverse frazioni del comune: una soluzione per chi cerca autonomia durante un soggiorno di più giorni.</p><p className="fine">Percorsi, difficoltà, transitabilità e condizioni meteorologiche devono essere verificati presso fonti escursionistiche e locali aggiornate.</p><Link className="button" href="/it/alloggi">Scopri gli alloggi ↗</Link></div></section>
  </Shell>; }
