"""
Attribution: https://gist.github.com/andreasvc/8317989
@andreasvc on github

Apply PCA to a CSV file and plot its datapoints (one per line).
The first column should be a category (determines the color of each datapoint),
the second a label (shown alongside each datapoint).
"""
import sys
import pandas
import pylab as pl
import sklearn
from sklearn import preprocessing
from sklearn.decomposition import PCA

def plotpca(csvfile, title):
	data = pandas.read_csv(csvfile, index_col=(0, 1))

	# first column provides labels
	ylabels = [a for a, _ in data.index]
	labels = [text for _, text in data.index]
	encoder = preprocessing.LabelEncoder().fit(ylabels)

	xdata = data.to_numpy(data.columns)
	ydata = encoder.transform(ylabels)
	target_names = encoder.classes_
	generate_pca(xdata, ydata, target_names, labels, csvfile, title)


def generate_pca(xdata, ydata, target_names, items, filename, title):
	"""Make plot."""
	pca = PCA(n_components=2)
	components = pca.fit(preprocessing.normalize(xdata)).transform(xdata)

	pl.figure()  # Make a plotting figure
	pl.subplots_adjust(bottom=0.1)

	# NB: a maximum of 7 targets will be plotted
	# CHANGE COLORS HERE
	for i, (c, m, target_name) in enumerate(zip(
			'yrbmmcg', 'o^s*v+x', target_names)):
		pl.scatter(components[ydata == i, 0], components[ydata == i, 1],
				color=c, marker=m, label=target_name)
		for n, x, y in zip(
				(ydata == i).nonzero()[0],
				components[ydata == i, 0],
				components[ydata == i, 1]):
			pl.annotate(
					items[n],
					xy=(x, y),
					xytext=(5, 5),
					textcoords='offset points',
					color=c,
					fontsize='small',
					ha='left',
					va='top')
	pl.legend()
	pl.title(title)
	pl.show()
