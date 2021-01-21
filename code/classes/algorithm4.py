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
import pandas as pd
from pandas import DataFrame


reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

data = pd.DataFrame(columns=['x', 'y'])
