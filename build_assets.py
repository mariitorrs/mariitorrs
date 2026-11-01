import textwrap, html

FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', monospace"

REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none !important}}"

# ---------------------------------------------------------------- pixel cat
SPRITE = [
    "..##........##..",
    ".###........###.",
    ".#pp########pp#.",
    ".##############.",
    "################",
    "################",
    "################",
    "################",
    "##cc###nn###cc##",
    "##cc##m##m##cc##",
    ".##############.",
    ".##############.",
    ".##############.",
    ".###..####..###.",
    ".###........###.",
]
COL = {"#": "#F8C9DB", "p": "#E26C97", "c": "#FF86AE", "n": "#C9456F", "m": "#8A3E5E"}
SHADE = "#EDA3C0"


def pixel_cat(px=10):
    out = []
    for r, row in enumerate(SPRITE):
        for c, ch in enumerate(row):
            if ch in ".":
                continue
            color = COL[ch]
            if ch == "#" and r >= 11:
                color = SHADE
            out.append(f'<rect x="{c*px}" y="{r*px}" width="{px}" height="{px}" fill="{color}"/>')
    body = "\n".join(out)
    eyes = ""
    for cx in (3, 11):
        eyes += (f'<g class="eye"><rect x="{cx*px}" y="{5*px}" width="{2*px}" height="{2*px}" fill="#3A1F2D"/>'
                 f'<rect x="{cx*px}" y="{5*px}" width="{px}" height="{px}" fill="#fff"/></g>')
    # tail: two frames toggling
    t1 = "".join(f'<rect x="{x*px}" y="{y*px}" width="{px}" height="{px}" fill="{SHADE}"/>'
                 for x, y in [(15, 12), (16, 12), (17, 11), (17, 10)])
    t2 = "".join(f'<rect x="{x*px}" y="{y*px}" width="{px}" height="{px}" fill="{SHADE}"/>'
                 for x, y in [(15, 12), (16, 12), (17, 12), (17, 13)])
    tail = (f'<g>{t1}<animate attributeName="opacity" values="1;0;1" keyTimes="0;.5;1" dur="1.4s" '
            f'calcMode="discrete" repeatCount="indefinite"/></g>'
            f'<g>{t2}<animate attributeName="opacity" values="0;1;0" keyTimes="0;.5;1" dur="1.4s" '
            f'calcMode="discrete" repeatCount="indefinite"/></g>')
    return body + eyes + tail


STAR = "M0 -10 L2.6 -2.6 L10 0 L2.6 2.6 L0 10 L-2.6 2.6 L-10 0 L-2.6 -2.6Z"


def sparkle(x, y, s, delay, color="#FFD3E4"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="tw" style="animation-delay:{delay}s" '
            f'd="{STAR}" fill="{color}"/></g>')


# ---------------------------------------------------------------- banner
def banner():
    W, H = 1200, 360
    sparks = "".join([
        sparkle(880, 80, 1.1, 0), sparkle(1135, 95, .8, .7), sparkle(1150, 245, 1.2, 1.3),
        sparkle(870, 255, .7, 1.9), sparkle(1050, 38, .6, .4), sparkle(770, 40, .5, 1.1),
    ])
    wave = "M0 335 q150 -24 300 0 t300 0 t300 0 t300 0 t300 0 t300 0 t300 0 t300 0 V360 H0 Z"
    roles = [
        "Assistente de Desenvolvimento · Risco de Crédito @ PicPay",
        "Estudante de Tecnologia @ Germinare Tech",
        "UX/UI · Front-end · Dados · IA",
        "design + code + data ✿",
    ]
    role_svg = "".join(
        f'<text class="r r{i+1}" x="70" y="258" font-size="25" fill="#FFD9E8" font-family="{FONT}">{html.escape(t)}</text>'
        for i, t in enumerate(roles))
    chips = ""
    x = 70
    for label, w in [("UX/UI", 74), ("Front-end", 104), ("Dados &amp; IA", 108), ("Python", 84)]:
        chips += (f'<rect x="{x}" y="284" width="{w}" height="30" rx="15" fill="#fff" fill-opacity=".12" '
                  f'stroke="#fff" stroke-opacity=".28"/>'
                  f'<text x="{x+w/2}" y="304" font-size="14" text-anchor="middle" fill="#FFE6F0" font-family="{FONT}">{label}</text>')
        x += w + 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Mariana Torres — Mari</title>
