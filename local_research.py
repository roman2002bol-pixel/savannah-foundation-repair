"""Source-backed area guidance. Re-run after HTML generation; safe to repeat."""
from pathlib import Path
import json, re
from html import escape

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'local_research.json').read_text(encoding='utf-8'))

def section(title, cards, intro='', tail=''):
    return ('\n<!-- LOCAL-RESEARCH START -->\n<section class="field-guide" id="local-planning"><div class="container">'
            '<span class="eyebrow">Local planning guide</span><h2>'+escape(title)+'</h2>'
            + ('<p class="guide-intro">'+escape(intro)+'</p>' if intro else '')
            + '<div class="guide-grid">'+cards+'</div>'+tail+'</div></section>\n<!-- LOCAL-RESEARCH END -->\n')

def insert(text, addition):
    cta = text.rfind('<div class="cta-band">')
    at = text.rfind('<section', 0, cta) if cta >= 0 else -1
    if at < 0: at = text.find('</main>')
    if at < 0: raise ValueError('Missing main/CTA insertion point')
    return text[:at].rstrip() + addition + text[at:]

def apply_site(root=ROOT):
    for path in sorted(root.glob('service-areas/*.html')):
        text = path.read_text(encoding='utf-8'); original = text
        # Area pages already have their own local context; repeated service scenarios add no value.
        old = re.search(r'<!-- FIELD-GUIDE START -->.*?<!-- FIELD-GUIDE END -->', text, re.S)
        preserved = ''
        if old and path.stem not in DATA:
            match = re.search(r'<div class="guide-source">(.*?)</div>', old.group(), re.S)
            if match: preserved = match.group(1)
        text = re.sub(r'\n?<!-- FIELD-GUIDE START -->.*?<!-- FIELD-GUIDE END -->\n?', '', text, flags=re.S)
        if path.stem in DATA or path.stem == 'index':
            text = re.sub(r'\n?<!-- LOCAL-RESEARCH START -->.*?<!-- LOCAL-RESEARCH END -->\n?', '', text, flags=re.S)
        if path.stem in DATA:
            d = DATA[path.stem]; cards = ''
            for title, body, url, label in d['cards']:
                source = '<p class="guide-source"><a href="'+escape(url)+'">'+escape(label)+'</a></p>' if url else ''
                cards += '<article><h3>'+escape(title)+'</h3><p>'+escape(body)+'</p>'+source+'</article>'
            tail = '<p>'+escape(d['next'])+' <a href="../services/'+d['service']+'.html">'+escape(d['anchor'])+'</a>.</p><p class="guide-source">Local sources checked September 23, 2026. Confirm current requirements for the address and proposed scope.</p>'
            text = insert(text, section(d['title'], cards, tail=tail))
        elif path.stem == 'index':
            cards = ''.join('<article><h3><a href="'+slug+'.html#local-planning">'+escape(d['name'])+'</a></h3><p>'+escape(d['summary'])+'</p></article>' for slug,d in DATA.items())
            text = insert(text, section('Plan for the location before choosing the work', cards))
        elif preserved and '<!-- LOCAL-RESEARCH START -->' not in text:
            # Retain the earlier local note without its duplicated illustrative job.
            text = insert(text, section('Before arranging work at this address', '<article>'+preserved+'</article>'))
        if text != original: path.write_text(text, encoding='utf-8')
    # Link related service information to the relevant researched area, with descriptive anchors.
    for slug,d in DATA.items():
        path = root / 'services' / (d['service']+'.html')
        text = path.read_text(encoding='utf-8'); original = text
        marker = '<!-- LOCAL-LINK '+slug+' -->'
        text = re.sub(re.escape(marker)+r'.*?<!-- /LOCAL-LINK -->', '', text, flags=re.S)
        note = marker+'<p class="guide-source">Planning in '+escape(d['name'])+'? <a href="../service-areas/'+slug+'.html#local-planning">'+escape(d['title'])+'</a>.</p><!-- /LOCAL-LINK -->'
        end = text.find('<!-- FIELD-GUIDE END -->')
        at = text.rfind('</div></section>', 0, end) if end >= 0 else -1
        if at < 0: raise ValueError('Missing service field guide: '+str(path))
        text = text[:at]+note+text[at:]
        if text != original: path.write_text(text, encoding='utf-8')

if __name__ == '__main__':
    apply_site()
