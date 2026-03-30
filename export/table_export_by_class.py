import pandas as pd
import sys
import os
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/analytics')
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/vizualization/dashbords')
from class_table import class_detail_dashboard
from table_class import  get_class, table_class
from mean_by_class import mean_class_chart
from all_school_viz import save_combined_report
from levels_class import aggression_levels_chart 
def make_excel_dashbords() -> pd.DataFrame:   
    all_classes = get_class()
    print(f"Доступні класи: {all_classes}")
    for i in all_classes:
        if all_classes:
            class_detail_dashboard(i)
            result_df = class_detail_dashboard(i)
            file_path = os.path.join('/home/bohdan/Стільниця/school-survey-poject/export/tables_for_each_class', f"{i}.xlsx")
            result_df.to_excel(file_path, index = False)
            print(f'Excel {i} made!')
def make_html_for_mean():
    df_mean = mean_class_chart()
    file_path = os.path.join('/home/bohdan/Стільниця/school-survey-poject/export/Середні_по_класах', f"Середні по класах.html")
    df_mean.write_html(file_path)
    print('Файл сердні значення збережено в html')
def make_html_for_levels():
    df_level = aggression_levels_chart()
    file_path = os.path.join('/home/bohdan/Стільниця/school-survey-poject/export/Середні_по_класах', f"Рівні.html")
    df_level.write_html(file_path)
    print('Файл сердні значення збережено в html')

f_path = '/home/bohdan/Стільниця/school-survey-poject/export/report.html'


if __name__ == '__main__':
    make_excel_dashbords()
    make_html_for_mean()      
    make_html_for_levels()  
    save_combined_report(f_path)
            
