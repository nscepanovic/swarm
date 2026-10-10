"""Colosseum deck v8 (2026-10-10): pravac 1, platforma gde ljudi poseduju farmu. Tri kolone: desilo se (proslo vreme, izvor), radi danas (samo potvrdjeno), sledece ("next").
Poceli kao community owned farm, platforma to ponavlja za druge farme. Stil kao v6 (YC: jedna
ideja po slajdu, recenica u naslovu; redosled po Pixar strukturi), tamna pozadina, zuti naslovi.
Tekst je i u content/colosseum/deck.md (izvor istine za tekst i izvore).
Pokretanje: python3 infra/deck_build_v8.py <izlaz.pptx>
Ikonice: Noto Emoji v2.042 (Google, Apache 2.0), u infra/deck_icons/."""
import sys, math, os
ICONS=os.path.join(os.path.dirname(os.path.abspath(__file__)),'deck_icons')
def icon_pic(s,name,cx,y,size=1.25):
    s.shapes.add_picture(os.path.join(ICONS,name+'.png'),Inches(cx-size/2),Inches(y),Inches(size),Inches(size))
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree

Y=RGBColor(0xEF,0xB7,0x3E); W=RGBColor(0xFF,0xFF,0xFF); G=RGBColor(0x9A,0x9A,0xA0)
R=RGBColor(0xD9,0x60,0x5A); L=RGBColor(0x8A,0x8A,0x90)
FONT='Poppins'
prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
C,Lf,Rt=PP_ALIGN.CENTER,PP_ALIGN.LEFT,PP_ALIGN.RIGHT

def slide(notes=''):
    s=prs.slides.add_slide(prs.slide_layouts[6])
    f=s.background.fill; f.gradient(); f.gradient_angle=315
    f.gradient_stops[0].color.rgb=RGBColor(0x1C,0x1C,0x1F); f.gradient_stops[1].color.rgb=RGBColor(0x38,0x37,0x3C)
    if notes: s.notes_slide.notes_text_frame.text=notes
    return s

def tb(s,x,y,w,h,runs,size=20,color=W,bold=False,align=C,anchor=MSO_ANCHOR.TOP,font=FONT):
    """runs: string, ili lista (tekst, boja) za vise boja u jednom redu; '\n' pravi novi pasus."""
    t=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h)).text_frame
    t.word_wrap=True; t.vertical_anchor=anchor
    if isinstance(runs,str): runs=[(runs,color)]
    p=t.paragraphs[0]; p.alignment=align
    for text,col in runs:
        parts=text.split('\n')
        for i,part in enumerate(parts):
            if i>0: p=t.add_paragraph(); p.alignment=align
            if not part: continue
            r=p.add_run(); r.text=part; r.font.size=Pt(size); r.font.bold=bold
            r.font.color.rgb=col
            if font: r.font.name=font
    return t

def arrow(s,x1,y,x2):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y),Inches(x2),Inches(y))
    c.line.color.rgb=L; c.line.width=Pt(1.25)
    ln=c.line._get_or_add_ln(); ln.append(etree.SubElement(ln,qn('a:tailEnd'),type='triangle'))

NODES=[(1.7,'farmer','Farmer'),(5.0,'factory','Food company'),(8.3,'store','Store'),(11.6,'customer','Customer')]
def chain(s,y=1.5):
    for x,icon,label in NODES:
        icon_pic(s,icon,x,y)
        tb(s,x-1.4,y+1.35,2.8,0.5,label,18,W,True)
    for i in range(3):
        arrow(s,NODES[i][0]+0.9,y+0.7,NODES[i+1][0]-0.9)

def head1(s,text,size=38): tb(s,0.8,0.6,11.7,1.6,text,size,Y,True,Lf)
def big(s,y,text,size=30,color=W,bold=True,x=0.8,w=11.7,h=0.9): tb(s,x,y,w,h,text,size,color,bold,Lf)
def xs(s,y=1.5):
    for i in range(3):
        mid=(NODES[i][0]+NODES[i+1][0])/2
        tb(s,mid-0.4,y+0.33,0.8,0.7,'X',30,R,True)

def tag(s,text,color=G): tb(s,0.8,6.75,11.7,0.4,text,13,color,False,Lf)

# 1 cover
s=slide('We are HiveBits. HiveBits is the platform where people own the farm. We did it first: we asked for $140K for our own farm, and in 27 hours 150 people offered $243K.\n\n'
        'KOLONA A. IZVOR: HiveBits na MetaDAO launchpadu, $NECTAR, status COMPLETE (screenshot, news.md 10.10.2026): cilj $140K, ponudjeno $243K, 173%, 150 funders. 27 sati: post @hivebits_io 08.09.2026.')
