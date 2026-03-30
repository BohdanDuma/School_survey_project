import sqlite3 
import pandas as pd
from pathlib import Path
DB_PATH = Path('/home/bohdan/Стільниця/school-survey-poject/data/db/survey.db')
def get_con():
    return sqlite3.connect(DB_PATH)
def save_to_sql(df: pd.DataFrame, table_name: str):
    conn = get_con()
    df.to_sql(table_name, conn, if_exists='replace',index=False)
    conn = sqlite3.connect(DB_PATH)
    tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

    print(tables)#перевірка які таблиці зберегло в базу

    conn.close()