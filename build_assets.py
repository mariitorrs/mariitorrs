"""Gera os SVGs do README (títulos, tecnologias, projetos, Spotify, rodapé).

Usa só a biblioteca padrão do Python. Os stickers e a fita são PNGs recortados
da folha de adesivos e ficam direto na pasta assets/.

    python build_assets.py
"""
import html
import pathlib
import textwrap

ASSETS = pathlib.Path(__file__).parent / "assets"

CREAM = "#FFF0DA"
RASP = "#A32235"
BERRY = "#CA3042"
OLIVE = "#626B34"
FOREST = "#23311E"
ROSE = "#E6B2A0"
GOLD = "#D9A843"
SAGE = "#B9C283"
PLUM = "#6C3840"
INK = "#3D3026"

HEART = ("M12 21 C12 21 3 14.5 3 8.5 C3 5.4 5.3 3 8.2 3 C9.9 3 11.3 3.9 12 5.2 "
         "C12.7 3.9 14.1 3 15.8 3 C18.7 3 21 5.4 21 8.5 C21 14.5 12 21 12 21 Z")

GINGHAM = """<defs><pattern id="gh" width="22" height="22" patternUnits="userSpaceOnUse">
<rect width="22" height="22" fill="#F7E4D2"/>
<rect width="11" height="22" fill="#A32235" opacity=".28"/>
<rect width="22" height="11" fill="#A32235" opacity=".28"/>
<rect width="6" height="22" fill="#A32235" opacity=".12" x="14"/>
<rect width="22" height="6" fill="#A32235" opacity=".12" y="14"/>
</pattern></defs>"""


def svg(w, h, title, body, css=""):
    import pixel
    css = css + pixel.PIXEL_CSS
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img">\n<title>{html.escape(title)}</title>\n'
            f'<style>{css}</style>\n{body}\n</svg>\n')


BOB_CSS = """
.bob{animation:bob 2.6s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.bob2{animation:bob 2.6s ease-in-out .9s infinite;transform-box:fill-box;transform-origin:center}
.twinkle{animation:tw 3s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
@keyframes tw{0%,100%{opacity:.35;transform:scale(.8)}50%{opacity:1;transform:scale(1.15)}}
"""


def heart(x, y, s, color, cls="bob"):
    import pixel
    return pixel.sprite_group("heart", x, y, max(2, round(s * 2)), cls=cls, color=color)


def header(name, text):
    w, h = 900, 92
    body = (
        f'{GINGHAM}'
        f'<rect x="4" y="4" width="892" height="84" rx="42" fill="url(#gh)"/>'
        f'<rect x="10" y="10" width="880" height="72" rx="36" fill="{CREAM}" '
        f'stroke="{RASP}" stroke-width="3" stroke-dasharray="10 7"/>'
        f'{heart(58, 30, 1.6, RASP, "bob")}'
        f'{heart(806, 30, 1.6, OLIVE, "bob2")}'
        f'<text x="450" y="58" text-anchor="middle" font-family="Georgia, DejaVu Serif, serif" '
        f'font-size="32" fill="{RASP}">{html.escape(text)}</text>'
    )
    (ASSETS / name).write_text(svg(w, h, text, body, BOB_CSS))


def tech_board(name):
    rows = [
        ("desenvolvimento", RASP, ["HTML5", "CSS3", "JavaScript", "Python", "Java",
                                    "FastAPI", "Kotlin", "Android Studio"]),
        ("dados e inteligência artificial", OLIVE, ["SQL", "PostgreSQL", "Pandas", "PySpark",
                                                     "LangGraph", "Qdrant", "BI", "Estatística"]),
        ("design e experiência", BERRY, ["Figma", "UX/UI", "Design Thinking", "Prototipação",
                                          "Acessibilidade", "Pesquisa com usuários"]),
        ("ferramentas e infra", PLUM, ["Git", "GitHub", "Linux", "Docker", "Kubernetes"]),
    ]
    width = 900
    y = 20
    parts = []
    idx = 0
    for label, color, items in rows:
        parts.append(
            f'<text x="26" y="{y+14}" font-family="Verdana, DejaVu Sans, sans-serif" '
            f'font-size="13" font-weight="bold" fill="{color}" letter-spacing="1">'
            f'{html.escape(label.upper())}</text>')
        y += 26
        x = 26
        for item in items:
            pw = int(len(item) * 7.6 + 30)
            if x + pw > width - 26:
                x = 26
                y += 40
            parts.append(
                f'<g class="pill" style="animation-delay:{idx*0.07:.2f}s">'
                f'<rect x="{x}" y="{y}" width="{pw}" height="30" rx="15" fill="{color}"/>'
                f'<text x="{x+pw/2}" y="{y+20}" text-anchor="middle" '
                f'font-family="Verdana, DejaVu Sans, sans-serif" font-size="13" fill="{CREAM}">'
                f'{html.escape(item)}</text></g>')
            x += pw + 10
            idx += 1
        y += 52
    height = y + 4
    css = """
.pill{animation:pop .55s cubic-bezier(.2,.9,.3,1.3) both}
@keyframes pop{from{opacity:0;transform:translateY(8px) scale(.9)}to{opacity:1;transform:none}}
"""
    body = "".join(parts)
    (ASSETS / name).write_text(svg(width, height, "O que eu uso e estudo", body, css))


