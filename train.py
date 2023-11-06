import pandas as pd
#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

import pickle


df = pd.read_csv('HR Employee Attrition.csv')
df.columns = df.columns.str.lower()

attrition_values = {
    'Yes': 1,
    'No': 0
}
df.attrition = df.attrition.map(attrition_values)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=2)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.attrition.values
y_val = df_val.attrition.values
y_test = df_test.attrition.values
y_full_train = df_full_train.attrition.values

del df_train['attrition']
del df_full_train['attrition']
del df_val['attrition']
del df_test['attrition']

dv = DictVectorizer(sparse=False)

ftrain_dict = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(ftrain_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)

model_regression = LogisticRegression(solver='liblinear', C=10, max_iter=1000)
model_regression.fit(X_full_train, y_full_train)

with open('model.bin', 'wb') as f_out: 
    pickle.dump((dv, model_regression), f_out)