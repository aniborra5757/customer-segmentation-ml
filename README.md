Thanks for the screenshot! You're right — the **README formatting is breaking**, especially in the folder structure and table areas.

Let me give you a **clean, copy-paste `README.md`** that:

* Displays perfectly in GitHub
* Uses proper code blocks and spacing
* Looks good in both light and dark mode

---

### ✅ FINAL CLEAN `README.md` (well-formatted for GitHub)

Copy and paste **exactly this**:

```markdown
# 🛍️ Customer Segmentation using K-Means Clustering

This project segments mall customers into distinct groups based on **Annual Income** and **Spending Score**, using unsupervised machine learning (K-Means). It includes an interactive **Streamlit web app** for live predictions, visualizations, and downloads.

---

## 📌 Project Goals

- Perform customer segmentation using K-Means
- Visualize cluster formation using Elbow and Scatter plots
- Evaluate cluster quality using Silhouette Score
- Build an interactive web app to upload, cluster, and download customer data

---

## 🧠 Tech Stack

| Layer        | Tools Used                      |
|--------------|---------------------------------|
| Language     | Python 3.x                      |
| ML Libraries | scikit-learn, pandas, numpy     |
| Plotting     | matplotlib, seaborn             |
| App Framework| Streamlit                       |
| Deployment   | GitHub + (optional Streamlit Cloud) |

---

## 📁 Project Structure

```

customer-segmentation-ml/
├── app.py
├── cluster\_plot.png
├── elbow\_plot.png
├── data/
│   └── Mall\_Customers.csv
├── models/
│   ├── kmeans\_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── customer\_segmentation.ipynb
├── src/
│   └── customer\_segmentation.py
├── requirements.txt
└── README.md

````

---

## 📊 Dataset

**Source:** [Mall Customers Dataset - Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

**Columns Used:**
- `Annual Income (k$)`
- `Spending Score (1-100)`

---

## 🚀 Setup & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-segmentation-ml.git
cd customer-segmentation-ml
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Model Training (Optional)

```bash
python src/customer_segmentation.py
```

**Outputs:**

* `models/kmeans_model.pkl`
* `models/scaler.pkl`
* `elbow_plot.png`
* `cluster_plot.png`

---

## 🌐 Streamlit App

```bash
streamlit run app.py
```

Open in browser: `http://localhost:8501`

---

## ⚙️ App Features

* Upload CSV with `Annual Income` and `Spending Score`
* Preview raw data and clustered results
* Visualize clusters using scatter plot
* View dataset summary statistics
* Pairplot of features grouped by cluster
* Download clustered CSV file

---

## 📷 Screenshots

### Cluster Visualization

![Cluster Plot](cluster_plot.png)

### Elbow Method

![Elbow Plot](elbow_plot.png)

---

## 🔐 .gitignore

```
venv/
__pycache__/
*.pyc
*.pkl
*.csv
```

---

## 🚀 Deploy to Streamlit Cloud (Optional)

1. Visit: [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Choose your repo and set the file to `app.py`
4. Click **Deploy**

---

## 🔮 Future Enhancements

* Let user select number of clusters (K)
* Use PCA for 2D/3D projection
* Add additional features (e.g., Age, Gender)
* REST API with FastAPI or Flask
* Streamlit dashboard with filters

---

## 👨‍💻 Author

Created by \[aniborra5757]

```

---

✅ This version uses:
- Triple backticks for code blocks
- Proper table and folder tree spacing
- Clean headings and emoji alignment
- Works **perfectly on GitHub preview**

Let me know once you've updated it, or if you'd like a `LICENSE`, deployment badge, or LinkedIn-ready description.
```
