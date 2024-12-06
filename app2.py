import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
import openpyxl

favicon_path = 'favicon.png'

image_path = 'prio_01.png'

excel_path = r'https://static.vecteezy.com/system/resources/previews/027/179/360/non_2x/microsoft-excel-icon-logo-symbol-free-png.png'

url_destino = "https://www.google.com"

st.set_page_config(page_title="Vendor Weekly Report Subsea", page_icon=favicon_path)

# CSS para remover a barra superior
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}  /* Esconde o menu de hambúrguer */
footer {visibility: hidden;}     /* Esconde o rodapé */
header {visibility: hidden;}     /* Esconde o cabeçalho */
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('Vendor Weekly Report Subsea')

st.logo(image_path, size='large', link=None, icon_image=None)

st.sidebar.title('Modelo de reporte:')

st.sidebar.text('''Explicar processo, como funciona para adicionar uma nova PO ou contrato.
Modelo de atualização, página de links e etc 
                
Essa versão é apenas uma versão inicial de testes, não deve ser incluída nela dados reais.''',)

df_comercial = pd.read_excel('Dados mock comercial.xlsx', index_col=None).reset_index(drop=True)
df_comercial = df_comercial.set_index('Item')

if "show_comercial" not in st.session_state:
    st.session_state["show_comercial"] = False
    # login = False
    show_comercial = False
if st.session_state["show_comercial"] == True:
    show_comercial = True

if "show_propostas" not in st.session_state:
    st.session_state["show_propostas"] = False
    # login = False
    show_propostas = False
if st.session_state["show_propostas"] == True:
    show_propostas = True

if "show_pagamento" not in st.session_state:
    st.session_state["show_pagamento"] = False
    # login = False
    show_pagamento = False
if st.session_state["show_pagamento"] == True:
    show_pagamento = True

if "show_engenharia" not in st.session_state:
    st.session_state["show_engenharia"] = False
    # login = False
    show_engenharia = False
if st.session_state["show_engenharia"] == True:
    show_engenharia = True


if "show_schedule" not in st.session_state:
    st.session_state["show_schedule"] = False
    # login = False
    show_schedule = False
if st.session_state["show_schedule"] == True:
    show_schedule = True


if "show_abas" not in st.session_state:
    st.session_state["show_abas"] = False
    # login = False
    show_abas = False
else:
    show_abas = True
if "show_preencher_comercial" not in st.session_state:
    st.session_state["show_preencher_comercial"] = False
    # login = False
    show_preencher_comercial = False

# Função de autenticação
def autenticar_usuario(username, password):
    # Exemplo de validação simples (substitua por lógica mais segura, como validação em banco de dados)
    credenciais_validas = {
        "admin": "Luis",  # Username: senha
        "teste@prio3.com.br": "@Prio2024"
    }
    return credenciais_validas.get(username) == password

# Interface de login
def tela_login():
    st.title("Login")
    
    # Formulário de login
    with st.form("login_form"):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submit_button = st.form_submit_button("Entrar")
    
    if submit_button:
        if autenticar_usuario(username, password):
            st.success("Login realizado com sucesso!")
            st.session_state["logged_in"] = True
        else:
            st.error("Usuário ou senha inválidos.")

# Tela inicial após login
def tela_inicial():
    if st.button("Sair"):
        st.session_state["logged_in"] = False
        st.session_state["show_comercial"] = False
        st.session_state["show_propostas"] = False
        st.session_state["show_pagamento"] = False
        st.session_state["show_engenharia"] = False
        st.session_state["show_schedule"] = False

def show_comercial():
    st.session_state["show_menu"] = True
    st.session_state["show_comercial"] = True
    st.session_state["show_propostas"] = False
    st.session_state["show_pagamento"] = False
    st.session_state["show_engenharia"] = False
    st.session_state["show_schedule"] = False
    show_comercial = True
    show_propostas = False
    show_pagamento = False
    show_engenharia = False
    show_schedule = False
    return show_comercial, show_propostas, show_pagamento, show_engenharia, show_schedule

