import streamlit as st
import pandas as pd
import joblib
from fpdf import FPDF
import datetime
import os
from PyPDF2 import PdfReader

# ------------------- Page Styling -------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f4f7fc, #ffffff);
        font-family: 'Segoe UI', sans-serif;
    }
    .title-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0a58ca;
        padding-bottom: 1rem;
        text-shadow: 1px 1px 2px #ccc;
    }
    .input-section {
        background-color: #ffffffd8;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        transition: 0.3s ease-in-out;
    }
    .input-section:hover {
        background-color: #eef4ff;
    }
    .stButton>button {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #0f2b61, #22438c);
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    }z
    </style>
""", unsafe_allow_html=True)

def show():
    st.markdown("<div class='title-header'>🔮 Salary Prediction Tool</div>", unsafe_allow_html=True)

    # Load your trained pipeline model (ensure correct path)
    model = joblib.load("models/salary_model.pkl")

    with st.container():
        st.markdown("<div class='input-section'>", unsafe_allow_html=True)
        st.subheader("👤 Enter Employee Information")

        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Age", 22, 60, 30)
            gender = st.selectbox("Gender", ["Male", "Female"])
            education = st.selectbox("Education Level", ["High School", "Bachelors", "Masters", "PhD"])
            experience = st.slider("Years of Experience", 0.0, 40.0, 2.0)
            department = st.selectbox("Department", ["Tech", "HR", "Finance", "Marketing", "Operations", "Support"])
            title = st.selectbox("Job Title", ["Engineer", "Manager", "Analyst", "Lead", "Executive"])
        with col2:
            performance = st.slider("Performance Rating (1-5)", 1, 5, 3)
            city = st.selectbox("City Tier", ["Tier 1", "Tier 2", "Tier 3"])
            size = st.selectbox("Company Size", ["Startup", "Mid", "Enterprise"])
            ctype = st.selectbox("Company Type", ["Private", "Public", "MNC"])
            tech = st.slider("Technical Skills Score (0-100)", 0, 100, 60)
            certs = st.slider("Number of Certifications", 0, 10, 2)
            english = st.selectbox("English Proficiency", ["Basic", "Intermediate", "Advanced"])

        st.markdown("</div>", unsafe_allow_html=True)

    # Prepare input dataframe with raw categorical strings
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Education": education,
        "Experience": experience,
        "Department": department,
        "Title": title,
        "Performance": performance,
        "CityTier": city,
        "CompanySize": size,
        "CompanyType": ctype,
        "TechSkill": tech,
        "Certs": certs,
        "English": english
    }])

    prediction = None
    if st.button("💰 Predict Salary"):
        try:
            prediction = model.predict(input_df)[0]
            st.subheader(f"💸 Predicted Salary: ₹{int(prediction):,}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

    # Resume Upload (Optional PDF Parsing)
    with st.expander("📄 Upload Resume (Optional PDF Parsing)"):
        uploaded_file = st.file_uploader("Upload Resume", type="pdf", key="resume_upload")
        if uploaded_file:
            try:
                reader = PdfReader(uploaded_file)
                text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
                st.text_area("📑 Extracted Resume Text", text, height=250)
            except Exception as e:
                st.error(f"⚠️ Error reading PDF: {e}")

    # PDF Report Generation
    def generate_pdf(salary, inputs):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Employee Salary Prediction Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Predicted Salary: ₹{int(salary):,}", ln=True)

        for k, v in inputs.items():
            pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)

        os.makedirs("downloads", exist_ok=True)
        filename = f"Salary_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(f"downloads/{filename}")
        return filename

    if prediction:
        if st.button("📄 Download Salary Report"):
            try:
                filename = generate_pdf(prediction, input_df.iloc[0].to_dict())
                st.success(f"Report generated: downloads/{filename}")
            except Exception as e:
                st.error(f"Failed to generate report: {e}")
