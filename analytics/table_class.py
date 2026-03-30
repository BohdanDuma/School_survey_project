import pandas as pd
import sqlite3
from queries import query_table, query_class_list
import sys
import os
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/src')
from load_sql import get_con

def get_class()->list: 
    conn = get_con()
    class_list = pd.read_sql(query_class_list,conn)['class'].tolist() 
    conn.close()
    return class_list
def table_class(param)-> pd.DataFrame:
    conn = get_con()
    df = pd.read_sql(query_table,conn,params=[param])
    conn.close()
    return df
