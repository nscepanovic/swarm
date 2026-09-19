# Pcelinjak — dizajn igre

**Verzija:** v0.1 · 2026-09-19
**Za:** developera igre (engine i vizuelni stil vec postoje) i Nemanju
**Status:** prvi nacrt. Otvorena pitanja su na dnu.

---

## 1. U jednoj recenici

Igrac postaje pcelar: postavlja pcelinjak, brine o zajednicama kroz sezone,
proizvodi i prodaje med i druge proizvode u gradu, i usput nauci kako pcele
zive, zasto su vazne, i sta ih ugrozava.

## 2. Principi

1. **Znanje otkljucava napredak, ne samo novac.** Bolja oprema, novi
   proizvodi i nova mesta se otvaraju kad igrac zavrsi lekciju i pokaze da
   je razume. Novac sam nije dovoljan.
2. **Igrac uci radeci.** Ne citanjem teksta, nego odlukom: otvori kosnicu,
   pogledaj ram, odluci sta je problem. Tacna odluka daje dobar ishod.
3. **Posledice su realne i sa zakasnjenjem.** Kao u pravom pcelarstvu:
   greska u avgustu (varoa) se vidi u februaru (mrtva zajednica).
   Igra posle objasni vezu.
4. **Propast je lekcija, ne kraj.** Zajednica moze da umre. Igrac dobije
   objasnjenje zasto, i nastavlja.
5. **Pcele nisu same.** Pesticidi, zagadjenje, susa i bolesti su deo sveta.
   Igrac ne resava sve sam: ubedjuje ljude, saradjuje sa drugim pcelarima.

## 3. Svet i mapa

Isti izometrijski stil kao postojeca igra. Jedna regija za pocetak, sa:

| Mesto | Sta je tu | Zasto postoji |
|---|---|---|
| Zemljiste igraca | prazna parcela na kojoj pravi pcelinjak | pocetak igre |
| Bagremova suma | cveta u maju | glavna prolecna pasa |
| Lipe (drvored, suma) | cvetaju u junu | letnja pasa |
| Njive suncokreta | cvetaju u julu | velika letnja pasa; ovde se najcesce prska (vidi 9) |
| Njive uljane repice | cvetaju u aprilu | rana pasa, takodje se prska |
| Livade, vocnjaci | rano prolece | razvoj zajednice posle zime |
| Reka, potok | voda | pcelama treba voda; mesto za pcelinjak blizu vode je bolje |
| Fabrika | zagadjuje vazduh i vodu u svom okrugu | problem koji igrac resava |
| Grad (jedan ili vise) | pijaca, zadruga, laboratorija, udruzenje pcelara, veterinar | prodaja, narudzbine, edukacija |

**Radijus leta.** Pcele najvise skupljaju u krugu od oko 3 km od kosnice
`[proveriti za igru: uzeti 3 km kao pravilo, prikazati kao krug na mapi]`.
Kad igrac bira mesto za pcelinjak, vidi krug i sta cveta u njemu. To je prva
lekcija: **mesto odredjuje med.**

**Vise paša, vise vrsta meda.** Svaka pasa daje svoj med, sa svojom bojom,
ukusom i cenom: bagrem, lipa, livada, suncokret (i repica). Igrac koji zna
kad sta cveta i gde, moze da ima vise vrsta meda u jednoj godini. To je
najveci razlog da se uci kalendar cvetanja.

**Selidba na pasu.** Kasnije u igri igrac moze da preveze kosnice (prikolica)
blizu bagrema ili suncokreta dok cvetaju. Tako rade pravi pcelari.

## 4. Kalendar i vreme

Igra ide kroz godisnja doba. Svaka sezona ima svoj posao:

