import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar arquivos
jan = pd.read_excel("arquivos/01-relfatporlinhaveiculoviagem_jan25.xlsx")
fev = pd.read_excel("arquivos/02-relfatporlinhaveiculoviagem_fev25.xlsx")
mar = pd.read_excel("arquivos/03-relfatporlinhaveiculoviagem_mar25.xlsx")
rel = pd.read_csv("arquivos/relveiculos (ABR25).csv", sep=';', encoding='latin1')

# Adicionando a Coluna "Mês" nas 3 tabelas
jan['Mês'] = 'Janeiro'
fev['Mês'] = 'Fevereiro'
mar['Mês'] = 'Março'

# Juntando as tabelas em uma (df)
df = pd.concat([jan, fev, mar], ignore_index=True)

# Definindo colunas relevantes que serão usadas
colunas = [
    'Data Coleta', 'Nome Linha', 'Numero Veículo',
    'Data Hora Início Operação', 'Data Hora Final Operação',
    'Passageiros', 'Passagens', 'Passagens Integração',
    'Total Eletrônico', 'Valor Total Eletrônico', 'Mês'
]

df = df[colunas]

# Definindo a quantidade de viagens com e sem passageiros
def grafico_prop_viagens_semP(df):

    semP = len(df[df['Passageiros'] == 0])
    comP = len(df[df['Passageiros'] > 0])

    valores = [semP, comP]
    labels01 = ['Viagens sem passageiros', 'Viagens com passageiros']

    # Gráfico
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels01, autopct='%1.1f%%', startangle=90,colors=['salmon', 'mediumseagreen'])
    ax.set_title('Proporção de Viagens com e sem Passageiros')
    ax.axis('equal')

    return fig
    
df['Data Hora Início Operação'] = pd.to_datetime(df['Data Hora Início Operação'], errors='coerce')
df['hora_inicio'] = df['Data Hora Início Operação'].dt.hour

# Verificando as linhas com mais viagens vazias
def grafico_top_linhas_vazias(df):
    df_semP = df[df['Passageiros'] == 0]
    top_linhas_vazias = df_semP['Nome Linha'].value_counts().head(10)

    # Gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_linhas_vazias.index, top_linhas_vazias.values, color='red', height=0.4)
    ax.set_title("Top 10 Linhas com Mais Viagens Vazias")
    ax.set_xlabel("Número de viagens com 0 passageiros")
    ax.set_ylabel("Nome Linha")

    return fig

df_semP = df[df['Passageiros'] == 0]
top_linhas_vazias = df_semP['Nome Linha'].value_counts().head(10)
df_semP = df[df['Passageiros'] == 0]

# Verificando essas viagens por horário de início
def grafico_viagens_semP_por_hora(df):
    
    df_semP['Data Hora Início Operação'] = pd.to_datetime(df_semP['Data Hora Início Operação'], errors='coerce')
    viagens_sem_passageiros_por_hora = df_semP['hora_inicio'].value_counts().sort_index()

    # Gráfico
    fig, ax = plt.subplots()
    ax.plot(viagens_sem_passageiros_por_hora.index, viagens_sem_passageiros_por_hora.values, marker='o')
    ax.set_title('Viagens sem Passageiros por Hora de Início')
    ax.set_xlabel("Hora do Dia")
    ax.set_ylabel("Número de Viagens sem Passageiros")
    ax.set_title("Viagens sem Passageiros por Hora de Início")

    return fig

# Verificar a presença de ar condicionado
def grafico_ar_condicionado(rel):
    rel['TEM_AR'] = rel['TIPO VEICULO'].str.contains('C/AR|C/ AR', case=False, na=False)
    Ar = rel.groupby('TEM_AR')['QUANTIDADE VEICULO'].sum()

    valores = [Ar[False], Ar[True]]
    labels02 = ['Sem Ar-Condicionado', 'Com Ar-Condicionado']

    # Gráfico
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels02, autopct='%1.1f%%', startangle=90,colors=['salmon', 'skyblue'])
    ax.set_title('Distribuição da Frota por Ar-Condicionado')
    ax.axis('equal')

    return fig

# Verificando a quantidade de veiculos fabricados até 2015
def grafico_veiculos_antes_2015(rel):
    rel['ANO FAB'] = rel['ANO FAB'].astype(int)
    rel['QUANTIDADE VEICULO'] = rel['QUANTIDADE VEICULO'].astype(int)

    veiculos_antes_2015 = rel[rel['ANO FAB'] <= 2015]['QUANTIDADE VEICULO'].sum()
    veiculos_apos_2015 = rel[rel['ANO FAB'] > 2015]['QUANTIDADE VEICULO'].sum()

    print(f"Veículos fabricados até 2015: {veiculos_antes_2015}")
    print(f"Veículos fabricados a partir de 2016: {veiculos_apos_2015}")

    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(['Fabricados até 2015', 'Fabricados a partir de 2016'], [veiculos_antes_2015, veiculos_apos_2015], color=['salmon', 'mediumseagreen'])
    ax.set_title('Distribuição da Frota por Ano de Fabricação')
    ax.set_ylabel('Quantidade de Veículos')
    return fig


