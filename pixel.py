"""Sprites de pixel art animados (só biblioteca padrão).

Cada sprite é uma máscara matemática desenhada em uma grade pequena;
cada célula vira um retângulo. A animação usa steps() pra ter aquele
movimento "de pixel", parecido com a capa.
"""
import html
import math

CREAM = "#FFF0DA"
RASP = "#A32235"
BERRY = "#CA3042"
HIGH = "#EC726C"
OLIVE = "#626B34"
SAGE = "#B9C283"
LEAF = "#8FA04E"
FOREST = "#23311E"
ROSE = "#E6B2A0"
PINK = "#F2C4B8"
GOLD = "#D9A843"
SKY = "#F7DCCB"

PIXEL_CSS = """
.bob{animation:bob 1.6s steps(2,end) infinite}
.bob2{animation:bob 1.6s steps(2,end) .8s infinite}
.beat{animation:beat 1.2s steps(2,end) infinite;transform-box:fill-box;transform-origin:center}
.sway{animation:sway 2.4s steps(3,end) infinite;transform-box:fill-box;transform-origin:50% 100%}
.sway2{animation:sway 2.4s steps(3,end) .6s infinite;transform-box:fill-box;transform-origin:50% 100%}
.twinkle{animation:tw 1.8s steps(2,end) infinite;transform-box:fill-box;transform-origin:center}
.float{animation:float 3.6s linear infinite;opacity:0}
.cloud{animation:drift 38s linear infinite}
.petal{animation:fall 5s linear infinite;opacity:0}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@keyframes beat{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
@keyframes sway{0%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}100%{transform:rotate(-5deg)}}
@keyframes tw{0%,100%{opacity:.3;transform:scale(.7)}50%{opacity:1;transform:scale(1.15)}}
@keyframes float{0%{transform:translateY(0);opacity:0}15%{opacity:1}100%{transform:translateY(-70px);opacity:0}}
@keyframes drift{from{transform:translateX(-240px)}to{transform:translateX(1140px)}}
@keyframes fall{0%{transform:translate(0,-10px) rotate(0);opacity:0}10%{opacity:1}100%{transform:translate(30px,200px) rotate(200deg);opacity:0}}
"""


def _mask_to_grid(w, h, cell_fn):
    return [[cell_fn(i, j) for i in range(w)] for j in range(h)]


def _inside(grid, i, j):
    return 0 <= j < len(grid) and 0 <= i < len(grid[0]) and grid[j][i] != "."


def rects(grid, pal, p, ox=0, oy=0):
    """Desenha a grade juntando células da mesma cor na mesma linha (menos elementos)."""
    out = []
    for j, row in enumerate(grid):
        i = 0
        while i < len(row):
            c = row[i]
            if c == ".":
                i += 1
                continue
            k = i
            while k + 1 < len(row) and row[k + 1] == c:
                k += 1
            out.append(f'<rect x="{ox + i*p}" y="{oy + j*p}" width="{(k-i+1)*p}" height="{p}" fill="{pal[c]}"/>')
            i = k + 1
    return "".join(out)


def raspberry_grid():
    w, h = 12, 13
    def cell(i, j):
        x, y = (i - 5.5) / 5.6, (j - 7.0) / 6.0
        if x * x + y * y <= 1 and j >= 2:
            # bordas em tom mais escuro
            edge = any(not (0 <= i+di < w and 0 <= j+dj < h) or
                       ((((i+di)-5.5)/5.6)**2 + (((j+dj)-7.0)/6.0)**2 > 1)
                       for di, dj in ((1,0),(-1,0),(0,1),(0,-1)))
            if edge:
                return "r"
            return "H" if (i % 3 == 1 and j % 3 == 0) else "R"
        if j <= 1 and 4 <= i <= 7:
            return "L" if j == 1 or i != 5 else "l"
        return "."
    return _mask_to_grid(w, h, cell)


def heart_grid():
    return [list(r) for r in [
        ".RRR...RRR.",
        "RHHRRRRRRRR",
        "RHRRRRRRRRR",
        "RRRRRRRRRRR",
        ".RRRRRRRRR.",
        "..RRRRRRR..",
        "...RRRRR...",
        "....RRR....",
        ".....R.....",
    ]]


def flower_grid():
    w, h = 11, 14
    cx, cy = 5, 4.5
    def cell(i, j):
        d_center = math.hypot(i - cx, j - cy)
        if d_center <= 1.6:
            return "Y"
        for k in range(5):
            a = math.radians(-90 + k * 72)
            px, py = cx + 2.9 * math.cos(a), cy + 2.9 * math.sin(a)
            d = math.hypot(i - px, j - py)
            if d <= 2.1:
                return "W" if d < 1.0 and (i + j) % 2 == 0 else "P"
        if i == 5 and 9 <= j <= 13:
            return "L"
        if j == 11 and i in (3, 4):
            return "l"
        return "."
    return _mask_to_grid(w, h, cell)


def sparkle_grid():
    return [
        ".." + "Y" + "..",
        ".." + "Y" + "..",
        "YYWYY",
        ".." + "Y" + "..",
        ".." + "Y" + "..",
    ]


