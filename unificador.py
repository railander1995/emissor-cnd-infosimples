from PyPDF2 import PdfMerger

def unificar_certidoes(lista_arquivos, cnpj):
    merger = PdfMerger()
    for pdf in lista_arquivos:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Erro ao unificar {pdf}: {e}")
    destino = f"/tmp/certidoes_unificadas_{cnpj}.pdf"
    merger.write(destino)
    merger.close()
    return destino