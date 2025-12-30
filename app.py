import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- 頁面高級配置 ---
st.set_page_config(page_title="CapitalFlow Pro", page_icon="💎", layout="wide")

# --- 注入高級 UI (CSS) ---
st.markdown("""
    <style>
    .main { background: #0b0e14; color: #e0e0e0; }
    div[data-testid="stMetric"] { background: rgba(30, 41, 59, 0.7); border-radius: 12px; padding: 15px; border: 1px solid #334155; }
    h1, h2, h3 { color: #38bdf8; text-shadow: 0px 0px 10px rgba(56, 189, 248, 0.3); }
    .stButton>button { background: linear-gradient(90deg, #38bdf8, #818cf8); color: white; border-radius: 20px; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 CapitalFlow Pro")

# --- 數據側邊導航 ---
with st.sidebar:
    st.markdown("### 導航菜單")
    mode = st.radio("選擇功能", ["📊 儀表板", "🧠 心理分析", "🧮 計算機"])

# 模擬數據
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-12-25', periods=7),
    'PnL': [200, -150, 600, 1000, -400, 300, 800],
    'Mistake': ['無', '太早出場', '無', '無', 'FOMO', '無', '無']
})
df['Equity'] = df['PnL'].cumsum()

if mode == "📊 儀表板":
    c1, c2 = st.columns(2)
    c1.metric("總損益", f"${df['PnL'].sum()}", "+15%")
    c2.metric("勝率", "71.4%")
    
    st.subheader("📈 淨值成長曲線")
    fig = px.area(df, x='Date', y='Equity', template="plotly_dark")
    fig.update_traces(line_color='#38bdf8', fillcolor='rgba(56, 189, 248, 0.2)')
    st.plotly_chart(fig, use_container_width=True)

elif mode == "🧠 心理分析":
    st.subheader("🧠 心理弱點追蹤")
    fig_pie = px.pie(df, names='Mistake', hole=0.5, template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)

elif mode == "🧮 計算機":
    st.subheader("🧮 風險管理計算")
    balance = st.number_input("帳戶餘額", value=10000)
    risk = st.slider("風險比例 (%)", 0.5, 5.0, 1.0)
    st.info(f"建議單筆損失控制在: ${balance * risk / 100}")
