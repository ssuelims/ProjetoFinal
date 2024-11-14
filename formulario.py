import streamlit as st
import pandas as pd
from ai import predict, accuracia




# Definir o título
st.set_page_config(page_title="Formulário de Pesquisa", page_icon="📝", layout="wide")

# Título principal do formulário
st.title("Formulário de Pesquisa de Bem-estar no Trabalho")

# Seção de dados pessoais
st.header("🔹 Dados Pessoais")
col1, col2 = st.columns(2)
with col1:
    idade = st.number_input("Qual a sua idade?", min_value=0, max_value=120)
    genero = st.radio("Qual o seu gênero?", ['Masculino', 'Feminino', 'Outro', 'Prefiro não dizer'])
with col2:
    trabalha = st.radio("Você trabalha?", ['Sim', 'Não'])
    forma_trabalho = st.selectbox("Qual a sua forma de trabalho?", ['Presencial', 'Remoto', 'Híbrido'])

# Seção de trabalho e horários
st.header("🔹 Informações sobre o Trabalho")
col1, col2 = st.columns(2)
with col1:
    horas_trabalho = st.number_input("Quantas horas você trabalha por dia?", min_value=0, max_value=24)
    anos_trabalho = st.number_input("A quantos anos você trabalha?", min_value=0)
with col2:
    reunioes_mes = st.number_input("Quantas reuniões você costuma ter no mês?", min_value=0)
    setor_trabalho = st.selectbox("Qual o setor do seu trabalho?",['Área de atendimento','não trabalho','Área de TI','Área serviço público','Área de Educação'
    ,'Área de saúde','Área de logística','Área administrativa','Área de comércio'])

# Seção de satisfação e equilíbrio
st.header("🔹 Satisfação e Bem-estar")
col1, col2 = st.columns(2)
with col1:
    satisfacao = st.slider("Qual o seu nível de satisfação com o seu emprego?", 0, 5, 2)
    balanceamento_trabalho = st.slider("Qual o balanceamento do seu trabalho com a sua vida pessoal?", 0, 5, 2)
    nivel_educacao = st.selectbox("Qual o seu nível de educação?", ['Estou cursando a faculdade', 'Já Finalizei a faculdade',
       'Não finalizei o ensino medio', 'Estou cursando o ensino medio',
       'Já finalizei o Ensino Medio', 'Não finalizei o ensino fudamental'
       ])
with col2:
    atividade_fisica = st.radio("Você realiza atividades físicas frequentemente?", ['Sim', 'Não'])
    nivel_stresse = st.slider("Qual o seu nível de stresse em uma semana?", 0, 5, 2)
    acesso_saude_mental = st.radio("Você tem um acesso fácil a recursos de saúde mental?", ['Sim', 'Não'])

# Seção de socialização e saúde
st.header("🔹 Socialização e Saúde")
col1, col2 = st.columns(2)
with col1:
    saidas_amigos = st.number_input("Quantas vezes em uma semana você costuma sair com amigos?", min_value=0)
    qualidade_sono = st.slider("Qual a qualidade de seu sono normalmente?", 0, 5, 2)
with col2:
    relacao_familia = st.slider("Como é a sua relação com sua família?", 0, 5, 2)
    problemas_mentais = st.radio("Você se identifica ou já se identificou com problemas mentais?", ['Sim', 'Não'])

# Botão para enviar o formulário

# Exibição de agradecimento ao final