<desc id="d">Banner animado: Mariana Torres, assistente de desenvolvimento em risco de crédito no PicPay e estudante de tecnologia na Germinare Tech, com um gatinho pixel rosa.</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#2A1422"/><stop offset=".55" stop-color="#5C2D46"/><stop offset="1" stop-color="#A9577F"/>
  </linearGradient>
  <radialGradient id="glow" cx=".84" cy=".42" r=".42">
    <stop offset="0" stop-color="#FF9CC6" stop-opacity=".5"/><stop offset="1" stop-color="#FF9CC6" stop-opacity="0"/>
  </radialGradient>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#fff" opacity=".13"/></pattern>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="28"/></clipPath>
</defs>
<style>
  .tw{{transform-box:fill-box;transform-origin:center;animation:tw 3s ease-in-out infinite}}
  @keyframes tw{{0%,100%{{opacity:.2;transform:scale(.6)}}50%{{opacity:1;transform:scale(1.15)}}}}
  .bob{{animation:bob 3.4s ease-in-out infinite}}
  @keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
  .eye{{transform-box:fill-box;transform-origin:center;animation:blink 4.2s infinite}}
  @keyframes blink{{0%,92%,100%{{transform:scaleY(1)}}95%{{transform:scaleY(.1)}}}}
  .halo{{transform-box:fill-box;transform-origin:center;animation:halo 4s ease-in-out infinite}}
  @keyframes halo{{0%,100%{{transform:scale(.94);opacity:.5}}50%{{transform:scale(1.06);opacity:1}}}}
  .w1{{animation:drift 11s linear infinite}} .w2{{animation:drift 17s linear infinite reverse}}
  @keyframes drift{{from{{transform:translateX(0)}}to{{transform:translateX(-600px)}}}}
  .dot{{transform-box:fill-box;transform-origin:center;animation:pulse 1.8s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.35;transform:scale(1.7)}}}}
  .r{{opacity:0;animation:rot 12s infinite}} .r1{{opacity:1}} .r2{{animation-delay:3s}} .r3{{animation-delay:6s}} .r4{{animation-delay:9s}}
  @keyframes rot{{0%{{opacity:0;transform:translateY(12px)}}4%,22%{{opacity:1;transform:translateY(0)}}27%,100%{{opacity:0;transform:translateY(-10px)}}}}
  .fl{{animation:fl 6s ease-in-out infinite}} @keyframes fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-14px)}}}}
  {REDUCED}
</style>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <rect width="{W}" height="{H}" fill="url(#dots)"/>
  <g class="fl" opacity=".5"><circle cx="640" cy="95" r="7" fill="none" stroke="#FFC2DB" stroke-width="2.5"/></g>
  <g class="fl" style="animation-delay:-3s" opacity=".4"><rect x="800" y="300" width="12" height="12" rx="3" fill="#FFC2DB"/></g>
  {sparks}

  <rect x="64" y="50" width="214" height="34" rx="17" fill="#fff" fill-opacity=".13" stroke="#fff" stroke-opacity=".3"/>
  <circle class="dot" cx="87" cy="67" r="5" fill="#7DF0B1"/>
  <text x="104" y="72" font-size="15" fill="#FFE6F0" font-family="{FONT}">atualmente no PicPay</text>

  <text x="70" y="132" font-size="25" fill="#FFB8D3" font-family="{FONT}">oi, eu sou a ♡</text>
  <text x="66" y="206" font-size="76" font-weight="800" fill="#FFFFFF" font-family="{FONT}" letter-spacing="-1.5">Mariana Torres</text>
  {role_svg}
  {chips}

  <circle class="halo" cx="1010" cy="178" r="118" fill="#fff" fill-opacity=".07"/>
  <circle class="halo" style="animation-delay:-2s" cx="1010" cy="178" r="84" fill="#fff" fill-opacity=".07"/>
  <ellipse cx="1008" cy="272" rx="78" ry="9" fill="#000" opacity=".25"/>
  <g transform="translate(930 112)"><g class="bob">{pixel_cat(10)}</g></g>

  <g class="w2" opacity=".5"><path d="{wave}" fill="#E48DB2" transform="translate(-150 -8)"/></g>
  <g class="w1" opacity=".95"><path d="{wave}" fill="#FFF0F5"/></g>
