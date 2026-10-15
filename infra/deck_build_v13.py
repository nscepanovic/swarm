"""Colosseum deck v13 (2026-10-12; v12 plus dizajn po YC clanku "How to design a better pitch deck": slajd 2 bez slika, slajd 3 naslov sa brojkama, slajd 4 tri kutije, slajd 6 dve velike brojke, slajd 7 cetiri reda umesto matrice)

Osnova, v12 (2026-10-12; v11 plus tri Nemanjine izmene: naslovna u pet reci bez $140K, slajd 3 "removes the middleman", slajd 5 "community is our first buyer")

Osnova, v11 (2026-10-12): po Nemanjinom brief-u od 12.10 i odobrenom
rasporedu od osam slajdova. Jedna masina (krug) umesto tri stuba, otvara se
dokazom (rejz), jasno kaze sta je on-chain na Solani.
Stil kao v6-v10 (jedna ideja po slajdu, recenica u naslovu), tamna pozadina,
zuti naslovi. Mesta za prave fotografije su isprekidani okviri.
Tekst je i u content/colosseum/deck.md (izvor istine za tekst i izvore);
kad se menja tekst, menjaju se oba.
Pokretanje: python3 infra/deck_build_v13.py <izlaz.pptx>
Ikonice: Noto Emoji v2.042 (Google, Apache 2.0), u infra/deck_icons/."""
import sys, os
ICONS=os.path.join(os.path.dirname(os.path.abspath(__file__)),'deck_icons')
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.oxml.ns import qn
from lxml import etree

Y=RGBColor(0xEF,0xB7,0x3E); W=RGBColor(0xFF,0xFF,0xFF); G=RGBColor(0x9A,0x9A,0xA0)
L=RGBColor(0x8A,0x8A,0x90); D=RGBColor(0x2A,0x2A,0x2E); GR=RGBColor(0x6F,0xC2,0x8A); BL=RGBColor(0x7F,0xB3,0xE6)
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

def icon_pic(s,name,cx,y,size=1.25):
    s.shapes.add_picture(os.path.join(ICONS,name+'.png'),Inches(cx-size/2),Inches(y),Inches(size),Inches(size))

def arrow(s,x1,y,x2,color=L):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y),Inches(x2),Inches(y))
    c.line.color.rgb=color; c.line.width=Pt(1.5)
    ln=c.line._get_or_add_ln(); ln.append(etree.SubElement(ln,qn('a:tailEnd'),type='triangle'))

def rect(s,x,y,w,h,fill=D,line=L,lw=1.0,rounded=True,dash=False):
    r=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    if fill is None: r.fill.background()
    else: r.fill.solid(); r.fill.fore_color.rgb=fill
    if line is None: r.line.fill.background()
    else:
        r.line.color.rgb=line; r.line.width=Pt(lw)
        if dash: r.line.dash_style=MSO_LINE_DASH_STYLE.DASH
    r.shadow.inherit=False
    return r

def photo(s,x,y,w,h,label):
    """Mesto za pravu fotografiju: isprekidan okvir sa opisom. Zamenjuje se u Slides-u."""
    rect(s,x,y,w,h,D,L,1.25,False,True)
    tb(s,x+0.2,y+h/2-0.5,w-0.4,1.0,label,14,G,False,C,MSO_ANCHOR.MIDDLE)

def head1(s,text,size=34,w=11.7): tb(s,0.8,0.5,w,1.6,text,size,Y,True,Lf)
def sub(s,text,y=2.2,size=20,w=11.7,color=W): tb(s,0.8,y,w,0.9,text,size,color,False,Lf)
def foot(s,text,color=G,size=13): tb(s,0.8,6.85,11.7,0.4,text,size,color,False,Lf)
def tag(s,x,y,text,color):
    r=rect(s,x,y,1.4,0.34,None,color,1.0)
    tb(s,x,y+0.02,1.4,0.3,text,10,color,True,C)

