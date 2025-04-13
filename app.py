import streamlit as st
import pickle
import time
from model import JEERankPredictor
from streamlit_lottie import st_lottie
import requests
import json

# ----------------------- UTILS ---------------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
# Try to load local CSS if it exists, otherwise create it
try:
    local_css("style.css")
except:
    # We'll inject CSS directly instead
    pass

# Load predictor
with open("jee_predictor.pkl", "rb") as f:
    predictor = pickle.load(f)




# ----------------------- PAGE CONFIG ---------------------------


st.set_page_config(page_title="Best JEE Advanced Rank Predictor", page_icon="📊",layout="wide")


# Hide default Streamlit UI and set background/theme
theme_override = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Modern animated background */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #24243e);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Card styling */
.card {
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(7px);
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* Custom button */
.stButton > button {
    background: linear-gradient(45deg, #3a7bd5, #00d2ff);
    border: none;
    border-radius: 20px;
    color: white;
    font-weight: bold;
    padding: 10px 20px;
    text-align: center;
    text-transform: uppercase;
    transition: all 0.3s ease;
    cursor: pointer;
    width: 100%;
    margin-top: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}
.stButton > button:hover {
    background: linear-gradient(45deg, #00d2ff, #3a7bd5);
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
}

/* Input fields */
.stNumberInput > div > div > input {
    border-radius: 5px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
}
.stSelectbox > div > div {
    border-radius: 5px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
}

/* Text styling */
h1, h2, h3, h4 {
    color: white;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
p, li, div {
    color: rgba(255, 255, 255, 0.9);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Particles animation */
.particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    pointer-events: none;
}

/* Result animation */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}
.result-container {
    animation: pulse 2s infinite;
    padding: 20px;
    border-radius: 10px;
    background: linear-gradient(45deg, #1e3c72, #2a5298);
    margin-top: 20px;
    text-align: center;
}

/* Success and error messages */
.success-msg {
    background: linear-gradient(45deg, #56ab2f, #a8e063);
    border-radius: 8px;
    padding: 15px;
    color: white;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
}
.error-msg {
    background: linear-gradient(45deg, #cb356b, #bd3f32);
    border-radius: 8px;
    padding: 15px;
    color: white;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
}
</style>

<!-- Particles JS -->
<div class="particles" id="particles-js"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 80,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#ffffff"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    }
                },
                "opacity": {
                    "value": 0.3,
                    "random": false,
                    "anim": {
                        "enable": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.2,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "push": {
                        "particles_nb": 4
                    }
                }
            },
            "retina_detect": true
        });
    });
</script>
"""
st.markdown(theme_override, unsafe_allow_html=True)

# ----------------------- APP LAYOUT ---------------------------
# Create three columns for layout
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # ----------------------- TITLE ---------------------------
    # More engaging header animation
    lottie_header = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_khzniaya.json")
    st_lottie(lottie_header, height=250, key="header")
    
    st.markdown("<h1 style='text-align: center; margin-top: -20px;'>🚀 JEE Advanced Rank Predictor</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size: 18px;'>
    Welcome to the <span style='background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
    AI-powered predictor</span> to estimate your JEE Advanced Rank!
    </p>
    """, unsafe_allow_html=True)
    
    # ----------------------- INPUT FORM ---------------------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>🧾 Candidate Details</h2>", unsafe_allow_html=True)
    
    marks = st.number_input("Total Marks Obtained", min_value=0.0, value=250.0, step=1.0)
    provided_total_marks = st.number_input("Total Marks of the Exam", min_value=1.0, value=360.0, step=1.0)
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["📊 Subject Marks", "🎯 Category & Difficulty"])
    
    with tab1:
        st.markdown("<h3>📚 Individual Subject Marks</h3>", unsafe_allow_html=True)
        # Put subjects in columns for better layout
        pcol1, pcol2, pcol3 = st.columns(3)
        with pcol1:
            physics = st.number_input("Physics Marks", min_value=0.0, value=80.0, step=1.0)
        with pcol2:
            chemistry = st.number_input("Chemistry Marks", min_value=0.0, value=85.0, step=1.0)
        with pcol3:
            maths = st.number_input("Maths Marks", min_value=0.0, value=85.0, step=1.0)
        
        subject_marks = [physics, chemistry, maths]
        subject_total = provided_total_marks / 3
    
    with tab2:
        st.markdown("<h3>📋 Selection Criteria</h3>", unsafe_allow_html=True)
        
        # Visual category selection
        category = st.selectbox("Select Your Category", ['CRL', 'GEN-EWS', 'OBC-NCL', 'SC', 'ST'])
        
        # Use st.radio for difficulty selection
        difficulty = st.radio("Select Difficulty", ['Easy', 'Avg', 'Hard'], index=1)
        target_bucket = difficulty.lower()
            
        st.markdown(f"<p>Selected difficulty: <b>{target_bucket.upper()}</b></p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # ----------------------- PREDICTION ---------------------------
    if st.button("🔍 PREDICT MY RANK NOW"):
        with st.spinner('⏳ Analyzing your performance...'):
            # Add a bit of animation delay for dramatic effect
            time.sleep(0.5)
            
            # Show a loading animation while "calculating"
            lottie_calc = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_rwq6ciql.json")
            lottie_placeholder = st.empty()
            with lottie_placeholder.container():
                st_lottie(lottie_calc, height=200, key="calculating")
            
            time.sleep(1.5)
            lottie_placeholder.empty()
            
            try:
                result = predictor.predict_ranks(
                    marks=marks,
                    provided_total_marks=provided_total_marks,
                    target_bucket=target_bucket,
                    category=category,
                    subject_marks=subject_marks,
                    subject_total=subject_total
                )
    
                if result['status'] == 'Qualified':
                    st.markdown("<div class='success-msg'>✅ Congratulations! You qualified the JEE Advanced cutoff!</div>", unsafe_allow_html=True)
                    # Show result with animation
                    st.markdown("<div class='result-container'>", unsafe_allow_html=True)
                    st.markdown(f"<h2>🏆 Your Common Rank: <span style='font-size: 2em; color: #FFD700;'>{result['common_rank']}</span></h2>", unsafe_allow_html=True)
                    if category != 'CRL':
                        st.markdown(f"<h3>📊 Your {category} Rank: <span style='font-size: 1.5em; color: #90EE90;'>{result['category_rank']}</span></h3>", unsafe_allow_html=True)
                    # Show a celebration animation
                    lottie_celebrate = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_touohxv0.json")
                    st_lottie(lottie_celebrate, height=150, key="celebration")
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='error-msg'>❌ You did not qualify.</div>", unsafe_allow_html=True)
                    st.markdown(f"<p><b>Reason:</b> {result['reason']}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p>Your Percentage: <b>{result['percentage']}%</b></p>", unsafe_allow_html=True)
                    st.markdown("""
                    <div style='text-align: center; margin-top: 20px;'>
                        <p>Don't give up! Many successful people faced setbacks before achieving greatness.</p>
                    </div>
                    """, unsafe_allow_html=True)
    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    
    # ----------------------- FOOTER ---------------------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>📝 Instructions:</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Fill in your <b>total marks</b> and <b>subject marks</b>.</li>
        <li>Marks should be consistent with the total paper.</li>
        <li><b>Subject marks</b> are used to check whether you cleared cutoff.</li>
        <li><b>CRL</b> = Common Rank List; category ranks are shown only if applicable.</li>
        <li>This is a prediction and may not reflect actual results.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add a floating button for feedback
    st.markdown("""
    <div style='position: fixed; bottom: 20px; right: 20px; background-color: rgba(255,255,255,0.2); padding: 10px; border-radius: 50%; cursor: pointer; backdrop-filter: blur(5px);'>
        <span style='font-size: 24px;'>💬</span>
    </div>
    """, unsafe_allow_html=True)
