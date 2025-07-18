---

🛍️ Customer Segmentation using K-Means Clustering

This project segments mall customers into distinct groups based on **Annual Income** and **Spending Score**, using unsupervised machine learning (K-Means). It includes an interactive **Streamlit web app** for live predictions, visualizations, and downloads.

---

📌 Project Goals

* Perform customer segmentation using K-Means
* Visualize cluster formation using Elbow and Scatter plots
* Evaluate cluster quality using Silhouette Score
* Build an interactive web app to upload, cluster, and download customer data

---

🧠 Tech Stack

| Layer         | Tools Used                          |
| ------------- | ----------------------------------- |
| Language      | Python 3.x                          |
| ML Libraries  | scikit-learn, pandas, numpy         |
| Plotting      | matplotlib, seaborn                 |
| App Framework | Streamlit                           |
| Deployment    | GitHub + (optional Streamlit Cloud) |

---

📁 Project Structure

```
customer-segmentation-ml/
├── app.py
├── cluster_plot.png
├── elbow_plot.png
├── data/
│   └── Mall_Customers.csv
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── customer_segmentation.ipynb
├── src/
│   └── customer_segmentation.py
├── requirements.txt
└── README.md
```

---

📊 Dataset

Source: [https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

Columns Used:

* `Annual Income (k$)`
* `Spending Score (1-100)`

---

🚀 Setup & Run Locally

1. Clone the Repository

```bash
git clone https://github.com/aniborra5757/customer-segmentation-ml.git
cd customer-segmentation-ml
```

2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On macOS/Linux
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

🏋️‍♂️ Train the Model (Optional)

```bash
python src/customer_segmentation.py
```

Outputs:

* models/kmeans\_model.pkl
* models/scaler.pkl
* elbow\_plot.png
* cluster\_plot.png
* Silhouette Score in terminal

---

🌐 Run the Streamlit App

```bash
streamlit run app.py
```

Open in browser: [http://localhost:8501](http://localhost:8501)

---

⚙️ App Features

* Upload a CSV with Annual Income and Spending Score
* View raw and clustered data
* View cluster scatter plot
* View data summary statistics
* View pairplot by clusters
* Download clustered CSV file

---

📷 Screenshots

Cluster Plot
(elbow\_plot.png and cluster\_plot.png will be rendered here on GitHub if pushed)

---

🔐 .gitignore

```
venv/
__pycache__/
*.pyc
*.pkl
*.csv
```

---

🚀 Deploy to Streamlit Cloud

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Select this repo and choose `app.py`
4. Click Deploy

---

🔮 Future Enhancements

* Allow user to change number of clusters (K)
* Add PCA-based visualization
* Add more features like Age, Gender
* REST API with FastAPI or Flask
* Dashboard UI with filters

---

👨‍💻 Author

Created by aniborra5757
