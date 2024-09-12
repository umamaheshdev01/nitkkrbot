import json
from fuzzywuzzy import process

data = [
    {
        "className": "IT-A",
        "strength": 80,
        "Class Representative or CR": 'Punith Raj',
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
        },
        
    },
     
    {
        "className": "IT-B",
        "strength": 80,
        "Class Representative or CR": 'Mrunmai Lakade',
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
        },
        "students" :   {
    "section": "IT-B",
    "subsection": "IT-08",
    "name & roll_no": [
        {
        "roll_number": "12213144",
        "name": "RASHMI SHAW"
        },
        {
        "roll_number": "12213145",
        "name": "MANSI SARKAR"
        },
        {
        "roll_number": "12213146",
        "name": "TAMANNA"
        },
        {
        "roll_number": "12213147",
        "name": "JARUPLA BHAGYASREE"
        },
        {
        "roll_number": "12213148",
        "name": "AKHIL MEENA"
        },
        {
        "roll_number": "12213149",
        "name": "CHEVURI SAI KIRAN"
        },
        {
        "roll_number": "12213150",
        "name": "UMAR AHMAD"
        },
        {
        "roll_number": "12213151",
        "name": "SANTHOSH KUMAR BHUKYA"
        },
        {
        "roll_number": "12213152",
        "name": "AYUSH MINZ"
        },
        {
        "roll_number": "12213153",
        "name": "ANOOP SINGH"
        },
        {
        "roll_number": "12213154",
        "name": "SHASHANK SINGH"
        },
        {
        "roll_number": "12213155",
        "name": "KORRA PRADEEP KUMAR"
        },
        {
        "roll_number": "12213156",
        "name": "ADITYA ARYAN"
        },
        {
        "roll_number": "12213157",
        "name": "SAHIL DAGAR"
        },
        {
        "roll_number": "12213158",
        "name": "NITISH KUMAR"
        },
        {
        "roll_number": "12213159",
        "name": "SANYAM"
        },
        {
        "roll_number": "12213160",
        "name": "PORAS YADAV"
        },
        {
        "roll_number": "12213161",
        "name": "AARAV SRIVASTAVA"
        },
        {
        "roll_number": "12213162",
        "name": "BADAL"
        },
        {
        "roll_number": "12213163",
        "name": "KUNAL"
        },
        {
        "roll_number": "12213164",
        "name": "NITESH"
        }
    ]}
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


