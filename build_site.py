# -*- coding: utf-8 -*-
# Сборщик прототипа сайта «Настоящие отношения». v2: иконки, инфографика, журнальная сетка.
import pathlib

ROOT = pathlib.Path(__file__).parent

# ============ ИКОНКИ (линейные, stroke=currentColor) ============
def ic(body, vb=48):
    return (f'<svg class="ic" viewBox="0 0 {vb} {vb}" fill="none" stroke="currentColor" '
            f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')

ICONS = {
# книга: понимание без изменений
"book": ic('<path d="M24 12c-4-3-10-4-15-3v26c5-1 11 0 15 3 4-3 10-4 15-3V9c-5-1-11 0-15 3z"/><path d="M24 12v26"/>'),
# петля-повтор
"loop": ic('<path d="M14 18a12 12 0 0 1 21 6"/><path d="M34 30a12 12 0 0 1-21-6"/><path d="M35 15v9h-9"/><path d="M13 33v-9h9"/>'),
# щит с трещиной: сильный снаружи
"shield": ic('<path d="M24 6l14 5v11c0 9-6 16-14 20-8-4-14-11-14-20V11z"/><path d="M24 14l-3 7h6l-4 9"/>'),
# две чашки: быт
"cups": ic('<path d="M8 20h12v7a6 6 0 0 1-12 0z"/><path d="M28 20h12v7a6 6 0 0 1-12 0z"/><path d="M20 22h3M40 22h3"/><path d="M10 38h28"/>'),
# стрелка в потолок
"ceiling": ic('<path d="M8 10h32"/><path d="M24 38V18"/><path d="M17 25l7-7 7 7"/><path d="M14 14l-2-2M34 14l2-2"/>'),
# линза-знак
"lens": ic('<circle cx="19" cy="24" r="12"/><circle cx="29" cy="24" r="12"/>'),
# слои: глубина
"layers": ic('<path d="M24 8l16 8-16 8-16-8z"/><path d="M8 24l16 8 16-8"/><path d="M8 32l16 8 16-8"/>'),
# люди кругом: группа
"people": ic('<circle cx="24" cy="14" r="5"/><circle cx="10" cy="30" r="5"/><circle cx="38" cy="30" r="5"/><path d="M17 20l-3 5M31 20l3 5M16 34h16"/>'),
# календарь-практика
"calendar": ic('<rect x="8" y="10" width="32" height="30" rx="3"/><path d="M8 18h32M16 6v8M32 6v8"/><path d="M17 28l5 5 9-10"/>'),
# речь: разговор
"speech": ic('<path d="M8 12h32v20H22l-8 8v-8H8z"/><path d="M15 20h18M15 26h12"/>'),
# механизм
"gear": ic('<circle cx="24" cy="24" r="7"/><path d="M24 8v6M24 34v6M8 24h6M34 24h6M13 13l4 4M31 31l4 4M35 13l-4 4M17 31l-4 4"/>'),
# развилка-путь
"route": ic('<path d="M12 40V22a8 8 0 0 1 8-8h16"/><path d="M30 8l6 6-6 6"/><circle cx="12" cy="43" r="2.4"/>'),
# цель
"target": ic('<circle cx="24" cy="24" r="16"/><circle cx="24" cy="24" r="9"/><circle cx="24" cy="24" r="2.4"/>'),
# рассвет: утро
"sunrise": ic('<path d="M8 34h32"/><path d="M16 34a8 8 0 0 1 16 0"/><path d="M24 12v6M12 20l3 3M36 20l-3 3"/>'),
# гора: опора
"mountain": ic('<path d="M6 38l12-20 7 11 5-7 12 16z"/><path d="M18 18l3 5"/>'),
# монеты: деньги и дело
"coins": ic('<circle cx="18" cy="30" r="10"/><circle cx="30" cy="18" r="10"/><path d="M27 18h6M30 15v6"/>'),
# пламя: энергия
"flame": ic('<path d="M24 6c2 6 10 10 10 19a10 10 0 0 1-20 0c0-5 3-8 5-11 1 3 2 4 5 6 0-6-2-9 0-14z"/>'),
}

def icon(name, color="var(--wine)"):
    return f'<span class="icwrap" style="color:{color}">{ICONS[name]}</span>'

# ============ ИНФОГРАФИКА ============
def loop_diagram(dark=False):
    ring = "#D08A5F" if dark else "#6E3B4B"
    soft = "rgba(242,237,228,.75)" if dark else "#6B615C"
    node_bg = "#22303C" if dark else "#FFFFFF"
    node_line = "rgba(208,138,95,.45)" if dark else "rgba(110,59,75,.3)"
    txt = "#F2EDE4" if dark else "#322D2B"
    sage = "#8FA48B" if dark else "#7D8C74"
    def node(x, y, num, label, cap, anchor="middle"):
        return f'''
<g>
<circle cx="{x}" cy="{y}" r="34" fill="{node_bg}" stroke="{node_line}" stroke-width="1.5"/>
<text x="{x}" y="{y+9}" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="26" fill="{ring}">{num}</text>
</g>
<text x="{x}" y="{y-48}" text-anchor="{anchor}" font-family="Manrope,sans-serif" font-weight="700" font-size="16" fill="{txt}">{label}</text>
<text x="{x}" y="{y-30}" text-anchor="{anchor}" font-family="Manrope,sans-serif" font-size="12.5" fill="{soft}">{cap}</text>'''
    return f'''<svg viewBox="0 0 520 560" role="img" aria-label="Событийный круг: событие, эмоция, старое решение, сценарий" style="max-width:520px;width:100%;height:auto">
<circle cx="260" cy="290" r="150" fill="none" stroke="{ring}" stroke-width="1.6" stroke-dasharray="3 7" opacity=".8"/>
<g fill="{ring}">
<path d="M398 217 l14 -3 -6 13 z"/>
<path d="M330 425 l-3 14 12 -7 z"/>
<path d="M122 363 l-14 3 6 -13 z"/>
<path d="M190 155 l3 -14 -12 7 z"/>
</g>
{node(260, 140, "1", "Событие", "слово, взгляд, цифра на счёте")}
{node(410, 290, "2", "Эмоция", "тело вспыхивает раньше мысли")}
{node(260, 440, "3", "Старое решение", "принятое когда-то, чаще в детстве")}
{node(110, 290, "4", "Сценарий", "финал знакомый, круг замыкается")}
<text x="260" y="285" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="19" fill="{txt}">Событийный</text>
<text x="260" y="308" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="19" fill="{txt}">круг</text>
<text x="260" y="330" text-anchor="middle" font-family="Manrope,sans-serif" font-size="12" fill="{sage}">быстрее сознания</text>
</svg>'''

def timeline_svg():
    return '''<svg viewBox="0 0 980 190" role="img" aria-label="Путь программы: три модуля с перерывами 3-5 недель" style="width:100%;height:auto">
<line x1="60" y1="70" x2="920" y2="70" stroke="rgba(110,59,75,.25)" stroke-width="2" stroke-dasharray="2 6"/>
<g font-family="Manrope,sans-serif">
<circle cx="110" cy="70" r="30" fill="#6E3B4B"/>
<text x="110" y="79" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="24" fill="#FAF5F0">I</text>
<text x="110" y="128" text-anchor="middle" font-weight="700" font-size="15" fill="#322D2B">Возвращение к себе</text>
<text x="110" y="148" text-anchor="middle" font-size="13" fill="#6B615C">2,5 дня очно</text>
<text x="255" y="52" text-anchor="middle" font-size="12.5" fill="#7D8C74">3-5 недель</text>
<text x="255" y="92" text-anchor="middle" font-size="11.5" fill="#6B615C">интеграция</text>
<circle cx="400" cy="70" r="30" fill="#6E3B4B"/>
<text x="400" y="79" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="24" fill="#FAF5F0">II</text>
<text x="400" y="128" text-anchor="middle" font-weight="700" font-size="15" fill="#322D2B">Внутренняя свобода</text>
<text x="400" y="148" text-anchor="middle" font-size="13" fill="#6B615C">5 дней очно</text>
<text x="545" y="52" text-anchor="middle" font-size="12.5" fill="#7D8C74">3-5 недель</text>
<text x="545" y="92" text-anchor="middle" font-size="11.5" fill="#6B615C">интеграция</text>
<circle cx="690" cy="70" r="30" fill="#17222C"/>
<text x="690" y="79" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="22" fill="#D08A5F">III</text>
<text x="690" y="128" text-anchor="middle" font-weight="700" font-size="15" fill="#322D2B">Создатель реальности</text>
<text x="690" y="148" text-anchor="middle" font-size="13" fill="#6B615C">3 месяца в жизни</text>
<path d="M735 70h120" stroke="#D08A5F" stroke-width="3"/>
<path d="M845 62l14 8-14 8z" fill="#D08A5F"/>
<text x="800" y="52" text-anchor="middle" font-size="12.5" fill="#D08A5F">результаты остаются</text>
</g>
</svg>'''

FAVICON = ("data:image/svg+xml,"
  "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
  "%3Ccircle cx='38' cy='50' r='28' fill='none' stroke='%237D8C74' stroke-width='6'/%3E"
  "%3Ccircle cx='62' cy='50' r='28' fill='none' stroke='%236E3B4B' stroke-width='6'/%3E"
  "%3Cpath d='M50 24.7 A28 28 0 0 1 50 75.3 A28 28 0 0 1 50 24.7 Z' fill='%236E3B4B'/%3E%3C/svg%3E")

CSS = """
@font-face{font-family:'Playfair Display';src:url('/chizhovy/fonts/playfair-cyrillic.woff2') format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;font-weight:400 900;font-display:swap}
@font-face{font-family:'Playfair Display';src:url('/chizhovy/fonts/playfair-latin.woff2') format('woff2');unicode-range:U+0000-00FF,U+2000-206F;font-weight:400 900;font-display:swap}
@font-face{font-family:'Manrope';src:url('/chizhovy/fonts/manrope-cyrillic.woff2') format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;font-weight:200 800;font-display:swap}
@font-face{font-family:'Manrope';src:url('/chizhovy/fonts/manrope-latin.woff2') format('woff2');unicode-range:U+0000-00FF,U+2000-206F;font-weight:200 800;font-display:swap}
:root{--bg:#FAF7F2;--ink:#322D2B;--ink-soft:#6B615C;--wine:#6E3B4B;--wine-deep:#552C3A;--sage:#7D8C74;--sage-deep:#5C6B54;--linen:#EFE9DF;--sand:#C9A87C;--line:rgba(110,59,75,.14);--night:#17222C;--night2:#22303C;--copper:#D08A5F;--ntext:#F2EDE4;color-scheme:light}
*{box-sizing:border-box}
html{font-size:17px;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Manrope',-apple-system,'Segoe UI',sans-serif;line-height:1.72;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:var(--wine)}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.narrow{max-width:720px;margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;line-height:1.2;text-wrap:balance;margin:0 0 .5em}
h2{font-size:clamp(1.7rem,4vw,2.3rem);font-weight:600}
h3{font-size:1.22rem;font-weight:600}
p{margin:0 0 1.1em}
section{padding:76px 0}
.eyebrow{font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--wine);margin:0 0 16px;display:flex;align-items:center;gap:10px}
.eyebrow::before{content:'';width:26px;height:2px;background:var(--sand)}
.hero .eyebrow::before{display:none}
.center .eyebrow::before{display:none}
.sub{color:var(--ink-soft);max-width:640px}
.btn{display:inline-block;padding:16px 30px;border-radius:5px;font-weight:700;font-size:.98rem;text-decoration:none;letter-spacing:.01em}
.btn-wine{background:var(--wine);color:#FAF5F0}.btn-wine:hover{background:var(--wine-deep)}
.btn-ghost{color:var(--wine);border:1.5px solid var(--wine)}
.btn-copper{background:var(--copper);color:#1B1410}
.dark .btn-ghost{color:var(--ntext);border-color:rgba(242,237,228,.5)}

/* Иконки */
.icwrap{display:inline-flex;width:46px;height:46px;align-items:center;justify-content:center;border-radius:10px;background:rgba(110,59,75,.07);margin-bottom:16px}
.icwrap .ic{width:27px;height:27px}
.dark .icwrap{background:rgba(208,138,95,.12)}

/* Контурные номера (по референсу) */
.card{position:relative}
.bignum{position:absolute;top:8px;right:16px;font-family:'Playfair Display',Georgia,serif;font-size:3.2rem;line-height:1;font-weight:600;color:transparent;-webkit-text-stroke:1.3px rgba(201,168,124,.6);pointer-events:none}
.dark .bignum{-webkit-text-stroke-color:rgba(208,138,95,.45)}

/* Сферы жизни кружками */
.spheres{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;text-align:center}
.sphere .ring{width:122px;height:122px;margin:0 auto 16px;border-radius:50%;border:1.5px solid rgba(201,168,124,.8);display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 35% 30%,#fff,var(--linen))}
.sphere .ring .ic{width:46px;height:46px;color:var(--wine)}
.sphere b{display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.08rem;margin-bottom:4px}
.sphere span{font-size:.82rem;color:var(--ink-soft);line-height:1.5}

/* Меню */
.nav{position:sticky;top:0;z-index:50;background:rgba(250,247,242,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;gap:22px;padding-top:12px;padding-bottom:12px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);margin-right:auto}
.logo b{font-family:'Playfair Display',Georgia,serif;font-size:1.02rem;line-height:1.1}
.logo span{display:block;font-size:.68rem;color:var(--ink-soft)}
.menu{display:flex;gap:20px;align-items:center;flex-wrap:wrap}
.menu a{font-size:.9rem;font-weight:600;color:var(--ink);text-decoration:none}
.menu a:hover,.menu a.on{color:var(--wine)}
.menu .cta{padding:10px 18px;border-radius:5px;background:var(--wine);color:#FAF5F0}
.menu .cta:hover{background:var(--wine-deep);color:#FAF5F0}
#mtoggle{display:none}
.burger{display:none;cursor:pointer;padding:8px;margin-left:auto}
.burger span{display:block;width:22px;height:2px;background:var(--ink);margin:5px 0}
@media (max-width:920px){
  .burger{display:block}
  .logo{margin-right:0}
  .nav .wrap{flex-wrap:wrap;gap:8px}
  .menu{display:none;width:100%;flex-direction:column;align-items:flex-start;gap:4px;padding:10px 0 14px}
  .menu a{padding:9px 0;font-size:1rem}
  #mtoggle:checked ~ .menu{display:flex}
}

/* Хиро */
.hero{position:relative;background:var(--night);color:var(--ntext)}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.48}
.hero .veil{position:absolute;inset:0;background:linear-gradient(165deg,rgba(23,34,44,.5),rgba(23,34,44,.93) 80%)}
.hero .in{position:relative;z-index:1;max-width:860px;margin:0 auto;padding:110px 24px 92px}
.hero.short .in{padding:78px 24px 64px}
.hero .eyebrow{color:var(--copper)}
.hero h1{font-size:clamp(2.3rem,6vw,3.7rem);font-weight:500;color:#fff}
.hero .lead{font-size:1.17rem;line-height:1.65;color:rgba(242,237,228,.85);max-width:640px;margin-top:22px}
.hero .acts{margin-top:34px;display:flex;gap:14px;flex-wrap:wrap}

/* Сетки */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.card{background:var(--linen);border:1px solid var(--line);border-radius:8px;padding:26px 24px}
.card h3{margin-bottom:8px}
.card p{margin:0;font-size:.93rem;color:var(--ink-soft)}
.card a{font-weight:700;font-size:.9rem;text-decoration:none}
.white{background:#fff}
.nails{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.nail{background:#fff;border:1px solid var(--line);border-radius:8px;padding:20px}
.nail b{display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.9rem;font-weight:600;color:var(--wine);font-variant-numeric:tabular-nums}
.nail span{font-size:.8rem;color:var(--ink-soft);line-height:1.5}
.dark{background:var(--night);color:var(--ntext)}
.dark h2,.dark h3{color:#fff}
.dark p{color:rgba(242,237,228,.8)}
.dark .eyebrow{color:var(--copper)}
.dark .eyebrow::before{background:rgba(208,138,95,.6)}
.dark .card{background:var(--night2);border-color:rgba(208,138,95,.25)}
.dark .card h3{color:#fff}
.dark .card p{color:rgba(242,237,228,.65)}

/* Диаграмма + легенда */
.diagrow{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.legend{display:grid;gap:14px}
.legend .li{display:flex;gap:14px;align-items:flex-start}
.legend .li i{font-style:normal;font-family:'Playfair Display',Georgia,serif;font-size:1.15rem;color:var(--copper);flex:0 0 26px;text-align:center}
.legend .li b{display:block;font-size:.95rem}
.legend .li span{font-size:.85rem;color:rgba(242,237,228,.65);line-height:1.5}

/* Таймлайн */
.timeline{background:#fff;border:1px solid var(--line);border-radius:10px;padding:34px 26px 20px;overflow-x:auto}
.timeline svg{min-width:760px}

/* Фото */
.ph{border-radius:8px;overflow:hidden;border:1px solid var(--line)}
.ph img{width:100%;height:100%;object-fit:cover}
.mosaic{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:210px;gap:12px}
.mosaic .ph:first-child{grid-column:span 2;grid-row:span 2}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:44px;align-items:center}
.split .ph{aspect-ratio:4/3}

/* Цитаты */
.pull{border-left:3px solid var(--wine);padding:4px 0 4px 26px;margin:30px 0}
.pull .q{font-family:'Playfair Display',Georgia,serif;font-size:1.3rem;line-height:1.45;font-weight:500}
.pull .who{margin-top:10px;font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft)}
.dark .pull{border-color:var(--copper)}
.dark .pull .q{color:#fff}
.dark .pull .who{color:rgba(242,237,228,.6)}

/* Афиша */
.poster{position:relative;border-radius:10px;overflow:hidden;background:var(--night);color:var(--ntext)}
.poster .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.4}
.poster .veil{position:absolute;inset:0;background:linear-gradient(rgba(23,34,44,.55),rgba(23,34,44,.92))}
.poster .in{position:relative;z-index:1;padding:56px 48px}
.poster h3{font-size:2rem;font-weight:500;color:#fff}
.poster p{color:rgba(242,237,228,.75);max-width:520px}

/* FAQ */
details{background:#fff;border:1px solid var(--line);border-radius:8px;padding:4px 24px;margin-bottom:12px}
details summary{cursor:pointer;font-weight:700;padding:16px 0;list-style:none;display:flex;justify-content:space-between;gap:14px;align-items:center}
details summary::after{content:'+';font-family:'Playfair Display',Georgia,serif;font-size:1.5rem;color:var(--wine);flex:0 0 auto}
details[open] summary::after{content:'\\2212'}
details p{color:var(--ink-soft);padding-bottom:16px;margin:0}

/* Футер */
footer{background:var(--night);color:var(--ntext);padding:64px 0 40px}
footer h4{font-family:'Playfair Display',Georgia,serif;font-size:1rem;color:var(--copper);margin:0 0 14px}
footer .cols{display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:32px}
footer a{color:rgba(242,237,228,.8);text-decoration:none;display:block;padding:4px 0;font-size:.9rem}
footer a:hover{color:#fff}
footer .fine{margin-top:44px;padding-top:20px;border-top:1px solid rgba(242,237,228,.15);font-size:.78rem;color:rgba(242,237,228,.5);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}

@media (max-width:860px){
  section{padding:52px 0}
  .grid2,.grid3,.split,.diagrow{grid-template-columns:1fr}
  .mosaic{grid-template-columns:1fr 1fr;grid-auto-rows:160px}
  .nails,.spheres{grid-template-columns:1fr 1fr}
  .poster .in{padding:36px 26px}
  footer .cols{grid-template-columns:1fr 1fr}
}
@media (max-width:480px){
  .nails{grid-template-columns:1fr}
  .btn{padding:14px 20px;font-size:.92rem}
  .hero .acts .btn{width:100%;text-align:center}
}
"""

LOGO_SVG = """<svg width="42" height="36" viewBox="0 0 100 100" aria-hidden="true"><circle cx="38" cy="50" r="28" fill="none" stroke="#7D8C74" stroke-width="4"/><circle cx="62" cy="50" r="28" fill="none" stroke="#6E3B4B" stroke-width="4"/><path d="M50 24.7 A28 28 0 0 1 50 75.3 A28 28 0 0 1 50 24.7 Z" fill="#6E3B4B" opacity=".9"/></svg>"""

MENU = [
    ("/chizhovy/metod/", "Метод"),
    ("/chizhovy/programma/", "Программа"),
    ("/chizhovy/para/", "Для пар"),
    ("/chizhovy/vedushchie/", "Ведущие"),
    ("/chizhovy/otzyvy/", "Отзывы"),
    ("/chizhovy/voprosy/", "Вопросы"),
    ("/chizhovy/gid/", "Гайд"),
]

def nav(active=""):
    items = "".join(
        f'<a href="{u}"{" class=\"on\"" if u.strip("/").endswith(active) and active else ""}>{t}</a>'
        for u, t in MENU)
    return f"""<nav class="nav"><div class="wrap">
<a class="logo" href="/chizhovy/">{LOGO_SVG}<div><b>Настоящие отношения</b><span>Школа Алексея и&nbsp;Ирины Чижовых</span></div></a>
<label class="burger" for="mtoggle" aria-label="Меню"><span></span><span></span><span></span></label>
<input type="checkbox" id="mtoggle">
<div class="menu">{items}<a class="cta" href="/chizhovy/sessiya/">Ознакомительная сессия</a></div>
</div></nav>"""

FOOTER = """<footer><div class="wrap">
<div class="cols">
<div>
""" + LOGO_SVG + """
<p style="margin:14px 0 0;color:rgba(242,237,228,.7);font-size:.9rem;max-width:280px">Школа трансформации Алексея и&nbsp;Ирины Чижовых. Очные тренинги малыми группами и&nbsp;сопровождение до&nbsp;результата.</p>
</div>
<div><h4>Школа</h4>
<a href="/chizhovy/metod/">Метод</a>
<a href="/chizhovy/programma/">Программа целиком</a>
<a href="/chizhovy/modul-1/">Модуль I. Возвращение к&nbsp;себе</a>
<a href="/chizhovy/modul-2/">Модуль II. Внутренняя&nbsp;свобода</a>
<a href="/chizhovy/marafon/">Модуль III. Создатель&nbsp;реальности</a>
</div>
<div><h4>Люди</h4>
<a href="/chizhovy/vedushchie/">Алексей и&nbsp;Ирина</a>
<a href="/chizhovy/otzyvy/">Истории учеников</a>
<a href="/chizhovy/para/">Тренинг для пар</a>
</div>
<div><h4>Начать</h4>
<a href="/chizhovy/gid/">Гайд «Кто пишет сценарий твоей жизни»</a>
<a href="/chizhovy/sessiya/">Ознакомительная сессия</a>
<a href="https://t.me/+LVptSH6Mt4hhYmFi">Telegram-канал</a>
</div>
</div>
<div class="fine"><span>«Настоящие отношения» · chizhovy.ru</span><span>Прототип сайта. Результаты участников индивидуальны.</span></div>
</div></footer>"""

def page(title, desc, active, body):
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="/chizhovy/site.css">
</head>
<body>
{nav(active)}
{body}
{FOOTER}
</body>
</html>"""

P = {}

# ================= ГЛАВНАЯ =================
P["index.html"] = ("Настоящие отношения · школа трансформации Чижовых",
"Очный тренинг и три месяца сопровождения: выход из повторяющихся сценариев в отношениях, деле и состоянии.", "", f"""
<div class="hero"><div class="bg" style="background-image:url('/chizhovy/images/site-hero.png')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Школа трансформации Алексея и&nbsp;Ирины Чижовых</p>
<h1>Верни себе авторство своей жизни</h1>
<p class="lead">Очный тренинг и&nbsp;три месяца сопровождения. Выходишь из&nbsp;повторяющихся сценариев и&nbsp;начинаешь строить отношения, дело и&nbsp;себя из&nbsp;осознанного выбора.</p>
<div class="acts"><a class="btn btn-copper" href="/chizhovy/sessiya/">Записаться на&nbsp;сессию</a><a class="btn btn-ghost" href="/chizhovy/gid/">Скачать гайд бесплатно</a></div>
</div></div>

<section><div class="wrap">
<div class="nails">
<div class="nail"><b>16&nbsp;лет</b><span>в&nbsp;трансформационной практике</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе, каждого знаем по&nbsp;имени</span></div>
<div class="nail"><b>3</b><span>модуля очного погружения</span></div>
<div class="nail"><b>3&nbsp;месяца</b><span>сопровождения после тренинга</span></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Для тебя, если</p>
<h2>Узнаёшь себя хотя&nbsp;бы в&nbsp;одном</h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('book')}<h3>Всё понимаешь, а&nbsp;не&nbsp;меняется</h3><p>Книги прочитаны, курсы пройдены, выводы сделаны. Реакции те&nbsp;же, что пять лет назад.</p></div>
<div class="card"><span class="bignum">02</span>{icon('loop','var(--sage-deep)')}<h3>Сценарии повторяются</h3><p>Разные люди, разные обстоятельства, финал одинаковый. В&nbsp;отношениях, в&nbsp;деньгах, в&nbsp;теле.</p></div>
<div class="card"><span class="bignum">03</span>{icon('shield','var(--sand)')}<h3>Сильный снаружи, устал внутри</h3><p>Бизнес, семья, статус, всё по&nbsp;списку. И&nbsp;усталость, о&nbsp;которой некому рассказать.</p></div>
<div class="card"><span class="bignum">04</span>{icon('cups','var(--sage-deep)')}<h3>Близость ушла в&nbsp;быт</h3><p>Календарь общий, разговоры про логистику. Не&nbsp;ссоритесь, потому что незачем.</p></div>
<div class="card"><span class="bignum">05</span>{icon('ceiling','var(--sand)')}<h3>Деньги упёрлись в&nbsp;потолок</h3><p>Рывки вверх быстро выравниваются обратно. Цифра дохода годами почти одна.</p></div>
<div class="card"><span class="bignum">06</span>{icon('lens')}<h3>Хочется настоящего</h3><p>Не&nbsp;казаться, а&nbsp;быть. В&nbsp;паре, в&nbsp;деле, с&nbsp;собой. С&nbsp;этого запроса у&nbsp;нас начинали многие.</p></div>
</div>
</div></section>

