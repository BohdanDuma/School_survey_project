import pandas as pd
import numpy as np
from pathlib import Path
df = pd.read_csv(Path('/home/bohdan/Стільниця/school-survey-poject/data/processed/staging.csv')) 
scales = {
        'Фізична': {'Q1':'+', 'Q9':'-', 'Q17':'-', 'Q25':'+', 'Q33':'+', 'Q41':'+', 'Q48':'+', 'Q55':'+', 'Q62':'+', 'Q68':'+'},
        'Вербальна': {'Q7':'+', 'Q15':'+', 'Q23':'+', 'Q31':'+', 'Q39':'-', 'Q46':'+', 'Q53':'+', 'Q60':'+', 'Q66':'-', 'Q71':'+', 'Q73':'+', 'Q74':'-', 'Q75':'-'},
        'Опосередкована': {'Q2':'+', 'Q10':'+', 'Q18':'+', 'Q26':'-', 'Q34':'+', 'Q42':'+', 'Q49':'-', 'Q56':'+', 'Q63':'+'},
        'Негативізм': {'Q4':'+', 'Q12':'+', 'Q20':'+', 'Q28':'+', 'Q36':'-'},
        'Роздратування': {'Q6':'+', 'Q11':'-', 'Q19':'+', 'Q27':'+', 'Q35':'-', 'Q43':'+', 'Q50':'+', 'Q57':'+', 'Q64':'+', 'Q69':'-', 'Q72':'+'},
        'Підозріливість': {'Q6':'+', 'Q14':'+', 'Q22':'+', 'Q30':'+', 'Q38':'+', 'Q45':'+', 'Q52':'+', 'Q59':'+', 'Q65':'-', 'Q70':'-'},
        'Образа': {'Q5':'+', 'Q13':'+', 'Q21':'+', 'Q29':'+', 'Q37':'+', 'Q44':'+', 'Q51':'+', 'Q58':'+'},
        'Провина': {'Q8':'+', 'Q16':'+', 'Q24':'+', 'Q32':'+', 'Q40':'+', 'Q47':'+', 'Q54':'+', 'Q61':'+', 'Q7':'+'}
    }
def calc_agression(df: pd.DataFrame) -> pd.DataFrame:
    df_calc = df[['name', 'class', 'gender', 'Sport_YN']].copy()
    for scale_name,keys in scales.items():
        score = 0
        for q_key, expected in keys.items():
            if q_key in df.columns:
                score += (df[q_key] == expected).astype(int)
        df_calc[scale_name] = score
    df_calc['Індекс_ворожості'] = round(((df_calc['Образа'] + df_calc['Підозріливість'])/2),0)
    df_calc['Індекс_агресивності'] = round(((df_calc['Фізична'] + df_calc['Вербальна'] + df_calc['Опосередкована'])),0)
    df_calc['Фізична'] = df_calc['Фізична'] * 10
    df_calc['Вербальна'] = df_calc['Вербальна'] * 7.7
    df_calc['Опосередкована'] = df_calc['Опосередкована'] * 11
    df_calc['Негативізм'] = df_calc['Негативізм'] * 20
    df_calc['Роздратування'] = df_calc['Роздратування'] * 9
    df_calc['Підозріливість'] = df_calc['Підозріливість'] * 10
    df_calc['Образа'] = df_calc['Образа'] * 12.5
    df_calc['Провина'] = df_calc['Провина'] * 11
  
    return df_calc
def save_calc(df: pd.DataFrame, path: str) -> None:  
    df.to_csv(path)
    print('Calc is saved')
    

