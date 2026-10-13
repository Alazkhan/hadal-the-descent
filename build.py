"""Makes index.html (opens in any browser, served by GitHub Pages) from page.html (the page as published to claude.ai)."""
import pathlib
here = pathlib.Path(__file__).parent
page = (here / 'page.html').read_text(encoding='utf-8')
SITE = 'https://alazkhan.github.io/hadal-the-descent/'
DESC = ('A first-person underwater horror and survival game. An ocean planet has one wound in its seafloor, '
        'and something at the bottom of it is sending a signal.')
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Crect width='32' height='32' fill='%2303090c'/%3E"
        "%3Ccircle cx='16' cy='16' r='9' fill='none' stroke='%23f2b552' stroke-width='2'/%3E"
        "%3Ccircle cx='16' cy='16' r='2.5' fill='%23f2b552'/%3E%3C/svg%3E")
head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#03090c">
<meta property="og:type" content="website">
<meta property="og:title" content="HADAL: The Descent">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}img/anchorage-aerial.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{ICON}">
<style>body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
'''
(here / 'index.html').write_text(head + page + '\n</body>\n</html>\n', encoding='utf-8')
print('index.html written')
