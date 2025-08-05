# appticket
aplicacion que genera un ticket de servicio personalizado para pequeños negocios locales.
# Sistema de Emissão de Etiquetas para Loja 

Este é um sistema simples de emissão de etiquetas térmicas de 80mm, desenvolvido com **Streamlit** e **ReportLab**, que permite gerar etiquetas personalizadas com dados de serviço, descrição, preço, código, funcionário, nota do cliente e método de pagamento. O sistema também imprime diretamente e insere cabeçalho com logo, informações de contato e mensagens fixas no rodapé.

## Funcionalidades

* Interface web simples para preenchimento de dados
* Impressão de etiquetas em PDF para impressora de 80mm
* Inserção de logo da empresa automaticamente
* Campos adicionais: funcionário, nota do cliente e forma de pagamento
* Rodapé com três mensagens fixas sobre políticas da loja
* Geração automática de arquivos PDF organizados na pasta `/etiquetas`

## Estrutura do Projeto

```
/etiquetas/                 # PDFs gerados serão salvos aqui
/utils/
  etiquetas.py              # Lógica para gerar o PDF da etiqueta
  logo.jpeg                 # Logo da loja usado na etiqueta
app.py                      # Interface principal Streamlit
requirements.txt            # Dependências do projeto
README.md                   # Este arquivo
```

## Instalação Local

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/streamlit-etiquetas.git
cd streamlit-etiquetas
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

## Deploy (Streamlit Cloud)

1. Crie um repositório no GitHub com estes arquivos
2. Acesse [https://share.streamlit.io](https://share.streamlit.io)
3. Conecte sua conta do GitHub e selecione o repositório
4. Escolha `app.py` como arquivo principal
5. Clique em "Deploy"

## Licença

Este projeto é fornecido sob licença MIT. Você pode usá-lo, modificá-lo e revendê-lo como quiser.

## Contato

Para sugestões, melhorias ou consultoria:
**Seu Nome**
[seuemail@dominio.com](mailto:seuemail@dominio.com)