| Period | Sta se desava u prirodi | Posao pcelara |
|---|---|---|
| Zima (dec-feb) | zajednica u klubetu, ne leti | ne otvara kosnice; slusa, meri tezinu; popravlja opremu, pravi ramove, uci |
| Rano prolece (mar) | prvi izlet, prvi polen | prvi pregled kad je toplo, provera matice i hrane |
| Prolece (apr-maj) | brz razvoj, voce, repica, bagrem | prosirivanje kosnice, sprecavanje rojenja, prvo vrcanje |
| Leto (jun-jul) | lipa, suncokret | vrcanje, selidba, pazi na prskanje |
| Kraj leta (avg) | pasa slabi | posle poslednjeg vrcanja tretman protiv varoe |
| Jesen (sep-nov) | priprema za zimu | prihrana, provera matice, suzavanje leta, zastita od miseva i osa |

Koliko traje godina u igri je otvoreno pitanje (vidi dno). Predlog je da se
jedna sezona odigra za nekoliko sati igre, tako da igrac vidi posledice svojih
odluka iz jedne sezone u sledecoj.

## 5. Zajednica (srce igre)

Svaka kosnica je zajednica sa stanjem koje igrac ne vidi direktno. Vidi ga
samo kad otvori kosnicu i pogleda ramove. To je namerno: **pregled je vestina.**

**Stanje koje se pamti po kosnici:**
- broj pcela (leti je jaka zajednica desetine hiljada, zimi mnogo manje)
- matica: ima je / nema, starost, kvalitet polaganja
- leglo: jaja, larve, poklopljeno leglo, raspored (lep ili rupicast)
- hrana: med i polen u ramovima
- varoa: nivo zaraze
- bolest: nema / neka od bolesti iz sekcije 9
- pritisak rojenja: raste kad je gusto i puno hrane
- narav: mirne ili agresivne pcele
- prostor: broj nastavaka i ramova

**Pregled kosnice (glavna interakcija):**
Igrac otvara kosnicu i vadi ramove jedan po jedan. Na svakom ramu vidi
nacrtano sta je u njemu. Zadatak je da prepozna sta vidi, i to je
edukacija, isto kao zadaci iz matematike u postojecoj igri:

| Zadatak | Sta igrac nauci |
|---|---|
| Nadji maticu medju pcelama | kako izgleda matica, trut, radilica |
| Ima li jaja? | jaja znace da je matica bila tu pre par dana, i bez vidjenja matice |
| Lep ili rupicast raspored legla? | rupicasto leglo znaci problem (matica, bolest) |
| Maticnjaci na dnu rama ili na sredini? | rojevni ili matica se menja: razlicita odluka |
| Test na varou (secer u prahu ili alkohol) | kako se meri zaraza, i kad je vreme za tretman |
| Koliko ramova je zauzeto? | kad treba dodati prostor, a kad ne |

**Razvoj pcele** (ide u lekciju, i koristi se u simulaciji):
matica 16 dana, radilica 21 dan, trut 24 dana od jajeta do izlaska
`[proveriti: Nemanja potvrdjuje brojke pre nego sto udju u igru]`.

**Pravilo pregleda:** kosnica se ne otvara po kisi, hladnom vremenu ni zimi.
Ako igrac to uradi, zajednica trpi. Tako se uci kad se sme raditi.

## 6. Pcelinjak i oprema

**Postavljanje pcelinjaka.** Igrac bira mesto na svom zemljistu i dobija
ocenu mesta: sunce, zaklon od vetra, voda blizu, sta cveta u radijusu, koliko
je daleko od puta i od kuca. Kosnice ne stoje prema stazi kojom ljudi hodaju.

**Tipovi kosnica** (u nasem kraju najcesce): LR, Dadant-Blatt, AZ
`[proveriti koje tri uzeti za pocetak]`. Svaka ima prednosti. Pocetak je
jedna vrsta, ostale se otkljucavaju.

**Oprema, sa sta otkljucava:**

