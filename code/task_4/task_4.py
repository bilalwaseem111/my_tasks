import streamlit as st # type: ignore
import time
import random
from streamlit.components.v1 import html # type: ignore

# Custom CSS for styling and animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #f4f4f9, #e0e0f5);
    color: #333;
    animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 16px;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

.stProgress>div>div>div {
    background-color: #4CAF50;
}

.header {
    font-size: 2.5rem;
    font-weight: 600;
    color: #4CAF50;
    text-align: center;
    margin-bottom: 20px;
    animation: slideIn 1s ease-in-out;
}

.subheader {
    font-size: 1.5rem;
    font-weight: 400;
    color: #555;
    text-align: center;
    margin-bottom: 30px;
    animation: slideIn 1.5s ease-in-out;
}

.lesson-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    transition: transform 0.3s ease;
    animation: fadeIn 2s ease-in-out;
}

.lesson-card:hover {
    transform: translateY(-5px);
}

.quiz-question {
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 15px;
    animation: fadeIn 2s ease-in-out;
}

.achievement-badge {
    background: #4CAF50;
    color: white;
    padding: 5px 10px;
    border-radius: 12px;
    font-size: 0.9rem;
    display: inline-block;
    margin: 5px;
    animation: fadeIn 2s ease-in-out;
}

@keyframes slideIn {
    from { transform: translateY(-20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.footer {
    text-align: center;
    font-size: 0.9rem;
    color: #777;
    animation: fadeIn 2s ease-in-out;
}

.footer img {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-left: 10px;
    transition: transform 0.3s ease;
}

.footer img:hover {
    transform: scale(1.2);
}

.language-selector {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 30px;
}

.language-selector button {
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.language-selector button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

.language-selector button.active {
    background-color: #45a049;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Logo and LinkedIn link
st.markdown("""

""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="header">Language Learning App</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Learn, Quiz, Achieve!</div>', unsafe_allow_html=True)

# Language Selection
languages = {
    "Spanish": {
        "greetings": "Hola",
        "numbers": ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"],
        "phrases": ["Gracias", "Por favor", "¿Cómo estás?", "Buenos días"],
    },
    "French": {
        "greetings": "Bonjour",
        "numbers": ["Un", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix"],
        "phrases": ["Merci", "S'il vous plaît", "Comment ça va?", "Bonjour"],
    },
    "German": {
        "greetings": "Hallo",
        "numbers": ["Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs", "Sieben", "Acht", "Neun", "Zehn"],
        "phrases": ["Danke", "Bitte", "Wie geht's?", "Guten Tag"],
    },
    "Japanese": {
        "greetings": "こんにちは (Konnichiwa)",
        "numbers": ["一 (Ichi)", "二 (Ni)", "三 (San)", "四 (Shi)", "五 (Go)", "六 (Roku)", "七 (Nana)", "八 (Hachi)", "九 (Kyuu)", "十 (Juu)"],
        "phrases": ["ありがとう (Arigatou)", "お願いします (Onegaishimasu)", "お元気ですか? (Ogenki desu ka?)", "こんにちは (Konnichiwa)"],
    },
}

# Language Selector
st.markdown('<div class="header">Choose a Language</div>', unsafe_allow_html=True)
selected_language = st.radio("", list(languages.keys()), index=0, key="language_selector", horizontal=True)

# User Progress Tracking
if 'progress' not in st.session_state:
    st.session_state['progress'] = 0
if 'achievements' not in st.session_state:
    st.session_state['achievements'] = []

# Lessons
lessons = [
    {"title": f"Lesson 1: Greetings in {selected_language}", "content": f"Learn how to say greetings like '{languages[selected_language]['greetings']}'."},
    {"title": f"Lesson 2: Numbers in {selected_language}", "content": f"Learn numbers from 1 to 10: {', '.join(languages[selected_language]['numbers'])}."},
    {"title": f"Lesson 3: Common Phrases in {selected_language}", "content": f"Learn phrases like: {', '.join(languages[selected_language]['phrases'])}."},
]

# Display Lessons
st.markdown('<div class="header">Lessons</div>', unsafe_allow_html=True)
for lesson in lessons:
    with st.container():
        st.markdown(f'<div class="lesson-card">{lesson["title"]}<br><small>{lesson["content"]}</small></div>', unsafe_allow_html=True)
        if st.button(f"Start {lesson['title']}", key=lesson['title']):
            st.session_state['progress'] += 10
            st.success(f"Completed {lesson['title']}! Your progress is now {st.session_state['progress']}%.")
            if st.session_state['progress'] % 30 == 0:
                achievement = f"Achievement Unlocked: Completed {st.session_state['progress']}%"
                st.session_state['achievements'].append(achievement)
                st.balloons()

# Quizzes
quizzes = [
    {"question": f"How do you say 'Hello' in {selected_language}?", "options": [languages[selected_language]['greetings'], "Goodbye", "Thank you"], "answer": languages[selected_language]['greetings']},
    {"question": f"What is '5' in {selected_language}?", "options": [languages[selected_language]['numbers'][4], languages[selected_language]['numbers'][1], languages[selected_language]['numbers'][9]], "answer": languages[selected_language]['numbers'][4]},
    {"question": f"How do you say 'Thank you' in {selected_language}?", "options": [languages[selected_language]['phrases'][0], "Please", "Goodbye"], "answer": languages[selected_language]['phrases'][0]},
]

# Display Quizzes
st.markdown('<div class="header">Quizzes</div>', unsafe_allow_html=True)
for i, quiz in enumerate(quizzes):
    with st.container():
        st.markdown(f'<div class="quiz-question">Q{i+1}: {quiz["question"]}</div>', unsafe_allow_html=True)
        user_answer = st.radio(f"Options for Q{i+1}", quiz["options"], key=f"quiz_{i}")
        if st.button(f"Submit Q{i+1}", key=f"submit_{i}"):
            if user_answer == quiz["answer"]:
                st.success("Correct! 🎉")
                st.session_state['progress'] += 5
            else:
                st.error("Incorrect. Try again!")

# Progress Tracking
st.markdown('<div class="header">Your Progress</div>', unsafe_allow_html=True)
st.progress(st.session_state['progress'] / 100)

# Achievements
st.markdown('<div class="header">Achievements</div>', unsafe_allow_html=True)
for achievement in st.session_state['achievements']:
    st.markdown(f'<div class="achievement-badge">{achievement}</div>', unsafe_allow_html=True)

# Community Forum (Simulated)
st.markdown('<div class="header">Community Forum</div>', unsafe_allow_html=True)
st.write("Join the discussion and connect with other learners!")
forum_topics = [
    "Best way to practice speaking?",
    "How to remember vocabulary?",
    "Share your favorite language learning resources!",
]
for topic in forum_topics:
    st.markdown(f'<div class="lesson-card">{topic}</div>', unsafe_allow_html=True)
    if st.button(f"Join Discussion on '{topic}'", key=f"forum_{topic}"):
        st.write(f"Redirecting to discussion: {topic}...")

# Footer with LinkedIn logo
st.markdown("---")
st.markdown("""
<div class="footer">
    Made with ❤️ by Bilal Waseem 
    <a href="https://www.linkedin.com/in/bilal-waseem-b44006338" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn Logo">
    </a>
</div>
""", unsafe_allow_html=True)

# JavaScript for additional animations
html("""
<script>
document.addEventListener("DOMContentLoaded", function() {
    const elements = document.querySelectorAll('.fadeIn');
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = 1;
        }, index * 300);
    });
});
</script>
""")