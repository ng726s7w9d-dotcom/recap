import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Zella Mobile", layout="centered")

st.title("📱 TradeZella Mobile")

# 簡易輸入區
with st.expander("➕ 新增交易", expanded=True):
    with st.form("trade_form"):
        symbol = st.text_input("商品", value="BTC")
        side = st.selectbox("方向", ["Long", "Short"])
        pnl = st.number_input("盈虧 ($)", value=0.0)
        submitted = st.form_submit_button("儲存並更新")

# 數據看板
c1, c2 = st.columns(2)
c1.metric("今日損益", "$1,250")
c2.metric("勝率", "65%")

# 簡單圖表
df_sim = pd.DataFrame({'Trade': range(5), 'Balance': [100, 120, 110, 150, 140]})
fig = px.line(df_sim, x='Trade', y='Balance', title="淨值走勢")
st.plotly_chart(fig, use_container_width=True)