| Oprema | Sta omogucava | Otkljucava se |
|---|---|---|
| Zastitno odelo i rukavice | manje uboda pri pregledu | od pocetka (osnovno), bolje posle lekcije |
| Dimilica | mirnije pcele pri pregledu | lekcija "Kako se prilazi kosnici" |
| Pcelarski nozic | vadjenje ramova | od pocetka |
| Maticna resetka | cist med bez legla u medistu | lekcija o matici |
| Hranilica | prihrana u prolece i jesen | lekcija "Zima" |
| Vrcaljka (rucna, pa elektricna) | vadjenje meda | prvo vrcanje |
| Topionica voska | vosak od starih ramova i poklopaca | lekcija o vosku |
| Hvataci polena, propolisa | novi proizvodi | lekcije o tim proizvodima |
| Prikolica | selidba na pasu | reputacija + lekcija o selidbi |

## 7. Proizvodi

| Proizvod | Kako nastaje u igri | Sta utice na kvalitet |
|---|---|---|
| Med (bagremov, lipov, suncokretov, livadski) | vrcanje posle pase | vrsta pase, zrelost (poklopljen med), cistoca, rezidue |
| Vosak | topljenje poklopaca i starih ramova | cistoca, da li je bilo lekova |
| Propolis | struganje ili hvatac | kasnije u igri |
| Polen | hvatac polena na letu | ne sme da se preteruje, zajednici treba |
| Roj i matice | prodaja drugim igracima | napredno |
| Maticni mlec, apitoksin | napredno, zahteva posebnu edukaciju | kasnije, vidi otvorena pitanja |

**Zrelost meda.** Nezreo med (nepoklopljen) ima previse vode i moze da
fermentise. Igrac koji vrca prerano dobije losiji med, i laboratorija u gradu
mu to pokaze. Zakonska granica za vodu u medu je 20%
`[proveriti za Srbiju]`.

**Kristalizacija.** Bagremov med dugo ostaje tecan, repicin kristalise brzo.
Kupac u gradu koji pita "zasto se med skamenio" je zadatak za edukaciju
kupca, ne greska igraca.

**Usluga oprasivanja** (kasnije u igri). Vocar ili plantaza zove pcelara
da donese kosnice dok vocnjak cveta, i placa za to. Prvi takav posao je
**oprasivanje badema**, pa ostalo voce. Badem cveta veoma rano, pa
zajednica mora da bude jaka vec na kraju zime: igrac koji je dobro pripremio
zimu moze da uzme posao, ostali ne mogu. Uci da je oprasivanje vrednije od
meda: bez pcela nema ni ploda. `[proveriti: kad badem cveta u nasem kraju]`

## 8. Grad, trgovina i narudzbine

- **Pijaca:** igrac prodaje sta ima. Cena zavisi od vrste i kvaliteta.
- **Narudzbine:** NPC trazi "5 tegli bagremovog do kraja proleca" ili
  "vosak za svece". Ispunjena narudzbina daje novac i reputaciju.
- **Laboratorija:** analiza meda (voda, rezidue, poreklo). Med sa
  sertifikatom vredi vise. Tu igrac saznaje da mu fabrika ili prskanje
  kvare med.
- **Udruzenje pcelara:** lekcije, takmicenja, i drugi igraci.
- **Veterinar:** dijagnoza bolesti, obavezna prijava nekih bolesti.

## 9. Problemi i opasnosti

### Za pcele

| Problem | Kako se pojavi | Sta igrac radi | Sta nauci |
|---|---|---|---|
| Varoa | uvek prisutna, raste kroz leto | meri, tretira u pravo vreme | najveci ubica zajednica; tretman posle poslednjeg vrcanja, ne pre |
| Americka kuga legla | retko, iz kupljenih ramova ili od grabeza | prepozna, zove veterinara, spaljuje | obavezna prijava; spore traju godinama `[proveriti]` |
| Nozema, krecno leglo | slaba zajednica, lose vreme | jaca zajednicu, menja maticu | slaba zajednica je bolesna zajednica |
| Rojenje | gusto, puno hrane, prolece | prosiri, napravi vestacki roj | roj odnese pola pcela i vecinu meda te godine |
| Grabez i ose | kraj leta | suzi leto, ne prosipa med | jaka zajednica se sama brani, slaba ne |
| Misevi zimi | jesen | stavi zastitu na leto | male stvari pre zime spasavaju zajednicu |
| Susa | leto | voda, selidba | bez vode i cveta nema meda |
| **Prskanje pesticida** | poljoprivrednik prska u cvetu, danju | vidi mrtve pcele ispred kosnice, ide kod njega | vidi niz ispod |
| **Fabrika** | zagadjuje okrug oko sebe | laboratorija pokaze rezidue, pcelinjak slabi | vidi niz ispod |

