🚀 JEE Advanced Rank Predictor
An interactive, AI-powered web app that predicts your JEE Advanced rank based on your score, category, difficulty level, and subject-wise performance. Built with Streamlit and powered by real historical data across multiple years and categories.
👉 Live App: https://jeeadvancedbestrankguru.streamlit.app

🔍 Features

Predicts Common Rank List (CRL) and category-wise ranks (GEN-EWS, OBC-NCL, SC, ST)

Accepts total marks, category, subject-wise marks, and paper difficulty

Uses real JEE Advanced data from 2016 to 2024

Beautiful UI with Lottie animations

Fast and responsive, deployed on Streamlit Cloud

🧠 Tech Stack

Python 3.9.6

Streamlit 1.32.2

NumPy, Pandas, Scikit-learn, XGBoost, Joblib

Streamlit-Lottie

📁 Files and Structure
app.py → Main Streamlit app
model.py → Rank prediction logic and dataset
jee_predictor.pkl → Serialized ML model
requirements.txt → Project dependencies
runtime.txt → Python version for deployment
Procfile → For Heroku or Render deployment

🧪 How to Run Locally

Clone the repo

Create and activate a virtual environment

Install dependencies

Run the app using Streamlit

Commands:
git clone https://github.com/your-username/JEEAdvanced-Rank-Predictor.git
cd JEEAdvanced-Rank-Predictor
python3 -m venv venv
source venv/bin/activate (on Windows: venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py

🚀 Deployment Notes
This app is deployed on Streamlit Cloud, but can also be deployed on Heroku, Render, or Railway.
Make sure the following files are in your GitHub repo:

app.py

model.py

jee_predictor.pkl

requirements.txt

runtime.txt

Procfile

🙌 Acknowledgements
Rank and score data manually sourced from official JEE Advanced results.
UI built with Streamlit and Lottie animations.
Thanks to open-source contributors and educational forums.

📄 License
MIT License — free for personal, educational, or academic us
