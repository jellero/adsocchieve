"use client";
import { useMemo, useState } from "react";
import { stays } from "@/lib/data";
import { Card } from "./UI";

export function StayFilters() {
  const [village, setVillage] = useState("all");
  const [guests, setGuests] = useState("0");
  const villages = Array.from(new Set(stays.map((stay) => stay.village))).sort();
  const filtered = useMemo(() => stays.filter((stay) => (village === "all" || stay.village === village) && (!Number(guests) || (stay.capacity !== undefined && stay.capacity >= Number(guests)))), [village, guests]);

  return <>
    <div className="filters" aria-label="Filtra gli alloggi">
      <label>Località
        <select value={village} onChange={(e) => setVillage(e.target.value)}>
          <option value="all">Tutte le località</option>
          {villages.map((v) => <option value={v} key={v}>{v}</option>)}
        </select>
      </label>
      <label>Numero di ospiti
        <select value={guests} onChange={(e) => setGuests(e.target.value)}>
          <option value="0">Qualsiasi</option>
          {[2,3,4,5,6,7,8,9].map((n) => <option value={n} key={n}>{n} o più</option>)}
        </select>
      </label>
      <span className="count" aria-live="polite">{filtered.length} risultati</span>
    </div>
    <p className="fine">I filtri per ospiti mostrano solo alloggi con capienza verificata. Prezzi e disponibilità sono gestiti su Slope.</p>
    {filtered.length ? <div className="cards">{filtered.map((stay) => <Card key={stay.slug} stay={stay}/>)}</div> : <p className="empty">Nessun alloggio corrisponde ai filtri selezionati.</p>}
  </>;
}
