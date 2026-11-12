import type { Metadata } from "next";
import Link from "next/link";
import { BookingLink } from "@/components/BookingLink";
import { Shell } from "@/components/UI";
import { EMAIL, SLOPE, TEL } from "@/lib/data";
export const metadata: Metadata = {title:"Contact Col Gentile | Socchieve, Carnia", description:"Get in touch with Col Gentile Albergo Diffuso in Socchieve, Carnia. Email and telephone contact details.", alternates:{canonical:"/en/contact"}};
export default function EnglishContact() {return <Shell english>
  <section className="container page-intro"><p className="breadcrumb"><Link href="/en">Home</Link> / Contact</p><h1>Contact Col Gentile.</h1><p>For enquiries about apartments and village stays in Carnia.</p></section>
  <section className="container two-col" style={{paddingBottom:90,alignItems:"start"}}><div className="alt-panel"><h2>Reception</h2><p>Via Roma 20, 33020 Mediis, Socchieve (UD), Italy</p><p><a className="text-link" href={"mailto:"+EMAIL}>{EMAIL}</a></p><p><a className="text-link" href={"tel:"+TEL}>+39 0433 819934</a></p></div><div><h2>Book your stay</h2><p>Check dates and actual availability through the official booking system.</p><BookingLink href={SLOPE} placement="contacts_en">Check availability ↗</BookingLink></div></section>
  </Shell>; }
