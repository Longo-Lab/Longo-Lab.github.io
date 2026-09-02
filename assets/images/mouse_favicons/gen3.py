import cairosvg, os
from PIL import Image

OUT = "/sessions/wonderful-trusting-lamport/mnt/outputs/mouse_favicons"
CARDINAL = "#8C1515"
# scale+center used to keep entire character inside the r=32 circle
TRANSFORM = 'transform="translate(32,32) scale(0.7) translate(-32,-32)"'

def bg_circle():
    return f'<circle cx="32" cy="32" r="32" fill="{CARDINAL}"/>'

def character(fur, ear_inner, shirt, eye_style="bored", muzzle="#F4F4F4"):
    if eye_style == "bored":
        eyes = '''
        <path d="M20 30 Q24 33 28 30" stroke="#2E2D29" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <path d="M36 30 Q40 33 44 30" stroke="#2E2D29" stroke-width="2.2" fill="none" stroke-linecap="round"/>'''
    else:
        eyes = eye_style
    return f'''
    <path d="M4 64 Q4 46 16 42 L48 42 Q60 46 60 64 Z" fill="{shirt}"/>
    <path d="M24 42 Q32 48 40 42 L40 46 Q32 51 24 46 Z" fill="#2E2D29" opacity="0.15"/>
    <rect x="26" y="38" width="12" height="8" rx="3" fill="{fur}"/>
    <path d="M10 60 Q22 52 32 58 Q42 52 54 60 L54 66 L10 66 Z" fill="{shirt}" opacity="0.85"/>
    <circle cx="14" cy="14" r="11" fill="{fur}"/>
    <circle cx="14" cy="14" r="6" fill="{ear_inner}"/>
    <circle cx="50" cy="14" r="11" fill="{fur}"/>
    <circle cx="50" cy="14" r="6" fill="{ear_inner}"/>
    <ellipse cx="32" cy="34" rx="22" ry="19" fill="{fur}"/>
    <ellipse cx="32" cy="42" rx="12" ry="8" fill="{muzzle}"/>
    {eyes}
    <ellipse cx="32" cy="39" rx="3" ry="2.2" fill="#2E2D29"/>
    <path d="M32 41 Q32 46 27 47" stroke="#2E2D29" stroke-width="1.6" fill="none" stroke-linecap="round"/>
    <path d="M32 41 Q32 46 37 47" stroke="#2E2D29" stroke-width="1.6" fill="none" stroke-linecap="round"/>
    <path d="M12 40 L22 39" stroke="#2E2D29" stroke-width="1" opacity="0.45"/>
    <path d="M12 45 L22 43" stroke="#2E2D29" stroke-width="1" opacity="0.45"/>
    <path d="M52 40 L42 39" stroke="#2E2D29" stroke-width="1" opacity="0.45"/>
    <path d="M52 45 L42 43" stroke="#2E2D29" stroke-width="1" opacity="0.45"/>
    <rect x="29" y="45" width="3" height="4" fill="#fff" stroke="#d8d8d8" stroke-width="0.4"/>
    <rect x="32" y="45" width="3" height="4" fill="#fff" stroke="#d8d8d8" stroke-width="0.4"/>
    '''

def svg_wrap(bg, group_inner):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">{bg}<g {TRANSFORM}>{group_inner}</g></svg>'

icons = {}

# 1. Poppy hoodie, shades, illuminating gold chain
char = character(fur="#7F7776", ear_inner="#DAD7CB", shirt="#E98300", eye_style="")
extra = '''
    <path d="M12 56 Q32 62 52 56" stroke="#FEC51D" stroke-width="3.5" fill="none" stroke-linecap="round"/>
    <circle cx="24" cy="59" r="2.6" fill="#FEC51D"/>
    <rect x="15" y="25" width="16" height="8" rx="3" fill="#2E2D29"/>
    <rect x="33" y="25" width="16" height="8" rx="3" fill="#2E2D29"/>
    <rect x="31" y="27" width="2" height="2" fill="#2E2D29"/>
'''
icons["mouse_01_shades_chain"] = svg_wrap(bg_circle(), char + extra)

# 2. Sky sweater, spirited beanie
char = character(fur="#B6B1A9", ear_inner="#F4F4F4", shirt="#4298B5")
extra = '''
    <path d="M11 18 Q32 -2 53 18 Q46 12 32 12 Q18 12 11 18 Z" fill="#E04F39"/>
    <rect x="10" y="14" width="44" height="7" rx="3" fill="#C74632"/>
    <circle cx="32" cy="9" r="4" fill="#FEDD5C"/>
'''
icons["mouse_02_beanie"] = svg_wrap(bg_circle(), char + extra)

