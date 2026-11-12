import type { Metadata } from "next";
import Link from "next/link";
import { Shell } from "@/components/UI";
import { photos } from "@/lib/data";
export const metadata: Metadata = { title: "Socchieve and Carnia | Villages and mountains", description: "Explore the villages of Socchieve in Carnia, Friuli Venezia Giulia, and plan your holiday in the mountains.", alternates: {canonical:"/en/territory"} };
export default function EnglishTerritory() { return <Shell english>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/en">Home</Link> / Territory</p><h1>Discover Socchieve and Carnia.</h1><p>Eight villages, mountain landscapes and traditional houses in northeastern Italy.</p></section>
  <section className="container two-col" style={{paddingBottom:90}}>{/* eslint-disable-next-line @next/next/no-img-element */}<img className="story-photo" src={photos.lungis} alt="The mountain village of Lungis in Carnia"/><div><h2>A different way to discover the mountains.</h2><p>Socchieve includes the villages of Socchieve, Nonta, Mediis, Priuso, Lungis, Dilignidis, Feltrone and Viaso.</p><Link className="button" href="/en/alloggi">Explore accommodation ↗</Link></div></section>
  </Shell>; }
