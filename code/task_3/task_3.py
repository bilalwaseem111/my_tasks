import random
import streamlit as st   # type: ignore
import pandas as pd  # type: ignore
from datetime import datetime

# Custom CSS for styling and animations
st.markdown(
    """
    <style>

    @keyframes gradientBackground {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    body {
        background: linear-gradient(270deg, #87CEEB, #ADD8E6, #87CEEB);
        background-size: 200% 200%;
        animation: gradientBackground 10s ease infinite;
        color: #ADD8E6;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .css-1d391kg h1 {
        color: rgb(173, 216, 230)

;
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }

    .css-1d391kg label {
        color: rgb(173, 216, 230)

;
        font-size: 18px;
        margin: 10px 0;
    }

    .css-1d391kg .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .css-1d391kg .stRadio > div > label {
        background: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 10px;
        transition: all 0.3s ease;
        color: #333;
    }

    .css-1d391kg .stRadio > div > label:hover {
        background: rgba(255, 255, 255, 1);
        transform: scale(1.05);
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }

    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
        border-radius: 5px;
        border: 1px solid #4CAF50;
    }

    .stSelectbox>div>div>select {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
        border-radius: 5px;
        border: 1px solid #4CAF50;
    }

    .stDataFrame {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 10px;
    }

    .stProgress>div>div>div>div {
        background-color: #4CAF50;
    }

    .stMarkdown {
        color: #333;
    }

    .footer {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }

    .footer img {
        width: 30px;
        height: 30px;
        transition: transform 0.3s ease;
    }

    .footer img:hover {
        transform: scale(1.2);
    }

    .home-header {
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    .home-content {
        animation: slideIn 1.5s ease-in-out;
    }

    @keyframes slideIn {
        0% { transform: translateY(-20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: scale(1.05);
    }

    .card h3 {
        margin-top: 0;
        color: #333;
    }

    .card p {
        margin-bottom: 0;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for storing workouts and goals
if "workouts" not in st.session_state:
    st.session_state.workouts = pd.DataFrame(columns=["Date", "Exercise", "Duration (mins)", "Calories Burned"])
if "goals" not in st.session_state:
    st.session_state.goals = {"Calories": 0, "Workouts": 0}
if "progress" not in st.session_state:
    st.session_state.progress = {"Total Workouts": 0, "Total Calories Burned": 0}

# App Title
st.title("🏋️‍♂️ Fitness Tracker App")
st.markdown("Track your workouts, set fitness goals, and monitor your progress over time!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Home", "Record Workout", "Set Goals", "View Progress"])

# Home Page
if page == "Home":
    st.markdown('<div class="home-header"><h1>Welcome to Your Fitness Tracker!</h1></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="home-content">
        <p>This app helps you:</p>
        <ul>
            <li>Record and track your workouts</li>
            <li>Set fitness goals</li>
            <li>View your progress over time</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add motivational quote
    st.markdown("### 💪 Motivational Quote of the Day")
    quotes = [
        "The only bad workout is the one you didn't do.",
        "Strive for progress, not perfection.",
        "Don't stop until you're proud.",
        "Sweat is fat crying.",
        "Your body can stand almost anything. It’s your mind that you have to convince.",
    ]
    st.markdown(f'<div style="text-align: center; font-size: 20px;">"{random.choice(quotes)}"</div>', unsafe_allow_html=True)

    # Add cards for quick stats
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>Total Workouts</h3>
                <p>{}</p>
            </div>
            """.format(st.session_state.progress["Total Workouts"]),
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>Total Calories Burned</h3>
                <p>{} kcal</p>
            </div>
            """.format(st.session_state.progress["Total Calories Burned"]),
            unsafe_allow_html=True,
        )

    # Add a fitness tip
    st.markdown("### 💡 Fitness Tip of the Day")
    tips = [
        "Drink plenty of water before, during, and after your workout.",
        "Warm up before exercising to prevent injuries.",
        "Mix cardio and strength training for the best results.",
        "Track your progress to stay motivated.",
        "Get enough sleep to allow your body to recover.",
    ]
    st.markdown(f'<div style="text-align: center; font-size: 18px;">"{random.choice(tips)}"</div>', unsafe_allow_html=True)

    # Add a progress visualization
    st.markdown("### 📈 Progress Visualization")
    if st.session_state.goals["Calories"] > 0:
        calorie_progress = min(st.session_state.progress["Total Calories Burned"] / st.session_state.goals["Calories"], 1.0)
        st.progress(calorie_progress)
        st.write(f"{calorie_progress * 100:.2f}% of your daily calorie burn goal")

    if st.session_state.goals["Workouts"] > 0:
        workout_progress = min(st.session_state.progress["Total Workouts"] / st.session_state.goals["Workouts"], 1.0)
        st.progress(workout_progress)
        st.write(f"{workout_progress * 100:.2f}% of your weekly workout goal")
# Record Workout Page
elif page == "Record Workout":
    st.header("Record Your Workout")
    with st.form("workout_form"):
        exercise = st.selectbox("Select Exercise", ["Running", "Cycling", "Weightlifting", "Yoga", "Swimming"])
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=30)
        calories = st.number_input("Calories Burned", min_value=1, max_value=1000, value=200)
        submitted = st.form_submit_button("Submit Workout")

        if submitted:
            new_workout = {
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Exercise": exercise,
                "Duration (mins)": duration,
                "Calories Burned": calories,
            }
            # Use pd.concat() instead of append()
            st.session_state.workouts = pd.concat([st.session_state.workouts, pd.DataFrame([new_workout])], ignore_index=True)
            st.session_state.progress["Total Workouts"] += 1
            st.session_state.progress["Total Calories Burned"] += calories
            st.success("Workout recorded successfully!")

    st.subheader("Workout History")
    st.dataframe(st.session_state.workouts)

# Set Goals Page
elif page == "Set Goals":
    st.header("Set Your Fitness Goals")
    with st.form("goals_form"):
        calorie_goal = st.number_input("Daily Calorie Burn Goal", min_value=1, max_value=5000, value=500)
        workout_goal = st.number_input("Weekly Workout Goal", min_value=1, max_value=20, value=5)
        submitted = st.form_submit_button("Set Goals")

        if submitted:
            st.session_state.goals["Calories"] = calorie_goal
            st.session_state.goals["Workouts"] = workout_goal
            st.success("Goals updated successfully!")

    st.subheader("Current Goals")
    st.write(f"Daily Calorie Burn Goal: {st.session_state.goals['Calories']} kcal")
    st.write(f"Weekly Workout Goal: {st.session_state.goals['Workouts']} workouts")

# View Progress Page
elif page == "View Progress":
    st.header("Your Progress")
    st.subheader("Total Workouts")
    st.write(f"{st.session_state.progress['Total Workouts']} workouts completed")

    st.subheader("Total Calories Burned")
    st.write(f"{st.session_state.progress['Total Calories Burned']} kcal burned")

    st.subheader("Progress Towards Goals")
    if st.session_state.goals["Calories"] > 0:
        calorie_progress = min(st.session_state.progress["Total Calories Burned"] / st.session_state.goals["Calories"], 1.0)
        st.progress(calorie_progress)
        st.write(f"{calorie_progress * 100:.2f}% of your daily calorie burn goal")

    if st.session_state.goals["Workouts"] > 0:
        workout_progress = min(st.session_state.progress["Total Workouts"] / st.session_state.goals["Workouts"], 1.0)
        st.progress(workout_progress)
        st.write(f"{workout_progress * 100:.2f}% of your weekly workout goal")

# Footer with LinkedIn logo
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        <p>Made by Bilal Waseem</p>
        <a href="www.linkedin.com/in/bilal-waseem-b44006338" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)