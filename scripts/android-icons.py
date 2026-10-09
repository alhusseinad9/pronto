"""Replace the default Capacitor launcher icons with the Pronto icon."""
import os, shutil, sys
from PIL import Image
res = 'android/app/src/main/res'
sizes = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
src = Image.open('icons/icon-512.png').convert('RGBA')
# legacy PNG icons are used instead of the adaptive-icon XML
shutil.rmtree(f'{res}/mipmap-anydpi-v26', ignore_errors=True)
for d, s in sizes.items():
    folder = f'{res}/mipmap-{d}'
    os.makedirs(folder, exist_ok=True)
    img = src.resize((s, s), Image.LANCZOS)
    for name in ('ic_launcher.png', 'ic_launcher_round.png', 'ic_launcher_foreground.png'):
        img.save(f'{folder}/{name}')
print('icons done')
