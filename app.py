import streamlit as st

st.title("じゃんけんアプリ")
st.caption("君は勝つことができるか!?")

st.subheader("操作方法")
st.text("グー、チョキ、パーのボタンを押すだけ!")

gu_btn = st.button("グー")
choki_btn = st.button("チョキ")
pa_btn = st.button("パー")

if gu_btn == True:
    st.text("グーが押されました!引き分け！")
if choki_btn == True:
    st.text("チョキが押されました!あなたの負け！")
if pa_btn == True:
    st.text("パーが押されました!あなたの勝ち！")
