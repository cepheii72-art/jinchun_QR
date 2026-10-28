import os
import json
import fitz
import docx

# 1. Inspect PDF detailed text and layout
with open('pdf_extracted.json', 'r', encoding='utf-8') as f:
    pdf_data = json.load(f)

with open('pdf_text_dump.txt', 'w', encoding='utf-8') as f:
    for page in pdf_data['pages']:
        f.write(f"==================== PAGE {page['page']} ====================\n")
        f.write(page['text'])
        f.write("\n\n")

print("PDF text dumped to pdf_text_dump.txt")

# 2. Inspect Word file if exists
src_dir = os.path.abspath(os.path.join(os.getcwd(), '..', 'data', 'QR웹페이지'))
for fname in os.listdir(src_dir):
    if fname.endswith('.docx'):
        doc_path = os.path.join(src_dir, fname)
        doc = docx.Document(doc_path)
        with open('docx_text_dump.txt', 'w', encoding='utf-8') as f:
            for p in doc.paragraphs:
                if p.text.strip():
                    f.write(p.text + "\n")
            for table in doc.tables:
                for row in table.rows:
                    row_text = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
                    f.write(" | ".join(row_text) + "\n")
        print(f"Docx {fname} dumped to docx_text_dump.txt")
