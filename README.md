🚀 JEE Advanced Rank Predictor
An interactive, AI-powered web app that predicts your JEE Advanced rank based on your score, category, difficulty level, and subject-wise performance. Built with Streamlit and powered by real historical data across categories and years.

👉 Live App: https://jeeadvancedbestrankguru.streamlit.app

🔍 Features
Predicts Common Rank List (CRL) and category-wise ranks (GEN-EWS, OBC-NCL, SC, ST)

Accepts inputs like total marks, category, subject-wise marks, and paper difficulty

Uses real JEE Advanced data (2016–2022) for prediction

Beautiful interface using Streamlit and Lottie animations

Fast & responsive — deploys instantly on Streamlit Cloud

🧠 Tech Stack
Python 3.9.6

Streamlit 1.32.2

NumPy, Pandas, Scikit-learn, XGBoost, Joblib

Streamlit-Lottie for animated illustrations

📁 Files and Structure
app.py → Main Streamlit app

model.py → Rank prediction logic and dataset

jee_predictor.pkl → Serialized ML model

requirements.txt → All required dependencies

runtime.txt → Python version for deployment

Procfile → Deployment configuration (for Heroku or other platforms)

🧪 How to Run Locally
Clone the repo

Create and activate a virtual environment

Install the dependencies

Run the app using Streamlit

bash
Copy
Edit
git clone https://github.com/your-username/JEEAdvanced-Rank-Predictor.git  
cd JEEAdvanced-Rank-Predictor  
python3 -m venv venv  
source venv/bin/activate  (or venv\Scripts\activate on Windows)  
pip install -r requirements.txt  
streamlit run app.py  
🚀 Deployment Notes
This app is deployed on Streamlit Cloud, but you can also deploy it on Heroku, Render, or Railway.

Just make sure the following files are present in your repository:

app.py

requirements.txt

runtime.txt

Procfile

jee_predictor.pkl

model.py

🙌 Acknowledgements
Rank & score data sourced from past JEE Advanced results

UI powered by Streamlit and Lottie animations

Thanks to open-source contributors and forums for insights and support

📄 License
Licensed under the MIT License — free to use for personal, educational, or academic purposes.
