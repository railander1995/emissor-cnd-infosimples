import streamlit as st
import requests
from certidoes.unir_pdfs import unir_pdfs
from certidoes.consultas_infosimples import consultar_certidoes

st.set_page_config(page_title="Emissor de CNDs", layout="centered")
st.title("🔍 Emissor de Certidões Negativas (CND)")

cnpj = st.text_input("Digite o CNPJ (somente números):", max_chars=14)
api_key = st.text_input("Chave da API Infosimples (confidencial):", type="password")

if st.button("Emitir Certidões"):
    with st.spinner("Consultando certidões..."):
        arquivos_pdf = consultar_certidoes(cnpj, api_key)
        if arquivos_pdf:
            caminho_arquivo = unir_pdfs(arquivos_pdf)
            with open(caminho_arquivo, 'rb') as f:
                st.success("✅ Certidões geradas com sucesso!")
                st.download_button("📥 Baixar Certidões em PDF", f, file_name="certidoes_unificadas.pdf")
        else:
            st.error("❌ Não foi possível gerar todas as certidões.")