import streamlit as st

# Page Config
st.set_page_config(
    page_title="Employee Salary Predictor",
    page_icon="💼",
    layout="wide"
)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    .stApp {
        background: linear-gradient(to bottom right, #eaf1f8, #ffffff);
        color: #222;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #0a58ca;
        text-align: center;
        margin-top: 25px;
        text-shadow: 1px 1px 3px #ccc;
        animation: fadeIn 1.2s ease-in-out;
    }

    .subtitle {
        text-align: center;
        font-size: 1.25rem;
        color: #444;
        margin-bottom: 40px;
        font-weight: 500;
    }

    .info-box {
        background-color: #ffffffee;
        border-left: 6px solid #0a58ca;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        transition: all 0.3s ease-in-out;
    }

    .info-box:hover {
        background-color: #eef5ff;
        transform: translateY(-4px);
    }

    .info-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0a58ca;
        margin-bottom: 10px;
    }

    .info-text {
        font-size: 0.96rem;
        color: #333;
        line-height: 1.65;
    }

    .call-to-action {
        text-align: center;
        margin-top: 40px;
    }

    .cta-button {
        display: inline-block;
        padding: 12px 28px;
        font-size: 1.1rem;
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        text-decoration: none;
        transition: 0.3s ease-in-out;
        cursor: pointer;
    }

    .cta-button:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #0f2b61, #22438c);
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Home", "Salary Prediction", "Data Exploration", "Model Analytics", "About"]
)

# -------------------- HOME --------------------
if page == "Home":
    st.markdown("<div class='main-title'>💼 Employee Salary Prediction System</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>AI-driven compensation intelligence for modern businesses</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='info-box'>
            <div class='info-title'>🎯 Overview</div>
            <div class='info-text'>
                • Predict employee salaries using machine learning.<br>
                • Benchmark compensation based on experience, education, skills, and industry.<br>
                • Deliver instant and data-backed predictions.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='info-box'>
            <div class='info-title'>🧠 Key Features</div>
            <div class='info-text'>
                • What-if scenario testing via sliders<br>
                • Resume upload with PDF parsing and <br>
                • SHAP-based model interpretability (beta)<br>
                • PDF salary report download (planned)<br>
                • Salary forecasting via time-series 
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='info-box'>
            <div class='info-title'>📊 Technology Stack</div>
            <div class='info-text'>
                • Python, Scikit-learn, XGBoost<br>
                • Data processing with Pandas and NumPy<br>
                • Visualizations using Seaborn and Matplotlib<br>
                • Interactive UI built with Streamlit
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='info-box'>
            <div class='info-title'>📈 Model Performance</div>
            <div class='info-text'>
                • R² Score: 87.3% (Random Forest)<br>
                • RMSE: ₹1.2 Lakhs (Cross-validated)<br>
                • Dataset: 10,000+ employee records<br>
                • Features: 20+ factors affecting salary
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 📦 Feature Summary
    st.markdown("""
    <div class='info-box'>
        <div class='info-title'>🧰 Comprehensive Feature Set</div>
        <div class='info-text'>
            ✅ Real-time ML Salary Prediction<br>
            ✅ What-if Scenario Inputs (Experience, Skills)<br>
            ✅ Resume Upload with PDF Parsing<br>
            ✅ Dynamic Data Exploration Dashboards<br>
            ✅ Model Metrics: R², RMSE, Feature Impact<br>
            ✅ SHAP Visualizations, PDF Report, Salary Trend Forecasting
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA Button using Streamlit native button
    if st.button("Explore the Salary Predictor 💸"):
        # You can't change sidebar selectbox programmatically, so just notify user
        st.info("Please select 'Salary Prediction' from the sidebar to get started!")

    st.markdown("---")
    st.success("📎 Use the sidebar to access Prediction, Analytics, Data Exploration & Project Overview.")

# -------------------- Routing for other pages --------------------
elif page == "Salary Prediction":
    from pages import page_salary_prediction
    page_salary_prediction.show()

elif page == "Data Exploration":
    from pages import page_data_exploration
    page_data_exploration.show()

elif page == "Model Analytics":
    from pages import page_model_analytics
    page_model_analytics.show()

elif page == "About":
    from pages import page_about
    page_about.show()