<section class="dark"><div class="wrap">
<div class="diagrow">
<div>
<p class="eyebrow">Метод</p>
<h2>Мы работаем с&nbsp;причиной</h2>
<p>Повторы держатся не&nbsp;на&nbsp;характере и&nbsp;не&nbsp;на&nbsp;«таком партнёре». Их&nbsp;крутит событийный круг: старое решение включается быстрее сознания и&nbsp;доигрывает знакомый финал.</p>
<p>Разорвать круг усилием не&nbsp;выходит. Мы&nbsp;разбираем его там, где он&nbsp;записан: в&nbsp;эмоции и&nbsp;теле, в&nbsp;живой групповой работе.</p>
<p style="margin-top:24px"><a class="btn btn-ghost" href="/chizhovy/metod/">Разобрать метод подробно</a></p>
</div>
<div>{loop_diagram(dark=True)}</div>
</div>
</div></section>

<section style="padding-bottom:0"><div class="wrap">
<p class="eyebrow">Работаем по&nbsp;всей жизни</p>
<h2>Четыре сферы, которые сдвигаются вместе</h2>
<p class="sub">Запись одна, а&nbsp;платит за&nbsp;неё вся жизнь сразу. Поэтому и&nbsp;меняются сферы вместе, когда причина найдена.</p>
<div class="spheres" style="margin-top:32px">
<div class="sphere"><div class="ring">{ICONS['lens']}</div><b>Отношения</b><span>пара, дети, родители, близость</span></div>
<div class="sphere"><div class="ring">{ICONS['coins']}</div><b>Деньги и&nbsp;дело</b><span>доход, рост, решения без страха</span></div>
<div class="sphere"><div class="ring">{ICONS['flame']}</div><b>Энергия и&nbsp;тело</b><span>силы, сон, спорт, ясная голова</span></div>
<div class="sphere"><div class="ring">{ICONS['people']}</div><b>Окружение</b><span>команда, друзья, среда роста</span></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Программа</p>
<h2>Три модуля, один путь</h2>
<div class="timeline" style="margin-top:28px">{timeline_svg()}</div>
<div class="grid3" style="margin-top:26px">
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy/images/site-m1.png" alt="Утро, женщина пишет в дневник у окна" loading="lazy"></div><h3>I. Возвращение к&nbsp;себе</h3><p>Увидеть свои паттерны, установки и&nbsp;то, откуда они родом. Первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy/modul-1/">Про первый модуль</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy/images/real/real-07.jpg" alt="Группа тренинга в тёплом зале" loading="lazy"></div><h3>II. Внутренняя свобода</h3><p>Страх, вина, обида, чужие ожидания. Перезапись решений, которые правили годами.</p><p style="margin-top:12px"><a href="/chizhovy/modul-2/">Про второй модуль</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy/images/real/real-10.jpg" alt="Команда выпуска тренинга" loading="lazy"></div><h3>III. Создатель реальности</h3><p>Команда, еженедельные встречи, новые действия и&nbsp;результаты, которые остаются.</p><p style="margin-top:12px"><a href="/chizhovy/marafon/">Про Марафон</a></p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Какие возможности откроются</p>
<h2>Что становится возможным</h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('ceiling')}<h3>Дело выходит из&nbsp;потолка</h3><p>Видишь, что именно держало обороты и&nbsp;заставляло цепляться за&nbsp;«стабильный» заработок. Убираешь причину, не&nbsp;симптом.</p></div>
<div class="card"><span class="bignum">02</span>{icon('route','var(--sage-deep)')}<h3>Ясность про себя</h3><p>Кто я, куда бегу, почему всё повторяется по&nbsp;спирали. Видишь свои сильные стороны и&nbsp;путь к&nbsp;целям.</p></div>
<div class="card"><span class="bignum">03</span>{icon('lens','var(--sand)')}<h3>Крепкие отношения</h3><p>Выходишь из&nbsp;разрушающих связей и&nbsp;затяжных конфликтов, налаживаешь отношения с&nbsp;близкими.</p></div>
<div class="card"><span class="bignum">04</span>{icon('mountain','var(--sage-deep)')}<h3>Спокойствие и&nbsp;уверенность</h3><p>Внутренняя опора вместо выдержки на&nbsp;зубах. Острые моменты перестают выбивать из&nbsp;седла.</p></div>
<div class="card"><span class="bignum">05</span>{icon('people','var(--sand)')}<h3>Своё окружение</h3><p>Люди, с&nbsp;которыми можно в&nbsp;разведку и&nbsp;в&nbsp;дело. Навык слышать, договариваться, играть вместе.</p></div>
<div class="card"><span class="bignum">06</span>{icon('sunrise')}<h3>От понимания к&nbsp;действию</h3><p>Перестаёшь откладывать жизнь на&nbsp;потом. Путь от&nbsp;идеи до&nbsp;реализации сокращается в&nbsp;разы.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Как это выглядит</p>
<h2>Наши группы, без стоковых улыбок</h2>
<p class="sub">Это живые выпуски школы. Малые группы, очная работа, люди, которых мы&nbsp;знаем по&nbsp;именам и&nbsp;историям.</p>
<div class="mosaic" style="margin-top:28px">
<div class="ph"><img src="/chizhovy/images/real/real-05.jpg" alt="Выпуск группы тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-06.jpg" alt="Группа тренинга в зале" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-01.jpg" alt="Группа у камина с сертификатами" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-11.jpg" alt="Команда участников" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-13.jpg" alt="Выпуск модуля" loading="lazy"></div>
</div>
</div></section>