def wrap(text, width):
    return textwrap.wrap(text, width=width)


def project_card(name, title, text, tags, color):
    w, h = 430, 250
    lines = wrap(text, 46)
    body_parts = [
        f'<rect x="2" y="2" width="426" height="246" rx="22" fill="{CREAM}" '
        f'stroke="{color}" stroke-width="4"/>',
        f'<rect x="12" y="12" width="406" height="226" rx="14" fill="none" '
        f'stroke="{color}" stroke-width="1.5" stroke-dasharray="2 6" opacity=".6"/>',
        f'<path d="M2 24 Q2 2 24 2 L406 2 Q428 2 428 24 L428 66 L2 66 Z" fill="{color}"/>',
        f'<text x="26" y="46" font-family="Georgia, DejaVu Serif, serif" font-size="24" '
        f'fill="{CREAM}">{html.escape(title)}</text>',
        heart(386, 22, 1.0, GOLD, "twinkle"),
    ]
    y = 96
    for line in lines[:5]:
        body_parts.append(
            f'<text x="26" y="{y}" font-family="Verdana, DejaVu Sans, sans-serif" '
            f'font-size="14" fill="{INK}">{html.escape(line)}</text>')
        y += 22
    body_parts.append(
        f'<text x="26" y="222" font-family="Verdana, DejaVu Sans, sans-serif" font-size="12" '
        f'font-weight="bold" fill="{OLIVE}">{html.escape(tags)}</text>')
    (ASSETS / name).write_text(svg(w, h, title, "".join(body_parts)))


def link_pill(name, label, color):
    w, h = 210, 46
    body = (
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="23" fill="{color}"/>'
        f'{heart(22, 23, 1.0, CREAM, "beat")}'
        f'<text x="{w/2+12}" y="{h/2+5}" text-anchor="middle" '
        f'font-family="Verdana, DejaVu Sans, sans-serif" font-size="15" fill="{CREAM}">'
        f'{html.escape(label)}</text>'
    )
    (ASSETS / name).write_text(svg(w, h, label, body, BOB_CSS))


def spotify_card(tracks, name="spotify-recent.svg"):
    """tracks: lista de dicts com title, artist, minutes e explicit (opcional)."""
    colors = [FOREST, RASP, OLIVE, BERRY, PLUM]
    w = 600
    row_h = 58
    top = 92
    h = top + row_h * len(tracks) + 44
    parts = [
        f'<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="24" fill="{CREAM}" '
        f'stroke="{RASP}" stroke-width="3"/>',
        f'<rect x="12" y="12" width="{w-24}" height="{h-24}" rx="16" fill="none" '
        f'stroke="{RASP}" stroke-width="1.2" stroke-dasharray="2 6" opacity=".5"/>',
        f'<text x="30" y="52" font-family="Georgia, DejaVu Serif, serif" font-size="25" '
        f'fill="{RASP}">o que eu ouvi por último</text>',
        f'<text x="30" y="74" font-family="Verdana, DejaVu Sans, sans-serif" font-size="12" '
        f'fill="{OLIVE}">Spotify · tocadas recentemente</text>',
    ]
    for i in range(4):
        x = 520 + i * 14
        delay = i * 0.18
        parts.append(
            f'<rect class="eq" style="animation-delay:{delay:.2f}s" x="{x}" y="34" '
            f'width="8" height="28" rx="3" fill="{GOLD if i % 2 else OLIVE}"/>')
    y = top
    for i, t in enumerate(tracks):
        c = colors[i % len(colors)]
        initial = html.escape(t["title"][:1].upper())
        parts.append(f'<rect x="28" y="{y+6}" width="42" height="42" rx="9" fill="{c}"/>')
        parts.append(
            f'<text x="49" y="{y+34}" text-anchor="middle" '
            f'font-family="Georgia, DejaVu Serif, serif" font-size="20" fill="{CREAM}">{initial}</text>')
        title = t["title"] if len(t["title"]) < 38 else t["title"][:36] + "…"
        parts.append(
            f'<text x="84" y="{y+25}" font-family="Verdana, DejaVu Sans, sans-serif" '
            f'font-size="15" font-weight="bold" fill="{INK}">{html.escape(title)}</text>')
        artist_x = 84
        parts.append(
            f'<text x="{artist_x}" y="{y+43}" font-family="Verdana, DejaVu Sans, sans-serif" '
            f'font-size="12" fill="{OLIVE}">{html.escape(t["artist"])}</text>')
        if t.get("explicit"):
            parts.append(
                f'<rect x="{artist_x + 8 + len(t["artist"]) * 7}" y="{y+31}" width="16" height="14" '
                f'rx="3" fill="{OLIVE}"/>'
                f'<text x="{artist_x + 16 + len(t["artist"]) * 7}" y="{y+42}" text-anchor="middle" '
                f'font-family="Verdana, DejaVu Sans, sans-serif" font-size="9" fill="{CREAM}">E</text>')
        mins = t["minutes"]
        ago = "agora" if mins < 1 else f"há {mins} min"
        parts.append(
            f'<text x="{w-32}" y="{y+30}" text-anchor="end" '
            f'font-family="Verdana, DejaVu Sans, sans-serif" font-size="12" fill="{RASP}">{ago}</text>')
        if i < len(tracks) - 1:
            parts.append(
                f'<line x1="28" y1="{y+row_h-4}" x2="{w-28}" y2="{y+row_h-4}" '
                f'stroke="{ROSE}" stroke-width="1.5" stroke-dasharray="3 4"/>')
        y += row_h
    parts.append(
        f'<text x="{w/2}" y="{h-18}" text-anchor="middle" '
        f'font-family="Verdana, DejaVu Sans, sans-serif" font-size="11" fill="{OLIVE}">'
        f'atualizado automaticamente</text>')
    css = """
.eq{transform-box:fill-box;transform-origin:bottom;animation:eq 1.1s ease-in-out infinite}
@keyframes eq{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
"""
    body = "".join(parts)
    out = svg(w, h, "Músicas recentes no Spotify", body, css)
    (ASSETS / name).write_text(out)
    return out