def line_arrow(s,x1,y1,x2,y2,color=Y,width=2.0):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y1),Inches(x2),Inches(y2))
    c.line.color.rgb=color; c.line.width=Pt(width)
    ln=c.line._get_or_add_ln(); ln.append(etree.SubElement(ln,qn('a:tailEnd'),type='triangle'))

# 1 cover
s=slide('Hi, I am Nemanja, founder of HiveBits. We build community-owned farms and we sell what they produce.\n\nA: $140K raised, 150 people, 27 hours (Nemanja 12.10; MetaDAO screenshot, news.md 10.10; post @hivebits_io 08.09.2026). Main sentence is the approved one from 12.10, word for word. C: "builds farms" in plural and "sells" are the model; one farm is funded and under construction, sales have not started (said on slides 4 and 5).')
tb(s,0.8,1.9,11.7,0.9,'HiveBits',40,W,True,C)
tb(s,0.8,3.0,11.7,2.6,'Community-owned farms.\nNo middlemen.',48,Y,True,C)

# 2 proof
s=slide('[Proof]\n\nWe started the farm with one idea: let anyone invest in beekeeping. We raised 140 thousand dollars through our token, NECTAR, on MetaDAO. 150 people funded 300 smart hives in 27 hours. It is the first tokenized farm owned by the community.\n\nA: "we raised $140K through $NECTAR on Futard for the first tokenized farm owned by the community" (Nemanja 12.10). 150 funders, $140K target, $243K offered, 173% (MetaDAO screenshot, news.md 10.10). 27 hours: post @hivebits_io 08.09.2026 ("one day and three hours"). futard.io/launch/AbTuTsoBJS2jQggvfb7d1LA2SfbHa5NB5HbJqX8C2PnS. "First tokenized smart bee farm is live on @solana": @SuperteamBR, RT @hivebits_io 07.09.2026. B: farm under construction in Bosnia, documented (Nemanja brief 11.10; post @hivebits_io 16.09). On-chain today: the raise and the token. Nothing else on this slide is claimed as on-chain.\n\nNE PISE: "Target: $140,000", $243K (#49), revenue, returns.\n\nSLIKE: levo screenshot Futard stranice (Nemanja ga daje), desno prava fotka farme.')
head1(s,'We raised $140K for the first tokenized farm owned by the community.',32)
for i,(num,lab) in enumerate([('150','people'),('300','smart hives'),('27','hours')]):
    x=0.8+i*4.0
    tb(s,x,2.3,3.8,1.4,num,80,Y,True,Lf)
    tb(s,x,3.8,3.8,0.6,lab,24,W,False,Lf)
tb(s,0.8,4.75,11.7,0.9,'On Solana: the raise and the token.\n$NECTAR on Futard, in the MetaDAO ecosystem.',20,GR,True,Lf)
tb(s,0.8,6.1,11.7,0.6,'The farm is being built in Bosnia. We record every step.',20,W,True,Lf)

# 3 problem (slajd iz v10, tekst nepromenjen)
s=slide('[Problem]\n\nNow the problem. The farmer does not set his price. In the US, a beekeeper who sells to a middleman gets about one third of what he gets when he sells direct. We remove the middleman. Crypto was built for that.\n\nA: USDA NASS Honey, March 2026: 2025 average price sold to co-ops/packers $2.45/lb; retail (beekeeper sells direct) $7.15/lb. https://esmis.nal.usda.gov/sites/default/release-files/795818/hony0326.txt (market.md 4a). One category, one country, one primary source. B: the marketplace runs on crypto infrastructure; cards are accepted too, everything settles in stablecoins (Nemanja 12.10). HiveBits takes 5% of a sale; the packer takes the gap between $2.45 and $7.15.\n\nNE GOVORI: "all intermediaries are unnecessary", "every farmer gets one third".')
head1(s,'A beekeeper gets $2.45 a pound. Selling direct, $7.15.',36)
yc=2.7
nodes=[(1.7,'farmer','Beekeeper'),(5.0,'factory','Packer'),(8.3,'store','Store'),(11.6,'customer','Customer')]
for x,icon,label in nodes:
    icon_pic(s,icon,x,yc,1.3); tb(s,x-1.3,yc+1.4,2.6,0.5,label,20,W,True)