<section class="dark" style="padding:0"><div class="wrap" style="padding-top:76px;padding-bottom:76px">
<div class="pull"><div class="q">«Появилось ощущение, что вижу себя на&nbsp;всей шахматной доске, а&nbsp;не&nbsp;в&nbsp;одной клетке.»</div><div class="who">Участник тренинга, предприниматель</div></div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy/otzyvy/">Читать истории целиком</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Ведущие</p>
<h2>Двое, у&nbsp;которых совпадают слова&nbsp;и&nbsp;жизнь</h2>
<p>Алексей: коуч с&nbsp;сертификацией ICF, 16&nbsp;лет в&nbsp;трансформационной практике, триатлет. Ирина: трансформационный тренер, шесть лет готовилась к&nbsp;этому формату, работает на&nbsp;глубине, которую участники вспоминают годами.</p>
<p>Вместе 17&nbsp;лет. Школу отношений ведёт пара, у&nbsp;которой отношения живые: с&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них.</p>
<p style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy/vedushchie/">Познакомиться</a></p>
</div>
<div class="ph"><img src="/chizhovy/images/real/real-02.jpg" alt="Команда школы за общим столом" loading="lazy"></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="poster"><div class="bg" style="background-image:url('/chizhovy/images/site-dark.png')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Ближайшее погружение</p>
<h3>Модуль II. Внутренняя свобода</h3>
<p>Пять дней, после которых страх, вина и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p>
<p style="margin-top:24px"><a class="btn btn-copper" href="/chizhovy/sessiya/">Занять место</a></p>
</div></div>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Начни с&nbsp;часа разговора</h2>
<p class="sub" style="margin:0 auto 26px">Ознакомительная сессия с&nbsp;Алексеем: час о&nbsp;твоей ситуации и&nbsp;честный ответ, чем школа может помочь. Без обязательств идти дальше.</p>
<a class="btn btn-wine" href="/chizhovy/sessiya/">Записаться на&nbsp;сессию</a>
</div></section>
""")

# ================= МЕТОД =================
P["metod/index.html"] = ("Метод школы · Настоящие отношения",
"Событийный круг, состояние и психодрама: как устроена перезапись сценариев.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/site-metod.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Метод</p><h1>Жизнь слушается состояния</h1>
<p class="lead">Мы&nbsp;не&nbsp;учим «правильно общаться». Мы&nbsp;находим запись, которая пишет твои реакции, и&nbsp;помогаем её&nbsp;переписать.</p></div></div>

<section><div class="narrow">
<p class="eyebrow">Главная идея</p>
<h2>Муравей и&nbsp;слон</h2>
<p>Разум мал и&nbsp;суетлив, как муравей. Состояние огромно, как слон. Пока слон лежит или идёт в&nbsp;другую сторону, муравей может тащить план куда угодно: масса не&nbsp;та. Поэтому решения «с&nbsp;понедельника» держатся до&nbsp;первого настоящего стресса.</p>
<p>Управлять получается наоборот: сначала состояние, потом действия. Меняется состояние, меняются решения. Меняются решения, меняется жизнь. Ученики после тренинга говорят об&nbsp;этом коротко: мир зеркалит состояние.</p>
</div></section>

<section class="dark"><div class="wrap">
<div class="diagrow">
<div>{loop_diagram(dark=True)}</div>
<div>
<p class="eyebrow">Механика</p>
<h2>Событийный круг</h2>
<div class="legend" style="margin-top:8px">
<div class="li"><i>1</i><div><b>Событие</b><span>Что-то происходит: слово, взгляд, сумма на&nbsp;счёте. Само по&nbsp;себе оно нейтрально.</span></div></div>
<div class="li"><i>2</i><div><b>Эмоция</b><span>Реакция тела опережает мысль: аварийный центр мозга получает сигнал за&nbsp;миллисекунды до&nbsp;осмысления.</span></div></div>
<div class="li"><i>3</i><div><b>Старое решение</b><span>«Злиться опасно», «просить стыдно», «я&nbsp;сам». Принято в&nbsp;детстве, работает во&nbsp;взрослой жизни.</span></div></div>
<div class="li"><i>4</i><div><b>Сценарий</b><span>Поведение идёт по&nbsp;записи, финал тот&nbsp;же, что в&nbsp;прошлый раз. Круг замыкается и&nbsp;укрепляется.</span></div></div>
</div>
</div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">Инструмент</p>
<h2>Психодрама: перезапись в&nbsp;живой&nbsp;сцене</h2>
<p>Разговорами запись не&nbsp;берётся: она хранится в&nbsp;эмоции и&nbsp;теле, ниже этажа слов. Поэтому ядро работы у&nbsp;нас процессное. Психиатр Якоб Морено сто лет назад придумал психодраму: человек возвращается в&nbsp;ключевую сцену своей жизни, проживает её&nbsp;заново, смотрит на&nbsp;неё&nbsp;глазами других участников и&nbsp;прямо внутри сцены принимает другое решение.</p>
<svg viewBox="0 0 900 300" style="width:100%;height:auto;margin:26px 0 8px" role="img" aria-label="Два этажа психики: этаж слов и этаж эмоции с телом">
<rect x="60" y="30" width="780" height="105" rx="10" fill="#FFFFFF" stroke="rgba(110,59,75,.25)"/>
<rect x="60" y="160" width="780" height="105" rx="10" fill="#EFE9DF" stroke="rgba(110,59,75,.4)" stroke-width="1.5"/>
<text x="92" y="72" font-family="Playfair Display,Georgia,serif" font-size="21" fill="#322D2B">Этаж слов</text>
<text x="92" y="102" font-family="Manrope,sans-serif" font-size="14" fill="#6B615C">книги, разговоры, решения «с понедельника». Сюда стучались прошлые попытки</text>
<text x="92" y="202" font-family="Playfair Display,Georgia,serif" font-size="21" fill="#6E3B4B">Этаж эмоции и тела</text>
<text x="92" y="232" font-family="Manrope,sans-serif" font-size="14" fill="#6B615C">здесь хранится запись. И здесь же её переписывают: в живой сцене</text>
<path d="M775 105 v66" stroke="#6E3B4B" stroke-width="3"/>
<path d="M775 185 l-9 -13 h18 z" fill="#6E3B4B"/>
<text x="770" y="95" text-anchor="end" font-family="Manrope,sans-serif" font-size="12.5" fill="#6E3B4B">работа идёт сюда</text>
</svg>
<p>Морено называл это спонтанностью: способностью дать новый ответ на&nbsp;старую ситуацию. По-нашему: момент, когда пульт возвращается к&nbsp;хозяину.</p>
<div class="pull"><div class="q">«Труднее всего было принять точку&nbsp;А. Признать, где я&nbsp;на&nbsp;самом деле. Дальше всё началось.»</div><div class="who">Участник тренинга</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Три опоры результата</p>
<h2>Почему изменения остаются</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('layers')}<h3>Глубина</h3><p>Очные модули по&nbsp;несколько дней: время дойти до&nbsp;причины, а&nbsp;не&nbsp;снять симптом.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Группа</h3><p>10-20 человек. В&nbsp;чужих историях узнаёшь свою, в&nbsp;своих перестаёшь быть один.</p></div>
<div class="card">{icon('calendar','var(--sand)')}<h3>Практика</h3><p>Три месяца сопровождения: новые реакции закрепляются действиями в&nbsp;обычной жизни, пока не&nbsp;станут своими.</p></div>
</div>
<p style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy/programma/">Смотреть программу</a></p>
</div></section>
""")

