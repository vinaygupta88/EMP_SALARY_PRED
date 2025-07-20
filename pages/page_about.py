import streamlit as st
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f6f9fc, #ffffff);
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #11457e;
    font-weight: 700;
}
.stMarkdown {
    font-size: 16px;
}
.stButton>button {
    background-color: #11457e;
    color: white;
    border-radius: 8px;
    padding: 8px 20px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background-color: #0c3b6e;
    transform: scale(1.03);
}
[data-testid="stMetricValue"] {
    color: #0a58ca;
    font-weight: 600;
}
div[data-testid="column"] {
    padding: 1rem;
    background: #ffffffd4;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

def show():
    st.title("ℹ️ About the Employee Salary Prediction System")

    st.markdown("### 🎯 Project Overview")
    st.write("""
    The **Employee Salary Prediction System** is a comprehensive machine learning application built to estimate employee salaries in the Indian job market.  
    It demonstrates advanced data science and machine learning techniques within a real-world HR analytics context.
    """)

    st.markdown("### 🔧 Technical Implementation")
    st.write("""
    **Machine Learning Pipeline**:
    - **Data Generation**: Synthetic employee dataset with over 10,000 records  
    - **Data Preprocessing**: Handling missing values, outliers, and scaling  
    - **Feature Engineering**: Creating domain-driven features and interactions  
    - **Model Training**: Algorithms like Random Forest, XGBoost, and Linear Regression  
    - **Model Evaluation**: Cross-validation, performance metrics, feature importance  
    - **Deployment**: Fully interactive web application using Streamlit
    """)

    st.markdown("### 🛠️ Technologies Used")
    st.markdown("""
    - **Python** – Core programming language  
    - **Pandas & NumPy** – Data manipulation  
    - **Scikit-learn** – Machine learning and preprocessing  
    - **XGBoost** – Boosting algorithm  
    - **Streamlit** – Web app deployment  
    - **Plotly & Seaborn** – Visualizations  
    - **Jupyter Notebook** – Development & EDA
    """)

    st.markdown("### 📊 Dataset Features")
    st.write("""
    This model analyzes 20+ features, including:
    - Personal demographics (age, gender, education)  
    - Experience level and technical skills  
    - Job title, department, and performance  
    - Geographic location and city tier  
    - Company type and size  
    - Certifications and English proficiency  
    """)

    st.markdown("### 📈 Key Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Prediction Accuracy", "87.3%")
    col2.metric("Dataset Size", "10,000+ Records")
    col3.metric("Features Analyzed", "20+")

    col4, col5, col6 = st.columns(3)
    col4.metric("Model Types", "4 Algorithms")
    col5.metric("Cities Covered", "22 Indian Cities")
    col6.metric("Salary Range", "₹2L – ₹50L")

    st.markdown("### 🎯 Business Applications")
    st.markdown("""
    - **HR Analytics**: Salary benchmarking and compensation planning  
    - **Recruitment**: Estimating fair salary offers  
    - **Budget Planning**: Workforce cost forecasting  
    - **Market Research**: Trend analysis and policy planning  
    - **Performance Management**: Objective salary evaluation  
    """)

    st.markdown("### 🔬 Technical Deep Dive")

    with st.expander("🔍 Data Pipeline"):
        st.write("""
        - Business logic-based realistic employee profiles  
        - Dynamic salary generation with influencing factors  
        - Missing values and noise for real-world simulation  
        """)

    with st.expander("🧹 Data Cleaning"):
        st.write("""
        - Imputation with KNN and statistical strategies  
        - Outlier detection using IQR and Z-score  
        - Validating and type-casting structured data  
        """)

    with st.expander("🛠 Feature Engineering"):
        st.write("""
        - New features from domain knowledge  
        - Interaction and polynomial features  
        - Label encoding and scaling for models  
        """)

    with st.expander("📌 Feature Selection"):
        st.write("""
        - Univariate selection using statistical tests  
        - Recursive Feature Elimination (RFE)  
        - Feature importance from Random Forest  
        """)

    st.markdown("### 🚀 Internship Project - AIML Track")
    st.success("✅ Built with ❤️ using Python, Streamlit, and Machine Learning")
    st.info("This project demonstrates complete ML pipeline development — from synthetic data generation to real-time prediction interface.")
