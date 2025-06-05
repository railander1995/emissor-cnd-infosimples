import streamlit as st
from receita_federal import emitir_cnd_receita_federal
from sefaz_ap import emitir_cnd_sefaz_ap
from fgts_caixa import emitir_crf_fgts
from trabalhista import emitir_cnd_trabalhista
from unificador import unificar_certidoes

st.set_page_config(page_title="CNDs Unificadas", layout="centered")
st.title("📄 Emissão Unificada de Certidões Negativas")

cnpj = st.text_input("Digite o CNPJ da empresa:", max_chars=14)

if st.button("Emitir e Unificar Certidões"):
    if not cnpj:
        st.warning("⚠️ Informe um CNPJ válido.")
    else:
        with st.spinner("Consultando certidões..."):
            token = "J5VHHc9RJgeyTBzeARK43R5A5a8PWXiFDF5OmulT"
            arquivos = []

            rf = emitir_cnd_receita_federal(cnpj, token)
            if rf: arquivos.append(rf)

            estadual = emitir_cnd_sefaz_ap(cnpj, token)
            if estadual: arquivos.append(estadual)

            fgts = emitir_crf_fgts(cnpj, token)
            if fgts: arquivos.append(fgts)

            trab = emitir_cnd_trabalhista(cnpj, token)
            if trab: arquivos.append(trab)

            if arquivos:
                caminho_final = unificar_certidoes(arquivos, cnpj)
                with open(caminho_final, "rb") as f:
                    st.success("✅ Certidões unificadas com sucesso!")
                    st.download_button("📥 Baixar Certidões Unificadas", f, file_name="certidoes_unificadas.pdf")
            else:
                st.error("❌ Nenhuma certidão foi gerada.")