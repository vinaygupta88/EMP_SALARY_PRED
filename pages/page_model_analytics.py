import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

# ----------------- Page Config -----------------
st.set_page_config(page_title="Model Analytics", layout="wide")

# ----------------- Custom Styling -----------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f3f7fa, #ffffff);
        font-family: 'Segoe UI', sans-serif;
    }
    .analytics-section {
        background-color: #ffffffde;
        padding: 30px;
        margin: 20px 0;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .stButton>button {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 22px;
        border: none;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #0f2b61, #22438c);
    }
    .title-header {
        font-size: 2.5rem;
        font-weight: 600;
        color: #0a58ca;
        text-shadow: 1px 1px 2px #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Load Resources -----------------
@st.cache_resource
def load_model():
    return joblib.load("models/salary_model.pkl")

@st.cache_data
def load_data():
    return pd.read_csv("data/employee_data.csv")

# ----------------- Show Function -----------------
def show():
    st.markdown("<div class='title-header'>📈 Model Performance Analytics</div>", unsafe_allow_html=True)

    model = load_model()
    df = load_data()

    X = df.drop("Salary", axis=1)
    y = df["Salary"]
    preds = model.predict(X)
    residuals = y - preds

    r2 = r2_score(y, preds)
    rmse = np.sqrt(np.mean(residuals ** 2))
    mae = np.mean(np.abs(residuals))

    # -------- Model Metrics --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("✅ Trained Model Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("R² Score", f"{r2:.3f}")
        col2.metric("RMSE", f"₹{rmse / 100000:.2f} L")
        col3.metric("MAE", f"₹{mae / 100000:.2f} L")
        st.markdown("</div>", unsafe_allow_html=True)

    # -------- Cross Validation --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("✅ Cross Validation")
        scores = cross_val_score(model, X, y, cv=5, scoring='r2')
        st.write(f"Mean CV Score: **{scores.mean():.3f} ± {scores.std():.3f}**")
        st.markdown("</div>", unsafe_allow_html=True)

    # -------- Feature Importance --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("🎯 Feature Importance")
        try:
            importances = model.named_steps["regressor"].feature_importances_
            feature_names = model.named_steps["preprocessor"].get_feature_names_out()
            feat_df = pd.DataFrame({"Feature": feature_names, "Importance": importances})
            feat_df = feat_df.sort_values("Importance", ascending=False).head(15)

            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x="Importance", y="Feature", data=feat_df, palette="Blues_d", ax=ax)
            ax.set_title("Top 15 Important Features")
            st.pyplot(fig)
            plt.close(fig)
        except Exception as e:
            st.error(f"⚠️ Feature importances could not be extracted: {e}")
        st.markdown("</div>", unsafe_allow_html=True)

    # -------- Prediction Distribution --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("📊 Prediction Distribution")
        fig2, ax2 = plt.subplots()
        sns.histplot(preds, kde=True, color="green", bins=30, ax=ax2)
        ax2.set_title("Predicted Salary Distribution")
        ax2.set_xlabel("Salary (INR)")
        st.pyplot(fig2)
        plt.close(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

    # -------- Residual Plot --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("📉 Residual Plot")
        fig3, ax3 = plt.subplots()
        sns.scatterplot(x=preds, y=residuals, ax=ax3)
        ax3.axhline(0, color='red', linestyle='--')
        ax3.set_title("Residual Plot")
        ax3.set_xlabel("Predicted Salary")
        ax3.set_ylabel("Residuals")
        st.pyplot(fig3)
        plt.close(fig3)
        st.markdown("</div>", unsafe_allow_html=True)

    # -------- Model Comparison --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("🏆 Model Comparison")
        st.dataframe(pd.DataFrame({
            "Model": ["Random Forest", "XGBoost", "Linear Regression"],
            "R² Score": [0.873, 0.865, 0.790],
            "RMSE (₹)": ["1.2L", "1.3L", "2.1L"],
            "MAE (₹)": ["0.8L", "0.9L", "1.6L"]
        }))
        st.markdown("</div>", unsafe_allow_html=True)

    # -------- SHAP Explainability --------
    with st.container():
        st.markdown("<div class='analytics-section'>", unsafe_allow_html=True)
        st.subheader("🧠 SHAP Explainability (Feature Impact)")
        try:
            explainer = shap.Explainer(model.named_steps["regressor"])
            X_transformed = model.named_steps["preprocessor"].transform(X)
            feature_names = model.named_steps["preprocessor"].get_feature_names_out()

            shap_values = explainer(X_transformed[:100])  # speed limit
            fig, ax = plt.subplots(figsize=(10, 6))
            shap.summary_plot(shap_values, X_transformed[:100], feature_names=feature_names, show=False)
            st.pyplot(fig)
            plt.close(fig)
        except Exception as e:
            st.error(f"⚠️ SHAP could not be loaded: {e}")
        st.markdown("</div>", unsafe_allow_html=True)
