---

```markdown
# 🛍️ Customer Segmentation using K-Means

Segment mall customers based on their Annual Income and Spending Score using K-Means Clustering. This helps identify distinct customer groups for targeted marketing and business insights.

---

## 📂 Project Structure

```

customer-segmentation-ml/
├── data/                # Dataset (Mall\_Customers.csv)
├── models/              # Trained KMeans model and scaler
├── notebooks/           # Optional Jupyter EDA (not added yet)
├── src/                 # Main clustering script
├── elbow\_plot.png       # Elbow Method result
├── cluster\_plot.png     # Final cluster visualization
├── requirements.txt     # Python dependencies
└── README.md            # Project overview

````

---

## 📊 Dataset

- File: `Mall_Customers.csv`
- Source: [Kaggle - Mall Customers Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- Features Used:
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

---

## ⚙️ How to Run

1. Clone or download this repository.
2. Create a virtual environment and activate it.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt

````

4. Run the main script:

   ```bash
   python src/customer_segmentation.py
   ```

5. View outputs:

   * `elbow_plot.png` → Elbow method plot to find optimal clusters
   * `cluster_plot.png` → Visualization of customer segments

---

## ✅ Output

* 🎯 **Silhouette Score** is printed in the terminal.
* 🧠 Saved models:

  * `models/kmeans_model.pkl`
  * `models/scaler.pkl`

---

## 🚀 Future Enhancements

* Apply PCA for better visualization in 2D/3D
* Add a Jupyter Notebook version for step-by-step exploration
* Create a Streamlit app for interactive segmentation
* Deploy model as a web API

---

## 📸 Screenshots

You can include images of `elbow_plot.png` and `cluster_plot.png` here after pushing to GitHub for better preview.

---

## 🛠️ Tech Stack

* Python 3.x
* Scikit-learn
* Pandas, NumPy
* Matplotlib, Seaborn
* Joblib

```

---

Let me know when you're ready to:
- Add notebook version
- Start GitHub deployment steps
- Or move on to another project 🚀
```
