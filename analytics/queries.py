import sqlite3
import pandas as pd
import sys
import os
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/src')
import load_sql 
query_mean_by_class = """
    SELECT class,
        AVG(Фізична)        AS фізична,
        AVG(Вербальна)      AS вербальна,
        AVG(Опосередкована)        AS непряма,
        AVG(Негативізм)     AS негативізм,
        AVG(Роздратування)  AS роздратування,
        AVG(Підозріливість)   AS підозрілість,
        AVG(Образа)         AS образа,
        AVG(Провина) AS провина,
        AVG(Індекс_ворожості) AS індекс_ворожості,
        AVG(Індекс_агресивності) AS індекс_агресивності
    FROM calc 
    GROUP BY class
    ORDER BY class
    """
query_class_levels = """
SELECT class,
    SUM(CASE WHEN Індекс_агресивності <= 10 THEN 1 ELSE 0 END) AS low_aggression,
    SUM(CASE WHEN Індекс_агресивності > 10 AND Індекс_агресивності <= 20 THEN 1 ELSE 0 END) AS medium_aggression,
    SUM(CASE WHEN Індекс_агресивності > 20 THEN 1 ELSE 0 END) AS high_aggression,
    SUM(CASE WHEN Фізична <= 25 THEN 1 ELSE 0 END) AS low_aggression_physical,
    SUM(CASE WHEN Фізична > 25 AND Фізична <= 75 THEN 1 ELSE 0 END) AS medium_aggression_physical,
    SUM(CASE WHEN Фізична > 75 THEN 1 ELSE 0 END) AS high_aggression_physical,
    SUM(CASE WHEN Вербальна <= 25 THEN 1 ELSE 0 END) AS low_aggression_verbal,
    SUM(CASE WHEN Вербальна > 25 AND Вербальна <= 75 THEN 1 ELSE 0 END) AS medium_aggression_verbal,
    SUM(CASE WHEN Вербальна > 75 THEN 1 ELSE 0 END) AS high_aggression_verbal,
    SUM(CASE WHEN Індекс_ворожості <= 4 THEN 1 ELSE 0 END) AS low_hostility_index,
    SUM(CASE WHEN Індекс_ворожості > 4 AND Індекс_ворожості <= 9 THEN 1 ELSE 0 END) AS medium_hostility_index,
    SUM(CASE WHEN Індекс_ворожості > 9 THEN 1 ELSE 0 END) AS high_hostility_index

FROM calc
GROUP BY class
ORDER BY class

"""

query_table ="""
SELECT *
FROM calc
WHERE class = ?  
ORDER BY name;
"""
query_all ="""
SELECT
    COUNT(*) AS total_students,
    SUM(Індекс_агресивності > 20) AS high_aggression,
    SUM(Індекс_ворожості > 4) AS високий_індекс_ворожості, -- ТУТ БУЛА ПОМИЛКА (додано кому)
    AVG(Індекс_агресивності) AS avg_aggression,
    AVG(Фізична) AS avg_фізична,
    AVG(Вербальна) AS avg_вербальна,
    AVG(Опосередкована) AS avg_непряма,
    AVG(Негативізм) AS avg_негативізм,
    AVG(Роздратування) AS avg_роздратування,
    AVG(Індекс_ворожості) AS avg_ворожості -- ТУТ БУЛА ПОМИЛКА (прибрано кому)
FROM calc;
"""

query_class_list = "SELECT DISTINCT class FROM calc"