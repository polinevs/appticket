import streamlit as st
from utils.etiquetas import gerar_etiqueta_pdf
import webbrowser
import os

st.set_page_config(page_title="Emision de Etiquetas", layout="centered")

st.title("📦 Emision de Etiquetas - Movil PLUS+")

with st.form("form_etiqueta"):
    st.subheader("Informacion del Producto/Servicio")

    produto = st.text_input("Producto")
    servico = st.text_input("Servicio")
    descricao = st.text_area("Descripcion")
    preco = st.text_input("Precio (€)")
    codigo = st.text_input("Código")

    st.subheader("Informacion Interna")

    funcionario = st.text_input("Funcionário Responsable")

    nota_cliente = st.selectbox(
        "Nota Cliente",
        options=["0", "1", "2", "3", "4", "5"],
        format_func=lambda x: {
            "0": "0 - MUY MALO",
            "1": "1 - MALO",
            "2": "2 - DESCONOCIDO",
            "3": "3 - NORMAL",
            "4": "4 - BUENO",
            "5": "5 - EXCELENTE"
        }[x]
    )

    metodo_pagamento = st.radio("Método de Pago", ["Tarjeta", "Metallico"])

    st.subheader("Logo Empresa")
    logo_path = st.file_uploader("Cargar logo (JPEG/PNG)", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("Generar Etiqueta")

if submitted:
    if not all([produto, servico, descricao, preco, codigo, funcionario]):
        st.warning("Rellene todos los campos obligatórios.")
    else:
        # Se o usuário carregar um novo logo, salvamos temporariamente
        caminho_logo = "assets/logo.jpeg"
        if logo_path:
            with open(caminho_logo, "wb") as f:
                f.write(logo_path.getbuffer())
        else:
            caminho_logo = "assets/logo.jpeg"  # default se não carregar

        caminho_pdf = gerar_etiqueta_pdf(
            produto, servico, descricao, preco, codigo,
            funcionario, nota_cliente, metodo_pagamento,
            logo_path=caminho_logo
        )

        st.success("✅ Etiqueta generada con exito!")
        with open(caminho_pdf, "rb") as f:
            st.download_button("📥 Descargar Etiqueta (PDF)", data=f, file_name="etiqueta.pdf")

        # Botão para imprimir diretamente (abre o PDF no navegador)
        if st.button("🖨️ Imprimir Etiqueta"):
            caminho_absoluto = os.path.abspath(caminho_pdf)

            webbrowser.open(f"file://{caminho_absoluto}")