def footer(name):
    w, h = 1000, 130
    body = (
        f'{GINGHAM}'
        f'<rect x="0" y="0" width="{w}" height="{h}" rx="0" fill="{CREAM}"/>'
        f'<text x="500" y="72" text-anchor="middle" font-family="Georgia, DejaVu Serif, serif" '
        f'font-size="36" fill="{RASP}">feito com carinho</text>'
        f'{heart(452, 88, 0.9, BERRY, "bob")}'
        f'{heart(518, 88, 0.9, OLIVE, "bob2")}'
        f'<rect x="0" y="{h-26}" width="{w}" height="26" fill="url(#gh)"/>'
    )
    (ASSETS / name).write_text(svg(w, h, "Feito com carinho", body, BOB_CSS))


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    header("title-sobre.svg", "um pouco sobre mim")
    header("title-usos.svg", "o que eu uso e estudo")
    header("title-projetos.svg", "projetos no caminho")
    header("title-musica.svg", "entre um código e outro")
    header("title-conversa.svg", "vamos conversar?")
    tech_board("tech-board.svg")

    project_card("project-frigus.svg", "Frigus",
                 "Uma plataforma para organizar estoques de alimentos, acompanhar validades "
                 "e ajudar a reduzir desperdícios. Eu cuido do design das interfaces e da "
                 "experiência do usuário.",
                 "UX/UI · Figma · Design Thinking · Prototipação", RASP)
    project_card("project-ai-advisor.svg", "Assessor financeiro com IA",
                 "Um assistente financeiro que reúne inteligência artificial, integrações e "
                 "dados. Um jeito de praticar agentes de IA e desenvolvimento de APIs.",
                 "Python · FastAPI · LangGraph · PostgreSQL · Qdrant", OLIVE)
    project_card("project-saveit.svg", "SaveIt",
                 "Um projeto sobre gestão de recursos e redução do desperdício, feito em "
                 "equipe. Uma chance de pensar como a tecnologia ajuda a aproveitar melhor "
                 "o que já temos.",
                 "Tecnologia · Sustentabilidade · Time", BERRY)
    project_card("project-ux.svg", "Interfaces e experiências",
                 "Estudos de telas, fluxos e protótipos que fazem parte do meu aprendizado em "
                 "design. Gosto de cuidar dos detalhes e deixar a interface mais clara.",
                 "Figma · Pesquisa com usuários · UI Kit · Acessibilidade", PLUM)

    link_pill("link-linkedin.svg", "LinkedIn", RASP)
    link_pill("link-instagram.svg", "Instagram", BERRY)
    link_pill("link-spotify.svg", "Spotify", OLIVE)
    link_pill("link-repositories.svg", "Repositórios", FOREST)

    footer("footer.svg")
    print("ok")
