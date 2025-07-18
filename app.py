import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Load model and scaler
model = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(page_title="Customer Segmentation", layout="centered")
st.title("🛍️ Customer Segmentation App")
st.write("This app segments customers based on Annual Income and Spending Score using K-Means clustering.")

uploaded_file = st.file_uploader("📂 Upload your customer CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Raw Data")
    st.dataframe(df.head())

    try:
        X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
        X_scaled = scaler.transform(X)

        clusters = model.predict(X_scaled)
        df['Cluster'] = clusters

        st.subheader("📊 Clustered Data")
        st.dataframe(df)

        st.subheader("🎯 Cluster Visualization")
        fig, ax = plt.subplots(figsize=(8,6))
        sns.scatterplot(
            x=X_scaled[:, 0],
            y=X_scaled[:, 1],
            hue=clusters,
            palette='Set2',
            s=100,
            ax=ax
        )
        ax.set_xlabel('Annual Income (scaled)')
        ax.set_ylabel('Spending Score (scaled)')
        ax.set_title('Customer Segments')
        st.pyplot(fig)

        # ➕ Additional Feature 1: Data Summary
        st.subheader("📈 Data Summary")
        st.dataframe(df.describe())

        # ➕ Additional Feature 2: Pairplot
        st.subheader("📷 Pairplot of Features by Cluster")
        with st.spinner("Generating pairplot..."):
            pair_df = df[['Annual Income (k$)', 'Spending Score (1-100)', 'Cluster']]
            pair_fig = sns.pairplot(pair_df, hue="Cluster", palette="Set2")
            st.pyplot(pair_fig)

        # ➕ Additional Feature 3: Download CSV
        st.subheader("⬇️ Download CSV with Cluster Labels")
        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        st.download_button("Download CSV", buffer, file_name="clustered_customers.csv", mime="text/csv")

    except Exception as e:
        st.error("⚠️ Error: Ensure your CSV has columns: 'Annual Income (k$)', 'Spending Score (1-100)'")
        st.code(str(e))
else:
    st.info("Please upload a CSV file to begin.")
