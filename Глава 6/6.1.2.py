
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pd.read_csv('heart.csv')


def output_column_name(target = 'target'):

    list_name_columns = list(df.columns)
    del_index = list_name_columns.index(target)
    del list_name_columns [del_index]
    return list_name_columns

X = df[output_column_name()]
y = df['target']
dtree = DecisionTreeClassifier()

dtree = dtree.fit(X, y)

features = output_column_name()
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('heart.png')

img=pltimg.imread('heart.png')
imgplot = plt.imshow(img)