tb(s,0.8,1.0,11.7,1.3,'HiveBits',66,W,True,Lf)
big(s,2.7,'The platform where people own the farm.',38,Y)
big(s,4.3,'We did it first. 150 people, $243K offered in 27 hours.',30)
big(s,5.1,'We asked for $140K.',30,G,False)

# 2 once upon a time
s=slide('[Once upon a time]\n\nHave you heard of the term "safe food"? It is food where you can check where it comes from and what is inside.\n\n'
        'Most people know only two kinds. Conventional food and organic food.\n\nDo you know what you eat?\n\nNemanjin slajd (Colosseum Deck V1 - Marketplace, 09.10).')
head1(s,'Do you know what you eat?',44)
tb(s,0.8,3.3,3.9,1.6,'Conventional\nfood',32,W,True)
tb(s,4.72,3.3,3.9,1.6,'Safe food',32,Y,True)
tb(s,8.63,3.3,3.9,1.6,'Organic food',32,W,True)

# 3 and every day
s=slide('[And every day]\n\nBetween you and the farmer there are two companies. You never see him. Take milk in Bosnia. You pay $1.09 for a liter. The farmer gets $0.34.\n\n'
        'He does not set his price. The dairy sets it, because the dairy is the only one who pays him. When cheap milk comes from import, the dairy pays him less. This year his price went down 25 percent, and he has nobody else to sell to.\n\n'
        'KOLONA A. IZVOR: otkupna cena Viteski.ba 29.09.2026 ($0.34, pad 25%), cena na polici 072info 29.07.2026 ($1.09). Dva izvora, dva datuma; sirovo naspram preradjenog, zato "od $1.09 farmeru stigne $0.34", ne "mlekara uzima dve trecine".')
head1(s,'You never see the farmer. And he does not set his price.',34)
Y3=2.3
chain(s,Y3)
tb(s,NODES[0][0]-1.4,Y3+1.9,2.8,0.7,'$0.34',34,Y,True)
tb(s,NODES[3][0]-1.4,Y3+1.9,2.8,0.7,'$1.09',34,Y,True)
tb(s,3.2,Y3+2.0,6.9,0.6,'one liter of milk in Bosnia',22,W,False)
tb(s,0.8,5.9,11.7,0.8,[('His price is ',W),('25% lower',R),(' than last year.',W)],28,W,True)

# 4 until one day: what we did (A)
s=slide('[Until one day]\n\nWe are beekeepers. Last month we did it the other way. We did not go to a bank or a buyer. We let anyone invest in our farm and own it.\n\n'
        '150 people did. They own a farm with 300 smart hives, and what the farm makes goes to them, on Solana. They know what they eat, because the farm is theirs.\n\n'
        'KOLONA A. IZVOR: 300 kosnica, $140K, MetaDAO: javni postovi @hivebits_io 07.09 i 08.09.2026 ("All revenue goes back to the onchain-governed, tokenholder-owned treasury"). 150 ulagaca: screenshot MetaDAO (news.md 10.10). "They own the farm": Nemanja 10.10 (open-questions #43: tacna formulacija vlasnistva).')
head1(s,'150 people own our farm. What it makes goes to them, on Solana.',34)
Y4=2.1
chain(s,Y4); xs(s,Y4)
x1,x2,y0,depth=NODES[0][0],NODES[3][0],Y4+2.55,1.3
pts=[]
for k in range(0,61):
    a=math.pi*k/60
    pts.append((Inches((x1+x2)/2-(x2-x1)/2*math.cos(a)),Inches(y0+depth*math.sin(a))))
fb=s.shapes.build_freeform(pts[0][0],pts[0][1]); fb.add_line_segments(pts[1:],close=False)
arc=fb.convert_to_shape(); arc.fill.background(); arc.line.color.rgb=Y; arc.line.width=Pt(2.5)
ln=arc.line._get_or_add_ln(); etree.SubElement(ln,qn('a:tailEnd'),type='triangle')
tb(s,4.17,Y4+2.55,5.0,0.6,'150 owners',30,Y,True)
tb(s,3.67,Y4+3.1,6.0,0.5,'Done. September 2026, on MetaDAO.',22,W,True)

