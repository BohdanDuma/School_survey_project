import pandas as pd
import sys
import os
sys.path.append('/home/bohdan/Стільниця/school-survey-poject/analytics')


from table_class import  get_class, table_class



def class_detail_dashboard(class_name):
    """
    Повертає styled dashboard (pandas Styler)
    для одного класу з коректним градієнтом для різних шкал
    """
    df = table_class(class_name)

    
    styled = df.style

    # 🔹 Шкала 0–100
    styled = styled.background_gradient(
        cmap="RdYlGn_r",
        subset=[
            "Фізична",
            "Вербальна",
            "Опосередкована",
            "Негативізм",
            "Роздратування",
            "Підозріливість",
            "Образа",
            "Провина"

        ],
        vmin=30,
        vmax=100
    )

    # 🔹 Шкала 0–30
    styled = styled.background_gradient(
        cmap="RdYlGn_r",
        subset=[
            
            "Індекс_агресивності"
        ],
        vmin=10,
        vmax=30
    )

    # 🔹 Шкала 0–10
    styled = styled.background_gradient(
        cmap="RdYlGn_r",
        subset=[
            "Індекс_ворожості"
        ],
        vmin=3,
        vmax=10
    )

    # 🔹 Загальні стилі
    styled = styled.set_properties(**{
        "text-align": "center",
        "font-size": "12px"
    }).set_table_styles([
        {
            "selector": "th",
            "props": [
                ("text-align", "center"),
                ("font-weight", "bold"),
                ("background-color", "#f0f2f6")
            ]
        }
    ])

    return styled

