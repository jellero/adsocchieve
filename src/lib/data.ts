export const BASE = "https://www.albergodiffusosocchieve.it";
export const SLOPE = "https://booking.slope.it/3460bf53-7a84-49a4-a9da-910cfd962010";
export const FARIE_BOOKING = "https://www.booking.com/hotel/it/la-farie-socchieve-fraz-lungis.it.html";
export const EMAIL = "info@albergodiffusosocchieve.it";
export const TEL = "+390433819934";

export const photos = {
  hero: "https://www.albergodiffusosocchieve.it/sites/default/files/Casa-Vanda-esterno_0_0.jpg",
  pradin: "https://www.albergodiffusosocchieve.it/sites/default/files/CasaPradin-esterno.jpg",
  vanda: "https://www.albergodiffusosocchieve.it/sites/default/files/Casa-Vanda-esterno_0_0.jpg",
  rosuline: "https://www.albergodiffusosocchieve.it/sites/default/files/ErnRosuline2-terrazzo_1.jpg",
  kitchen: "https://www.albergodiffusosocchieve.it/sites/default/files/Q30A9845_0.jpg",
  lungis: "https://www.albergodiffusosocchieve.it/sites/default/files/styles/slide/public/PanoramaLungis3.jpg?itok=3vbEWL7k",
  farie: "https://cf.bstatic.com/xdata/images/hotel/max1024x768/514929336.jpg?hp=1&k=431d996dfd96f9f41e9564de708b80fce853afcff44a58e3353475fad1393a11&o="
};

export type Stay = {
  slug: string;
  name: string;
  village: string;
  kind: "Residenza" | "Appartamento";
  capacity?: number;
  cin?: string;
  description: string;
  photo: string;
};

export const stays: Stay[] = [
  { slug: "casa-pradin", name: "Casa Pradin", village: "Feltrone", kind: "Residenza", capacity: 9, cin: "IT030110A1GDIE8AKW", photo: photos.pradin, description: "Casa su tre piani con terrazze in legno, portico ombreggiato e quattro camere matrimoniali, indicata per gruppi e famiglie numerose." },
  { slug: "casa-rovedo", name: "Casa Rovedo", village: "Feltrone", kind: "Residenza", capacity: 5, cin: "IT030110A1DP63JJDN", photo: photos.pradin, description: "Casa ristrutturata a Feltrone, con giardino privato, terrazze panoramiche, due camere e cucina." },
  { slug: "casa-vanda", name: "Casa Vanda", village: "Viaso", kind: "Residenza", capacity: 18, photo: photos.vanda, description: "Edificio storico con archi in pietra e ballatoi in legno, diviso in unità ricettive nella frazione di Viaso." },
  { slug: "casa-vanda-genziana", name: "Casa Vanda Genziana", village: "Viaso", kind: "Appartamento", capacity: 8, cin: "IT030110A1F58PGPCB", photo: photos.vanda, description: "Due camere, cucina, soggiorno e accesso alla terrazza in legno." },
  { slug: "casa-vanda-bucaneve", name: "Casa Vanda Bucaneve", village: "Viaso", kind: "Appartamento", capacity: 5, cin: "IT030110A1VMEPFPI7", photo: photos.vanda, description: "Camera, cucina e soggiorno con accesso alla terrazza." },
  { slug: "casa-vanda-iris", name: "Casa Vanda Iris", village: "Viaso", kind: "Appartamento", capacity: 6, cin: "IT030110A17XXDKLY9", photo: photos.vanda, description: "Più camere, soggiorno, cucina e terrazza in legno." },
  { slug: "casa-vanda-papavero", name: "Casa Vanda Papavero", village: "Viaso", kind: "Appartamento", capacity: 5, cin: "IT030110A1YUHRC6JJ", photo: photos.vanda, description: "Camera, cucina e ampio soggiorno affacciato sulla terrazza." },
  { slug: "ernesto-da-rosuline-1", name: "Ernesto da Rosuline 1", village: "Lungis", kind: "Appartamento", photo: photos.kitchen, description: "Appartamento della residenza Ernesto da Rosuline a Lungis." },
  { slug: "ernesto-da-rosuline-2", name: "Ernesto da Rosuline 2", village: "Lungis", kind: "Appartamento", photo: photos.rosuline, description: "Appartamento della residenza Ernesto da Rosuline, con ballatoi in legno." },
  { slug: "ernesto-da-rosuline-3", name: "Ernesto da Rosuline 3", village: "Lungis", kind: "Appartamento", photo: photos.rosuline, description: "Appartamento della residenza Ernesto da Rosuline a Lungis." },
  { slug: "ernesto-da-rosuline-terra-0", name: "Ernesto da Rosuline Terra", village: "Lungis", kind: "Appartamento", photo: photos.kitchen, description: "Unità della residenza Ernesto da Rosuline a Lungis." },
  { slug: "casa-ernesto-da-rosuline", name: "Casa Ernesto da Rosuline", village: "Lungis", kind: "Residenza", photo: photos.rosuline, description: "Residenza tradizionale nel borgo di Lungis con corte interna e più unità." },
  { slug: "casa-dal-miedi", name: "Casa dal Miedi", village: "Mediis", kind: "Appartamento", capacity: 8, cin: "IT030110A1C8FJEG48", photo: photos.hero, description: "Appartamento al primo piano con due camere, soggiorno con angolo cottura e terrazzo." },
  { slug: "casa-ai-pascoli", name: "Casa Ai Pascoli", village: "Mediis", kind: "Residenza", photo: photos.hero, description: "Residenza presente nel catalogo Albergo Diffuso Socchieve; dettagli da confermare." }
];
