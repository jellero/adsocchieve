import Link from "next/link";
import type { ReactNode } from "react";
import { BookingLink } from "./BookingLink";
import { EMAIL, SLOPE, TEL } from "@/lib/data";
import type { Stay } from "@/lib/data";

export function Header({ farie = false, english = false }: { farie?: boolean; english?: boolean }) {
  const base = farie ? "/la-farie" : english ? "/en" : "/it";
  const links = farie
    ? [["/la-farie", "La Farie"], ["/la-farie/camere", "Le camere"], ["/la-farie/contatti", "Contatti"]]
    : english
      ? [["/en", "Home"], ["/en/alloggi", "Stays"], ["/en/territory", "Territory"], ["/en/contact", "Contact"]]
      : [["/it", "Home"], ["/it/alloggi", "Alloggi"], ["/it/territorio", "Territorio"], ["/it/trekking", "Trekking"], ["/it/contact", "Contatti"]];
  return <header className="header">
    <div className="container nav-shell">
      <Link href={base} className="brand" aria-label={farie ? "La Farie" : "Col Gentile"}>
        <strong>{farie ? "LA FARIE" : "COL GENTILE"}</strong>
        <small>{farie ? "DIMORA A LUNGIS · CARNIA" : "ALBERGO DIFFUSO SOCCHIEVE"}</small>
      </Link>
      <nav className="nav-links" aria-label="Navigazione principale">
        {links.map(([url, label]) => <Link key={url} href={url}>{label}</Link>)}
        <Link href={farie ? "/it" : "/la-farie"}>{farie ? "Col Gentile ↗" : "La Farie ↗"}</Link>
        {!farie && <Link href={english ? "/it" : "/en"}>{english ? "IT" : "EN"}</Link>}
      </nav>
      <div className="nav-cta">
        {farie ? <Link className="button small" href="/la-farie/camere">Le camere ↗</Link> : <BookingLink href={SLOPE} placement="header" className="button small">{english ? "Book" : "Prenota"} ↗</BookingLink>}
        <details className="mobile-nav"><summary aria-label="Apri il menu">☰</summary>
          <nav className="mobile-menu" aria-label="Menu mobile">
            {links.map(([url, label]) => <Link key={url} href={url}>{label}</Link>)}
            <Link href={farie ? "/it" : "/la-farie"}>{farie ? "Col Gentile" : "La Farie"}</Link>
            {!farie && <Link href={english ? "/it" : "/en"}>{english ? "Italiano" : "English"}</Link>}
          </nav>
        </details>
      </div>
    </div>
  </header>;
}

export function Footer({ farie = false }: { farie?: boolean }) {
  return <footer className="footer">
    <div className="container footer-grid">
      <div><h3 className="serif">{farie ? "La Farie" : "Col Gentile"}</h3>
        <p>{farie ? "La Farie, Lungis · Socchieve · Carnia" : "Albergo Diffuso Socchieve. Case e appartamenti nei borghi della Carnia."}</p>
        {farie && <p>Parte del gruppo AD, con gestione delle prenotazioni distinta.</p>}
      </div>
      <div><h3>Esplora</h3><Link href="/it/alloggi">Appartamenti Col Gentile</Link><Link href="/la-farie">La Farie</Link><Link href="/it/territorio">Scopri Socchieve</Link></div>
      <div><h3>Contatti</h3>{farie ? <>
        <Link href="/la-farie/contatti">Recapiti La Farie</Link><p>Contatti dedicati da confermare.</p>
      </> : <>
        <a href={"mailto:" + EMAIL}>{EMAIL}</a><a href={"tel:" + TEL}>+39 0433 819934</a><p>Via Roma 20, Mediis, Socchieve (UD)</p><p>P.IVA 02790180307</p>
      </>}</div>
    </div>
    <div className="container footer-bottom"><span>© Albergo Diffuso Socchieve</span><span>Privacy e cookie policy: da aggiornare prima del go-live.</span></div>
  </footer>;
}

export function Shell({ children, farie = false, english = false }: { children: ReactNode; farie?: boolean; english?: boolean }) {
  return <div lang={english ? "en" : "it"} className={farie ? "farie" : ""}><Header farie={farie} english={english}/><main id="main">{children}</main><Footer farie={farie}/></div>;
}

export function Card({ stay, english = false }: { stay: Stay; english?: boolean }) {
  const url = (english ? "/en/alloggi/" : "/it/alloggi/") + stay.slug;
  return <article className="card">
    <Link href={url} aria-label={"Scopri " + stay.name}>
      {/* Immagine temporanea del sito esistente */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="card-photo" src={stay.photo} alt={stay.name + " a " + stay.village} loading="lazy"/>
    </Link>
    <div className="card-body"><div className="eyebrow">{stay.village} · {stay.kind}</div><h3><Link href={url}>{stay.name}</Link></h3>
      <div className="card-meta"><span>{stay.capacity ? (english ? "Up to " + stay.capacity + " guests" : "Fino a " + stay.capacity + " ospiti") : (english ? "Property details" : "Scheda della struttura")}</span><Link href={url}>{english ? "Details ↗" : "Scopri ↗"}</Link></div>
    </div>
  </article>;
}
