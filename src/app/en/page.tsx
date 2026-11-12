import type { Metadata } from "next";
import Link from "next/link";
import { BookingLink } from "@/components/BookingLink";
import { Shell, Card } from "@/components/UI";
import { photos, SLOPE, stays } from "@/lib/data";

export const metadata: Metadata = {
  title: "Where to stay in Carnia | Col Gentile Albergo Diffuso",
  description: "Discover houses and apartments in the villages of Socchieve, Carnia, in Friuli Venezia Giulia. Browse Col Gentile accommodation and check booking availability.",
  alternates: { canonical: "/en", languages: { "it-IT": "/it", "en-GB": "/en" } },
  openGraph: { locale: "en_GB", images: [photos.hero] }
};
export default function EnglishHome() { return <Shell english>
  <section className="hero">
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img src={photos.hero} alt="Traditional village accommodation in Socchieve, Carnia" className="bg"/>
    <div className="container hero-content"><span className="eyebrow light">Socchieve · Carnia · Friuli Venezia Giulia</span>
      <h1>Stay in Carnia. Live in the village.</h1>
      <p>Discover traditional houses and apartments across the villages of Socchieve, in the mountains of northeastern Italy.</p>
      <div className="hero-actions"><Link href="/en/alloggi" className="button light">Explore accommodation ↗</Link><BookingLink href={SLOPE} placement="homepage_en" className="button outline">Check availability ↗</BookingLink></div>
    </div>
  </section>
  <section className="section"><div className="container"><div className="section-head"><div><span className="eyebrow">Col Gentile</span><h2>Find your home in Carnia.</h2></div><p>Choose from houses and apartments across different villages. All prices and availability are confirmed on the official booking platform.</p></div>
    <div className="cards">{[stays[0],stays[2],stays[8]].map((stay)=><Card key={stay.slug} stay={stay}/>)}</div>
    <p style={{marginTop:30}}><Link href="/en/alloggi" className="text-link">All accommodation ↗</Link></p>
  </div></section>
  <section className="cta"><div className="container"><h2>Plan your stay in Carnia.</h2><p>Browse the accommodation and check available dates online.</p><BookingLink href={SLOPE} placement="homepage_en_bottom" className="button light">Check dates ↗</BookingLink></div></section>
  </Shell>; }
