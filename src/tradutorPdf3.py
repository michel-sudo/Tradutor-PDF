from pypdf import PdfReader

reader = PdfReader("/home/michel/Git/Tradutor-PDF/files/Artigo01.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)