for i in range(3): arrow(s,nodes[i][0]+0.85,yc+0.65,nodes[i+1][0]-0.85)
tb(s,0.2,yc+2.0,3.0,0.8,'$2.45',40,Y,True)
tb(s,10.1,yc+2.0,3.0,0.8,'$7.15',40,Y,True)
tb(s,0.8,5.9,11.7,1.0,'HiveBits removes the middleman between the farmer and the buyer. Crypto was built for that.',24,W,True,Lf)

# 4 marketplace
s=slide('[Marketplace]\n\nNow we are building the marketplace. You can rent a whole hive for a season, or you can just buy the product. The rent is paid upfront, so the farmer knows his harvest is sold before the season starts. We sell our own products first. Then we invite other beekeepers, dairy farmers and other farmers. We take 5 percent of every sale. We start with farmers we know. Our hive sensors show weight, temperature and humidity. They show what happens. They do not certify quality.\n\nC: marketplace is being built; no sales and no rentals yet (Nemanja 10.10 and 12.10). Rent a whole hive or a cow or just buy the product; our products first, then other beekeepers, dairy farmers and others; 5% of every sale: Nemanja 12.10, word for word. B: hive sensors measure weight, temperature, humidity (Nemanja brief 11.10; post @hivebits_io "every colony monitored by our own hardware"). Start with farmers we know: Nemanja brief 11.10.\n\nNE PISE: escrow, payment method, lab test, fee on rental as a separate number, sensors on cows.\n\nFOTO: desno mesto za pravu fotografiju pametne kosnice sa senzorom.')
head1(s,'Now we are building the marketplace that sells what farms produce.',32)
for i,(t,body) in enumerate([('RENT','Rent a whole hive for a season.'),('BUY','Or just buy the product.'),('5%','We take 5% of every sale.')]):
    x=0.8+i*4.0
    rect(s,x,2.5,3.7,3.4,D,Y,1.5)
    tb(s,x+0.3,2.8,3.1,1.0,t,48,Y,True,Lf)
    tb(s,x+0.3,4.1,3.1,1.6,body,24,W,False,Lf)

# 5 loop
s=slide('[The loop]\n\nThis is one machine, not three products. The community funds a farm on-chain. The farm produces, and the sensors show it. The products sell on the marketplace. Sales show that the farm works, so the community funds the next one. The new farm brings new products and new buyers. The community we are building is our first buyer. The first step is done. The marketplace closes the loop.\n\nA: step 1 happened once ($140K, 300 hives, Futard, on Solana). B: sensors exist on our hives. C: steps 3, 4 and 5 are the model (Nemanja 12.10: the community invests in new farms, products are sold through the same marketplace). "The community is our first buyer" (Nemanja 12.10) is the plan: no sale has happened yet. Do not state it as a number or a conversion rate. Only confirmed revenue: 5% of every sale. A fee on funding new farms and hardware sales are NOT confirmed and are not on the slide.')
head1(s,'One loop: the community funds a farm, the farm produces, the marketplace sells.',30)
bw,bh=3.6,1.5; xs=[0.8,4.87,8.93]; yt,yb=2.0,4.05
def node(x,y,num,icon,text,line=L,lw=1.0):
    rect(s,x,y,bw,bh,D,line,lw)
    icon_pic(s,icon,x+0.55,y+0.38,0.7)
    tb(s,x+1.05,y+0.08,0.4,0.4,num,13,Y,True,Lf)
    tb(s,x+1.05,y+0.38,bw-1.15,bh-0.4,text,14,W,False,Lf)
