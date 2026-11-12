import type { MetadataRoute } from "next";
import { BASE, stays } from "@/lib/data";
export default function sitemap(): MetadataRoute.Sitemap {
  const urls = ["/it","/it/alloggi","/it/territorio","/it/trekking","/it/cicloturismo","/it/contact","/en","/en/alloggi","/en/territory","/en/contact"];
  return [...urls, ...stays.map((stay) => "/it/alloggi/" + stay.slug)].map((url) => ({
    url: BASE + url,
    changeFrequency: url.indexOf("/alloggi/") !== -1 ? "monthly" : "weekly",
    priority: url === "/it" ? 1 : url.includes("alloggi") ? 0.8 : 0.6
  }));
}
