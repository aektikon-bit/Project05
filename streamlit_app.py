import streamlit as st
import random

# ตั้งค่า page
st.set_page_config(page_title="🧠 Quiz Game", page_icon="📝", layout="centered")

# CSS ให้สวยขึ้น
st.markdown("""
<style>
.app-title {
    text-align: center;
    color: #FF5733;
    font-weight: bold;
    font-size: 40px;
}
.big-emoji {
    font-size: 120px;
    text-align: center;
}
.question-box {
    background-color: #F0F8FF;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.option-button button {
    background-color: #1E90FF;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 10px;
}
.info-box {
    text-align: center;
    font-size: 20px;
    color: #333;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='app-title'>🧠 Quiz Game 🧠</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>ตอบคำถามให้ถูกเพื่อสะสมคะแนน!</p>", unsafe_allow_html=True)

# ตัวอย่างคำถาม
quiz = [
    {"question": "ประเทศไทยมีเมืองหลวงชื่ออะไร?", "options": ["กรุงเทพฯ", "เชียงใหม่", "ภูเก็ต", "นครราชสีมา"], "answer": "กรุงเทพฯ"},
    {"question": "สัตว์ตัวใดบินได้?", "options": ["ปลา", "นก", "ช้าง", "สุนัข"], "answer": "นก"},
    {"question": "2 + 3 = ?", "options": ["4", "5", "6", "7"], "answer": "5"},
    {"question": "สีของท้องฟ้าวันแจ่มใส?", "options": ["แดง", "ฟ้า", "เขียว", "ดำ"], "answer": "ฟ้า"},
]

# สุ่มคำถาม
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(quiz)
if 'รอบ' not in st.session_state:
    st.session_state.รอบ = 1
if 'คะแนน' not in st.session_state:
    st.session_state.คะแนน = 0

question = st.session_state.current_question

# แสดงคำถาม
st.markdown(f"<div class='question-box'><h3>{question['question']}</h3></div>", unsafe_allow_html=True)

# แสดงตัวเลือก
for option in question['options']:
    if st.button(option):
        if option == question['answer']:
            st.markdown("<div class='big-emoji'>🎉</div>", unsafe_allow_html=True)
            st.success(f"ถูกต้อง! ✅")
            st.session_state.คะแนน += 1
        else:
            st.markdown("<div class='big-emoji'>❌</div>", unsafe_allow_html=True)
            st.error(f"ผิด! คำตอบที่ถูกคือ: {question['answer']}")
        # สุ่มคำถามใหม่และเพิ่มรอบ
        st.session_state.current_question = random.choice(quiz)
        st.session_state.รอบ += 1
        st.experimental_rerun()  # รีโหลดหน้าเพื่อแสดงคำถามใหม่ทันที

# แสดงรอบและคะแนน
st.markdown(f"<p class='info-box'>รอบที่ {st.session_state.รอบ} | คะแนน: {st.session_state.คะแนน}</p>", unsafe_allow_html=True)