def show_propostas():
    st.session_state["show_menu"] = True
    st.session_state["show_comercial"] = False
    st.session_state["show_propostas"] = True
    st.session_state["show_pagamento"] = False
    st.session_state["show_engenharia"] = False
    st.session_state["show_schedule"] = False
    show_comercial = False
    show_propostas = True
    show_pagamento = False
    show_engenharia = False
    show_schedule = False
    return show_comercial, show_propostas, show_pagamento, show_engenharia, show_schedule

def show_pagamento():
    st.session_state["show_menu"] = True
    st.session_state["show_comercial"] = False
    st.session_state["show_propostas"] = False
    st.session_state["show_pagamento"] = True
    st.session_state["show_engenharia"] = False
    st.session_state["show_schedule"] = False
    show_comercial = False
    show_propostas = False
    show_pagamento = True
    show_engenharia = False
    show_schedule = False
    return show_comercial, show_propostas, show_pagamento, show_engenharia, show_schedule

def show_engenharia():
    st.session_state["show_menu"] = True
    st.session_state["show_comercial"] = False
    st.session_state["show_propostas"] = False
    st.session_state["show_pagamento"] = False
    st.session_state["show_engenharia"] = True
    st.session_state["show_schedule"] = False
    show_comercial = False
    show_propostas = False
    show_pagamento = False
    show_engenharia = True
    show_schedule = False
    return show_comercial, show_propostas, show_pagamento, show_engenharia, show_schedule


def show_schedule():
    st.session_state["show_menu"] = True
    st.session_state["show_comercial"] = False
    st.session_state["show_propostas"] = False
    st.session_state["show_pagamento"] = False
    st.session_state["show_engenharia"] = False
    st.session_state["show_schedule"] = True
    show_comercial = False
    show_propostas = False
    show_pagamento = False
    show_engenharia = False
    show_schedule = True
    return show_comercial, show_propostas, show_pagamento, show_engenharia, show_schedule

def hide_comercial_table():
    st.session_state["show_comercial"] = False
    st.session_state["show_preencher_comercial"] = True
    show_comercial = False
    show_preencher_comercial = True
    return show_preencher_comercial, show_comercial



# Configuração inicial
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Comercial"):
            show_comercial()

    with col2:
        if st.button("Propostas"):
            show_propostas()

    with col3:
        if st.button("Pagamento"):
            show_pagamento()

    with col4:
        if st.button("Engenharia"):
            show_engenharia()

    with col5:
        if st.button("Schedule update"):
            show_schedule()
    
    tela_inicial()
else:
    tela_login()



if show_comercial and st.session_state["show_comercial"] == True:
    st.subheader("Comercial")
    st.table(df_comercial)

    st.markdown("##### Existe alguma ordem que não está acima:")

    # Criar colunas para os botões
    col1, col2 = st.columns(2)

    

    with col1:
        if st.button("Sim"):
            hide_comercial_table()

    with col2:
        if st.button("Não"):
            st.success("Registro Adicionado!")

