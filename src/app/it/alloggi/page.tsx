import type { Metadata } from "next";
import { BookingLink } from "@/components/BookingLink";
import { StayFilters } from "@/components/StayFilters";
import { Shell } from "@/components/UI";
import { SLOPE } from "@/lib/data";

export const metadata: Metadata = {
  title: "Alloggi in Carnia | Case e appartamenti a Socchieve",
  description: "Sfoglia gli alloggi dell'Albergo Diffuso Col Gentile tra Feltrone, Viaso, Lungis e Mediis. Filtra per località e numero di ospiti e prenota su Slope.",
  alternates: { canonical: "/it/alloggi" }
};
export default function Alloggi() { return <Shell>
  <section className="container page-intro"><p className="breadcrumb"><a href="/it">Home</a> / Alloggi</p>
    <span className="eyebrow">Col Gentile · Albergo Diffuso</span><h1>Dove dormire a Socchieve, nel cuore della Carnia.</h1>
    <p>Esplora le case e gli appartamenti del nostro albergo diffuso. Ogni scheda racconta una residenza; i prezzi e la disponibilità aggiornati si verificano sul sistema ufficiale di prenotazione.</p>
    <BookingLink href={SLOPE} placement="catalog_top">Verifica disponibilità ↗</BookingLink>
  </section>
  <section className="container" style={{paddingBottom:90}}><StayFilters/></section>
  </Shell>; }