# 5 until one day: the platform (C)
s=slide('[Until one day]\n\nThat is what HiveBits makes repeatable. We are building the platform where this works for other farms, not only ours.\n\n'
        'You invest in a farm and own a part of it. You rent a hive or a cow for a season and get what it makes. Or you simply buy the product.\n\n'
        'KOLONA C. Platforma ne postoji jos kao proizvod (open-questions #8 bez odgovora), zato naslov kaze "We are building". Tri koraka i redosled: Nemanja 10.10. Pravac 1 (Nemanja 10.10): skaliranje na druge profitabilne grane poljoprivrede plus rentanje plus prodaja.')
head1(s,'We are building the platform that repeats it.',38)
big(s,2.4,'1.  Invest in a farm and own a part of it.',36)
big(s,3.5,'2.  Rent a hive or a cow for a season.',36)
big(s,4.6,'3.  Buy the product.',36)
big(s,5.7,'Step 1 is done once, with our farm. Steps 2 and 3 come next.',24,Y)

# 6 and because of that: why us (A/B facts)
s=slide('[And because of that]\n\nWhy us, and not a launchpad? Because a launchpad takes anyone. We pick farms that make money, and we check them before people put money in.\n\n'
        'We can do that because we are farmers. We sell out every season. We sold more than $200K of hives before this raise. And we built our own hive sensors.\n\n'
        'KOLONA A i B. IZVOR: $200K+ od kosnica: post @hivebits_io 05.09.2026. Rasprodato svake sezone: Nemanja (deck.md v3). Sopstveni senzori: post x.com/hivebits_io/status/2096269121751220404 ("every colony monitored by our own hardware"); da li senzori rade danas ili tek na novoj farmi: open-questions #45. '
        '"Pick farms that make money": pravac 1, Nemanja 10.10 ("profitabilne grane"). Provera farmi je nas posao, ne samo skupljanje novca: Nemanja 10.10. Kako tacno izgleda provera: #42, zato na slajdu nema procedure.')
head1(s,'We are farmers. We pick the farms that make money, and we check them.',32)
big(s,2.6,'We sell out every season.',34)
big(s,3.7,'We sold $200K+ of hives before this raise.',34)
big(s,4.8,'We built our own hive sensors.',34)

# 7 traction (A)
s=slide('[And because of that]\n\nWe asked for $140K to build a farm with 300 smart hives. In 27 hours, 150 people offered $243K.\n\n'
        'We could take only $140K. The other $103K had no farm to go to. That is the demand we build the platform for.\n\n'
        'KOLONA A. IZVOR: screenshot MetaDAO (news.md 10.10.2026): cilj $140K, ponudjeno $243K, 173%, 150 funders. 27 sati: post @hivebits_io 08.09.2026. $103K je racun (243 minus 140).')
head1(s,'We asked for $140K. 150 people offered $243K.')
tb(s,0.8,2.4,11.7,2.4,'$243K',150,Y,True,Lf)
big(s,5.2,'in 27 hours, on Solana',32)
big(s,6.0,'$103K had no farm to go to. Yet.',32,Y)

# 8 until finally: market
s=slide('[Until finally]\n\nWe start with honey, because that is our farm. 46 million households in the US buy honey. They spend $839M a year. Our 5 percent of that is $42M, from honey alone.\n\n'
        'Then other farms that make money. Milk is one, you saw the numbers. Every one of them is a farm people can own.\n\n'
        'IZVOR: NielsenIQ for National Honey Board, 52 weeks to 2 Nov 2024 (46.2M x $18.15 = $839M), honey.com/images/files/National-Honey-Board-Category-Review-Analysis-2024.pdf. 5%: Nemanja 24.09. Za trziste vlasnistva nad farmama nema brojke sa izvorom (researcher R3), zato nema druge brojke.')
head1(s,'Honey first. Then other farms that make money.',36)
big(s,2.5,'46 million US households buy honey. $839M a year.',32)
big(s,3.7,'Our 5% of honey alone is $42M.',32,Y)
big(s,4.9,'Every farm we add is a farm people can own.',32)

# 9 team and ask
s=slide('We are farmers and engineers. We are here to win and to join the Colosseum accelerator.\n\n'
        'The accelerator builds the platform and puts the second farm through it. Not our farm, that one is paid for.\n\n'
        'KOLONA C. Upotreba novca: predlog agenta 10.10, Nemanja nije potvrdio (open-questions #46). Druga farma nije u razgovoru ni sa kim (Nemanja 10.10). Iznos se ne pise (Nemanja 10.10).')
