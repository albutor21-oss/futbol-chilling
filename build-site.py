# Convierte la página de la app (fantasy-diario.html) en index.html instalable como app para GitHub Pages.
# Uso: python3 build-site.py ruta/a/fantasy-diario.html  -> escribe index.html junto a este script
import sys, os, re
src = open(sys.argv[1], encoding='utf-8').read()
src = re.sub(r'<title>.*?</title>', '', src, count=1, flags=re.S)
src = src.replace('<meta name="claude:viewport-fit-sides" content="cover">', '')
head = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Fútbol Chilling</title>
<meta name="description" content="Tu parte diario de LaLiga Fantasy: tu equipo, bajas, mercado y noticias.">
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Fútbol Chilling">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#e5ebe3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1d2420" media="(prefers-color-scheme: dark)">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}
body{margin:0;font:14px system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
html,body{overscroll-behavior-y:none}
</style>
'''
out = head + src + '\n</html>\n'
# los <link> y <style> de la app quedan en el body; los navegadores los aplican igual
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out))