node(xs[0],yt,'1','coin','The community funds a farm, on-chain.',GR,1.75)
node(xs[1],yt,'2','bee','The farm produces. Sensors show it.')
node(xs[2],yt,'3','store','Products sell on the marketplace. 5% to HiveBits.')
node(xs[2],yb,'4','handshake','Sales show the farm works. The community funds the next one.')
node(xs[0],yb,'5','seedling','The new farm brings new products and new buyers.')
line_arrow(s,xs[0]+bw+0.05,yt+bh/2,xs[1]-0.05,yt+bh/2)
line_arrow(s,xs[1]+bw+0.05,yt+bh/2,xs[2]-0.05,yt+bh/2)
line_arrow(s,xs[2]+bw/2,yt+bh+0.05,xs[2]+bw/2,yb-0.05)
line_arrow(s,xs[2]-0.05,yb+bh/2,xs[0]+bw+0.05,yb+bh/2)
line_arrow(s,xs[0]+bw/2,yb-0.05,xs[0]+bw/2,yt+bh+0.05)
tb(s,xs[1],yb+0.05,bw,0.6,'the next farm',13,G,False,C)
tb(s,0.8,5.75,11.7,0.9,'The community we are building is our first buyer.',18,Y,True,Lf)
foot(s,'We did step 1 with our own farm. The marketplace closes the loop, and that is what we are building now.',W,14)

# 6 market and expansion
s=slide('[Market and expansion]\n\nWe start with honey. In the US, people eat about 4.4 billion dollars of honey a year, at shelf price. In the European Union it is between 2.6 and 5.2 billion euros. Our vision is bigger than honey: new farms funded by the community, other kinds of sustainable agriculture, and one marketplace for all of it.\n\nMETHOD: households (or tonnes eaten) x yearly honey spend (or retail price) = size of the honey category per market. This is category demand, not our revenue. SAM and SOM are not calculated (#53).\nSAME METHOD FOR BOTH (Nemanja 12.10): all honey eaten in a year x average shelf price. This is a ceiling, not actual retail sales: part of the honey goes to industry and food service at bulk prices.\nUS: 688.6M lb eaten (2024, USDA ERS via National Honey Board) x $6.39/lb average shelf price (derived: $1,075M / 168.3M lb, NielsenIQ for National Honey Board, 52 wks to 2 Nov 2024, https://honey.com/images/files/National-Honey-Board-Category-Review-Analysis-2024.pdf) = $4.4B. For reference, what US households actually buy in stores: 46.2M households x $18.15 = $839M (same NielsenIQ report, p. 21).\nEU: 436.5K t apparent consumption (2022, CBI, https://www.cbi.eu/market-information/honey/certified-honey/market-potential); retail EUR 5.58-24.94/kg (Stiftung Warentest 4/2025, Germany, 24 honeys), EUR 6-12 taken as the typical range. Result is a range.\nMontreal (about 4,200 t a year, no retail price from a primary source) and Brazil (about 12,000 t a year, supply market first) are off the slide; numbers and sources stay in deck.md.\nC: expansion is vision (Nemanja 12.10: the community invests in new farms and other kinds of sustainable agriculture, products sold through the same marketplace). No numbers for other categories.')
head1(s,'We start with honey. The loop is built for other farms too.',32)
tb(s,0.8,2.0,11.7,0.5,'Honey eaten per year, at shelf price',20,G,True,Lf)
for i,(name,res) in enumerate([('United States','$4.4B'),('European Union','€2.6 to 5.2B')]):
    y=2.7+i*1.45
    tb(s,0.8,y+0.25,4.2,0.8,name,30,W,True,Lf)
    tb(s,5.0,y,7.6,1.2,res,60,Y,True,Lf)
tb(s,0.8,5.9,11.7,1.0,'Vision: new farms funded by the community. Other kinds of sustainable agriculture. One marketplace sells it all.',20,W,True,Lf)

