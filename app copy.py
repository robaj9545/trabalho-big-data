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

# Estilo personalizado
st.markdown("""
<style>
    .main-title {
        color: #1E3A8A;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-title {
        color: #1E3A8A;
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .problem-box {
        background-color: #FFEBEE;
        color: black;
        border-left: 5px solid #D32F2F;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
    .solution-box {
        background-color: #E8F5E9;
        color: black;
        border-left: 5px solid #388E3C;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
    .insight-box {
        background-color: #E3F2FD;
        color: black; 
        border-left: 5px solid #1976D2;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 30px;
        font-weight: bold;
        color: #1E3A8A;
    }
    .metric-label {
        font-size: 16px;
        color: #6B7280;
    }
</style>
""", unsafe_allow_html=True)

# Título e introdução
st.markdown('<p class="main-title">Análise do Sistema de Transporte Público (Ônibus) de Teresina</p>', unsafe_allow_html=True)

st.markdown("""
Esta análise examina o sistema de Transporte Público (Ônibus) por ônibus de Teresina, com foco em 
eficiência operacional, qualidade do serviço e uso de recursos. O estudo utiliza dados de 
janeiro a abril de 2025, identificando problemas críticos e propondo soluções viáveis.
""")

# Sidebar com informações do projeto
with st.sidebar:
    st.image("bus.jpg", width=250)
    st.markdown("### Projeto de Tópicos em Big Data")
    st.markdown("**Tema:** Transporte Público (Ônibus) em Teresina")
    st.markdown("**Período analisado:** Janeiro a Abril de 2025")
    st.markdown("**Foco:** Eficiência operacional e qualidade do serviço")
    
    st.markdown("---")
    st.markdown("### Navegação")
    navigation = st.radio("Ir para:", 
        ["Visão Geral", "Problema 1: Viagens Vazias", "Problema 2: Frota Antiga", "Problema 3: Conforto Térmico", "Recomendações"])

# Métricas principais
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><p class="metric-value">24.7%</p><p class="metric-label">Viagens sem passageiros</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><p class="metric-value">69.1%</p><p class="metric-label">Frota sem ar-condicionado</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><p class="metric-value">~83%</p><p class="metric-label">Veículos fabricados até 2015</p></div>', unsafe_allow_html=True)

# Função para mostrar seção baseada na navegação
def show_section(section_name):
    return navigation == section_name

# VISÃO GERAL
if show_section("Visão Geral"):
    st.markdown('<p class="section-title">Visão Geral do Sistema</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        
        # Viagens com e sem passageiros 
        st.markdown("### Proporção de Viagens com e sem Passageiros", unsafe_allow_html=True)
        fig1 = ad.grafico_prop_viagens_semP(ad.df)
        st.pyplot(fig1)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> Quase 1/4 das viagens (24,7%) ocorrem sem nenhum passageiro, 
        representando um desperdício significativo de recursos operacionais.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        
        # Horários de viagens vazias 
        st.markdown("### Viagens sem Passageiros por Hora de Início", unsafe_allow_html=True)
        fig3 = ad.grafico_viagens_semP_por_hora(ad.df)
        st.pyplot(fig3)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> O pico de viagens vazias ocorre às 5h da manhã, seguido por outro pico 
        às 18h-19h, sugerindo problemas nos horários de início e fim de operação.
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        
        # Ar condicionado 
        st.markdown("### Presença de Ar Condicionado", unsafe_allow_html=True)
        fig4 = ad.grafico_ar_condicionado(ad.rel)
        st.pyplot(fig4)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> Apenas 30,9% da frota possui ar-condicionado, comprometendo 
        o conforto dos passageiros no clima quente de Teresina.
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        
        # Ano de fabricação 
        st.markdown("### Veículos Fabricados até 2015", unsafe_allow_html=True)
        fig5 = ad.grafico_veiculos_antes_2015(ad.rel)
        st.pyplot(fig5)
        st.markdown("""
        <div class="insight-box">
        <strong>Análise:</strong> Aproximadamente 83% da frota foi fabricada até 2015, indicando uma 
        frota envelhecida que pode apresentar maiores custos de manutenção e menor eficiência.
        </div>
        """, unsafe_allow_html=True)

# PROBLEMA 1: VIAGENS VAZIAS
if show_section("Problema 1: Viagens Vazias"):
    st.markdown('<p class="section-title">Problema 1: Alto índice de viagens sem passageiros</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        
        st.markdown("### Top 10 Linhas com Mais Viagens Vazias", unsafe_allow_html=True)
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
    
    
    st.markdown("### Viagens sem Passageiros por Hora de Início", unsafe_allow_html=True)
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

# PROBLEMA 2: FROTA ANTIGA
if show_section("Problema 2: Frota Antiga"):
    st.markdown('<p class="section-title">Problema 2: Frota envelhecida</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        
        st.markdown("### Veículos Fabricados até 2015", unsafe_allow_html=True)
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

# PROBLEMA 3: CONFORTO TÉRMICO
if show_section("Problema 3: Conforto Térmico"):
    st.markdown('<p class="section-title">Problema 3: Baixa disponibilidade de ar-condicionado</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        
        st.markdown("### Presença de Ar Condicionado", unsafe_allow_html=True)
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

# RECOMENDAÇÕES FINAIS
if show_section("Recomendações"):
    st.markdown('<p class="section-title">Plano de Ação Integrado</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="solution-box">
    <h4>Recomendações Prioritárias:</h4>
    
    <h5>Curto Prazo (3-6 meses):</h5>
    <ol>
        <li>Realizar auditoria operacional detalhada das 10 linhas com maior incidência de viagens vazias</li>
        <li>Revisar os horários de início de operação, especialmente às 5h da manhã</li>
        <li>Implementar programa intensificado de manutenção preventiva para veículos mais antigos</li>
        <li>Estabelecer métricas claras de desempenho e monitoramento do sistema</li>
    </ol>
    
    <h5>Médio Prazo (6-18 meses):</h5>
    <ol>
        <li>Iniciar a renovação gradual da frota, priorizando a substituição dos veículos mais antigos</li>
        <li>Implementar sistema de monitoramento em tempo real da ocupação dos veículos</li>
        <li>Desenvolver plano de retrofit para instalação de ar-condicionado nos veículos mais novos</li>
        <li>Reconfigurar rotas e frequências com base nos dados coletados</li>
    </ol>
    
    <h5>Longo Prazo (18-36 meses):</h5>
    <ol>
        <li>Completar a renovação de pelo menos 50% da frota fabricada antes de 2015</li>
        <li>Implementar sistema dinâmico de ajuste de oferta conforme demanda</li>
        <li>Avaliar a viabilidade de veículos elétricos ou híbridos para novas aquisições</li>
        <li>Garantir que pelo menos 70% da frota possua ar-condicionado</li>
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
        Projeto acadêmico de Big Data - Transporte Público (Ônibus) de Teresina - 2025
    </p>
""", unsafe_allow_html=True)