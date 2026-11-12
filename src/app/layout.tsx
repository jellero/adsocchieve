import type { Metadata } from "next";
import type { ReactNode } from "react";
import { BASE } from "@/lib/data";
import "./globals.css";
export const metadata: Metadata = {
  metadataBase: new URL(BASE),
  title: { default: "Albergo Diffuso Socchieve | Dormire in Carnia", template: "%s | Albergo Diffuso Socchieve" },
  description: "Case e appartamenti a Socchieve, in Carnia. Scopri l'ospitalità nei borghi di Col Gentile e la dimora La Farie.",
  openGraph: { type: "website", locale: "it_IT", siteName: "Albergo Diffuso Socchieve" }
};
export default function RootLayout({ children }: { children: ReactNode }) {
  return <html lang="it"><body>{children}</body></html>;
}
