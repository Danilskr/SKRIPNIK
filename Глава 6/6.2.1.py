import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import compress
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split 

df = pd.read_csv('heart.csv')

df1 = df[df['target']==0].head(138)
df2 = df[df['target']==1].head(138)
df = pd.concat([df1, df2], ignore_index=True)

plt.rcParams['figure.figsize'] = (10,10)
sns.heatmap(df.drop(['target'], axis=1).corr(), annot=True)
plt.show()

print(df)
print(df['target'].value_counts())


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


X = df[['slope', 'thalach']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=None, stratify=y)


knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

import numpy as np
new_data = np.array([2, 108])
new_data = new_data.reshape(1, -1)
print('STEP3', knn.predict(new_data))
pred_X_test = knn.predict(X_test)
print('STEP4', pred_X_test)

y_pred_prob = knn.predict_proba(X_test)
print('STEP5', y_pred_prob[10:12])

print('STEP6', knn.score(X_test, y_test))

y_pred = knn.predict(X_test)


from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

from sklearn.metrics import confusion_matrix 
print(confusion_matrix(y_test, y_pred))
from sklearn.model_selection import cross_val_score

knn_cv = KNeighborsClassifier(n_neighbors=3)
cv_scores = cross_val_score(knn_cv, X, y, cv=5)
print(cv_scores)
print(cv_scores.mean())

from sklearn.model_selection import GridSearchCV
knn2 = KNeighborsClassifier()
param_grid = {'n_neighbors': np.arange(2, 10)}

knn_gscv = GridSearchCV(knn2, param_grid, cv=5)
knn_gscv.fit(X, y)
print(knn_gscv.best_params_)


