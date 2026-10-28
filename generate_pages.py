import json
import os

# Load data
with open('exhibition_data.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def render_content_en(item):
    item_type = item.get('type')
    html = ''
    
    if item_type == 'story':
        for sec in item['sections']:
            html += f'''
      <section class="section-group">
        <h2 class="section-subtitle">{sec['subtitle_en']}</h2>
        <p class="section-text">{sec['content_en']}</p>
      </section>'''
            
    elif item_type == 'poem':
        html += '<div class="poem-container">'
        for st in item['stanzas']:
            lines = st['en'].split('\n')
            html += '<div class="poem-stanza">'
            for l in lines:
                html += f'<div class="poem-line">{l}</div>'
            html += '</div>'
        html += '</div>'
        
    elif item_type == 'article':
        for p in item['paragraphs']:
            if p.get('is_quote'):
                quote_paras = p['en'].strip().split('\n\n')
                quote_html = ''.join([f'<p>{qp.strip()}</p>' for qp in quote_paras if qp.strip()])
                html += f'''
      <div class="quote-block">{quote_html}</div>'''
            else:
                html += f'''
      <p class="section-text">{p['en']}</p>'''
                
    elif item_type == 'genealogy':
        for sec in item['sections']:
            html += f'''
      <section class="section-group">
        <h2 class="section-subtitle">{sec['ref_title_en']}</h2>
        <p class="section-text">{sec['content_en']}</p>
      </section>'''
        
    elif item_type == 'donor':
        html += f'''
      <p class="section-text">{item['content_en']}</p>'''
        
    return html

# Generate pure English exhibit pages
for item in items:
    cid = item['id']
    content_en = render_content_en(item)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{item['title_en']}</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <main class="page-container">
    <article class="content-wrapper">
      <h1 class="exhibit-title">{item['title_en']}</h1>
      {content_en}
    </article>
  </main>
</body>
</html>'''

    # Save as page{cid}.html
    with open(f"page{cid}.html", 'w', encoding='utf-8') as f:
        f.write(html)

print("Generated clean English-only exhibit pages (page1~9).")
