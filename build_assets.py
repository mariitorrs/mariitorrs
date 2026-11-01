from pathlib import Path
from html import escape

OUT = Path(__file__).parent / 'assets'
OUT.mkdir(exist_ok=True)
CREAM = '#FFF0DA'
RED = '#A32235'
DARK = '#23311E'
OLIVE = '#626B34'
INK = '#3D3026'
ROSE = '#E6B2A0'
FONT = 'Verdana, DejaVu Sans, sans-serif'
SERIF = 'Georgia, DejaVu Serif, serif'

def svg(name, width, height, content, title):
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img"><title>{escape(title)}</title>{content}</svg>', encoding='utf-8')

def rect(x,y,w,h,fill,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'

def text(x,y,value,size=18,color=INK,font=FONT,extra=''):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{color}" {extra}>{escape(value)}</text>'

def sprite(rows, palette, x=0,y=0,u=2):
    return '<g shape-rendering="crispEdges">'+''.join(rect(x+c*u,y+r*u,u,u,palette[ch]) for r,row in enumerate(rows) for c,ch in enumerate(row) if ch in palette)+'</g>'

BERRY=['....gg.g....','...gggggg...','....gggg....','..rrrrrrrr..','.rrhrhrhrrr.','.rhrhrhrhrr.','.rrhrhrhrdr.','..rhrhrhdr..','..rrhrhrdr..','...rhrhdr...','....rhdr....','.....dd.....']
FLOWER=['....cc....','...cccc...','.cccyyccc.','ccccyycccc','.cccyyccc.','...cccc...','....cc....']
HEART=['.rr..rr.','rrrrrrrr','rrrrrrrr','.rrrrrr.','..rrrr..','...rr...']
PAL={'g':OLIVE,'r':'#CA3042','h':'#EC726C','d':RED,'c':CREAM,'y':'#D9A843'}

def berry(x=0,y=0,u=2):
    return sprite(BERRY,PAL,x,y,u)

def gingham(w,y,h=12,u=6):
    result=''
    for row in range((h+u-1)//u):
        for col in range((w+u-1)//u):
            fill=CREAM if row%2 and col%2 else RED if not row%2 and not col%2 else ROSE
            result+=rect(col*u,y+row*u,min(u,w-col*u),min(u,h-row*u),fill)
    return result

svg('raspberry.svg',24,24,berry(), 'Framboesa em pixel art')
svg('heart.svg',24,18,sprite(HEART,{'r':RED},0,0,3),'Coração em pixel art')
svg('divider.svg',1000,28,rect(0,13,458,1,ROSE)+rect(542,13,458,1,ROSE)+berry(488,1,2),'Divisor com framboesa')
svg('intro.svg',520,90,rect(0,0,520,90,CREAM)+berry(21,32,2)+text(260,59,'Oi, eu sou a Mari.',42,RED,SERIF,'text-anchor="middle"')+sprite(FLOWER,{**PAL,'c':ROSE},471,34,3),'Oi, eu sou a Mari.')

for file,label,color,width in [('linkedin','LinkedIn',RED,126),('instagram','Instagram',DARK,142),('spotify','Spotify',OLIVE,118),('repositories','Meus repositórios',RED,208)]:
    body=rect(4,0,width-8,32,color)+rect(0,4,width,24,color)+sprite(HEART,{'r':CREAM},12,10,1.6)+text(34,21,label,12,CREAM,FONT)
    svg(f'link-{file}.svg',width,32,body,label)

tech_groups={
'development': ('#A32235', ['HTML5','CSS3','JavaScript','Python','Java','FastAPI','Kotlin','Android Studio']),
'data': ('#23311E',['SQL','PostgreSQL','Pandas','PySpark','LangGraph','Qdrant']),
'design': ('#626B34',['Figma','UX/UI','Design Thinking','Prototipação','Acessibilidade']),
'infra': ('#6C3840',['Git','GitHub','Linux','Docker','Kubernetes'])
}
for group,(color,labels) in tech_groups.items():
    for label in labels:
        filename=label.lower().replace(' ','-').replace('/','-').replace('ç','c').replace('ã','a')
        w=round(len(label)*7.7+26)
        svg(f'tech-{filename}.svg',w,28,rect(2,0,w-4,28,color)+rect(0,2,w,24,color)+text(w/2,18.5,label,12,CREAM,FONT,'text-anchor="middle"'),label)

for name,label,w in [('frigus','Frigus',126),('ai-advisor','Assessor financeiro com IA',420),('saveit','SaveIt',128),('ux','Interfaces e experiências',402)]:
    svg(f'project-{name}.svg',w,42,rect(0,0,w,42,CREAM)+berry(0,9,2)+text(36,30,label,25,RED,SERIF),label)

def cassette(name,label,color):
    w,h=302,176
    body=rect(8,8,286,146,color)+rect(0,16,302,130,color)
    body+=rect(10,16,282,120,CREAM)+rect(18,8,266,8,CREAM)
    body+=text(151,45,label,26,color,SERIF,'text-anchor="middle"')
    body+=rect(28,59,246,39,color)+rect(75,68,152,21,CREAM)
    for x in [60,242]:
        body+=f'<circle cx="{x}" cy="79" r="15" fill="{CREAM}"/><circle cx="{x}" cy="79" r="7" fill="{color}"/>'
        body+=rect(x-2,65,4,28,color)+rect(x-14,77,28,4,color)
    body+=text(151,124,'lado A · na minha playlist',12,color,FONT,'text-anchor="middle"')
    body+=rect(88,146,126,8,CREAM)+rect(96,138,110,8,CREAM)
    body+=sprite(HEART,{'r':color},21,111,2)
    body+=rect(0,168,302,4,OLIVE)
    svg(f'music-{name}.svg',w,h,body,label+' — na minha playlist')
cassette('laufey','Laufey',RED)
cassette('billie','Billie Eilish',DARK)
svg('footer.svg',1000,66,rect(0,0,1000,66,CREAM)+text(500,29,'feito com carinho.',32,RED,SERIF,'text-anchor="middle"')+gingham(1000,50,16,8),'Feito com carinho.')
print('SVGs atualizados.')
