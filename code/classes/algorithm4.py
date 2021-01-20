""""
K means clustering
https://scikit-learn.org/stable/modules/clustering.html#k-means
"""

import load_data
import house
import battery
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()


# houses = make_blobs(n_samples=150, centers=5, n_features=5, cluster_std=1.6)

# points = houses[0]

# kmeans = KMeans(n_clusters = 5)

# kmeans.fit(points)

# plt.scatter(houses[0][:,0], houses[0][:,1])
# plt.savefig('ok.png')