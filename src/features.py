from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUM = ["call_duration","calls_last_7_days","hour_of_day"]
CAT = ["campaign_source"]

def transformer():
    return ColumnTransformer([
        ("num", StandardScaler(), NUM),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CAT)
    ])

