import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

def perform_kmeans(csv_path, k):
    df = pd.read_csv(csv_path)
    df = df.select_dtypes(include=['float64', 'int64'])  # Only numeric columns
    df.dropna(inplace=True)

    kmeans = KMeans(n_clusters=k, random_state=0)
    df['Cluster'] = kmeans.fit_predict(df)

    plt.figure(figsize=(8,6))
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=df['Cluster'], cmap='Set2', s=50)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title(f'Customer Segments using KMeans (k={k})')
    plot_path = os.path.join('static', 'kmeans_plot.png')
    plt.savefig(plot_path)
    plt.close()
    return plot_path
