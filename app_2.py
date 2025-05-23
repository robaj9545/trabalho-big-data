import streamlit as st
import analise_dados as ad
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(
    page_title="Ônibus de Teresina",
    page_icon="🚌",
    layout="centered"
)

# Título geral 
st.markdown("""
    <h1 style='text-align: center; color: #1F4E79;'>Análise do Transporte Coletivo de Teresina</h1>
    <hr style='border: 1px solid #ccc;'>
""", unsafe_allow_html=True)

# Viagens com e sem passageiros 
st.markdown("### Proporção de Viagens com e sem Passageiros", unsafe_allow_html=True)
fig1 = ad.grafico_prop_viagens_semP(ad.df)
st.pyplot(fig1)

# Top 10 linhas com viagens vazias
st.markdown("### Top 10 Linhas com Mais Viagens Vazias", unsafe_allow_html=True)
fig2 = ad.grafico_top_linhas_vazias(ad.df)
st.pyplot(fig2)

# Horários de viagens vazias 
st.markdown("### Viagens sem Passageiros por Hora de Início", unsafe_allow_html=True)
fig3 = ad.grafico_viagens_semP_por_hora(ad.df)
st.pyplot(fig3)

# Ar condicionado 
st.markdown("### Presença de Ar Condicionado", unsafe_allow_html=True)
fig4 = ad.grafico_ar_condicionado(ad.rel)
st.pyplot(fig4)

# Ano de fabricação 
st.markdown("### Veículos Fabricados até 2015", unsafe_allow_html=True)
fig5 = ad.grafico_veiculos_antes_2015(ad.rel)
st.pyplot(fig5)

# Rodapé 
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 0.9em; color: gray;'>
        Projeto acadêmico de Big Data - Transporte Público de Teresina
    </p>
""", unsafe_allow_html=True) 
