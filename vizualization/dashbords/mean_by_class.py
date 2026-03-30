
import pandas as pd
import sys
import os
import pandas as pd
import sys
import os
import plotly.express as px
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/analytics')
from mean_class import  mean_class, class_levels
def mean_class_chart():
    df = mean_class()
    df_melted = df.melt(
        id_vars="class",
        var_name="scale",
        value_name="mean_value"
    )

    fig = px.bar(
        df_melted,
        x="class",
        y="mean_value",
        color="scale",
        facet_col="scale",
        facet_col_wrap=2,      # 2 колонки — це оптимально для читабельності
        title="Аналіз агресії за шкалами",
        height=1700,           
        labels={"mean_value": "Середній бал", "class": "Клас"}
    )
    
    
    # 2. Для X — щоб підписи класів були під кожним квадратом
    fig.update_xaxes(matches=None, showticklabels=True)
    # ДОЗВОЛЯЄМО кожному графіку мати власну шкалу Y
    fig.update_yaxes(matches=None, showticklabels=True)
    
    # Прибираємо префікс "scale=" з заголовків підграфіків
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1].capitalize()))

    # Робимо заголовки жирнішими та підправляємо відступи
    fig.update_layout(
        title_font_size=24,
        showlegend=False,  # Легенда не потрібна, бо назви є над графіками
        margin=dict(t=80, b=50, l=50, r=30)
    )

    return fig


         
