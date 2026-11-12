import type { Metadata } from "next";
import Link from "next/link";
import { BookingLink } from "@/components/BookingLink";
import { Shell, Card } from "@/components/UI";
import { SLOPE, stays } from "@/lib/data";
export const metadata: Metadata = { title: "Accommodation in Carnia | Col Gentile apartments", description: "Discover apartments and village houses in Socchieve, Carnia. Check availability with the Col Gentile booking service.", alternates: {canonical:"/en/alloggi"} };
export default function EnglishStays() { return <Shell english>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/en">Home</Link> / Accommodation</p><span className="eyebrow">Col Gentile</span><h1>Where to stay in Carnia.</h1><p>Explore apartments and traditional houses in the villages of Socchieve. Availability and rates are confirmed by the official booking engine.</p><BookingLink href={SLOPE} placement="catalog_en">Check availability ↗</BookingLink></section>
  <section className="container" style={{paddingBottom:90}}><div className="cards">{stays.map((stay)=><Card key={stay.slug} stay={stay} english/>)}</div></section>
  </Shell>; }
