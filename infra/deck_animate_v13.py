"""Verzija decka v13 za snimanje videa: fade prelaz izmedju svih slajdova i
animacije na klik (fade in) samo na slajdu 5 (krug), da koraci prate govor iz
content/colosseum/pitch-video.md. Ne menja tekst ni raspored.

Pokretanje: python3 infra/deck_animate_v13.py <ulaz.pptx> <izlaz.pptx>

STEPS: po slajdu lista klikova; svaki klik je lista indeksa oblika (redosled
kojim ih pravi infra/deck_build_v13.py) koji se pojavljuju zajedno. Oblici
koji nisu ni u jednom kliku vide se od pocetka (naslov, izvor). Ako se u build
skripti doda ili izbaci oblik, indeksi ovde moraju da se poprave."""
import sys
from lxml import etree
from pptx import Presentation

def r(a, b): return list(range(a, b + 1))

STEPS = {
    5: [r(1, 4),                    # 1 community funds a farm
        [21] + r(5, 8),             # 2 farm produces
        [22] + r(9, 12),            # 3 marketplace
        [23] + r(13, 16),           # 4 sales, next farm
        [24, 26] + r(17, 20) + [25],  # 5 new farm, krug se zatvara
        [27],                       # community is our first buyer
        [28]],                      # step 1 is done
}

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'

def effect(ids, spid, first):
    node = 'clickEffect' if first else 'withEffect'
    return (
        f'<p:par><p:cTn id="{next(ids)}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" nodeType="{node}">'
        f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
        f'<p:set><p:cBhvr><p:cTn id="{next(ids)}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
        f'<p:to><p:strVal val="visible"/></p:to></p:set>'
        f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{next(ids)}" dur="400"/>'
        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
        f'</p:childTnLst></p:cTn></p:par>')

def timing(clicks):
    ids = iter(range(3, 100000))
    body = ''
    for spids in clicks:
        effs = ''.join(effect(ids, sp, i == 0) for i, sp in enumerate(spids))
        body += (
            f'<p:par><p:cTn id="{next(ids)}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
            f'<p:par><p:cTn id="{next(ids)}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            f'{effs}</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    return (
        f'<p:timing xmlns:p="{P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
        f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>{body}</p:childTnLst></p:cTn>'
        f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
        f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
        f'</p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')

prs = Presentation(sys.argv[1])
total = 0
for n, slide in enumerate(prs.slides, 1):
    sld = slide._element
    for tag in ('transition', 'timing'):
        for old in sld.findall(f'{{{P}}}{tag}'): sld.remove(old)
    # redosled u p:sld: cSld, clrMapOvr, transition, timing
    sld.append(etree.fromstring(f'<p:transition xmlns:p="{P}" spd="med"><p:fade/></p:transition>'))
    if n not in STEPS: continue
    shapes = list(slide.shapes)
    used = [i for c in STEPS[n] for i in c]
    assert len(used) == len(set(used)) and max(used) < len(shapes), f'slajd {n}: los indeks'
    assert n != 5 or len(shapes) == 29, 'slajd 5 je promenjen, popravi indekse'
    clicks = [[shapes[i].shape_id for i in c] for c in STEPS[n]]
    sld.append(etree.fromstring(timing(clicks)))
    total += len(clicks)
    print(f'slajd {n}: {len(clicks)} klikova')
prs.save(sys.argv[2]); print('fade prelaz na', len(prs.slides._sldIdLst), 'slajdova, ukupno klikova:', total)
