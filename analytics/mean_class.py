import pandas as pd
import sqlite3
from queries import query_mean_by_class, query_class_levels
import sys
import os
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/src')
from load_sql import get_con

def mean_class()-> pd.DataFrame:
    conn = get_con()
    df = pd.read_sql(query_mean_by_class,conn)
    return df
def class_levels():
    conn = get_con()
    df = pd.read_sql(query_class_levels, conn)
    conn.close()
    return df
if __name__ == '__main__':
    print(mean_class().head())
    print(class_levels().head())
