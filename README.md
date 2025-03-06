# 📊 Data Visualization Dashboard

## **Overview**
The **Data Visualization Dashboard** is a full-stack web application that enables users to upload CSV datasets or fetch data from an SQL database for interactive analysis. The dashboard provides data previews, statistical summaries, and various visualization options to help users explore insights efficiently.

## **Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Flask
- **Database:** PostgreSQL / MySQL / SQLite
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly, Matplotlib
- **Deployment:** Render / Railway (Backend), Streamlit Cloud (Frontend)

## **Features**
✅ Upload CSV files for analysis  
✅ Fetch real-time data from an SQL database  
✅ Display data preview with missing values & statistical summary  
✅ Generate interactive charts (Bar, Line, Scatter, Histogram, Box Plot)  
✅ Export charts as PNG for reporting  
✅ Fully deployed for easy access  

## **Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/data-visualization-dashboard.git
cd data-visualization-dashboard
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run Flask Backend**
```bash
python app.py
```
_Backend runs on **http://127.0.0.1:8501**_

### **5️⃣ Run Streamlit Frontend**
```bash
streamlit run dashboard.py
```

## **Usage**
1️⃣ Upload a CSV file or enter an SQL query  
2️⃣ View the data preview and statistics  
3️⃣ Select the type of chart and adjust parameters  
4️⃣ Download the generated chart as PNG  

## **Deployment**
### **Backend (Flask) on Render**
- Push code to GitHub
- Connect GitHub repo to Render
- Set **Start Command:** `gunicorn app:app`
- Deploy & get backend URL

### **Frontend (Streamlit) on Streamlit Cloud**
- Go to Streamlit Cloud
- Connect GitHub repo
- Deploy `dashboard.py`
- Update `BASE_URL` in `dashboard.py` with Flask API URL

## **Future Enhancements**
- [ ] Export reports as PDF
- [ ] Add AI-based insights & predictions
- [ ] Enhance UI with theme customization
- [ ] Implement user authentication



## **Contributing**
Pull requests are welcome! Please open an issue first to discuss changes.  