# ================= ПРОГРАММА =================
P["programma/index.html"] = ("Программа · Настоящие отношения",
"Три модуля школы: Возвращение к себе, Внутренняя свобода, Создатель реальности.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/real/real-06.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Программа</p><h1>Путь из&nbsp;трёх модулей</h1>
<p class="lead">Каждый модуль решает свою задачу: увидеть запись, переписать её, закрепить новую жизнь действиями. Между модулями 3-5 недель на&nbsp;интеграцию.</p></div></div>

<section><div class="wrap">
<div class="timeline">{timeline_svg()}</div>
<div class="grid3" style="margin-top:26px">
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy/images/site-m1.png" alt="Модуль I" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль I · 2,5 дня</p><h3>Возвращение к&nbsp;себе</h3><p>Видишь свои повторяющиеся паттерны, установки и&nbsp;их&nbsp;источники. Результат: осознанность и&nbsp;первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy/modul-1/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy/images/real/real-07.jpg" alt="Модуль II" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль II · 5 дней</p><h3>Внутренняя свобода</h3><p>Глубокая работа с&nbsp;состояниями: страх, вина, обида, зависимость от&nbsp;чужого мнения. Результат: сила, спокойствие, ясность.</p><p style="margin-top:12px"><a href="/chizhovy/modul-2/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy/images/real/real-13.jpg" alt="Модуль III" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль III · 3 месяца</p><h3>Создатель реальности</h3><p>Интеграция в&nbsp;жизнь: видение, команда, ежедневная практика, результаты в&nbsp;деле и&nbsp;отношениях. Это и&nbsp;есть Марафон.</p><p style="margin-top:12px"><a href="/chizhovy/marafon/">Подробнее</a></p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Как устроено участие</h2>
<div class="card white" style="margin-top:20px">{icon('speech')}<h3>Начало: ознакомительная сессия</h3><p>Час разговора с&nbsp;Алексеем о&nbsp;твоей ситуации. Честно решаем, подходит&nbsp;ли тебе школа. Условия участия в&nbsp;модулях обсуждаются там&nbsp;же, лично.</p></div>
<div class="card white" style="margin-top:12px">{icon('people','var(--sage-deep)')}<h3>Формат</h3><p>Очные модули в&nbsp;Москве малой группой 10-20 человек, между модулями 3-5 недель с&nbsp;поддержкой, после третьего модуля три месяца сопровождения.</p></div>
<div class="card white" style="margin-top:12px">{icon('target','var(--sand)')}<h3>Для кого</h3><p>Для взрослых людей, готовых брать ответственность: предприниматели, руководители, пары. Мы&nbsp;отбираем участников на&nbsp;сессии, потому что глубина требует готовности.</p></div>
<p style="margin-top:28px"><a class="btn btn-wine" href="/chizhovy/sessiya/">Записаться на&nbsp;сессию</a></p>
</div></section>
""")

# ================= МОДУЛЬ 1 =================
P["modul-1/index.html"] = ("Модуль I. Возвращение к себе · Настоящие отношения",
"Два с половиной дня: увидеть свои паттерны и их источники.", "modul-1", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/site-m1.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль I · два с&nbsp;половиной дня</p><h1>Возвращение к&nbsp;себе</h1>
<p class="lead">Первый модуль отвечает на&nbsp;вопрос, с&nbsp;которого начинается любой сдвиг: что со&nbsp;мной происходит на&nbsp;самом деле и&nbsp;откуда это взялось.</p></div></div>

<section><div class="narrow">
<h2>Что происходит за&nbsp;эти дни</h2>
<p>Пятничный вечер, суббота и&nbsp;воскресенье. Погружение начинается с&nbsp;эмоционального входа в&nbsp;пространство тренинга: телефоны в&nbsp;сторону, маски снимаются постепенно и&nbsp;сами.</p>
<div class="card white" style="margin:18px 0 12px">{icon('book')}<h3>Видишь свои паттерны</h3><p>Повторяющиеся реакции, роли и&nbsp;установки, из&nbsp;которых соткан твой день: где ты&nbsp;терпишь, где убегаешь, где стараешься казаться.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('route','var(--sage-deep)')}<h3>Находишь источники</h3><p>В&nbsp;живых процессах видно, где было принято старое решение и&nbsp;чью интонацию ты&nbsp;до&nbsp;сих пор носишь как свою.</p></div>
<div class="card white">{icon('lens','var(--sand)')}<h3>Возвращаешь контакт с&nbsp;собой</h3><p>К&nbsp;воскресному вечеру появляется то, что участники называют «впервые за&nbsp;годы услышал себя». Отсюда начинается настоящая работа.</p></div>
<div class="pull"><div class="q">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная.»</div><div class="who">Участник первого модуля</div></div>
<p><strong>Результат модуля: осознанность.</strong> Ты&nbsp;видишь свою запись. Развидеть её&nbsp;уже не&nbsp;получится, и&nbsp;это лучшее, что могло случиться.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy/sessiya/">Начать с&nbsp;сессии</a> <a class="btn btn-ghost" href="/chizhovy/modul-2/" style="margin-left:8px">Дальше: Модуль II</a></p>
</div></section>
""")

