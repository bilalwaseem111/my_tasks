import streamlit as st  # type: ignore
import pandas as pd     # type: ignore
import random

# 🎨 Custom CSS Styling
st.markdown("""
    <style>
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-20px);
        }
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(270deg, #f6d365, #fda085, #fbc2eb, #a18cd1);
        background-size: 800% 800%;
        animation: gradientShift 15s ease infinite;
        font-family: 'Arial', sans-serif;
        color: #333;
    }

    h1 {
        color: #fff;
        text-align: center;
        font-size: 3.5rem;
        animation: bounce 2s infinite;
        margin-top: 40px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    h2, h3 {
        color: #4CAF50;
        text-align: center;
    }

    .flashcard {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 8px 16px rgba(30,40,50,0.1);
        margin: 10px 0;
        text-align: center;
    }

    .button {
        background-color: #4CAF50 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
    }

    .footer {
        text-align: center; 
        margin-top: 40px; 
        font-size: 14px; 
        color: #000;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }

    .linkedin-logo {
        width: 35px;
        height: 35px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
    }

    .linkedin-logo:hover {
        transform: scale(0.3);
        box-shadow: 30 30 10px #0077b5;
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 Bouncing Animated App Title
st.markdown("<h1>🎓 Flashcard Quiz App</h1>", unsafe_allow_html=True)

# Initialize Session State
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = []

if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0

if 'score' not in st.session_state:
    st.session_state.score = 0

if 'quiz_active' not in st.session_state:
    st.session_state.quiz_active = False

# 🗂️ Menu Selection
menu = st.sidebar.radio("Menu", ("Add Flashcards!!!!", "📝 Take Quiz", "📊 View Flashcards"))

# ➕ Add Flashcards
if menu == "➕ Add Flashcards":
    st.header("➕ Add a New Flashcard")
    with st.form(key='add_flashcard'):
        question = st.text_input("Question")
        answer = st.text_input("Answer")
        submit = st.form_submit_button("Add Flashcard")
        if submit:
            if question and answer:
                st.session_state.flashcards.append({'question': question, 'answer': answer})
                st.success("✅ Flashcard Added!")
                st.balloons()  # Animation
            else:
                st.error("⚠️ Please fill both fields.")

# 📊 View Flashcards
elif menu == "📊 View Flashcards":
    st.header("📚 Your Flashcards")
    if st.session_state.flashcards:
        for idx, card in enumerate(st.session_state.flashcards):
            with st.expander(f"Flashcard {idx + 1}"):
                st.markdown(f"<div class='flashcard'><strong>Q:</strong> {card['question']}<br><strong>A:</strong> {card['answer']}</div>", unsafe_allow_html=True)
    else:
        st.info("No flashcards found! Add some first.")

# 📝 Take Quiz
elif menu == "📝 Take Quiz":
    st.header("📝 Quiz Yourself!")
    if not st.session_state.flashcards:
        st.warning("⚠️ You need to add flashcards before taking a quiz.")
    else:
        if not st.session_state.quiz_active:
            st.session_state.quiz_flashcards = st.session_state.flashcards.copy()
            random.shuffle(st.session_state.quiz_flashcards)
            st.session_state.quiz_index = 0
            st.session_state.score = 0
            st.session_state.quiz_active = True
            st.experimental_rerun()

        if st.session_state.quiz_index < len(st.session_state.quiz_flashcards):
            current_card = st.session_state.quiz_flashcards[st.session_state.quiz_index]
            st.subheader(f"Question {st.session_state.quiz_index + 1} of {len(st.session_state.quiz_flashcards)}")
            st.markdown(f"<div class='flashcard'><strong>Q:</strong> {current_card['question']}</div>", unsafe_allow_html=True)

            user_answer = st.text_input("Your Answer")

            if st.button("Submit Answer", key=st.session_state.quiz_index):
                if user_answer.strip().lower() == current_card['answer'].strip().lower():
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                    st.snow()  # Animation
                else:
                    st.error(f"❌ Incorrect! The correct answer was: {current_card['answer']}")
                st.session_state.quiz_index += 1
                st.experimental_rerun()

        else:
            st.success(f"🎉 Quiz Completed! Your Score: {st.session_state.score}/{len(st.session_state.quiz_flashcards)}")
            if st.session_state.score == len(st.session_state.quiz_flashcards):
                st.balloons()  # Celebration Animation
            st.session_state.quiz_active = False

# 🎨 Footer with LinkedIn Logo
st.markdown("""
    <div class='footer'>
        <span>Made by Bilal Waseem</span>
        <a href='https://www.linkedin.com/in/bilal-waseem-b44006338' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' alt='LinkedIn' class='linkedin-logo'>
        </a>
    </div>
""", unsafe_allow_html=True)
