import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { BookingLink } from "@/components/BookingLink";
import { Shell } from "@/components/UI";
import { BASE, SLOPE, stays } from "@/lib/data";

export function generateStaticParams() { return stays.map((stay) => ({ slug: stay.slug })); }

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const stay = stays.find((item) => item.slug === slug);
  if (!stay) return { title: "Alloggio non trovato" };
  return {
    title: stay.name + " a " + stay.village + " | Alloggi in Carnia",
    description: stay.description + " Scopri la struttura e verifica la disponibilità.",
    alternates: { canonical: "/it/alloggi/" + slug },
    openGraph: { images: [stay.photo] }
  };
}
export default async function StayPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const stay = stays.find((item) => item.slug === slug);
  if (!stay) notFound();
  const breadcrumb = {
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    itemListElement: [
      { "@type": "ListItem", position: 1, name: "Home", item: BASE + "/it" },
      { "@type": "ListItem", position: 2, name: "Alloggi", item: BASE + "/it/alloggi" },
      { "@type": "ListItem", position: 3, name: stay.name, item: BASE + "/it/alloggi/" + slug }
    ]
  };
  return <Shell>
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumb) }}/>
    <section className="container page-intro">
      <p className="breadcrumb"><Link href="/it">Home</Link> / <Link href="/it/alloggi">Alloggi</Link> / {stay.name}</p>
      <span className="eyebrow">{stay.village} · {stay.kind}</span><h1>{stay.name}</h1>
      <p>Un soggiorno nel borgo di {stay.village}, a Socchieve, in Carnia.</p>
    </section>
    <section className="container two-col" style={{alignItems:"start",paddingBottom:90}}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="detail-photo" src={stay.photo} alt={stay.name + ", alloggio a " + stay.village}/>
      <div><h2>La struttura</h2><p>{stay.description}</p>
        <div><span className="pill">Località: {stay.village}</span>{stay.capacity && <span className="pill">Fino a {stay.capacity} ospiti</span>}</div>
        {stay.cin && <p className="fine" style={{marginTop:20}}>CIN: {stay.cin}</p>}
        <div className="booking-box"><h3>Organizza il tuo soggiorno</h3><p>Le date, le tariffe e la disponibilità effettiva sono gestite da Slope. Non stiamo mostrando prezzi o disponibilità non verificate.</p>
          <BookingLink href={SLOPE} placement={"stay_" + slug}>Verifica date e disponibilità ↗</BookingLink></div>
        <p className="fine" style={{marginTop:20}}>Dati e fotografie della scheda da verificare con il catalogo operativo prima della pubblicazione.</p>
        <p><Link href="/it/alloggi" className="text-link">← Tutti gli alloggi</Link></p>
      </div>
    </section>
  </Shell>;
}