# ================= МОДУЛЬ 2 =================
P["modul-2/index.html"] = ("Модуль II. Внутренняя свобода · Настоящие отношения",
"Пять дней глубокой работы: страх, вина, обида, внутренняя опора.", "modul-2", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/site-dark.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль II · пять дней</p><h1>Внутренняя свобода</h1>
<p class="lead">Самый глубокий модуль школы. Пять дней, после которых страх, вина и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p></div></div>

<section><div class="narrow">
<h2>С чем работаем</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('flame')}<h3>Страх и&nbsp;важность</h3><p>Разбираем, как раздутая ставка парализует действия, и&nbsp;возвращаем способность решать спокойно.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Вина и&nbsp;ответственность</h3><p>Вина сливает энергию и&nbsp;притягивает наказание. Ответственность возвращает силу. Учимся различать их&nbsp;телом.</p></div>
<div class="card">{icon('loop','var(--sand)')}<h3>Обида</h3><p>Старые обиды держат сценарии годами. Проживаем их&nbsp;до&nbsp;конца в&nbsp;безопасном пространстве группы.</p></div>
<div class="card">{icon('mountain')}<h3>Внутренняя опора</h3><p>Собираем состояние, в&nbsp;котором ты&nbsp;не&nbsp;зависишь от&nbsp;оценки, настроения партнёра и&nbsp;погоды на&nbsp;рынке.</p></div>
</div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p><strong>Результат модуля: сила, спокойствие, ясность.</strong> Плюс инструменты, которыми ты&nbsp;дальше пользуешься сам: тело помнит, как выходить из&nbsp;захвата.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy/sessiya/">Занять место</a> <a class="btn btn-ghost" href="/chizhovy/marafon/" style="margin-left:8px">Дальше: Марафон</a></p>
</div></section>
""")

# ================= МАРАФОН =================
P["marafon/index.html"] = ("Модуль III. Создатель реальности · Настоящие отношения",
"Три месяца практики в жизни: команда, еженедельные встречи, результаты, которые остаются.", "marafon", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/real/real-10.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль III · три месяца</p><h1>Создатель реальности</h1>
<p class="lead">Инсайты выветриваются за&nbsp;две недели, если их&nbsp;не&nbsp;закрепить действиями. Марафон существует ровно для этого: три месяца новая жизнь тренируется в&nbsp;настоящей.</p></div></div>

<section><div class="narrow">
<h2>Как устроены три месяца</h2>
<div class="card white" style="margin:20px 0 12px">{icon('people')}<h3>Команда</h3><p>Ты&nbsp;идёшь не&nbsp;один: группа становится командой с&nbsp;общей целью и&nbsp;напарником у&nbsp;каждого. Поддержка работает даже в&nbsp;два часа ночи.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Еженедельные встречи</h3><p>Разборы с&nbsp;Алексеем и&nbsp;Ириной: что получилось, где старая запись взяла своё, какой следующий шаг.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('sunrise','var(--sand)')}<h3>Ежедневная практика</h3><p>Утром формулируешь главный фокус дня, вечером подводишь итог: открытия и&nbsp;благодарности. Простая дисциплина, которая за&nbsp;90&nbsp;дней перепрошивает привычный способ жить.</p></div>
<div class="card white">{icon('target')}<h3>Реальные цели</h3><p>Работа идёт на&nbsp;твоих живых задачах: дело, деньги, отношения, тело. Результат меряем фактами, не&nbsp;ощущениями.</p></div>

<div class="pull"><div class="q">«Раньше я&nbsp;отсеивал людей по&nbsp;уровню жизни. Сейчас просто строю настоящие отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами.»</div><div class="who">Выпускник Марафона, предприниматель</div></div>
<p><strong>Результат: новые действия и&nbsp;новые результаты.</strong> Не&nbsp;состояние после тренинга, а&nbsp;жизнь, которая продолжает расти, когда сопровождение закончилось.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Выпуски Марафона</p>
<div class="mosaic">
<div class="ph"><img src="/chizhovy/images/real/real-10.jpg" alt="Команда Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-11.jpg" alt="Выпуск Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-13.jpg" alt="Финал модуля" loading="lazy"></div>
</div>
<p style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy/sessiya/">Обсудить участие на&nbsp;сессии</a></p>
</div></section>
""")

