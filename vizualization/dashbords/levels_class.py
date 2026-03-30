
import pandas as pd
import sys
import os
import pandas as pd
import sys
import os
import plotly.express as px
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/analytics')
from mean_class import  mean_class, class_levels

def aggression_levels_chart(df=class_levels()):
    df_melted = df.melt(id_vars="class", var_name="category", value_name="count")
    
    def split_category(cat):
        if 'physical' in cat: label = 'Фізична'
        elif 'verbal' in cat: label = 'Вербальна'
        elif 'hostility' in cat: label = 'Ворожість'
        else: label = 'Загальна агресія'
        
        if 'low' in cat: level = '1. Низький'
        elif 'medium' in cat: level = '2. Середній'
        else: level = '3. Високий'
        return label, level

    res = df_melted['category'].apply(split_category)
    df_melted['Metric'] = [x[0] for x in res]
    df_melted['Level'] = [x[1] for x in res]

    fig = px.bar(
        df_melted,
        x="class",
        y="count",
        color="Level",
        facet_row="Metric",
        title="Відсотковий розподіл рівнів агресії по класах",
        text_auto='.1f',  # ДОДАЄМО ЦЕ: відображає значення з одним знаком після коми
        color_discrete_map={
            '1. Низький': '#2ecc71',
            '2. Середній': '#f1c40f',
            '3. Високий': '#e74c3c'
        },
        height=1200,
        labels={"count": "Відсоток учнів", "Level": "Рівень"}
    )

    # Налаштування 100% стеку та позиції тексту
    fig.update_layout(barmode='stack', barnorm='percent')
    
    # Робимо текст всередині стовпців білим або чорним автоматично для контрасту
    fig.update_traces(textposition='inside', insidetextanchor='middle')
    
    # Щоб підписи не зливалися, якщо сегмент замалий
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

    fig.update_xaxes(matches=None, showticklabels=True)
    
    return fig
