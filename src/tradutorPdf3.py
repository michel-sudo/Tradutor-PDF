import deepl

input_path = input("Arquivo para tradução: ")
output_path = input("Arquivo de saída: ")

auth_key = "a768d155-308d-4405-bca0-598305f822cc:fx"
translator = deepl.DeepLClient(auth_key)

#input_path = "/home/michel/Git/Tradutor-PDF/files/Artigo01.pdf"
#output_path = "/home/michel/Git/Tradutor-PDF/files/Artigo01Trad.pdf"

translator.translate_document_from_filepath(input_path, output_path, target_lang="PT-BR", formality="more")