head1(s,'We are here to win and join the Colosseum accelerator.',34)
big(s,2.6,'Nemanja Šćepanović',32); big(s,3.3,'CEO, beekeeper. 10 years in engineering and IoT.',22,W,False)
big(s,4.1,'Siniša Kežić',32); big(s,4.8,'COO, chief beekeeper. Runs the farm build.',22,W,False)
big(s,5.8,'The accelerator builds the platform and puts the second farm through it.',22,Y)

# appendix
s=slide('Dodatak. Ovi slajdovi nisu deo videa od tri minuta. Sluze za pitanja i za prijavu.')
tb(s,0.8,3.0,11.7,1.2,'Appendix',54,W,True,Lf)

# A1 done / next (tri kolone, i prijava ranijeg rada koju FAQ trazi)
s=slide('What is done, and what comes next. Colosseum asks us to disclose earlier work, so here it is.\n\n'
        'Done: two earlier Colosseum entries pitched the farm. The farm is now funded by 150 people and being built. We sold $200K+ of hives before that. We built our own hive sensors.\n\n'
        'Next: the platform where other farms get funded the same way, the check before a farm gets in, renting, and product sales. The second farm.\n\n'
        'IZVOR: ranije prijave: colosseum.com/projects/explore/hivebits (Cypherpunk 2025) i /hivebits-1 (Frontier 2026). Farma se gradi: postovi od 16.09 (Bosna, Sinisa) i klip 10. Ostalo kao slajdovi 4, 6, 7. Kolona B (sta radi danas) ceka Nemanjine odgovore (open-questions #45, #8).')
head1(s,'Done, and next.',40)
big(s,2.3,'Done',26,Y,True,0.8,5.6); big(s,2.3,'Next',26,Y,True,7.0,5.6)
tb(s,0.8,2.9,5.6,3.6,'Two Colosseum entries pitched the farm.\n\n150 people funded it. It is being built.\n\n$200K+ of hives sold before that.\n\nOur own hive sensors, built.',22,W,False,Lf)
tb(s,7.0,2.9,5.6,3.6,'The platform: other farms funded the same way.\n\nThe check before a farm gets in.\n\nRenting and product sales.\n\nThe second farm.',22,W,False,Lf)

# A2 how we earn
s=slide('We earn in three places. A fee when a farm is funded, once. A share of every rental, every season. And 5 percent of every sale.\n\n'
        'The first pays for bringing a farm in. The other two grow with the number of farms.\n\n'
        'For renting and buying, the money is locked on Solana in stablecoins until the farmer delivers.\n\n'
        'IZVOR: 5%: Nemanja 24.09 (farmer bira ko snosi). Naknada pri finansiranju i deo od rentanja: Nemanja 10.10, bez procenta (#39, #40). Da li firma zaradjuje od nase farme kao operater: #44. Escrow samo za rent i buy: Nemanja 10.10.')
head1(s,'We earn when a farm is funded, rented, or sells.')
big(s,2.5,'A fee when a farm is funded. Once.',34)
big(s,3.7,'A share of every rental. Every season.',34)
big(s,4.9,'5% of every sale.',34)

# A3 go to market
s=slide('We start with what we know. Our own farm is funded. Next is a second farm, with a farmer we know, funded the same way. '
        'For renting and buying, a farm can join without being funded first. Then other farms that make money.\n\n'
        'IZVOR: Nemanja 10.10. "Farmer we know" je namera, bez imena i bez razgovora.')
head1(s,'First our farm. Then a farmer we know. Then the rest.')
big(s,2.5,'1.  Our own farm. Funded by 150 people.',30)
big(s,3.7,'2.  A second farm, with a farmer we know.',30)
big(s,4.9,'3.  Any farm that makes money, for owning, renting, or buying.',30)

# A4 competition
s=slide('Many teams tried a farm marketplace here. None of them won. They were all software with no farmer behind it.\n\n'
        'We are farmers. We have our farm, our sensors, and 150 people who already own a farm with us.\n\n'
        'IZVOR: Colosseum Copilot, cetiri hakatona od marta 2024 do septembra 2025, provereno 10.10.2026 (competition.md). 3Bee, Pollenity, Honeyverse rentaju samo svoje kosnice, van lanca.')
head1(s,'No farm marketplace won here. They had no farm.')
big(s,2.5,'We have our own farm.',34)
big(s,3.7,'We have our own hardware.',34)
big(s,4.9,'150 people already own a farm with us.',34)

prs.save(sys.argv[1]); print(len(prs.slides._sldIdLst),'slides')