**Niz zadataka "Komsija prska".** Glavno mesto za ovo su **njive suncokreta**,
jer se tu prska najvise, a suncokret je i velika pasa. Ljudi koji seju su
publika za edukaciju, ne neprijatelji. Poljoprivrednik NPC prska u podne
dok cveta. Igrac ujutru nadje mrtve pcele. Ide kod njega i razgovara. Opcije
nisu "pobedi ga", nego ubedi ga cinjenicama:
- da prska uvece, kad pcele ne lete
- da ne prska dok biljka cveta
- da javi pcelarima dan ranije, da zatvore kosnice
- da predje na organsku zastitu (duza linija zadataka)
- da shvati da i njemu pcele trebaju: suncokret koji pcele oprase daje vise
  semena `[proveriti formulaciju]`
Pogresan pristup (vikanje, pretnja) zatvara saradnju za neko vreme. Tacan
pristup menja NPC-jevo ponasanje za celu mapu, i to koristi i drugim
igracima.

**Niz zadataka "Fabrika".** Igrac primeti slabije zajednice i losiju analizu
meda u okrugu oko fabrike. Moze da seli pcelinjak (kratko resenje), ili da
skupi dokaze (analize vise pcelara), udruzi se sa drugim igracima i trazi
promenu (dugo resenje, zajednicki cilj servera). Uci da su pcele
**bioindikator**: ono sto se nadje u medu, ima i u okolini.

### Za ljude (opasnosti od pcela)

| Situacija | Sta igrac nauci |
|---|---|
| Pregled bez odela ili dima | ubod boli, pcele se brane kad ih uznemirimo |
| Rad po kisi, sa jakim mirisom, naglim pokretima | kad i kako se prilazi kosnici |
| Posetilac uboden, otice mu lice i tesko dise | to je alergijska reakcija i hitan slucaj: zvati hitnu pomoc, ne cekati |
| Uboden igrac: kako se vadi zaoka | struganjem, ne stiskanjem `[proveriti]` |
| Dete prilazi kosnicama | kako objasniti deci da se pcele ne boje ako ih ne diramo |

Ovo ide kroz NPC situacije, ne kroz tekst upozorenja.

## 10. Napredak: znanje, iskustvo, reputacija

Tri odvojene stvari:
- **Znanje** = zavrsene lekcije. Lekciju daje NPC (stari pcelar, veterinar,
  udruzenje). Lekcija se zavrsava zadatkom u igri, ne kvizom na papiru.
  Primer: "Rojenje" se zavrsava kad igrac prepozna rojevne maticnjake i
  napravi vestacki roj.
- **Iskustvo** = sezone koje je zajednica prezivela, uspesni pregledi.
- **Reputacija** u gradu = ispunjene narudzbine, kvalitet meda, pomoc
  drugima.

Otkljucavanje trazi kombinaciju. Elektricna vrcaljka trazi novac i
iskustvo. Selidba trazi znanje i reputaciju.

