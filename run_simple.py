"""
Nomadix - Versão Simplificada para Demonstração
Sistema de Insights para Planejamento Turístico em Angola -  Lili
"""

import sys
import os
import random
from datetime import datetime, timedelta

# Verificar se streamlit está disponível
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False

# Verificar outras dependências
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

def show_dependencies_status():
    """Mostra o status das dependências"""
    print("=== STATUS DAS DEPENDÊNCIAS ===")
    print(f"Streamlit: {'✓ Disponível' if STREAMLIT_AVAILABLE else '✗ Não disponível'}")
    print(f"Pandas: {'✓ Disponível' if PANDAS_AVAILABLE else '✗ Não disponível'}")
    print(f"Plotly: {'✓ Disponível' if PLOTLY_AVAILABLE else '✗ Não disponível'}")
    print("=" * 35)

def generate_sample_data():
    """Gera dados de exemplo para demonstração"""
    if not PANDAS_AVAILABLE:
        return None
    
    # Dados de exemplo (1 USD ≈ 825 AOA - taxa aproximada)
    data = {
        'Província': ['Luanda', 'Benguela', 'Huíla', 'Namibe', 'Kwanza Sul'],
        'Visitantes_2023': [450000, 120000, 85000, 65000, 45000],
        'Visitantes_2024': [520000, 135000, 92000, 78000, 52000],
        'Receita_AOA': [10312500000, 2640000000, 1732500000, 1485000000, 990000000],  # Convertido para AOA
        'Hotéis': [45, 18, 12, 8, 6],
        'Satisfação': [4.2, 4.5, 4.7, 4.3, 4.1]
    }
    
    df = pd.DataFrame(data)
    return df

def run_console_version():
    """Executa uma versão console da aplicação"""
    print("\n🌍 NOMADIX - Dashboard Turístico de Angola")
    print("=" * 50)
    
    show_dependencies_status()
    
    if PANDAS_AVAILABLE:
        print("\n📊 DADOS DE TURISMO - PROVÍNCIAS PRINCIPAIS")
        print("=" * 50)
        
        df = generate_sample_data()
        print(df.to_string(index=False))
        
        print(f"\n📈 ESTATÍSTICAS RESUMO:")
        print(f"Total de Visitantes 2024: {df['Visitantes_2024'].sum():,}")
        print(f"Receita Total: {df['Receita_AOA'].sum():,.0f} AOA")
        print(f"Média de Satisfação: {df['Satisfação'].mean():.1f}/5.0")
        print(f"Província com Maior Crescimento: {df.loc[df['Visitantes_2024'].idxmax(), 'Província']}")
    
    print(f"\n🎯 INSIGHTS PRINCIPAIS:")
    print("• Luanda mantém liderança no turismo nacional")
    print("• Crescimento médio de 15% no número de visitantes")
    print("• Huíla apresenta maior índice de satisfação")
    print("• Potencial de desenvolvimento no interior")
    
    print(f"\n🔄 Para executar a versão web completa:")
    print("1. Instale: pip install streamlit pandas plotly")
    print("2. Execute: streamlit run src/app.py")

