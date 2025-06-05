import streamlit as st
from receita_federal import emitir_cnd_receita_federal

st.set_page_config(page_title="CND Receita Federal", layout="centered")
st.title("🔍 Emitir Certidão da Receita Federal (PGFN)")

cnpj = st.text_input("Digite o CNPJ da empresa (somente números):", max_chars=14)

if st.button("Emitir CND Receita Federal"):
    if not cnpj:
        st.warning("⚠️ Informe um CNPJ válido.")
    else:
        with st.spinner("Consultando a Receita Federal..."):
            token = "J5VHHc9RJgeyTBzeARK43R5A5a8PWXiFDF5OmulT"
            caminho_pdf = emitir_cnd_receita_federal(cnpj, token)
            if caminho_pdf:
                with open(caminho_pdf, "rb") as f:
                    st.success("✅ Certidão gerada com sucesso!")
                    st.download_button("📥 Baixar Certidão", f, file_name="cnd_receita_federal.pdf")
            else:
                st.error("❌ Não foi possível gerar a certidão. Verifique o CNPJ ou o token.")