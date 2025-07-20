import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Cache the data loading for performance
@st.cache_data
def load_data():
    return pd.read_csv("data/employee_data.csv")  # Adjust path if needed

def show():
    st.title("📊 Data Exploration & Insights")

    # Load dataset
    df = load_data()

    # Dataset overview
    st.subheader("📋 Dataset Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Employees", len(df))
    col2.metric("Features", len(df.columns))
    col3.metric("Avg Salary", f"₹{df['Salary'].mean() / 100000:.2f} L")
    col4.metric("Salary Range", f"₹{df['Salary'].min() / 100000:.2f} L - ₹{df['Salary'].max() / 100000:.2f} L")

    # Filters
    st.subheader("🎛️ Data Filters")
    col1, col2, col3 = st.columns(3)

    departments = ["All"] + sorted(df["Department"].unique())
    cities = ["All"] + sorted(df["CityTier"].unique())
    dept = col1.selectbox("Department", departments)
    city = col2.selectbox("City Tier", cities)
    exp_range = col3.slider(
        "Years of Experience Range",
        float(df["Experience"].min()),
        float(df["Experience"].max()),
        (float(df["Experience"].min()), float(df["Experience"].max()))
    )

    # Apply filters
    filtered_df = df.copy()
    if dept != "All":
        filtered_df = filtered_df[filtered_df["Department"] == dept]
    if city != "All":
        filtered_df = filtered_df[filtered_df["CityTier"] == city]
    filtered_df = filtered_df[(filtered_df["Experience"] >= exp_range[0]) & (filtered_df["Experience"] <= exp_range[1])]

    st.write(f"🔍 Filtered Dataset: {len(filtered_df)} employees")
    st.dataframe(filtered_df.head(10))

    # Salary Analysis Boxplot
    st.subheader("📈 Salary Analysis")
    if len(filtered_df) > 0:
        fig = px.box(
            filtered_df,
            x="Department",
            y="Salary",
            color="Department",
            title="Salary Distribution by Department"
        )
        st.plotly_chart(fig, use_container_width=True)

        # Demographics pie charts
        st.subheader("👥 Demographics")
        col1, col2 = st.columns(2)
        with col1:
            fig = px.pie(filtered_df, names="Gender", title="Gender Distribution")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.pie(filtered_df, names="Education", title="Education Level")
            st.plotly_chart(fig, use_container_width=True)

        # Company Insights Bar Chart
        st.subheader("🏢 Company Insights")
        company_avg_salary = filtered_df.groupby("CompanyType")["Salary"].mean().reset_index()
        fig = px.bar(
            company_avg_salary,
            x="CompanyType",
            y="Salary",
            title="Avg Salary by Company Type",
            color="CompanyType"
        )
        st.plotly_chart(fig, use_container_width=True)

        # Correlation Heatmap (Numerical Features)
        st.subheader("📊 Correlation Heatmap (Numerical)")
        num_df = filtered_df.select_dtypes(include=['float64', 'int64'])
        corr = num_df.corr()

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("⚠️ No data available for selected filters.")


