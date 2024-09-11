import json
from fuzzywuzzy import process

data = [
    {
        "className": "IT-A",
        "strength": 80,
        "syllabus": {
            "Machine Learning": [
                "Unit-1 Introduction",
                "Unit-2 Regression Techniques and Analysis",
                "Unit-3 Classification",
                "Unit-4 Clustering",
                "Unit-5 Advances in Machine Learning"
            ],
            "Theory of Computation": [
                "Unit-1 Introduction to Finite State Machine",
                "Unit-2 Regular Languages",
                "Unit-3 Context Free Grammars",
                "Unit-4 Turing Machine Definition"
            ],
            "Data Mining and Analysis": [
                "Unit-1 Data Mining and Data Pre-processing",
                "Unit-2 Clustering",
                "Unit-3 Association Rule Mining",
                "Unit-4 Dimension Reduction and Introduction to Analytics",
                "Unit-5 Web Data Mining"
            ],
            "Full Stack Development": [
                "Unit 1. Planning Your Work",
                "Unit 2. Designing Systems",
                "Unit 3: Front End",
                "Unit 4. Back-End Development and Storing Data"
            ],
            "Information Security": [
                "Unit 1. Introduction to Information Security",
                "Unit 2 Introduction to Number theory",
                "Unit 3. Introduction to Cryptography",
                "Unit 4. System and Operating Security",
                "Unit 5. Network Security"
            ]
        }
    },
    {
        "className": "IT-B",
        "strength": 80,
        "Class Representative": 'Mrunmai Lakade',
        "syllabus": {
            "Machine Learning": [
                "Unit-1 Introduction",
                "Unit-2 Regression Techniques and Analysis",
                "Unit-3 Classification",
                "Unit-4 Clustering",
                "Unit-5 Advances in Machine Learning"
            ],
            "Theory of Computation": [
                "Unit-1 Introduction to Finite State Machine",
                "Unit-2 Regular Languages",
                "Unit-3 Context Free Grammars",
                "Unit-4 Turing Machine Definition"
            ],
            "Data Mining and Analysis": [
                "Unit-1 Data Mining and Data Pre-processing",
                "Unit-2 Clustering",
                "Unit-3 Association Rule Mining",
                "Unit-4 Dimension Reduction and Introduction to Analytics",
                "Unit-5 Web Data Mining"
            ],
            "Full Stack Development": [
                "Unit 1. Planning Your Work",
                "Unit 2. Designing Systems",
                "Unit 3: Front End",
                "Unit 4. Back-End Development and Storing Data"
            ],
            "Information Security": [
                "Unit 1. Introduction to Information Security",
                "Unit 2 Introduction to Number theory",
                "Unit 3. Introduction to Cryptography",
                "Unit 4. System and Operating Security",
                "Unit 5. Network Security"
            ]
        }
    }
]


def get_class_data(user_input):
    try:
        class_names = [entry["className"] for entry in data]
        best_match, score = process.extractOne(user_input, class_names)

        if score > 80:
            for entry in data:
                if entry["className"] == best_match:
                    return entry
        else:
            return {}
    except Exception as e:
        return {}