</g>
</svg>'''


# ---------------------------------------------------------------- now (currently)
def now_card():
    def card(x, tag, tag_w, title, sub, en, accent):
        return f'''<g transform="translate({x} 0)">
  <rect x="2" y="2" width="486" height="166" rx="22" fill="#FFF6F9" stroke="#EDC3D4" stroke-width="2"/>
  <rect x="14" y="30" width="5" height="108" rx="2.5" fill="{accent}"/>
  <rect x="34" y="26" width="{tag_w}" height="28" rx="14" fill="#FBDDE8"/>
  <circle class="dot" cx="52" cy="40" r="5" fill="#E0568C"/>
  <text x="66" y="45" font-size="13" font-weight="700" fill="#9B4468" font-family="{FONT}" letter-spacing="1">{tag}</text>
  <text x="34" y="96" font-size="30" font-weight="800" fill="#6A2F4A" font-family="{FONT}">{title}</text>
  <text x="34" y="124" font-size="16" font-weight="600" fill="#8E4E69" font-family="{FONT}">{sub}</text>
  <text x="34" y="148" font-size="13" font-style="italic" fill="#AA7B90" font-family="{FONT}">{en}</text>
</g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="170" viewBox="0 0 1000 170" role="img" aria-label="Atualmente: assistente de desenvolvimento em risco de crédito no PicPay; estudante de tecnologia na Germinare Tech">
<style>
  .dot{{transform-box:fill-box;transform-origin:center;animation:pulse 1.8s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.35;transform:scale(1.7)}}}}
  {REDUCED}
</style>
{card(0, "TRABALHANDO AGORA", 206, "PicPay", "Assistente de Desenvolvimento · Risco de Crédito", "Development Assistant · Credit Risk", "#D4658F")}
{card(510, "ESTUDANDO AGORA", 188, "Germinare Tech", "Estudante de Tecnologia", "Tech student · front-end, back-end, data, AI &amp; UX/UI", "#E9A3BE")}
</svg>'''


# ---------------------------------------------------------------- project cards
def project_card(glyph, title, tags, pt, en, delay):
    pt_l = textwrap.wrap(pt, 56)
    en_l = textwrap.wrap(en, 62)
    pt_svg = "".join(f'<text x="34" y="{118+i*21}" font-size="14.5" fill="#5E3C4C" font-family="{FONT}">{html.escape(l)}</text>' for i, l in enumerate(pt_l))
    en_svg = "".join(f'<text x="34" y="{172+i*18}" font-size="12.5" font-style="italic" fill="#A27A8C" font-family="{FONT}">{html.escape(l)}</text>' for i, l in enumerate(en_l))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="214" viewBox="0 0 490 214" role="img" aria-label="Projeto {html.escape(title)}">
<defs>
  <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#F3B3CB"/><stop offset=".5" stop-color="#D4658F"/><stop offset="1" stop-color="#F3B3CB"/></linearGradient>
  <clipPath id="c"><rect x="2" y="2" width="486" height="210" rx="22"/></clipPath>
</defs>
<style>
  .ic{{animation:fl 3.6s ease-in-out infinite;animation-delay:{delay}s}}
  @keyframes fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
  .sh{{animation:sh 4.5s ease-in-out infinite;animation-delay:{delay}s}}
  @keyframes sh{{0%{{transform:translateX(-200px)}}60%,100%{{transform:translateX(500px)}}}}
  {REDUCED}
</style>
<rect x="2" y="2" width="486" height="210" rx="22" fill="#FFF6F9" stroke="#EDC3D4" stroke-width="2"/>
<g clip-path="url(#c)"><rect x="2" y="2" width="486" height="7" fill="url(#g)"/>
  <rect class="sh" x="0" y="2" width="120" height="7" fill="#fff" opacity=".7"/></g>
<g class="ic"><circle cx="58" cy="52" r="24" fill="#FBDDE8"/><text x="58" y="62" font-size="26" text-anchor="middle" fill="#C24E7B" font-family="{FONT}">{glyph}</text></g>
<text x="96" y="50" font-size="23" font-weight="800" fill="#6A2F4A" font-family="{FONT}">{html.escape(title)}</text>
<text x="96" y="72" font-size="13" font-weight="600" fill="#B0638A" font-family="{FONT}" letter-spacing=".4">{html.escape(tags)}</text>
<line x1="34" y1="92" x2="456" y2="92" stroke="#F1D2DE" stroke-width="1.5" stroke-dasharray="3 5"/>
{pt_svg}
{en_svg}
</svg>'''


