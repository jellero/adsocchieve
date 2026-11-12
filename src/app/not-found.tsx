import Link from "next/link";
import { Shell } from "@/components/UI";
export default function NotFound(){return <Shell><section className="container page-intro" style={{paddingBottom:130}}><span className="eyebrow">404</span><h1>Pagina non trovata.</h1><p>La pagina che stai cercando non è disponibile.</p><Link href="/it" className="button">Torna alla homepage ↗</Link></section></Shell>}
