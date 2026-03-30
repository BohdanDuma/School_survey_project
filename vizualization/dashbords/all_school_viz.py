import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import sys
import os
import pandas as pd
import sys
import os
import plotly.express as px
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/analytics')
import plotly.graph_objects as go
from school_analit import all_school
def school_gauges(df):
    fig = go.Figure()

    # Спідометр для агресивності
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = df['avg_aggression'].iloc[0],
        title = {'text': "Середня агресивність"},
        gauge = {'axis': {'range': [None, 30]}, # Припустимо, 30 - максимум
                 'bar': {'color': "#e74c3c"}},
        domain = {'x': [0, 0.45], 'y': [0, 1]}
    ))

    # Спідометр для ворожості
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = df['avg_ворожості'].iloc[0],
        title = {'text': "Середня ворожість"},
        gauge = {'axis': {'range': [None, 9]}, 
                 'bar': {'color': "#3498db"}},
        domain = {'x': [0.55, 1], 'y': [0, 1]}
    ))
    
    fig.update_layout(height=400)
    return fig
import plotly.express as px

def school_radar_profile(df):
    # Готуємо дані (назви шкал та їх середні значення)
    categories = ['Фізична', 'Вербальна', 'Непряма', 'Негативізм', 'Роздратування']
    values = [
        df['avg_фізична'].iloc[0], 
        df['avg_вербальна'].iloc[0], 
        df['avg_непряма'].iloc[0], 
        df['avg_негативізм'].iloc[0], 
        df['avg_роздратування'].iloc[0]
    ]

    fig = px.line_polar(r=values, theta=categories, line_close=True,
                        title="Профіль шкільної агресії (середні бали)")
    fig.update_traces(fill='toself', line_color='#9b59b6')
    return fig
def high_risk_donut(df):
    total = df['total_students'].iloc[0]
    high = df['high_aggression'].iloc[0]
    
    fig = px.pie(
        values=[high, total - high], 
        names=['Висока агресія', 'Норма'],
        hole=0.5,
        color_discrete_sequence=['#e74c3c', '#ecf0f1'],
        title="Частка учнів у групі ризику"
    )
    return fig
def save_combined_report(f_path):
    """Об'єднує всі графіки в один професійний HTML-звіт"""
    df = all_school()#Підключаємо датафрейм
    # 1. Створюємо всі об'єкти графіків
    fig_gauges = school_gauges(df)
    fig_radar = school_radar_profile(df)
    fig_donut = high_risk_donut(df)
    
    # Створюємо список графіків для зручності
    all_figures = [fig_gauges, fig_radar, fig_donut]

    # 2. Використовуємо 'with' для безпечного запису у файл
    os.makedirs(os.path.dirname(f_path) if os.path.dirname(f_path) else '.', exist_ok=True)
    
    with open(f_path, 'w', encoding='utf-8') as f:
        # Додаємо базову HTML-структуру та стилі для краси
        f.write("<html><head>")
        f.write("<meta charset='utf-8'/><title>Звіт по школі</title>")
        f.write("<style>body { font-family: sans-serif; margin: 40px; background-color: #f4f7f6; } ")
        f.write(".chart-container { background: white; padding: 20px; margin-bottom: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }</style>")
        f.write("</head><body>")
        
        f.write("<h1 style='text-align:center; color: #2c3e50;'>Загальний аналіз шкільного середовища</h1>")
        f.write("<p style='text-align:center; color: #7f8c8d;'>Сформовано автоматично на основі результатів опитування</p>")

        # 3. Записуємо графіки один за одним
        for i, fig in enumerate(all_figures):
            f.write("<div class='chart-container'>")
            
            # include_plotlyjs='cdn' додаємо тільки для першого графіка, 
            # щоб не дублювати важкий скрипт кілька разів
            is_first = (i == 0)
            f.write(fig.to_html(full_html=False, include_plotlyjs='cdn' if is_first else False))
            
            f.write("</div>")

        f.write("</body></html>")
    
    print(f"Звіт успішно створено: {os.path.abspath(f_path)}")