import streamlit as st  # type: ignore
import random

# --------------------------
# App Config
# --------------------------
st.set_page_config(page_title="✨ Random Quote Generator ✨", page_icon="💬", layout="centered")

# --------------------------
# Custom CSS Styling + Animations
# --------------------------
st.markdown("""
    <style>
    /* Full-page background animation */
.stApp {
    background: linear-gradient(-45deg, #d0f0fd, #a1c4fd, #c2e9fb, #d0f0fd);
    background-size: 400% 400%;
    animation: gradientBG 19s ease infinite;
}

@keyframes gradientBG {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Optional: Make your quote box pop a little more */
.quote-box {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

    h1 {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #8B0000; /* Dark Red */
        margin-bottom: 40px;
        animation: bounce 2s infinite, colorShiftDarkRed 6s ease-in-out infinite;
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-15px); }
        60% { transform: translateY(-7px); }
    }

    @keyframes colorShiftDarkRed {
        0%   { color: #8B0000; }
        50%  { color: #B22222; }
        100% { color: #8B0000; }
    }
    /* Floating quote box with smooth fade-in */
    .quote-box {
        font-family: 'Trebuchet MS', sans-serif;
        background: rgba(255, 255, 255, 0.85);
        color: #333;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: floatBox 4s ease-in-out infinite, fadeIn 1.5s ease;
        margin-bottom: 30px;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes floatBox {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    /* Stylish quote text */
    .quote-text {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        color: #444;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    .quote-author {
        text-align: right;
        font-size: 1.4rem;
        font-style: italic;
        color: #666;
    }

    /* Animated button */
    .share-button {
        background: linear-gradient(90deg, #a1c4fd, #c2e9fb, #fbc2eb);
        color: #333;
        border: none;
        border-radius: 20px;
        padding: 15px 15px;
        cursor: pointer;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.2s ease;
        display: block;
        margin: 0 auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    .share-button:hover {
        background: linear-gradient(270deg, #fbc2eb, #a1c4fd);
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 12px 24px rgba(0,0,0,0.3);
    }

    /* Footer styling */
    footer {
        text-align: center;
        margin-top: 20px;
        color: #000000;
        font-size: 1rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* Footer container for name + LinkedIn */
    .footer-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin-top: 7px;
    }

    /* LinkedIn logo with hover effect */
    .linkedin-logo {
        width: 50px;
        height: 50px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        border-radius: 50%;
        
        padding: 5px;
    }

    .linkedin-logo:hover {
        transform: scale(1.3) rotate(10deg);
        box-shadow: 20 80px 160px rgba(20,20,20,20.3);
    }

    </style>
""", unsafe_allow_html=True)
 

# --------------------------
# Quotes List
# --------------------------
quotes = [
    {"quote": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"quote": "Don't let yesterday take up too much of today.", "author": "Will Rogers"},
    {"quote": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
    {"quote": "If you are working on something exciting, it will keep you motivated.", "author": "Steve Jobs"},
    {"quote": "Success is not in what you have, but who you are.", "author": "Bo Bennett"},
    {"quote": "The harder you work for something, the greater you'll feel when you achieve it.", "author": "Anonymous"},
    {"quote": "Dream bigger. Do bigger.", "author": "Anonymous"},
    {"quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Great things never come from comfort zones.", "author": "Neil Strauss"},
    {"quote": "Push yourself, because no one else is going to do it for you.", "author": "Anonymous"},
]

# --------------------------
# Function to Generate Random Quote
# --------------------------
def get_random_quote():
    return random.choice(quotes)

# --------------------------
# Streamlit App UI
# --------------------------
st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown("<h1>Random Quote Generator </h1>", unsafe_allow_html=True)

if "quote" not in st.session_state:
    st.session_state.quote = get_random_quote()

if st.button("✨ Generate New Quote ✨", use_container_width=True):
    st.session_state.quote = get_random_quote()

# Display the Quote
quote = st.session_state.quote
st.markdown(f"""
    <div class="quote-box">
        <div class="quote-text">“{quote['quote']}”</div>
        <div class="quote-author">- {quote['author']}</div>
    </div>
""", unsafe_allow_html=True)

# Copy to clipboard button
st.markdown("""
    <br>
    <button class="share-button" onclick="navigator.clipboard.writeText(document.querySelector('.quote-text').innerText + ' ' + document.querySelector('.quote-author').innerText)">
        📋 Copy Quote
    </button>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer with LinkedIn Logo
st.markdown("""
    <footer>
        <div class="footer-container">
            <p><strong>Made by Bilal Waseem 👉</strong></p>
            <a href="https://www.linkedin.com/in/bilal-waseem-b44006338" target="_blank">
                <img class="linkedin-logo" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
            </a>
        </div>
    </footer>
""", unsafe_allow_html=True)
