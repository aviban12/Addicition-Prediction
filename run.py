from Dataset2147b1d.Prediction import Linear_predict
from Dataset2147b1d.Preprocess_train import TrainData
from Dataset2147b1d.preprocess_test import TestData
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame([['Patient_ID','Greater_Risk_Probability']])
    TrainData()
    TestData()
    Linear_predict(df)
