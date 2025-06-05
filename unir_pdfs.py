from PyPDF2 import PdfMerger

def unir_pdfs(lista_arquivos):
    merger = PdfMerger()
    for pdf in lista_arquivos:
        merger.append(pdf)
    caminho_saida = "/tmp/certidoes_unificadas.pdf"
    merger.write(caminho_saida)
    merger.close()
    return caminho_saida