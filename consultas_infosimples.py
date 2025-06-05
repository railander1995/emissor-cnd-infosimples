import requests

def consultar_certidao(endpoint, cnpj, api_key, nome_arquivo):
    url = f"https://api.infosimples.com/api/v2/{endpoint}/"
    params = {
        "cnpj": cnpj,
        "token": api_key,
        "timeout": 300,
        "resposta_tipo": "arquivo"
    }
    resposta = requests.get(url, params=params)
    if resposta.status_code == 200:
        caminho = f"/tmp/{nome_arquivo}"
        with open(caminho, "wb") as f:
            f.write(resposta.content)
        return caminho
    return None

def consultar_certidoes(cnpj, api_key):
    arquivos = []
    certidoes = [
        ("receita-federal/certidao-debitos-relativos-tributos-federais", "cnd_receita.pdf"),
        ("trabalhista/certidao-debitos-trabalhistas", "cnd_trabalhista.pdf"),
        ("fgts/regularidade-fgts", "cnd_fgts.pdf"),
        ("estadual/certidao-debitos-estaduais", "cnd_estadual.pdf")
    ]
    for endpoint, nome_arquivo in certidoes:
        pdf = consultar_certidao(endpoint, cnpj, api_key, nome_arquivo)
        if pdf:
            arquivos.append(pdf)
    return arquivos