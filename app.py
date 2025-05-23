import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import analise_dados as ad

# Configuração da página
st.set_page_config(
    page_title="Análise do Transporte Público (Ônibus) de Teresina",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado com animações e transições suaves
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background-color: #F9FAFB;
    }

    /* TITLES */
    .main-title {
        font-size: 100px;
        font-weight: 1500;
        color: #0F172A;
        background: linear-gradient(to right, #93C5FD, #60A5FA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 30px 0 20px;
        animation: fadeIn 1s ease-in-out;
    }

    .subtitle {
        color: #3B82F6;
        font-size: 20px;
        font-weight: 400;
        text-align: center;
        margin-bottom: 40px;
        opacity: 0.85;
        animation: fadeIn 1.5s ease-in-out;
    }

    .section-title {
        font-size: 30px;
        font-weight: 700;
        color: #1E3A8A;
        background-color: #EFF6FF;
        border-left: 6px solid #2563EB;
        padding: 15px 20px;
        border-radius: 10px;
        margin-top: 40px;
        animation: slideInLeft 0.5s ease;
    }

    /* CARDS */
    .metric-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 30px 20px;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease-in-out;
        animation: fadeInUp 0.5s ease forwards;
    }

    .metric-card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 25px rgba(0,0,0,0.15);
    }

    .metric-icon {
        font-size: 36px;
        color: #3B82F6;
        margin-bottom: 15px;
    }

    .metric-value {
        font-size: 40px;
        font-weight: 900;
        color: #1E3A8A;
    }

    .metric-label {
        font-size: 16px;
        font-weight: 500;
        color: #6B7280;
        margin-top: 5px;
    }

    /* BOXES */
    .problem-box, .solution-box, .insight-box {
        padding: 25px;
        margin-bottom: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        animation: fadeInUp 0.5s ease;
        border-left: 6px solid;
    }

    .problem-box {
        background: #FFF1F2;
        color: #7F1D1D;
        border-color: #EF4444;
    }

    .solution-box {
        background: #ECFDF5;
        color: #065F46;
        border-color: #10B981;
    }

    .insight-box {
        background: #EFF6FF;
        color: #1E40AF;
        border-color: #3B82F6;
    }

    /* TABLES */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
    }

    .styled-table thead {
        background-color: #2563EB;
        color: #FFFFFF;
        font-weight: 700;
    }

    .styled-table th, .styled-table td {
        padding: 16px;
        text-align: left;
        font-size: 15px;
    }

    .styled-table tbody tr {
        border-bottom: 1px solid #E5E7EB;
    }

    .styled-table tbody tr:nth-child(even) {
        background-color: #F9FAFB;
    }

    .styled-table tbody tr:hover {
        background-color: #E0F2FE;
    }

    /* CHARTS */
    .chart-container {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        animation: fadeInUp 0.6s ease;
    }

    .chart-title {
        font-size: 20px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 15px;
        text-align: center;
    }

    /* TIMELINE */
    .timeline-item {
        position: relative;
        padding-left: 25px;
        margin-bottom: 25px;
        border-left: 4px solid #3B82F6;
    }

    .timeline-item:before {
        content: "";
        position: absolute;
        left: -9px;
        top: 0;
        width: 18px;
        height: 18px;
        background-color: #3B82F6;
        border-radius: 50%;
    }

    .timeline-title {
        font-weight: 700;
        color: #1D4ED8;
        margin-bottom: 8px;
    }

    /* RECOMMENDATION CARDS */
    .recommendation-card {
        background-color: #FFFFFF;
        border-top: 5px solid #3B82F6;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        animation: fadeIn 0.7s ease;
    }

    .recommendation-title {
        font-size: 18px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 10px;
    }

    /* FOOTER */
    .footer {
        text-align: center;
        color: #9CA3AF;
        font-size: 14px;
        padding: 20px;
        margin-top: 40px;
        border-top: 1px solid #E5E7EB;
        animation: fadeIn 1s ease;
    }

    /* ANIMAÇÕES */
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    @keyframes fadeInUp {
        0% {opacity: 0; transform: translateY(20px);}
        100% {opacity: 1; transform: translateY(0);}
    }

    @keyframes slideInLeft {
        0% {opacity: 0; transform: translateX(-30px);}
        100% {opacity: 1; transform: translateX(0);}
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<p style="font-size:30px;" class="main-title">Análise do Sistema de Transporte Público (Ônibus) de Teresina</p>', unsafe_allow_html=True)


# Introdução
st.markdown("""
Esta análise examina o sistema de Transporte Público (Ônibus) de Teresina, com foco em 
eficiência operacional, qualidade do serviço e uso de recursos. O estudo utiliza dados de 
janeiro a abril de 2025, identificando problemas críticos e propondo soluções viáveis.
""")

# Sidebar com menu expandido
with st.sidebar:

    st.image("bus_2.jpg", use_container_width=True)

    with st.expander("🧭 Navegação", expanded=True):
        navigation = st.radio("Selecione uma seção:", 
            ["Visão Geral", 
             "Problema 1: Viagens Vazias", 
             "Problema 2: Frota Antiga", 
             "Problema 3: Conforto Térmico", 
             "Recomendações"]
        )

    with st.expander("ℹ️ Sobre o Projeto", expanded=False):
        st.markdown("**Projeto de Tópicos em Big Data**")
        st.markdown("**Tema:** Transporte Público (Ônibus) em Teresina")
        st.markdown("**Período analisado:** Janeiro a Abril de 2025")
        st.markdown("**Foco:** Eficiência operacional e qualidade do serviço")
        st.markdown("**Discentes:** Roberto Marques Araújo - 201909000973, Rodrigo de Sepulvida Sousa - 202308416901, Tayanny Rojecy Pereira Sousa - 202502313764, Herick Ruan Silva Viana - 202304276471")
        st.markdown("**Fonte:** Dados públicos obtido através do Processo Administrativo Nº 00077.007***/2025-50 destinado a STRANS no SEI (Sistema Eletrônico de Informações) da Prefeitura Municipal de Teresina, usando a Lei nº 12.527/2011 de Acesso à Informação.")
        

# Métricas principais
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><p class="metric-value">24.7%</p><p class="metric-label">Viagens sem passageiros</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><p class="metric-value">69.1%</p><p class="metric-label">Frota sem ar-condicionado</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><p class="metric-value">~83%</p><p class="metric-label">Veículos fabricados até 2015</p></div>', unsafe_allow_html=True)

st.markdown('')

# Função de navegação
def show_section(section):
    return navigation == section

# As seções abaixo permanecem conforme seu script original
# --- Visão Geral
if show_section("Visão Geral"):
    st.markdown('<p class="section-title">Visão Geral</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        # Viagens com e sem passageiros 
        #st.markdown("### Proporção de Viagens com e sem Passageiros", unsafe_allow_html=True)
        fig1 = ad.grafico_prop_viagens_semP(ad.df)
        st.pyplot(fig1)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> Quase 1/4 das viagens (24,7%) ocorrem sem nenhum passageiro, 
        representando um desperdício significativo de recursos operacionais.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        
        # Ar condicionado 
        #st.markdown("### Presença de Ar Condicionado", unsafe_allow_html=True)
        fig4 = ad.grafico_ar_condicionado(ad.rel)
        st.pyplot(fig4)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> Apenas 30,9% da frota possui ar-condicionado, comprometendo 
        o conforto dos passageiros no clima quente de Teresina.
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        
        # Horários de viagens vazias 
        #st.markdown("### Viagens sem Passageiros por Hora de Início", unsafe_allow_html=True)
        fig3 = ad.grafico_viagens_semP_por_hora(ad.df)
        st.pyplot(fig3)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> O pico de viagens vazias ocorre às 5h da manhã, seguido por outro pico 
        às 18h-19h, sugerindo problemas nos horários de início e fim de operação.
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        
        # Ano de fabricação 
        #st.markdown("### Veículos Fabricados até 2015", unsafe_allow_html=True)
        fig5 = ad.grafico_veiculos_antes_2015(ad.rel)
        st.pyplot(fig5)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> Aproximadamente 83% da frota foi fabricada até 2015, indicando uma 
        frota envelhecida que pode apresentar maiores custos de manutenção e menor eficiência.
        </div>
        """, unsafe_allow_html=True)

# --- Problema 1
elif show_section("Problema 1: Viagens Vazias"):
    st.markdown('<p class="section-title">Problema 1: Alto índice de viagens sem passageiros</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        
        #st.markdown("### Top 10 Linhas com Mais Viagens Vazias", unsafe_allow_html=True)
        fig2 = ad.grafico_top_linhas_vazias(ad.df)
        st.pyplot(fig2)
    
    with col2:
        st.markdown("""
        <div class="problem-box">
        <h4>Problema Identificado:</h4>
        <ul>
            <li>24,7% das viagens ocorrem sem passageiros</li>
            <li>Concentração de viagens vazias nas primeiras horas da manhã (5h)</li>
            <li>Dez linhas específicas concentram um grande número de viagens sem passageiros</li>
            <li>Desperdício operacional estimado em mais de 20% dos recursos</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    
    #st.markdown("### Viagens sem Passageiros por Hora de Início", unsafe_allow_html=True)
    fig3 = ad.grafico_viagens_semP_por_hora(ad.df)
    st.pyplot(fig3)
    
    st.markdown("""
    <div class="solution-box">
    <h4>Soluções Propostas:</h4>
    <ol>
        <li><strong>Replanejamento de horários:</strong> Ajustar os horários de início das operações, especialmente nas primeiras horas da manhã (5h), quando ocorre o maior pico de viagens vazias.</li>
        <li><strong>Otimização de itinerários:</strong> Revisar e otimizar as rotas das 10 linhas com maior incidência de viagens vazias, considerando:
            <ul>
                <li>Fusão de linhas com baixa demanda</li>
                <li>Redução da frequência em horários de baixa demanda</li>
                <li>Implementação de sistema de transporte sob demanda para áreas menos populosas</li>
            </ul>
        </li>
        <li><strong>Sistema de monitoramento em tempo real:</strong> Implementar tecnologia para monitorar a ocupação em tempo real e ajustar a oferta conforme a demanda.</li>
    </ol>
    </div>
    
    <div class="insight-box">
    <h4>Impacto Esperado:</h4>
    <ul>
        <li>Redução de até 15% nos custos operacionais</li>
        <li>Diminuição do consumo de combustível e emissões de CO₂</li>
        <li>Melhor alocação de recursos para linhas com maior demanda</li>
        <li>Aumento da taxa de ocupação média dos veículos</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Problema 2
elif show_section("Problema 2: Frota Antiga"):
    st.markdown('<p class="section-title">Problema 2: Frota envelhecida</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        
        #st.markdown("### Veículos Fabricados até 2015", unsafe_allow_html=True)
        fig5 = ad.grafico_veiculos_antes_2015(ad.rel)
        st.pyplot(fig5)
    
    with col2:
        st.markdown("""
        <div class="problem-box">
        <h4>Problema Identificado:</h4>
        <ul>
            <li>Aproximadamente 83% da frota foi fabricada até 2015</li>
            <li>Veículos com mais de 10 anos de uso</li>
            <li>Maiores custos de manutenção e reparos frequentes</li>
            <li>Menor eficiência energética e maiores emissões</li>
            <li>Maior probabilidade de falhas mecânicas e atrasos</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    
    
    st.markdown("""
    <div class="solution-box">
    <h4>Soluções Propostas:</h4>
    <ol>
        <li><strong>Plano de renovação gradual da frota:</strong> 
            <ul>
                <li>Substituição prioritária dos veículos mais antigos (fabricados antes de 2010)</li>
                <li>Aquisição de veículos com maior eficiência energética</li>
                <li>Análise de viabilidade para introdução de veículos elétricos ou híbridos</li>
            </ul>
        </li>
        <li><strong>Programa de manutenção preventiva intensificada:</strong> Para estender a vida útil dos veículos não priorizados para substituição imediata.</li>
        <li><strong>Parcerias público-privadas:</strong> Para financiamento da renovação da frota sem comprometer o orçamento municipal.</li>
    </ol>
    </div>
    
    <div class="insight-box">
    <h4>Impacto Esperado:</h4>
    <ul>
        <li>Redução de 30-40% nos custos de manutenção a médio prazo</li>
        <li>Diminuição significativa nas falhas mecânicas e quebras durante operação</li>
        <li>Melhoria na percepção do serviço pelos usuários</li>
        <li>Redução de emissões de poluentes</li>
        <li>Aumento da confiabilidade do sistema</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Problema 3
elif show_section("Problema 3: Conforto Térmico"):
    st.markdown('<p class="section-title">Problema 3: Baixa disponibilidade de ar-condicionado</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        
        #st.markdown("### Presença de Ar Condicionado", unsafe_allow_html=True)
        fig4 = ad.grafico_ar_condicionado(ad.rel)
        st.pyplot(fig4)
    
    with col2:
        st.markdown("""
        <div class="problem-box">
        <h4>Problema Identificado:</h4>
        <ul>
            <li>69,1% da frota não possui ar-condicionado</li>
            <li>Comprometimento do conforto dos passageiros no clima quente de Teresina</li>
            <li>Média anual de temperatura em Teresina: 28°C</li>
            <li>Média mensal de temperatura em Teresina: 30°C</li>
            <li>Temperaturas máximas frequentemente acima de 40°C</li>
            <li>Redução da atratividade do Transporte Público (Ônibus)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="solution-box">
    <h4>Soluções Propostas:</h4>
    <ol>
        <li><strong>Plano de retrofit:</strong> Instalação de sistemas de ar-condicionado em veículos mais novos que ainda não possuem o equipamento.</li>
        <li><strong>Critério de renovação:</strong> Estabelecer como requisito obrigatório a presença de ar-condicionado em todos os novos veículos adquiridos.</li>
        <li><strong>Medidas alternativas de conforto térmico:</strong>
            <ul>
                <li>Melhorias na ventilação dos veículos sem ar-condicionado</li>
                <li>Instalação de películas que reduzam a incidência solar</li>
                <li>Implementação de sistemas de circulação de ar mais eficientes</li>
            </ul>
        </li>
    </ol>
    </div>
    
    <div class="insight-box">
    <h4>Impacto Esperado:</h4>
    <ul>
        <li>Melhoria significativa na experiência dos usuários</li>
        <li>Aumento da atratividade do Transporte Público (Ônibus)</li>
        <li>Potencial aumento do número de passageiros</li>
        <li>Redução da evasão de usuários para transportes alternativos</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Recomendações
elif show_section("Recomendações"):
    st.markdown('<p class="section-title">Plano de Ação Integrado</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="solution-box">
    <h4>Recomendações Prioritárias:</h4>
    
    <h5>Curto Prazo (3-6 meses):</h5>
    <ol>
        <li>Realizar auditoria operacional detalhada das 10 linhas com maior incidência de viagens vazias.</li>
        <li>Revisar os horários de início de operação, especialmente às 5h da manhã.</li>
        <li>Implementar programa intensificado de manutenção preventiva para veículos mais antigos.</li>
        <li>Estabelecer métricas claras de desempenho e monitoramento do sistema.</li>
    </ol>
    
    <h5>Médio Prazo (6-18 meses):</h5>
    <ol>
        <li>Iniciar a renovação gradual da frota, priorizando a substituição dos veículos mais antigos.</li>
        <li>Implementar sistema de monitoramento em tempo real da ocupação dos veículos.</li>
        <li>Desenvolver plano de retrofit para instalação de ar-condicionado nos veículos mais novos.</li>
        <li>Reconfigurar rotas e frequências com base nos dados coletados.</li>
    </ol>
    
    <h5>Longo Prazo (18-36 meses):</h5>
    <ol>
        <li>Completar a renovação de pelo menos 50% da frota fabricada antes de 2015.</li>
        <li>Implementar sistema dinâmico de ajuste de oferta conforme demanda.</li>
        <li>Avaliar a viabilidade de veículos elétricos ou híbridos para novas aquisições.</li>
        <li>Garantir que pelo menos 70% da frota possua ar-condicionado.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>Conclusão:</h4>
    <p>A análise dos dados do sistema de Transporte Público (Ônibus) de Teresina revela significativas oportunidades de melhoria
    operacional e de qualidade de serviço. Os três principais problemas identificados - alto índice de viagens vazias,
    frota envelhecida e baixa disponibilidade de ar-condicionado - estão intrinsecamente relacionados e afetam tanto
    a eficiência operacional quanto a experiência dos usuários.</p>
    
    <p>A implementação das soluções propostas tem potencial para transformar o sistema de Transporte Público (Ônibus) da cidade,
    tornando-o mais eficiente, sustentável e atrativo para os cidadãos. Além dos benefícios financeiros diretos,
    as melhorias poderão contribuir para a redução do uso de transporte individual, diminuição de congestionamentos
    e melhoria da qualidade do ar na cidade.</p>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 0.9em; color: gray;'>
        Projeto de Tópicos em Big Data - Transporte Público (Ônibus) de Teresina - 2025
    </p>
""", unsafe_allow_html=True)
