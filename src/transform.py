import pandas as pd
import numpy as np
try:
    df = pd.read_csv('/home/bohdan/Стільниця/school-survey-poject/data/raw/Методика скринінг  (Ответы) - Ответы на форму (1).csv')
except FileNotFoundError:
    raise FileNotFoundError('Raw file not found at /home/bohdan/Стільниця/school-survey-poject/data/raw')
def transform_columns(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.rename(columns = {'Отметка времени': 'timestamp', 'Прізвище': 'name', 'Клас': 'class', 'Стать' : 'gender','Чи займаєтесь ви спортом?': 'Sport_YN', 'Яким видом?(Якщо ні то напишіть:"Ні")':'Kind_sport'}) 
    for i, col in enumerate(df.columns[6:]):
        df = df.rename(columns={col: f"Q{i+1}"})
    print('All is done') 
    print(df.columns)   
    return df
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = transform_columns(df)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d.%m.%Y %H:%M:%S')
    pattern = r'(\d+).*?([а-яА-ЯіІїЇєЄa-zA-Z])'
    df['gender'] = np.where(df['gender'].str.lower() == 'чоловіча', 'Ч', 'Ж')
    extracted = df['class'].str.extract(pattern, expand=True)
    df['class'] = extracted[0]+ extracted[1].fillna('').str.upper()
    df['class'] = df['class'].ffill().bfill()
   
    for i in df.columns[6:]: 
        condition = (df[i] == 'Так')|(df[i] == 'Можливо, так')  
        df[i] = np.where(condition, '+', '-') 
    map_dict = {
        '1-2 рази на тиждень':'1-2',
        '3 рази на тиждень':'3',
        '4 - 5 разів на тиждень':'4-5', 
        'Ні':'0',
        'більше 5 разів на тиждень': '5-6'
    }
    df['Sport_YN'] = df['Sport_YN'].map(map_dict)  
    return df

def save_staging(df: pd.DataFrame, path: str) -> None:  
    df.to_csv(path)
df = transform_columns(df)
df = transform_data(df)
