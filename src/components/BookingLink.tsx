"use client";
import type { ReactNode } from "react";

export function BookingLink({ href, brand = "col-gentile", placement, children, className = "button" }: {
  href: string; brand?: "col-gentile" | "la-farie"; placement: string; children: ReactNode; className?: string;
}) {
  function track() {
    const target = window as Window & { gtag?: (...args: unknown[]) => void };
    target.gtag?.("event", "booking_click", { brand, placement, destination: href });
  }
  return <a href={href} target="_blank" rel="noopener noreferrer" className={className} onClick={track}>{children}</a>;
}