# 7 competition
s=slide('[Competition]\n\nOthers do parts of this. Some let you adopt a hive or a tree. Some trade between businesses. Some sell farmland. But as far as we found, nobody holds the whole loop.\n\nIZVORI (web pretraga 11.10): Pollenity: EBRD news 2026 (Adopt-a-Hive subscription, single-origin honey), CORDIS 887791 (BeeBot, HiHive). CrowdFarming: Euronews 05.06.2026 (adoptions, 300+ producers), FreshPlaza; fee 16-32% (market.md). AgriDex: The Defiant ($9M stablecoin trades, B2B, Africa), The Block (first RWA trade on Solana, 0.15% per side). AcreTrader: accredited only, $10-25K minimum (2026 review). FarmTogether: accredited, $15K crowdfunding minimum, $50K fund (farmtogether.com). Competitor metrics stay in notes, not on the slide. "As far as we found": competition.md 24.09 (Colosseum corpus, other chains) plus web search 11.10; Frontier 2026 corpus not searched. Drenio is off the slide: not verifiable (drenio.rs does not load, web search 11.10 and 12.10 finds nothing), #52.\n\nHiveBits row: filled = exists today (community funding done once with our farm; sensors on our hives). Outline = in build (rent, buy, beyond one category).')
head1(s,'Each of them holds one part of the loop. As far as we found, none holds the whole loop.',28)
rows=[('Adopt a hive or a tree','Pollenity, CrowdFarming'),
      ('Trade between businesses','AgriDex'),
      ('Buy farmland','AcreTrader, FarmTogether'),
      ('Building the whole loop','HiveBits')]
y0=2.35; rh=1.05
for i,(what,who) in enumerate(rows):
    y=y0+i*rh; me=(who=='HiveBits')
    if me: rect(s,0.6,y+0.05,12.1,rh-0.1,RGBColor(0x3A,0x36,0x28),Y,1.5)
    tb(s,0.8,y,7.0,rh,what,30,Y if me else W,True,Lf,MSO_ANCHOR.MIDDLE)
    tb(s,7.8,y,4.7,rh,who,22 if not me else 30,Y if me else G,me,Rt,MSO_ANCHOR.MIDDLE)

# 8 team and next
s=slide('[Team and next]\n\nWe are two engineers and beekeepers. We were at Colosseum twice with the smart hive. Since then we raised the money and started to build the farm. Next we finish the farm, launch the marketplace, and fund the next farm with the community. We want the accelerator to help us expand faster into other kinds of agriculture and to scale this model. We are building all of it in public. Thank you.\n\nB: team, two confirmed sentences (Nemanja brief 11.10). Eduardo is not in the team (Nemanja 10.10). A: two earlier Colosseum entries, Cypherpunk 2025 (https://colosseum.com/projects/explore/hivebits) and Frontier 2026 (https://colosseum.com/projects/explore/hivebits-1), both pitched the smart hive, no prize. This is the disclosure of earlier work the FAQ asks for. C: five next steps, all from Nemanja 12.10, no dates, no amounts. No ask (not confirmed, #51). GitHub status not verified (#22).\n\nFOTO: levo dole, osnivaci.')
head1(s,'We run real hives. Now we build the marketplace.',34)
tb(s,0.8,1.9,5.0,0.4,'Team',16,Y,True,Lf)
tb(s,0.8,2.3,5.0,1.9,[('Nemanja Šćepanović\n',W),('Beekeeper and engineer. Runs an apitherapy centre.\n\n',G),('Siniša Kežić\n',W),('Manages the farm.',G)],15,W,False,Lf)
photo(s,0.8,4.3,5.0,2.4,'Photo: founders (real)')
tb(s,6.5,1.9,6.1,0.4,'Next',16,Y,True,Lf)
tb(s,6.5,2.3,6.1,2.6,'1.  Finish the farm in Bosnia. Keep recording every step.\n2.  Launch the marketplace with our own products.\n3.  Invite the first beekeepers and dairy farmers.\n4.  Open renting: a whole hive for a season.\n5.  Fund the next farm with the community.',16,W,False,Lf)
rect(s,6.5,5.0,6.1,1.7,D,L,1.0)
tb(s,6.75,5.08,5.6,0.4,'Colosseum before',13,Y,True,Lf)
tb(s,6.75,5.45,5.6,1.2,'Cypherpunk 2025 and Frontier 2026. Both pitched the smart hive. Since then: the raise, the farm, and now the marketplace.',14,W,False,Lf)

prs.save(sys.argv[1]); print(len(prs.slides._sldIdLst),'slides')
