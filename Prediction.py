import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, LogisticRegressionCV, RidgeClassifierCV
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multioutput import MultiOutputRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeRegressor


def store_csv(complete_data,df):
    """
    :param complete_data:
    :param df:
    :return: df
    """
    my_df1 = pd.DataFrame(complete_data)
    my_df1 = my_df1.T
    df = df.append(my_df1)
    return df

def Linear_predict(df):

    """
    :param df , train_file , test_file , patient_id , X_train ,y_train , X_test:
    :return: nothing -> save the preprocessed data in submission.csv file
    """
    train_file = pd.read_csv("/mnt/1f2870f0-1578-4534-b33f-0817be64aade/projects/Hackerearth/incedo2/Dataset2147b1d/datatrain.csv")
    test_file = pd.read_csv("/mnt/1f2870f0-1578-4534-b33f-0817be64aade/projects/Hackerearth/incedo2/Dataset2147b1d/datatest.csv")
    patient_id = list(test_file['ID'])
    X_train = train_file.drop(['probability'],1)
    y_train = train_file['probability']
    X_test = test_file
    model = RandomForestRegressor()
    model.fit(np.nan_to_num(X_train),np.nan_to_num(y_train))
    predict = model.predict(np.nan_to_num(X_test))
    list_data = []
    for j in predict:
        list_data.append(round(j))
    final = []
    final.append(patient_id)
    final.append(list_data)
    df = store_csv(final,df)
    df.to_csv("submission.csv",index=False, header=False)

if __name__ == "__main__":
    df = pd.DataFrame([['Patient_ID','Greater_Risk_Probability']])
    Linear_predict(df)