**Stablo znanja za pocetak:**
1. Zivot pcele (matica, radilica, trut) → otkljucava pregled ramova
2. Kako se prilazi kosnici → dimilica, bolje odelo
3. Pase i cvetanje → mapa pase, izbor mesta
4. Rojenje → vestacki roj, druga kosnica
5. Varoa → test i tretman
6. Vrcanje i zrelost meda → vrcaljka, prodaja
7. Zima → hranilica, priprema
8. Pesticidi i zagadjenje → zadaci sa poljoprivrednikom i fabrikom
9. Opasnosti i prva pomoc → zadaci sa posetiocima
10. Vosak, propolis, polen → novi proizvodi

## 11. NPC-jevi

| NPC | Uloga |
|---|---|
| Stari pcelar (mentor) | vodi kroz prve lekcije, komentarise greske |
| Poljoprivrednik | prska; kasnije saveznik |
| Veterinar | bolesti, obavezna prijava |
| Laborant | analize meda |
| Kupci na pijaci | narudzbine, pitanja o medu (edukacija kupca) |
| Direktor fabrike | dugi niz zadataka |
| Uciteljica sa decom | igrac drzi cas o pcelama: igrac postaje ucitelj |

## 12. Vise igraca i takmicenje

Takmicenje meri **dobro pcelarenje, ne kolicinu meda**:
- **Sajam meda** (u gradu, jednom po sezoni): ocenjuje se kvalitet, ne
  kolicina. Laboratorija ocenjuje, ne igraci.
- **Sezonska tabela:** procenat zajednica koje su prezivele zimu, zdravlje,
  zavrsene lekcije.

Saradnja, jer tako radi pravo pcelarstvo:
- **Varoa se prenosi izmedju susednih pcelinjaka.** Ako sused ne tretira,
  i tvoje zajednice se zaraze. Tretman u isto vreme u celom kraju radi
  bolje. Ovo je prirodan razlog da igraci razgovaraju.
- Prodaja i razmena rojeva i matica medju igracima.
- Zajednicki ciljevi servera: promena ponasanja poljoprivrednika, fabrika.

## 13. Prva igriva verzija

Dovoljno malo da se napravi, dovoljno da se vidi da igra radi:

- jedna mapa: zemljiste igraca, bagrem, livada, jedna njiva, reka, jedan grad
- jedna sezona: prolece (mart do kraja bagrema)
- do 3 kosnice po igracu, jedan tip kosnice
- pregled kosnice sa zadacima: matica, jaja, leglo, maticnjaci, prostor
- lekcije 1-4 i 6
- jedan proizvod: med (livadski i bagremov), prodaja na pijaci, narudzbine
- NPC: mentor, poljoprivrednik (niz "Komsija prska" na njivi uljane repice,
  jer suncokret cveta tek leti), kupac
- vise igraca na mapi kao u postojecoj igri, bez takmicenja

Van prve verzije: leto (lipa, suncokret), zima i jesen, varoa, bolesti,
fabrika, selidba, usluga oprasivanja (badem), ostali proizvodi, sajam.

## 14. Otvorena pitanja

**Za Nemanju:**
1. Kome je igra namenjena? Deci (kao matematika), odraslima koji pocinju sa
   pcelarstvom, ili oboma?
2. Jezik igre: srpski, engleski, oba?
3. Veza sa HiveBits-om: da li igra treba da ima bilo kakvu vezu (prave
   kosnice, $NECTAR, apiterapija), ili je potpuno odvojena?
4. Apitoksin i apiterapija u igri: da ili ne? Ako da, samo kao edukacija
   (sta je), bez tvrdnji o lecenju.
5. Koje tri vrste kosnica koristimo?
6. Potvrda svih mesta obelezenih sa `[proveriti]`.

**Za developera:**
1. Koliko traje dan i sezona u igri? Da li engine ima vreme i godisnja doba?
2. Da li engine podrzava stanje koje se menja dok igrac nije u igri
   (zajednica raste, varoa raste)?
3. Koliko igraca je na jednoj mapi, i da li mogu da vide tudje pcelinjake?
4. Kako se u postojecoj igri radi zadatak od NPC-ja: moze li zadatak da bude
   "klikni na pravu stvar na slici" (za pregled ramova)?