def run_streamlit_version():
    """Executa a versão Streamlit da aplicação"""
    try:
        # Configuração da página
        st.set_page_config(
            page_title="Nomadix - Dashboard Turístico",
            page_icon="🌍",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    except Exception as e:
        st.error(f"Erro na configuração: {e}")
        return
    
    # CSS customizado para os cards
    st.markdown("""
        <style>
        .metric-card {
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            margin-bottom: 1rem;
        }
        .metric-card-visitors {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .metric-card-revenue {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }
        .metric-card-satisfaction {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }
        .metric-card-growth {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        }
        .metric-title {
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            opacity: 0.9;
        }
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            margin: 0;
        }
        .metric-delta {
            font-size: 0.8rem;
            margin-top: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Título principal
    st.markdown("<h1 style='text-align: center; color: #FF6B35;'>🌍 NOMADIX</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Dashboard de Insights Turísticos - Angola</h3>", unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.header("🎛️ Configurações")
    st.sidebar.info("Sistema de análise turística para planejamento estratégico")
    
    # Dados
    if PANDAS_AVAILABLE:
        df = generate_sample_data()
        
        # Métricas principais com cards customizados
        col1, col2, col3, col4 = st.columns(4)
        
        total_visitantes = df['Visitantes_2024'].sum()
        receita_total = df['Receita_AOA'].sum()
        satisfacao_media = df['Satisfação'].mean()
        crescimento = ((df['Visitantes_2024'].sum() - df['Visitantes_2023'].sum()) / df['Visitantes_2023'].sum()) * 100
        
        with col1:
            st.markdown(f"""
                <div class="metric-card metric-card-visitors">
                    <div class="metric-title">👥 Total de Visitantes 2024</div>
                    <div class="metric-value">{total_visitantes:,}</div>
                    <div class="metric-delta">+{crescimento:.1f}% vs 2023</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            receita_bilhoes = receita_total / 1_000_000_000
            st.markdown(f"""
                <div class="metric-card metric-card-revenue">
                    <div class="metric-title">💰 Receita Total</div>
                    <div class="metric-value">{receita_bilhoes:.1f}B AOA</div>
                    <div class="metric-delta">Kwanza Angolano</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div class="metric-card metric-card-satisfaction">
                    <div class="metric-title">⭐ Satisfação Média</div>
                    <div class="metric-value">{satisfacao_media:.1f}/5.0</div>
                    <div class="metric-delta">Excelente qualidade</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
                <div class="metric-card metric-card-growth">
                    <div class="metric-title">📈 Crescimento Anual</div>
                    <div class="metric-value">{crescimento:.1f}%</div>
                    <div class="metric-delta">Tendência positiva</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Espaçamento
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Gráficos
        try:
            if PLOTLY_AVAILABLE:
                st.subheader("📊 Análise por Província")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    fig1 = px.bar(df, x='Província', y='Visitantes_2024', 
                                 title="Visitantes por Província (2024)",
                                 color_discrete_sequence=['#FF6B35'])
                    fig1.update_layout(showlegend=False)
                    st.plotly_chart(fig1, width='stretch')
                
                with col2:
                    fig2 = px.pie(df, values='Receita_AOA', names='Província', 
                                 title="Distribuição de Receita (AOA)",
                                 color_discrete_sequence=px.colors.qualitative.Set3)
                    fig2.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig2, width='stretch')
            else:
                st.warning("📊 Plotly não disponível. Instale com: pip install plotly")
        except Exception as e:
            st.error(f"Erro ao carregar gráficos: {e}")
            st.info("Os gráficos serão exibidos assim que as dependências forem resolvidas.")
        
        # Tabela de dados
        st.subheader("📋 Dados Detalhados")
        
        # Header colorido da tabela (mantendo o formato original bonito)
        st.markdown("""
        <div style="background-color: #FF6B35; padding: 12px; border-radius: 10px 10px 0 0; margin-bottom: 0;">
            <div style="display: flex; color: white; font-weight: bold;">
                <div style="flex: 2; text-align: left;">Província</div>
                <div style="flex: 1.5; text-align: center;">Visitantes 2023</div>
                <div style="flex: 1.5; text-align: center;">Visitantes 2024</div>
                <div style="flex: 2; text-align: center;">Receita (AOA)</div>
                <div style="flex: 1; text-align: center;">Hotéis</div>
                <div style="flex: 1.5; text-align: center;">Satisfação</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Dados da tabela com espaçamento reduzido
        for i, (_, row) in enumerate(df.iterrows()):
            bg_color = "#f9f9f9" if i % 2 == 0 else "#ffffff"
            
            st.markdown(f"""
            <div style="background-color: {bg_color}; padding: 8px 12px; margin: 0; border-bottom: 1px solid #e0e0e0;">
                <div style="display: flex; align-items: center;">
                    <div style="flex: 2; font-weight: bold; color: #333;">{row['Província']}</div>
                    <div style="flex: 1.5; text-align: center;">{row['Visitantes_2023']:,}</div>
                    <div style="flex: 1.5; text-align: center;">{row['Visitantes_2024']:,}</div>
                    <div style="flex: 2; text-align: center;">{row['Receita_AOA']:,.0f} AOA</div>
                    <div style="flex: 1; text-align: center;">{row['Hotéis']}</div>
                    <div style="flex: 1.5; text-align: center;">⭐ {row['Satisfação']}/5.0</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Fechamento da tabela
        st.markdown("""
        <div style="border-radius: 0 0 10px 10px; border: 1px solid #e0e0e0; height: 1px; margin-top: 0;"></div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("📊 Pandas não está disponível. Instale com: pip install pandas")
        # Mostrar dados básicos mesmo sem pandas
        st.subheader("📋 Dados Básicos (Exemplo)")
        st.info("""
        **Províncias Principais:**
        - 🏆 Luanda: 520,000 visitantes | 10.3B AOA
        - 🌊 Benguela: 135,000 visitantes | 2.6B AOA  
        - 🏔️ Huíla: 92,000 visitantes | 1.7B AOA
        - 🏖️ Namibe: 78,000 visitantes | 1.5B AOA
        - 🌿 Kwanza Sul: 52,000 visitantes | 990M AOA
        """)
    
    # Informações sobre dependências
    st.sidebar.subheader("🔧 Status do Sistema")
    status_info = f"""
    **Dependências:**
    - Streamlit: {'✅' if STREAMLIT_AVAILABLE else '❌'} 
    - Pandas: {'✅' if PANDAS_AVAILABLE else '❌'}
    - Plotly: {'✅' if PLOTLY_AVAILABLE else '❌'}
    
    **Para instalação completa:**
    ```
    pip install pandas plotly
    ```
    """
    st.sidebar.info(status_info)
    
    # Insights
    st.subheader("🎯 Insights Principais")
    
    insights = [
        "🏆 Luanda mantém liderança absoluta no setor turístico nacional",
        "📈 Crescimento consistente de 15% no número de visitantes",
        "⭐ Huíla apresenta o maior índice de satisfação dos turistas",
        "🌟 Grande potencial de desenvolvimento no turismo interior",
        "💰 Oportunidades de investimento em infraestrutura hoteleira"
    ]
    
    for insight in insights:
        st.info(insight)

if __name__ == "__main__":
    show_dependencies_status()
    
    if STREAMLIT_AVAILABLE:
        print("\n🚀 Iniciando versão Streamlit...")
        run_streamlit_version()
    else:
        print("\n🖥️ Streamlit não disponível, executando versão console...")
        run_console_version()