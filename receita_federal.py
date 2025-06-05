import requests

def emitir_cnd_receita_federal(cnpj, token):
    url = "https://api.infosimples.com/api/v2/receita-federal/pgfn/"
    params = {
        "cnpj": cnpj,
        "token": token,
        "timeout": 300,
        "resposta_tipo": "arquivo"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
        caminho_pdf = f"/tmp/cnd_receita_federal_{cnpj}.pdf"
        with open(caminho_pdf, "wb") as f:
            f.write(response.content)
        return caminho_pdf
    else:
        print("Erro:", response.status_code, response.text)
        return None