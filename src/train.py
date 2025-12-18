import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from features import transformer

df = pd.read_csv("data/processed/data.csv")

X = df.drop("converted", axis=1)
y = df["converted"]

Xtr, Xval, ytr, yval = train_test_split(X,y,test_size=0.2)

pipe = Pipeline([
    ("features", transformer()),
    ("model", LogisticRegression())
])

mlflow.start_run()
pipe.fit(Xtr, ytr)
acc = pipe.score(Xval, yval)
mlflow.log_metric("accuracy", acc)
mlflow.sklearn.log_model(pipe, "model")
mlflow.end_run()

print("Accuracy:", acc)