# 3. Palo verde hoodie, black headphones
char = character(fur="#766253", ear_inner="#DAD7CB", shirt="#279989")
extra = '''
    <path d="M10 26 Q10 2 32 2 Q54 2 54 26" stroke="#2E2D29" stroke-width="4" fill="none"/>
    <rect x="4" y="24" width="10" height="16" rx="4" fill="#2E2D29"/>
    <rect x="50" y="24" width="10" height="16" rx="4" fill="#2E2D29"/>
    <rect x="6" y="27" width="6" height="10" rx="2" fill="#544948"/>
    <rect x="52" y="27" width="6" height="10" rx="2" fill="#544948"/>
'''
icons["mouse_03_headphones"] = svg_wrap(bg_circle(), char + extra)

# 4. Bay shirt, illuminating bandana
char = character(fur="#544948", ear_inner="#D4D1D1", shirt="#6FA287", eye_style='''
        <path d="M19 27 L29 27" stroke="#2E2D29" stroke-width="2.4" stroke-linecap="round"/>
        <path d="M36 28 Q40 31 44 28" stroke="#2E2D29" stroke-width="2.2" fill="none" stroke-linecap="round"/>
''')
extra = '''
    <path d="M9 19 Q32 6 55 19 L55 24 Q32 14 9 24 Z" fill="#FEDD5C"/>
    <circle cx="20" cy="20" r="1.4" fill="#8C1515"/>
    <circle cx="26" cy="18" r="1.4" fill="#8C1515"/>
    <circle cx="34" cy="18" r="1.4" fill="#8C1515"/>
'''
icons["mouse_04_bandana"] = svg_wrap(bg_circle(), char + extra)

# 5. Plum jacket + cap + bow tie (PG, no cigar)
char = character(fur="#766253", ear_inner="#DAD7CB", shirt="#620059")
extra = '''
    <path d="M9 16 Q32 0 55 16 Q46 8 32 8 Q18 8 9 16 Z" fill="#350D36"/>
    <ellipse cx="47" cy="17" rx="10" ry="4" fill="#350D36"/>
    <path d="M26 55 L32 51 L38 55 L32 59 Z" fill="#FEC51D"/>
    <circle cx="32" cy="55" r="2" fill="#D1660F"/>
'''
icons["mouse_05_cap_bowtie"] = svg_wrap(bg_circle(), char + extra)

# 6. Spirited shirt, illuminating crown
char = character(fur="#DAD7CB", ear_inner="#F4F4F4", shirt="#E04F39")
extra = '''
    <path d="M16 14 L22 4 L28 12 L32 2 L36 12 L42 4 L48 14 L46 20 L18 20 Z" fill="#FEDD5C" stroke="#FEC51D" stroke-width="1"/>
    <circle cx="22" cy="10" r="1.6" fill="#279989"/>
    <circle cx="32" cy="7" r="1.6" fill="#4298B5"/>
    <circle cx="42" cy="10" r="1.6" fill="#279989"/>
'''
icons["mouse_06_crown"] = svg_wrap(bg_circle(), char + extra)

for name, svg in icons.items():
    svg_path = os.path.join(OUT, f"{name}.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    cairosvg.svg2png(url=svg_path, write_to=os.path.join(OUT, f"{name}_128.png"), output_width=128, output_height=128)
    cairosvg.svg2png(url=svg_path, write_to=os.path.join(OUT, f"{name}_32.png"), output_width=32, output_height=32)
    img = Image.open(os.path.join(OUT, f"{name}_128.png")).convert("RGBA")
    img.save(os.path.join(OUT, f"{name}.ico"), sizes=[(16,16),(32,32),(48,48),(64,64),(128,128)])

names = list(icons.keys())
imgs = [Image.open(os.path.join(OUT, f"{n}_128.png")).convert("RGBA") for n in names]
sheet = Image.new("RGBA", (128*3, 128*2), (255,255,255,255))
for i, im in enumerate(imgs):
    x = (i % 3) * 128
    y = (i // 3) * 128
    sheet.paste(im, (x,y), im)
sheet.save(os.path.join(OUT, "contact_sheet.png"))
print("done", names)
