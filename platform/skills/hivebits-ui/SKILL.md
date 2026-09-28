---
name: hivebits-ui
description: Pravila dizajna i UX-a za HiveBits platformu (mapa, kosnice, kupovina, pcelar, admin). Ucitaj pre nego sto napravis ili menjas bilo koji ekran, komponentu ili tekst na ekranu.
---

# HiveBits UI/UX

Ovo je nacin na koji HiveBits izgleda i ponasa se. Vazi za svaki ekran,
javni, kupcev, pcelarev i adminov. Kad je u sumnji: prostije.

## 1. Osecaj

Sajt treba da deluje kao **pcelinjak, ne kao kripto aplikacija**: pravi
ljudi, prave fotografije, brojke sa terena. Kupac treba da oseti da
gleda u kosnicu, ne u dashboard. Reference po osecaju, ne po kopiranju:
sajt malog proizvodjaca hrane sa dobrim fotografijama, i prognoza
vremena (velike brojke, jasne jedinice).

Sta se ne radi: ilustracije pcela iz stock biblioteka, gradijenti "web3"
tipa, neon, glassmorphism, tokeni i grafikoni cena, animirane pozadine,
bilo sta sto lici na berzu.

## 2. Boje

Tokeni, definisani na jednom mestu, svetla i tamna tema.

- `bg`: skoro bela (svetla) / skoro crna (tamna). Nikad cisto #fff / #000.
- `surface`: kartice, malo odvojene od pozadine.
- `text`, `text-muted`: dve nijanse, ne vise.
- `honey`: jedan topao zuto-narandzasti akcenat za primarno dugme i za
  "Live" indikator. Jedini jak akcenat na sajtu.
- `ok`, `warn`, `danger`: zelena, zuta, crvena, samo za stanja, nikad kao
  dekoracija.
- `line`: linije i okviri, tihe.

Pravilo: na jednom ekranu najvise jedan element u `honey` boji koji zove
na akciju. Ako ih ima dva, jedan je pogresan.

## 3. Tipografija

Jedan font za sve (sistemski ili jedan web font sa 2 debljine). Naslovi
krupni i mirni, bez velikih slova. Brojke sa senzora u tabularnom obliku
(cifre iste sirine) da ne skacu kad se menjaju. Velicine: 4 nivoa
naslova, 1 telo, 1 sitno. Ne vise.

## 4. Raspored

- Telefon prvo. Sirina 360px mora da radi bez horizontalnog skrola.
  Bocna margina 16px na telefonu, 24px+ na vecem.
- Jedna kolona na telefonu, najvise dve na desktopu (sadrzaj + bocna).
- Mapa: na telefonu zauzima gornjih 45% ekrana, lista ispod; prekidac
  "Map / List" prilepljen uz dno. Na desktopu mapa levo 55%, lista desno.
- Kartica kosnice: fotografija 4:3 preko cele sirine kartice, ispod ime,
  cena, mesta, oznake. Sve sto se klikne je cela kartica.
- Razmaci iz skale od 4px (4, 8, 12, 16, 24, 32, 48). Ne izmisljati 13px.
- Radijus: jedan za kartice i polja (npr. 12px), jedan za dugmad (isti ili
  pun). Senke tihe, jedna vrsta.

## 5. Dugmad i akcije

- **Primarno** (`honey` pozadina, tamni tekst): jedno po ekranu. "Take
  this hive", "Buy", "Publish", "Pay with card".
- **Sekundarno** (okvir, bez pozadine): "See apiary", "Add address".
- **Tiho** (samo tekst): "Cancel", "Back".
- **Opasno** (crveni okvir, crvena pozadina tek u dijalogu potvrde):
  "Refund", "Unpublish", "Delete".
- Visina 48px na telefonu, 44px na desktopu. Tekst je glagol + objekat,
  kratko: "Rent this hive", ne "Proceed to hive acquisition".
- Dugme koje ceka pokazuje spinner u sebi i ne moze dva puta da se
  klikne. Posle uspeha: promena teksta ili prelaz na sledeci ekran, ne
  oba.
- Dijalog potvrde samo za nepovratne stvari (refund, brisanje). Ne za
  Publish, ne za Pause.

## 6. Forme

- Jedno polje po redu. Labela iznad polja, uvek vidljiva (ne placeholder
  kao labela).
