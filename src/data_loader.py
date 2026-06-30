import sqlite3
import pandas as pd
import numpy as np


def load_data(data):
    df = pd.read_csv(data)

    conn = sqlite3.connect("Employee Salary Prediction.db")

    df.to_sql(
        "employee_table",
        conn,
        if_exists="replace",
        index=False
    )

    Query = "SELECT * FROM employee_table"

    final_df = pd.read_sql_query(Query,conn)

    conn.close()

    return final_df