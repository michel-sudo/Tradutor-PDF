import pymupdf

doc = pymupdf.open("/home/michel/Git/Tradutor-PDF/files/Artigo01.pdf") # open a document
#out = open("output.txt", "wb") # create a text output
#for page in doc: # iterate the document pages
page = doc[0]
text = (str) (page.get_text().encode("utf8")) # get plain text (is in UTF-8)
#out = text.splitlines()

a = 0
b = 2

line = ""
parChar = ""
textOut = ""

while (b < len(text)):
    parChar = text[a:b] 
    if(parChar != "\n"):
        line += parChar
    else:
        textOut += line + parChar
        line = ""
    a += 2
    b += 2


print(text[0:2])
    #out.write(text) # write text of page
    #out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
#out.close()