# ================= ДЛЯ ПАР =================
P["para/index.html"] = ("Тренинг для пар · Настоящие отношения",
"Муж и жена проходят тренинг вместе: близость растёт с двух сторон.", "para", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/site-para-itog.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Для пар</p><h1>Когда проходят вдвоём, меняется сама пара</h1>
<p class="lead">Можно годами носить с&nbsp;тренингов инсайты в&nbsp;дом, где тебя ждёт прежний человек. А&nbsp;можно прийти вдвоём и&nbsp;переписать общий сценарий с&nbsp;двух сторон сразу.</p></div></div>

<section><div class="narrow">
<h2>Что происходит с&nbsp;парой</h2>
<p>У&nbsp;пары всегда два сценария, и&nbsp;они цепляются друг за&nbsp;друга, как шестерёнки: её&nbsp;обида включает его&nbsp;молчание, его&nbsp;молчание кормит её&nbsp;обиду. На&nbsp;тренинге каждый работает со&nbsp;своей записью, и&nbsp;шестерёнки расцепляются.</p>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('mountain')}<h3>Он</h3><p>Возвращает опору и&nbsp;уверенность: решения из&nbsp;спокойствия, дело и&nbsp;достаток растут без надрыва.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Она</h3><p>Возвращает себя: раскрывается, вдохновляет, перестаёт жить в&nbsp;режиме ожидания и&nbsp;обслуживания.</p></div>
</div>
<p style="margin-top:24px">Дальше начинается то, ради чего школа носит своё имя: <strong>настоящие отношения.</strong> Разговоры, которые заканчиваются ближе, чем начинались. Быт, в&nbsp;котором снова видно человека. Общие цели вместо параллельных жизней.</p>
<p>Пары на&nbsp;группе работают наравне со&nbsp;всеми: часть процессов вместе, часть по&nbsp;отдельности. Прийти одному тоже можно: отношения меняются, даже когда запись переписывает один из&nbsp;двоих.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy/sessiya/">Записаться на&nbsp;сессию вдвоём</a></p>
</div></section>
""")

# ================= ВЕДУЩИЕ =================
P["vedushchie/index.html"] = ("Алексей и Ирина Чижовы · Настоящие отношения",
"Ведущие школы: коуч ICF и трансформационный тренер, вместе 17 лет.", "vedushchie", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/real/real-01.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Ведущие</p><h1>Алексей и&nbsp;Ирина Чижовы</h1>
<p class="lead">Школу отношений ведёт пара, которая 17&nbsp;лет строит свои. С&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них, поэтому в&nbsp;зале нет теории с&nbsp;чужих слов.</p></div></div>

<section><div class="narrow">
<div class="grid2">
<div class="card white">{icon('mountain')}<h3>Алексей</h3><p>Коуч с&nbsp;сертификацией ICF, 16&nbsp;лет в&nbsp;трансформационной практике. Держит структуру и&nbsp;точность процесса: с&nbsp;ним безопасно идти в&nbsp;глубину, потому что он&nbsp;видит дорогу целиком.</p></div>
<div class="card white">{icon('flame','var(--sand)')}<h3>Ирина</h3><p>Трансформационный тренер. Шесть лет готовилась к&nbsp;этому формату под руководством наставника. Работает на&nbsp;глубине: участники говорят, что она «вскрывает и&nbsp;собирает», и&nbsp;вспоминают её&nbsp;работу годами.</p></div>
</div>
<p style="margin-top:26px">Роли в&nbsp;зале дополняют друг друга: его&nbsp;опора и&nbsp;её&nbsp;чувствование, структура и&nbsp;глубина. Те&nbsp;же два начала, что мы&nbsp;помогаем соединить каждому участнику.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy/images/real/real-08.jpg" alt="Финиш забега" loading="lazy"></div>
<div>
<p class="eyebrow">Дисциплина как часть метода</p>
<h2>Слова, за&nbsp;которыми стоит тело</h2>
<p>Алексей: триатлет, финишер IronMan&nbsp;70.3. Не&nbsp;ради медалей: длинная дистанция каждый день проверяет то, чему школа учит в&nbsp;зале. Состояние первично, решения из&nbsp;спокойствия, играть в&nbsp;долгую.</p>
<p>Команды школы выходят на&nbsp;забеги вместе: тело быстро выдаёт, где ты&nbsp;себя обманываешь, и&nbsp;честно радуется, когда ты&nbsp;настоящий.</p>
</div>
</div>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Познакомиться лично</h2>
<p class="sub" style="margin:0 auto 26px">Ознакомительная сессия с&nbsp;Алексеем: час разговора о&nbsp;твоей ситуации, честный взгляд со&nbsp;стороны и&nbsp;понятный следующий шаг.</p>
<a class="btn btn-wine" href="/chizhovy/sessiya/">Записаться</a>
</div></section>
""")

