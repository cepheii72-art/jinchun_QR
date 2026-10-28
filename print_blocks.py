import sys
sys.stdout.reconfigure(encoding='utf-8')
import json

with open('pages_detail.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    print(f"*** PAGE {p['page']} (w={p['width']}, h={p['height']}) ***")
    for b in p['blocks']:
        txt = b['text'].replace('\n', ' // ')
        print(f"  [{b['bbox'][0]:.1f}, {b['bbox'][1]:.1f}] : {txt}")
    print()
