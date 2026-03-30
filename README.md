school-survey-project
│
├── src/                     # ETL
│   ├── extract.py
│   ├── transform.py
│   ├── calc.py
│   ├── load_sql.py
│   └── pipeline.py
│
├── analytics/               # SQL + аналітика
│   ├── queries/
│   │   ├── class_means.sql
│   │   ├── class_exceeded.sql
│   │   └── class_students.sql
│   │
│   ├── class_means.py
│   ├── class_exceeded.py
│   └── class_students.py
│
├── visualization/
│   ├── dashboards/
│   │   ├── class_dashboard.py
│   │   ├── compare_means.py
│   │   └── exceeded_norms.py
│   │
│   └── plots.py
│
├── data/
│   └── db/survey.db
│
├── state/
│   └── last_processed.txt
│
├── README.md
└── requirements.txt

This project is based on a real-world workflow. All sensitive data has been anonymized or replaced with synthetic data to ensure privacy and confidentiality.
