import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib
from src.preprocessing import preprocess_data
from sklearn.pipeline import Pipeline


def train_model(df):

    X = df.drop("salary", axis=1)
    y = df["salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    preprocessor = preprocess_data(X)

    model_pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", XGBRegressor(
            learning_rate=0.04,max_depth=6,n_estimators=385
        ))
    ])

    model_pipeline.fit(X_train, y_train)

    joblib.dump(model_pipeline, "models/final_model.pkl")

    return model_pipeline, X_test, y_test