# ---------------------------------------------------------------- divider
def divider():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="28" viewBox="0 0 1000 28" role="presentation" aria-hidden="true">
<defs><linearGradient id="l" x1="0" x2="1"><stop offset="0" stop-color="#E9A3BE" stop-opacity="0"/><stop offset=".5" stop-color="#E9A3BE"/><stop offset="1" stop-color="#E9A3BE" stop-opacity="0"/></linearGradient></defs>
<style>
  .s{{transform-box:fill-box;transform-origin:center;animation:t 2.8s ease-in-out infinite}}
  @keyframes t{{0%,100%{{transform:scale(.7);opacity:.5}}50%{{transform:scale(1.2);opacity:1}}}}
  .m{{animation:mv 7s linear infinite}} @keyframes mv{{from{{transform:translateX(-60px)}}to{{transform:translateX(1060px)}}}}
  {REDUCED}
</style>
<rect x="0" y="13" width="1000" height="2" fill="url(#l)"/>
<g class="m"><circle cx="0" cy="14" r="3" fill="#D4658F"/></g>
<g transform="translate(500 14)"><path class="s" d="{STAR}" fill="#D4658F" transform="scale(1.1)"/></g>
<g transform="translate(455 14)"><path class="s" style="animation-delay:.6s" d="{STAR}" fill="#F0B7CC" transform="scale(.55)"/></g>
<g transform="translate(545 14)"><path class="s" style="animation-delay:1.2s" d="{STAR}" fill="#F0B7CC" transform="scale(.55)"/></g>
</svg>'''


if __name__ == "__main__":
    open("assets/banner.svg", "w").write(banner())
    open("assets/now.svg", "w").write(now_card())
    open("assets/divider.svg", "w").write(divider())
    projs = [
        ("project-frigus", "❄", "Frigus", "UX/UI · product design · front-end",
         "Uma solução para organizar estoques de alimentos, acompanhar validades e ajudar a reduzir desperdícios.",
         "A food inventory experience designed to make organization easier and reduce waste.", 0),
        ("project-ai-advisor", "✦", "AI Financial Advisor", "Python · IA · APIs",
         "Projeto de um assistente financeiro com inteligência artificial, combinando lógica, integrações e dados.",
         "An AI-powered financial assistant combining logic, integrations and data.", .5),
        ("project-saveit", "✿", "SaveIt", "product thinking · tecnologia · sustentabilidade",
         "Projeto voltado à gestão de recursos e à redução do desperdício.",
         "A technology project exploring smarter resource management and sustainability.", 1),
        ("project-ux", "✧", "UX experiments & interfaces", "Figma · pesquisa com usuários · protótipos",
         "Gosto de transformar problemas em fluxos, interfaces e experiências mais intuitivas.",
         "Turning research and ideas into thoughtful, usable digital experiences.", 1.5),
    ]
    for name, g, t, tg, pt, en, d in projs:
        open(f"assets/{name}.svg", "w").write(project_card(g, t, tg, pt, en, d))
    print("ok")
