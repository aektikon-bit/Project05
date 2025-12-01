import streamlit as st
import random

# ตั้งค่า page
st.set_page_config(page_title="🧠 Quiz Game", page_icon="📝", layout="centered")

# CSS สำหรับสวยขึ้น
st.markdown("""
<style>
.app-title {
    text-align: center;
    color: #FF5733;
    font-weight: bold;
}
.big-emoji {
    font-size: 100px;
    text-align: center;
}
.button-style