if show_propostas and st.session_state["show_propostas"] == True:
    st.subheader("Propostas")
    conexao = sqlite3.connect('dados.db')
    # Carregar a tabela em um DataFrame
    query = "SELECT * FROM propostas"
    df_pagamentos = pd.read_sql_query(query, conexao).reset_index(drop=True)
    st.markdown("##### Minhas propostas:")
    st.dataframe(df_pagamentos)
    with st.form(key='proposta_new'):
        ctr = st.text_input(label='CTR/FCTR')
        # Criando uma lista de opções
        opcoes = ["Opção 1", "Opção 2", "Opção 3"]

        # Criando o dropdown
        situation = st.selectbox("Situação", opcoes)
        acao = st.text_input(label='Ação')
        status = st.text_input(label='Status')
        escopo = st.text_input(label='Escopo')
        resp_prio = st.text_input(label='Responsável PRIO')
        vencimento = st.date_input(
                    "Vencimento",
                    datetime.now().date(),
                      format="DD/MM/YYYY"  # Valor padrão: data atual
                )
        valor = st.text_input(label='Valor')
        input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO propostas (ctr, situacao, acao, status, escopo, resp_prio, vencimento, valor, user) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctr, situation, acao, status, escopo, resp_prio, vencimento, valor, 'teste@prio3.com.br'))
                conn.commit()
                st.success('Formulário enviado com sucesso!')
                df_pagamentos = pd.read_sql_query(query, conexao).reset_index(drop=True)
            except sqlite3.IntegrityError:
                print("Erro: Usuário já existe.")
                st.error("Erro no envio, tente novamente!")
            finally:
                conn.close()
    st.markdown("##### Possui atualização da última semana?")

    # Criar colunas para os botões
    col1, col2 = st.columns(2)



    with col1:
        if st.button("Sim"):
            st.success("Registro adicionado!")

    with col2:
        if st.button("Não"):
            st.success("Registro Adicionado!")
    


if show_pagamento and st.session_state["show_pagamento"] == True:
    st.subheader("Pagamento")
    conexao = sqlite3.connect('dados.db')
    # Carregar a tabela em um DataFrame
    query = "SELECT * FROM pagamentos"
    df_pagamentos = pd.read_sql_query(query, conexao).reset_index(drop=True)
    st.markdown("##### Meus pagamentos:")
    st.dataframe(df_pagamentos)
    with st.form(key='pagamento_new'):
        id_po = st.text_input(label='ID do PO ou contrato')
        vencimento = st.date_input(
                    "Vencimento",
                    datetime.now().date(),
                      format="DD/MM/YYYY"  # Valor padrão: data atual
                )
        # Criando uma lista de opções
        opcoes = ["Opção 1", "Opção 2", "Opção 3"]

        # Criando o dropdown
        status = st.selectbox("Status", opcoes)
        nf_invoice = st.text_input(label='NF/Invoice ou não')
        valor = st.text_input(label='Valor')
        tipo_servico = st.selectbox("Tipo de serviço", opcoes)
        num_parcela = st.text_input(label='Número da parcela')
        
        input_button_submit = st.form_submit_button('Enviar')

        if input_button_submit:
            conn = sqlite3.connect('dados.db')
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO pagamentos (po, vencimento, status, nf, valor, tipo_servico, num_parcela) VALUES (?, ?, ?, ?, ?, ?, ?)", (id_po, vencimento, status, nf_invoice, valor, tipo_servico, num_parcela))
                conn.commit()
                st.success('Formulário enviado com sucesso!')
                df_pagamentos = pd.read_sql_query(query, conexao).reset_index(drop=True)
            except sqlite3.IntegrityError:
                print("Erro: Usuário já existe.")
                st.error("Erro no envio, tente novamente!")
            finally:
                conn.close()

    # st.button("Colocar nova linha")
    st.markdown("##### Possui atualização da última semana?")

    # Criar colunas para os botões
    col1, col2 = st.columns(2)



    with col1:
        if st.button("Sim"):
            pass

    with col2:
        if st.button("Não"):
            st.success("Registro Adicionado!")


