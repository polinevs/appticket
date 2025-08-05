from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def gerar_etiqueta_pdf(produto, servico, descricao, preco, codigo,
                       funcionario, nota_cliente, metodo_pagamento,
                       logo_path="utils/logo.jpeg"):

    # Criação de pasta se não existir
    pasta = "etiquetas"
    os.makedirs(pasta, exist_ok=True)

    # Tamanho da etiqueta: 80mm x 100mm (altura maior para evitar cortes)
    largura, altura = 80 * mm, 100 * mm
    nome_arquivo = os.path.join(pasta, "etiqueta_gerada.pdf")
    c = canvas.Canvas(nome_arquivo, pagesize=(largura, altura))

    margem = 10  # margem em mm

    # Inserir logo
    if os.path.exists(logo_path):
        try:
            c.drawImage(logo_path, margem, altura - 25 * mm, width=50 * mm, height=15 * mm, preserveAspectRatio=True)
        except:
            pass  # evita erro caso a imagem não possa ser renderizada

    # Informações da empresa
    y = altura - 30 * mm
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margem, y, "Movil PLus")
    y -= 5
    c.setFont("Helvetica", 7)
    c.drawString(margem, y, "Calle Caracas, 6 - Fraga (Huesca)")
    y -= 10

    # Data e Hora
    data_atual = datetime.now().strftime("%d/%m/%Y")
    hora_atual = datetime.now().strftime("%H:%M")
    c.setFont("Helvetica", 7)
    c.drawString(margem, y, f"Fecha: {data_atual}   Hora: {hora_atual}")
    y -= 10

    # Produto e serviço
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margem, y, f"Producto: {produto}")
    y -= 10
    c.drawString(margem, y, f"Servicio: {servico}")
    y -= 10

    # Descrição
    c.setFont("Helvetica", 7)
    c.drawString(margem, y, "Descripción:")
    y -= 10
    for linha in descricao.split("\n"):
        c.drawString(margem + 5, y, linha[:60])
        y -= 10

    # Preço e código
    c.drawString(margem, y, f"Precio: €{preco}")
    y -= 10
    c.drawString(margem, y, f"Código: {codigo}")
    y -= 10

    # Info adicional
    c.drawString(margem, y, f"Atendido por: {funcionario}")
    y -= 10
    c.drawString(margem, y, f"Nota cliente: {nota_cliente} / Método: {metodo_pagamento}")
    y -= 15

    # Contato
    c.setFont("Helvetica", 6)
    c.drawString(margem, y, "Tel: +34 641 77 68 85  |  Email: movilplusfraga@gmail.com")
    y -= 10

    # Rodapé com mensagens fixas
    c.setFont("Helvetica-Oblique", 5)
    rodape = [
        "*No se admiten devoluciones de productos sin el embalaje original o con marcas de uso*",
        "*No se admiten cambios o devoluciones sin el ticket original*",
        "*Accesorios y móviles rotos o mojados no entran en la garantía*"
    ]
    for msg in rodape:
        c.drawString(margem, y, msg[:90])  # evita ultrapassar largura
        y -= 7

    c.save()
    return nome_arquivo