# ================= ОТЗЫВЫ =================
P["otzyvy/index.html"] = ("Истории учеников · Настоящие отношения",
"Живые истории выпускников школы: до, во время и после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/real/real-05.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истории учеников</p><h1>Их словами, без глянца</h1>
<p class="lead">Мы&nbsp;не&nbsp;переписываем отзывы под рекламу. Ниже живые фрагменты историй с&nbsp;согласия авторов. Каждая история личная, результат у&nbsp;каждого свой.</p></div></div>

<section><div class="narrow">
<!-- ПРОТОТИП: подписи и полные версии согласовать с авторами перед публикацией -->
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Предприниматель, пришёл в&nbsp;кризис</p>
<p>«Я&nbsp;находился в&nbsp;фазе, которую называют дном: кассовый разрыв, долги, расставание с&nbsp;девушкой, друзья отвернулись. Не&nbsp;хотелось ни&nbsp;с&nbsp;кем общаться, хотелось закрыться в&nbsp;коробочку и&nbsp;сидеть одному.</p>
<p>На&nbsp;тренинге я&nbsp;долго сопротивлялся, как баран. Труднее всего было принять точку&nbsp;А: признать, где я&nbsp;на&nbsp;самом деле. А&nbsp;потом увидел, что покупал отношения вместо того, чтобы их&nbsp;строить.</p>
<p style="margin-bottom:0">Сейчас строю настоящие отношения везде. Деньги начали приходить, энергии много, и&nbsp;я&nbsp;умею ей&nbsp;распоряжаться. Цели выросли кратно, научился играть в&nbsp;долгую. Одной фразой: получил новую версию себя».</p>
</div>
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Участница второго модуля</p>
<p style="margin-bottom:0">«Годами затыкала свои боли: научилась обезболивать и&nbsp;не&nbsp;слышать себя, стала чёрствой к&nbsp;себе. На&nbsp;модуле впервые за&nbsp;много лет плакала при людях и&nbsp;поняла, что это не&nbsp;стыдно. Теперь знаю, что могу быть яркой, настоящей, звонкой, сама по&nbsp;себе».</p>
</div>
<div class="card white">
<p class="eyebrow" style="margin-bottom:10px">Выпускница Марафона</p>
<p style="margin-bottom:0">«Полгода не&nbsp;могла решиться на&nbsp;поездку, даже паспорт найти не&nbsp;могла. После работы в&nbsp;группе просто приняла решение внутри, и&nbsp;всё сложилось за&nbsp;день. Мелочь? Для меня это была первая за&nbsp;годы вещь, сделанная для себя».</p>
</div>

<div class="pull"><div class="q">«Моя жизнь точно разделена на&nbsp;до&nbsp;и&nbsp;после.»</div><div class="who">Участница школы</div></div>
<div class="pull"><div class="q">«Спасибо, что помогли прожить стену, которую я&nbsp;так долго строил. Теперь она мне не&nbsp;нужна.»</div><div class="who">Участник школы</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="mosaic">
<div class="ph"><img src="/chizhovy/images/real/real-03.jpg" alt="Группа выпуска" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-09.jpg" alt="Участники тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
</div>
<p style="margin-top:30px;text-align:center"><a class="btn btn-wine" href="/chizhovy/sessiya/">Начать свою историю</a></p>
</div></section>
""")

# ================= ВОПРОСЫ =================
P["voprosy/index.html"] = ("Вопросы и ответы · Настоящие отношения",
"Честные ответы: формат, глубина, группа, условия участия.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Вопросы и&nbsp;ответы</p><h1>Спрашивают перед стартом</h1>
<p class="lead">Собрали то, что чаще всего звучит на&nbsp;ознакомительных сессиях. Если своего вопроса не&nbsp;нашёл, задай его лично: контакты внизу.</p></div></div>

<section><div class="narrow">
<details><summary>На чём основан метод?</summary><p>На&nbsp;практической психологии: психодрама Якоба Морено, работа с&nbsp;состоянием и&nbsp;групповые процессы, проверенные за&nbsp;16&nbsp;лет практики. Глубину даём через живой опыт, объясняем через понятные механизмы работы мозга и&nbsp;тела.</p></details>
<details><summary>Я уже ходил к&nbsp;психологу. Чем это отличается?</summary><p>Личная терапия работает словами и&nbsp;по&nbsp;часу в&nbsp;неделю. Здесь работа идёт в&nbsp;живых сценах, телом и&nbsp;эмоцией, в&nbsp;погружении на&nbsp;несколько дней. Это разные инструменты, и&nbsp;они хорошо дополняют друг друга.</p></details>
<details><summary>Боюсь групповой работы. Придётся раскрываться перед&nbsp;чужими?</summary><p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой. Обычно уже к&nbsp;вечеру первого дня группа перестаёт быть чужой: у&nbsp;людей одинаковые боли, и&nbsp;в&nbsp;чужой истории ты&nbsp;узнаёшь свою.</p></details>
<details><summary>Можно прийти одному, без&nbsp;партнёра?</summary><p>Да. Большинство участников приходят по&nbsp;одному. Отношения меняются, даже когда работает один из&nbsp;двоих: твоя половина общего сценария в&nbsp;твоих руках.</p></details>
<details><summary>Сколько времени занимает программа?</summary><p>Модуль I: два с&nbsp;половиной дня (пятничный вечер плюс выходные). Модуль II: пять дней. Модуль III: три месяца сопровождения при обычной жизни. Между модулями 3-5 недель.</p></details>
<details><summary>Что за ознакомительная сессия и&nbsp;сколько она стоит?</summary><p>Час личного разговора с&nbsp;Алексеем о&nbsp;твоей ситуации. Стоимость 3&nbsp;000&nbsp;рублей. По&nbsp;итогам ты&nbsp;понимаешь свой запрос и&nbsp;честно решаешь, идти&nbsp;ли дальше. Условия участия в&nbsp;модулях обсуждаются там&nbsp;же.</p></details>
<details><summary>Какие гарантии?</summary><p>Честная: метод работает, когда работаешь ты. Мы&nbsp;даём процесс, группу, сопровождение и&nbsp;16&nbsp;лет опыта. Результат складывается из&nbsp;этого и&nbsp;твоих действий, поэтому у&nbsp;каждого он&nbsp;свой.</p></details>
<details><summary>Как попасть на тренинг?</summary><p>Школа растёт через рекомендации, без массовой рекламы. Первый шаг один для всех: ознакомительная сессия. Запись через Telegram, кнопка ниже.</p></details>
<p style="margin-top:28px"><a class="btn btn-wine" href="/chizhovy/sessiya/">Записаться на&nbsp;сессию</a></p>
</div></section>
""")

