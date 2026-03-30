import pandas as pd
import sqlite3
from queries import query_all
import sys
import os
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/src')
from load_sql import get_con

def all_school()-> pd.DataFrame:
    conn = get_con()
    df = pd.read_sql(query_all,conn)
    return df

