import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline


def preprocess_data(df):
    
    numerical_col = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_col = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    numerical_pipeline = Pipeline(steps=[
        ("scaler", StandardScaler())
    ])
    categorical_pipeline = Pipeline(steps=[
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_pipeline, numerical_col),
            ("cat", categorical_pipeline, categorical_col)
        ]
    )

    return preprocessor