- Pomocni tekst ispod polja samo kad ima sta da se kaze ("Your exact
  location is never shown.").
- Greska ispod polja, crveno, recenica koju covek razume: "Add a shipping
  address so Sinisa knows where to send the honey." Ne "Field required".
- Validacija pri izlasku iz polja i pri slanju, ne dok se kuca.
- Nacrt se cuva sam. Ako korisnik ode i vrati se, unos je tu.
- Duge forme (Apply, Add hive) idu u jednom ekranu sa skrolom, ne u
  koracima; nista nije duze od jednog ekrana na desktopu osim liste
  fotografija.
- Dodavanje fotografija: prevuci ili dodirni, prikaz odmah, redosled se
  vuce, brisanje sa x. Velicina se smanjuje na klijentu pre slanja.

## 7. Stanja, sva

Svaka lista i svaki blok imaju cetiri stanja i sva su nacrtana:
- **Prazno**: recenica i, ako ima smisla, jedno dugme. "No hives yet.
  Add your first hive." Nikad prazan beli prostor.
- **Ucitavanje**: skelet u obliku sadrzaja (kartice), ne spinner na
  sredini.
- **Greska**: sta se desilo i sta da uradi, sa dugmetom "Try again".
- **Puno**: sadrzaj.

Posebna stanja koja moraju da postoje: "Sold out" (kartica ostaje, dugme
nestaje, tekst sivi), "No data since 3 days" (Live blok bez `honey`
boje), "Paused" (samo pcelar i admin vide), "Pending" (zapis na lancu
ceka; siva tacka, bez uzbune).

## 8. Live podaci

- Tri brojke u redu: tezina, temperatura, vlaga. Velike cifre, jedinica
  sitno pored (kg, °C, %). Ispod, sitno: "12 minutes ago".
- Zelena tacka + "Live" samo ako je merenje mladje od 24h. Nikad
  animacija pulsiranja.
- Grafik: jedna linija, tezina, 7 dana, bez mreze, bez legende, sa
  vrednoscu na dodir. 30 dana kao prekidac. Bez drugih grafika na strani
  kosnice.
- Ako nema senzora, blok ne postoji. Ne pisati "No sensor".

## 9. Tekst na ekranu

- Engleski, prost, kao da ga je napisao pcelar kome engleski nije
  maternji: kratke recenice, obicne reci. "Pick a hive. Watch it live.
  Get its honey."
- Bez em dasha (—) igde. Tacka ili zarez.
- Bez uzvicnika osim u potvrdi kupovine (jedan).
- Bez kripto reci u glavnom toku: ne "NFT", "mint", "on-chain", "tx",
  "wallet address" u kupcevom toku. Umesto toga "Hive Pass", "record on
  Solana", "Pay with USDC", "Connect wallet".
- Imena ljudi, ne uloge: "Sinisa will ship within 5 days", ne "The
  vendor will ship".
- Brojke uvek sa jedinicom, datumi kao "12 June 2026", nikad "06/12/26".
- Oznake (badges) su jedna ili dve reci: Live, Verified, Sold out, In
  stock, Lab tested, Featured.

## 10. Mapa

- Tacke su jednostavne (krug u `honey` boji sa brojem kosnica). Bez
  ikona pcela.
- Kad je vise tacaka blizu, grupisu se sa brojem.
- Nikad tacna lokacija. Aplikacija ne sme ni da ima nacin da javno
  prikaze tacnu koordinatu.
- Klik na tacku: mala kartica iznad tacke, sa fotografijom, imenom,
  brojem kosnica i dugmetom. Na telefonu kartica ide uz dno ekrana.
- Mapa u tihim bojama (siva ili blago topla), da tacke i fotografije
  budu jedino sto se istice.

## 11. Admin

Isti tokeni, gusce. Tabele sa fiksnim zaglavljem, pretraga gore, filteri
kao cipovi. Svaka opasna akcija trazi razlog u tekstu i pise ko i kad.
"View as" ima jasnu traku na vrhu ekrana: "You are viewing as Sinisa.
Exit." Admin nikad ne izgleda kao javni deo, da se ne pomesa.

## 12. Pristupacnost i brzina

- Kontrast teksta najmanje 4.5:1, ukljucujuci tekst na `honey` dugmetu.
- Sve se moze tastaturom; fokus je vidljiv.
- Svaka fotografija ima alt tekst (ime kosnice ili pcelinjaka).
- Velicina dodira najmanje 44px.
- Slike se ucitavaju lenjo i u pravoj velicini; pocetna sa mapom ispod
  2 sekunde na 4G.
- `prefers-reduced-motion` gasi svaku animaciju.

## 13. Kontrolna lista pre nego sto je ekran gotov

- [ ] Jedna primarna akcija, u `honey` boji, i samo jedna.
- [ ] Radi na 360px bez horizontalnog skrola.
- [ ] Prazno, ucitavanje, greska i puno stanje postoje i vidjeni su.
- [ ] Tekst je iz `spec.md` ili u istom tonu; bez kripto zargona; bez
      em dasha.
- [ ] Brojke imaju jedinice, datumi su ispisani.
- [ ] Fotografije prave, alt tekst postoji.
- [ ] Svetla i tamna tema obe proverene.
- [ ] Nista ne otkriva tacnu lokaciju ni tudju adresu.
- [ ] Screenshot u `screenshots/` sa imenom ekrana.
