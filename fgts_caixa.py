import requests

def emitir_crf_fgts(cnpj, token):
    url = "https://api.infosimples.com/api/v2/caixa/regularidade/"
    params = {
        "cnpj": cnpj, "token": token,
        "timeout": 300, "resposta_tipo": "arquivo"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
        path = f"/tmp/crf_fgts_{cnpj}.pdf"
        with open(path, "wb") as f:
            f.write(response.content)
        return path
    return None