# Organizando os dados para a previsão
resposta_do_formulario = {
    'Qual a sua idade': idade,
    'Quantas horas você trabalha por dia?': horas_trabalho,
    'A quantos anos você trabalha?': anos_trabalho,
    'Qual o seu nivel de satisfação com o seu emprego?': satisfacao,
    'Qual o balanceamento do seu trabalho com a sua vida pessoal?': balanceamento_trabalho,
    'Qual o seu gênero_Masculino': 1 if genero == 'Masculino' else 0,
    'Qual o seu gênero_Prefiro não dizer': 1 if genero == 'Prefiro não dizer' else 0,
    'Você trabalha?_Sim': 1 if trabalha == 'Sim' else 0,
    'Qual a sua forma de trabalho?_Presencial': 1 if forma_trabalho == 'Presencial' else 0,
    'Qual a sua forma de trabalho?_Remoto': 1 if forma_trabalho == 'Remoto' else 0,
    'Qual a sua forma de trabalho?_não trabalho': 1 if forma_trabalho == 'não trabalho' else 0,
    'Quantas reuniões você costuma ter no mês?_3 ou mais reuniões': 1 if reunioes_mes >= 3 else 0,
    'Quantas reuniões você costuma ter no mês?_3 ou mias reuniões': 1 if reunioes_mes == 3 else 0,
    'Quantas reuniões você costuma ter no mês?_Normalmente não há reuniões': 1 if reunioes_mes == 0 else 0,
    'Qual o setor do seu trabalho?_Área administrativa': 1 if setor_trabalho == 'Área administrativa' else 0,
    'Qual o setor do seu trabalho?_Área de Educação': 1 if setor_trabalho == 'Área de Educação' else 0,
    'Qual o setor do seu trabalho?_Área de TI': 1 if setor_trabalho == 'Área de TI' else 0,
    'Qual o setor do seu trabalho?_Área de atendimento': 1 if setor_trabalho == 'Área de atendimento' else 0,
    'Qual o setor do seu trabalho?_Área de comércio': 1 if setor_trabalho == 'Área de comércio' else 0,
    'Qual o setor do seu trabalho?_Área de logística': 1 if setor_trabalho == 'Área de logística' else 0,
    'Qual o setor do seu trabalho?_Área de saúde': 1 if setor_trabalho == 'Área de saúde' else 0,
    'Qual o setor do seu trabalho?_Área serviço público': 1 if setor_trabalho == 'Área serviço público' else 0,
    'Qual o seu nivel de educação?_Estou cursando o ensino medio': 1 if nivel_educacao == 'Estou cursando o ensino medio' else 0,
    'Qual o seu nivel de educação?_Já Finalizei a faculdade': 1 if nivel_educacao == 'Já Finalizei a faculdade' else 0,
    'Qual o seu nivel de educação?_Já finalizei o Ensino Medio': 1 if nivel_educacao == 'Já finalizei o Ensino Medio' else 0,
    'Qual o seu nivel de educação?_Não finalizei o ensino fudamental': 1 if nivel_educacao == 'Não finalizei o ensino fudamental' else 0,
    'Qual o seu nivel de educação?_Não finalizei o ensino medio': 1 if nivel_educacao == 'Não finalizei o ensino medio' else 0,
    'Você realiza atividades físicas frequentemente?_Sim': 1 if atividade_fisica == 'Sim' else 0,
    'Qual o seu nivel de stresse em uma semana?_Baixo': 1 if nivel_stresse == 0 else 0,
    'Qual o seu nivel de stresse em uma semana?_Medio': 1 if nivel_stresse == 2 else 0,
    'Você tem um acesso facil a recursos de saude mental?_Sim': 1 if acesso_saude_mental == 'Sim' else 0,
    'Quantas vezes em uma semana você costuma sair com amigos?_3 vezes ou mais': 1 if saidas_amigos >= 3 else 0,
    'Quantas vezes em uma semana você costuma sair com amigos?_Não costumo sair em grupo': 1 if saidas_amigos == 0 else 0,
    'Qual a qualidade de seu sono normalmente?_Mediana': 1 if qualidade_sono == 2 else 0,
    'Qual a qualidade de seu sono normalmente?_Ruim': 1 if qualidade_sono == 1 else 0,
    'Como é a sua relação com sua familia_Excelente': 1 if relacao_familia == 5 else 0,
    'Como é a sua relação com sua familia_Normal': 1 if relacao_familia == 3 else 0,
    'Como é a sua relação com sua familia_Pessima': 1 if relacao_familia == 0 else 0,
    'Como é a sua relação com sua familia_Ruim': 1 if relacao_familia == 1 else 0,
}

# Botão para enviar o formulário
st.markdown("---")
if st.button("Enviar Respostas"):
    st.subheader("🔍 Dados Enviados")

    # Realizando a previsão
    previsao = predict(pd.DataFrame([resposta_do_formulario]))  # Passando as respostas no formato DataFrame
    st.markdown("---")
    
    # Mapeando a previsão para as categorias
    classes_map = {
        'Ansiedade': 'Ansiedade',
        'Depressão': 'Depressão',
        'Nunca percebi nenhum problema': 'Nunca percebi nenhum problema',
        'Burnout': 'Burnout',
    }

    previsao_categoria = classes_map.get(previsao[0], "Erro na previsão")

    st.success(f"A previsão sobre problemas mentais é: {previsao_categoria}")


