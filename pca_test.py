import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


csvfile = "matrix_master_limited.csv"
# csvfile = "outputs/master_T_limited.csv"
data = pd.read_csv(csvfile)

pca = PCA()
pca.fit(preprocessing.normalize(data))
pca.transform(data)

# loading_scores = pd.Series(pca.components_[1])
# print(loading_scores.abs().sort_values(ascending=False)[0:10])

per_var = np.round(pca.explained_variance_ratio_ * 100, decimals = 1)

plt.bar(x=range(1,len(per_var) + 1), height=per_var)
plt.xticks(np.arange(1, len(per_var)+1, 5))
plt.ylabel('% Exp. Variance')
plt.xlabel('PC Component #')
plt.title('Scree Plot For Political Tweets')
plt.show()
