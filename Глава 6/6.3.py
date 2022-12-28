from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv('heart.csv')

def output_column_name(target = 'target'):

    list_name_columns = list(df.columns)
    del_index = list_name_columns.index(target)
    del list_name_columns [del_index]
    return list_name_columns


X = df[output_column_name()]
y = df['target']


X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.30, random_state=1, stratify=y)

clf = MLPClassifier(solver = 'lbfgs', alpha=1e-5, max_iter = 1000, random_state = 0, hidden_layer_sizes = (9,))

scale = StandardScaler()
clf = clf.fit(X_train, y_train)

X_test_scaled = scale.fit_transform(X_test)


print('Вывод исходных данных\n', df)
print('prediction:\n', clf.predict(X_test_scaled))
print('Точность предсказания', clf.score(X_test_scaled, y_test).round(2))