SPRITES = {
    "raspberry": (raspberry_grid(), {"R": RASP, "r": "#7E1A2A", "H": HIGH, "L": OLIVE, "l": LEAF}),
    "heart": (heart_grid(), {"R": BERRY, "H": HIGH}),
    "flower": (flower_grid(), {"P": PINK, "W": CREAM, "Y": GOLD, "L": OLIVE, "l": LEAF}),
    "sparkle": (sparkle_grid(), {"Y": GOLD, "W": CREAM}),
}


def sprite_group(name, x, y, p, cls="", color=None, anim_style=""):
    """Retorna um <g> com o sprite posicionado em (x, y), com p px por pixel."""
    grid, pal = SPRITES[name]
    pal = dict(pal)
    if color and name == "heart":
        pal["R"] = color
    cols = max(len(r) for r in grid)
    rows = len(grid)
    w, h = cols * p, rows * p
    style = f' style="{anim_style}"' if anim_style else ""
    return (f'<g transform="translate({x - w/2:.1f} {y - h/2:.1f})">'
            f'<g class="{cls}"{style}>{rects(grid, pal, p)}</g></g>')


def sprite_svg(name, title, p, cls):
    grid, pal = SPRITES[name]
    cols = max(len(r) for r in grid)
    rows = len(grid)
    w, h = cols * p, rows * p
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img"><title>{html.escape(title)}</title>'
            f'<style>{PIXEL_CSS}</style>'
            f'<g class="{cls}" shape-rendering="crispEdges">{rects(grid, pal, p)}</g></svg>')


def garden_svg(name="garden.svg"):
    """Jardim em pixel art com nuvens, colinas em bolinhas, flores que balançam,
    framboesas, corações flutuando e pétalas caindo."""
    W, H = 1000, 180
    p = 5
    parts = [f'<rect width="{W}" height="{H}" fill="{SKY}"/>']
    # nuvens em pixel
    cloud = [
        "......XXXX.........",
        "....XXXXXXXX.......",
        "..XXXXXXXXXXXX.....",
        ".XXXXXXXXXXXXXXX...",
        "XXXXXXXXXXXXXXXXXX.",
        "XXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXX",
    ]
    cpal = {"X": CREAM}
    for k, (top, delay) in enumerate([(18, -6), (44, -20), (10, -31)]):
        parts.append(f'<g class="cloud" style="animation-delay:{delay}s">'
                     f'<g transform="translate(0 {top})">{rects(cloud, cpal, 5)}</g></g>')
    # colinhas com bolinhas (pixel)
    rows_total = H // p
    ground_top = {}
    for i in range(W // p):
        ground_top[i] = 27 + round(2.2 * math.sin(i / 7.0)) + round(1.3 * math.sin(i / 2.3))
    grid = []
    for j in range(rows_total):
        row = []
        for i in range(W // p):
            if j < ground_top[i]:
                row.append(".")
            elif (i * 3 + j * 5) % 11 == 0 and j > ground_top[i] + 1:
                row.append("W")
            elif j == ground_top[i]:
                row.append("S")
            else:
                row.append("O")
        grid.append(row)
    parts.append(rects(grid, {"O": OLIVE, "S": SAGE, "W": CREAM}, p))
    # faixa de grama em bolinhas
    # flores e framboesas balançando sobre a colina
    base_y = 150
    for k, x in enumerate([60, 180, 330, 470, 610, 760, 900]):
        cls = "sway" if k % 2 == 0 else "sway2"
        parts.append(sprite_group("flower", x, base_y - 18, 3, cls=cls))
    for x, y in [(120, 150), (400, 152), (700, 150), (960, 152)]:
        parts.append(sprite_group("raspberry", x, y, 4, cls="bob"))
    # corações subindo
    for k, x in enumerate([260, 540, 820]):
        parts.append(sprite_group("heart", x, 120, 3, cls="float",
                                  anim_style=f"animation-delay:{k*1.2}s"))
    # pétalas caindo
    for k in range(8):
        x = 40 + k * 120 + (k * 37) % 40
        d = f"{(k*0.7)%5:.1f}s"
        parts.append(f'<rect class="petal" x="{x}" y="0" width="7" height="5" rx="1" fill="{PINK}" '
                     f'style="animation-delay:{d}"/>')
    # gingham na base
    gh = []
    for i in range(0, W, 10):
        gh.append(f'<rect x="{i}" y="{H-10}" width="10" height="10" fill="{RASP if (i//10)%2==0 else ROSE}"/>')
    parts.append("".join(gh))
    body = "".join(parts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">'
            f'<title>Jardim em pixel art animado</title><style>{PIXEL_CSS}</style>'
            f'<g shape-rendering="crispEdges">{body}</g></svg>\n')


def write_all(assets_dir):
    import pathlib
    d = pathlib.Path(assets_dir)
    titles = {"raspberry": "Framboesa animada", "heart": "Coração pixel",
              "flower": "Flor pixel animada", "sparkle": "Brilho pixel"}
    cls = {"raspberry": "bob", "heart": "beat", "flower": "sway", "sparkle": "twinkle"}
    for name in SPRITES:
        p = 6 if name != "sparkle" else 8
        (d / f"pixel-{name}.svg").write_text(
            sprite_svg(name, titles[name], p, cls[name]).replace(
                "<style>", "<style>", 1))
    (d / "garden.svg").write_text(garden_svg())
