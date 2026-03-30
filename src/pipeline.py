from extract import extract_raw
from transform import transform_columns, transform_data, save_staging
from pathlib import Path
from load_sql import save_to_sql
from calc import calc_agression, save_calc
#from analytics import pass
path_raw = Path('/home/bohdan/Стільниця/school-survey-poject/data/raw')
path_staging = Path('/home/bohdan/Стільниця/school-survey-poject/data/processed/staging.csv')
path_calc = Path('/home/bohdan/Стільниця/school-survey-poject/data/processed/calc.csv')
def run_pipeline():
    raw_df = extract_raw(path_raw)
    staging_df = transform_data(raw_df)
    save_staging(staging_df, path_staging)
    save_to_sql(staging_df, 'staging')
    df_calc = calc_agression(staging_df)
    save_calc(df_calc,path_calc)
    save_to_sql(df_calc, 'calc')
    
   
if __name__ == '__main__':
    run_pipeline()
