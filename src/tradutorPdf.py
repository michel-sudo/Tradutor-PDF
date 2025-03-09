import pdfplumber

with pdfplumber.open("/home/michel/Git/Tradutor-PDF/files/Artigo01.pdf") as pdf:
    first_page = pdf.pages[0]
    extractPage = first_page.extract_words()
    textAgroup = ''
    textAgroup2 = ''

    #print(textAgroup)
    print(extractPage)
    #print(extractPage[32]['chars'][0]['size'])
    #print(extractPage[32]['x0'])
    
    #print(first_page.extract_text(layout=False, x_tolerance=1, y_tolerance=2))
    