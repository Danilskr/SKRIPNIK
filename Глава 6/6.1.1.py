import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('heart.csv')

def output_column_name(target = 'target'):

    list_name_columns = list(df.columns)
    del_index = list_name_columns.index(target)
    del list_name_columns [del_index]
    return list_name_columns


X = df[output_column_name()]
y = df['target']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X.values, y)

def prediction():
    X_new = [30, 1, 0, 145, 233, 1, 0,150,0,2.3, 0, 0, 1]
    print('Справочная информация\n', ' [1] сужение диаметра > 50%\n', '[0] сужение диаметра < 50%\n')
    print('Предсказание:', dtree.predict([X_new]))

print("Вывод исходных данных\n", df)

prediction()

