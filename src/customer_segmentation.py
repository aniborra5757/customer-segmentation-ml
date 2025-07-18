import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # <--- ADD THIS LINE
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib
import os

# Load dataset
data_path = os.path.join("data", "Mall_Customers.csv")
df = pd.read_csv(data_path)

# Select features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.savefig("elbow_plot.png")
plt.close()

# Optimal K = 5 (from Elbow usually)
k = 5
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# Silhouette Score
score = silhouette_score(X_scaled, clusters)
print(f"Silhouette Score: {score:.2f}")

# Plot clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=clusters, palette='Set1', s=100)
plt.title('Customer Segments')
plt.xlabel('Annual Income (scaled)')
plt.ylabel('Spending Score (scaled)')
plt.savefig("cluster_plot.png")
plt.close()

# Save model and scaler
joblib.dump(kmeans, os.path.join("models", "kmeans_model.pkl"))
joblib.dump(scaler, os.path.join("models", "scaler.pkl"))
