import streamlit as st
import requests
import pandas as pd
import plotly.express as px

BASE_URL = "http://127.0.0.1:5000"

st.title("📊 Data Visualization Dashboard")

# Upload File
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    # Save file locally
    with open("uploaded.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload to Flask API
    files = {"file": open("uploaded.csv", "rb")}
    response = requests.post(f"{BASE_URL}/upload", files=files)

    if response.status_code == 200:
        st.sidebar.success("File uploaded successfully!")

        # Fetch Data
        params = {"file": "uploaded.csv"}
        data_response = requests.get(f"{BASE_URL}/data", params=params)

        if data_response.status_code == 200:
            df = pd.DataFrame(data_response.json()["preview"])
            st.subheader("📜 Data Preview")
            st.write(df)

            # Fetch Numeric Columns
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

            if numeric_columns:
                st.subheader("📊 Interactive Graphs")

                # Dropdown for X and Y axes
                x_axis = st.selectbox("Select X-axis", numeric_columns, index=0)
                y_axis = st.selectbox("Select Y-axis", numeric_columns, index=1 if len(numeric_columns) > 1 else 0)

                # Chart Type Selector
                chart_type = st.radio("Choose Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot"])

                # Generate Graph
                if chart_type == "Bar Chart":
                    fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart of {x_axis} vs {y_axis}")
                elif chart_type == "Line Chart":
                    fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart of {x_axis} vs {y_axis}")
                elif chart_type == "Scatter Plot":
                    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot of {x_axis} vs {y_axis}")

                st.plotly_chart(fig)
            else:
                st.warning("⚠ No numeric columns found for visualization.")

    else:
        st.sidebar.error("Error uploading file!")
