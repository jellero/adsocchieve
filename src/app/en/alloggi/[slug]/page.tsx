import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { BookingLink } from "@/components/BookingLink";
import { Shell } from "@/components/UI";
import { SLOPE, stays } from "@/lib/data";

export function generateStaticParams() { return stays.map((stay) => ({ slug: stay.slug })); }
export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const stay = stays.find((item) => item.slug === slug);
  if (!stay) return { title: "Accommodation not found" };
  return {
    title: stay.name + " in " + stay.village + " | Carnia accommodation",
    description: "Stay at " + stay.name + " in " + stay.village + ", Socchieve, Carnia. Check official accommodation availability.",
    alternates: { canonical: "/en/alloggi/" + slug }
  };
}
export default async function EnglishStay({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const stay = stays.find((item) => item.slug === slug);
  if (!stay) notFound();
  return <Shell english>
    <section className="container page-intro"><p className="breadcrumb"><Link href="/en">Home</Link> / <Link href="/en/alloggi">Accommodation</Link> / {stay.name}</p>
      <span className="eyebrow">{stay.village} · Carnia</span><h1>{stay.name}</h1>
      <p>A traditional place to stay in the village of {stay.village}, Socchieve, in the mountains of Carnia.</p>
    </section>
    <section className="container two-col" style={{alignItems:"start",paddingBottom:90}}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="detail-photo" src={stay.photo} alt={stay.name + " in " + stay.village}/>
      <div><h2>Stay in the village.</h2><p>Discover the Col Gentile accommodation in {stay.village}, part of the Albergo Diffuso Socchieve.</p>
        {stay.capacity && <span className="pill">Up to {stay.capacity} guests</span>}
        {stay.cin && <p className="fine" style={{marginTop:15}}>CIN: {stay.cin}</p>}
        <div className="booking-box"><h3>Check your dates</h3><p>Prices and availability are provided by the official Slope booking engine.</p>
          <BookingLink href={SLOPE} placement={"stay_en_" + slug}>Check availability ↗</BookingLink></div>
        <p style={{marginTop:24}}><Link href="/en/alloggi" className="text-link">← All accommodation</Link></p>
      </div>
    </section>
  </Shell>;
}