# ================= СЕССИЯ =================
P["sessiya/index.html"] = ("Ознакомительная сессия · Настоящие отношения",
"Час разговора с Алексеем: твоя ситуация, честный взгляд, понятный шаг. 3000 рублей.", "sessiya", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy/images/site-sessiya.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Первый шаг</p><h1>Ознакомительная сессия</h1>
<p class="lead">Час разговора с&nbsp;Алексеем один на&nbsp;один. Не&nbsp;продажа и&nbsp;не&nbsp;диагностика по&nbsp;чек-листу: живой разбор твоей ситуации.</p></div></div>

<section><div class="narrow">
<h2>Как проходит</h2>
<div class="card white" style="margin:20px 0 12px">{icon('speech')}<h3>Ты рассказываешь</h3><p>Что происходит и&nbsp;что уже пробовал. Без подготовки и&nbsp;правильных слов: как есть.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('gear','var(--sage-deep)')}<h3>Алексей показывает механику</h3><p>Где в&nbsp;твоей истории крутится сценарий и&nbsp;что его держит. Обычно уже этот час даёт первое «вот оно что».</p></div>
<div class="card white">{icon('route','var(--sand)')}<h3>Вы решаете, что дальше</h3><p>Подходит&nbsp;ли тебе школа, с&nbsp;какого модуля заходить, и&nbsp;стоит&nbsp;ли вообще. Отговорить можем так&nbsp;же честно, как пригласить.</p></div>

<div class="nails" style="grid-template-columns:1fr 1fr;margin-top:28px">
<div class="nail"><b>60&nbsp;минут</b><span>личного разговора, онлайн или очно</span></div>
<div class="nail"><b>3&nbsp;000&nbsp;₽</b><span>стоимость сессии. Условия модулей обсуждаются лично</span></div>
</div>

<div style="background:var(--linen);border:1px solid var(--line);border-radius:10px;padding:34px;margin-top:30px;text-align:center">
<h3 style="font-size:1.4rem">Записаться</h3>
<p class="sub" style="margin:8px auto 22px">Напиши слово «сессия» в&nbsp;наш Telegram. Ответим лично, без ботов и&nbsp;рассылок.</p>
<a class="btn btn-wine" href="https://t.me/+LVptSH6Mt4hhYmFi">Написать в&nbsp;Telegram</a>
</div>
</div></section>
""")

css_path = ROOT / "site.css"
css_path.write_text(CSS.strip() + "\n", encoding="utf-8")
n = 0
for rel, (title, desc, active, body) in P.items():
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(page(title, desc, active, body), encoding="utf-8")
    n += 1
print(f"OK v2: site.css + {n} страниц (иконки, диаграмма, таймлайн, мозаика, фавикон)")