if show_engenharia and st.session_state["show_engenharia"] == True:
    st.subheader("Engenharia")

    conexao = sqlite3.connect('dados.db')
    query = "SELECT * FROM duvidas"
    df_duvidas = pd.read_sql_query(query, conexao).reset_index(drop=True)
    st.markdown("##### Minhas dúvidas:")
    st.dataframe(df_duvidas)

    st.text("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("##### ")
        st.markdown("##### Consultas e dúvidas técnicas")


    with col2:
        st.markdown("##### Modelo padrão")
        # Renderiza a imagem clicável
        st.markdown(
            f"""
            <a href="{url_destino}" target="_blank">
                <img src="{excel_path}" alt="Arquivo Excel" style="width:300px;"/>
            </a>
            """,
            unsafe_allow_html=True
        )


    with col3:
        st.markdown("##### Upload")
        uploaded_file = st.file_uploader("Faça o upload do arquivo", type=["xlsx"])
        if uploaded_file is not None:
            workbook = openpyxl.load_workbook(uploaded_file)
            sheet = workbook.active
            celula = sheet["XFD1"]
            if celula.value == 10:
                df_duvidas = pd.read_excel(uploaded_file)
                for i, row in df_duvidas.iterrows():
                    conn = sqlite3.connect('dados.db')
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO duvidas (po, num_tq, assunto, classificacao, tipo, prioridade, impacto, resp_prio, comentarios) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (row['PO'], row['N° TQ'], row['Assunto'], row['Classificação'], row['Tipo'], row['Prioridade'], row['Impacto'], row['Responsável prio'], row['Comentários']))
                        conn.commit()
                    except sqlite3.IntegrityError:
                        print("Erro: Usuário já existe.")
                        st.error("Erro no envio, tente novamente!")
                    finally:
                        conn.close()
            else:
                st.error("Esse não é o arquivo modelo para o envio de dúvidas!")
        else:
            st.info("Aguardando o upload de um arquivo Excel.")

    with col4:
        st.markdown("##### Possui atualização da última semana?")
        # Criar colunas para os botões
        col1, col2 = st.columns(2)



        with col1:
            if st.button("Sim"):
                pass

        with col2:
            if st.button("Não"):
                st.success("Registro Adicionado!")

if show_schedule and st.session_state["show_schedule"] == True:
    st.subheader("Schedule Update")

    conexao = sqlite3.connect('dados.db')
    query = "SELECT * FROM schedule"
    df_schedule = pd.read_sql_query(query, conexao).reset_index(drop=True)
    st.markdown("##### Schedule:")
    st.dataframe(df_schedule)

    st.text("")

    st.markdown("### Upload por planilha")

    col1, col2 = st.columns(2)


    with col1:
        st.markdown("##### Modelo padrão")
        # Renderiza a imagem clicável
        st.markdown(
            f"""
            <a href="{url_destino}" target="_blank">
                <img src="{excel_path}" alt="Arquivo Excel" style="width:300px;"/>
            </a>
            """,
            unsafe_allow_html=True
        )


    with col2:
        st.markdown("##### Upload")
        uploaded_file = st.file_uploader("Faça o upload do arquivo", type=["xlsx"])
        if uploaded_file is not None:
            workbook = openpyxl.load_workbook(uploaded_file)
            sheet = workbook.active
            celula = sheet["XFD1"]
            if celula.value == 50:
                df_duvidas = pd.read_excel(uploaded_file)
                for i, row in df_duvidas.iterrows():
                    conn = sqlite3.connect('dados.db')
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO schedule (po, linha, atividade, progresso_planejado, progresso_realizado, comentario, localizacao, dimensao, peso, incoterm, ncm, entrega_planejada, entrega_esperada, valor_envio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row['PO'], row['Linha'], row['Atividade'], row['Progresso planejado'], row['Progresso Realizado'], row['Comentário'], row['Localização'], row['Dimensão'], row['Peso'], row['Incoterm'], row['NCM'], row['Entrega planejada'], row['Entrega esperada'], row['Valor do envio']))
                        conn.commit()
                    except sqlite3.IntegrityError:
                        print("Erro: Usuário já existe.")
                        st.error("Erro no envio, tente novamente!")
                    finally:
                        conn.close()
            else:
                st.error("Esse não é o arquivo modelo para o envio de dúvidas!")
        else:
            st.info("Aguardando o upload de um arquivo Excel.")

    st.text("")
    st.text("")

    st.markdown("##### Possui atualização da última semana?")
    # Criar colunas para os botões
    col1, col2 = st.columns(2)



    with col1:
        if st.button("Sim"):
            pass

    with col2:
        if st.button("Não"):
            st.success("Registro Adicionado!")