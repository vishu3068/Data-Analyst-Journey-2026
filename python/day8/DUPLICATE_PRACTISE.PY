import pandas as pd

data = {
    "Student": [
        "Vishwanth",
        "Abhi",
        "Sai",
        "Ravi",
        "Abhi",
        "Sai",
        "Karthik",
        "Vishwanth"
    ],
    "Department": [
        "AIML",
        "CSE",
        "IT",
        "ECE",
        "CSE",
        "IT",
        "AIML",
        "AIML"
    ],
    "Marks": [
        85,
        90,
        78,
        95,
        90,
        78,
        88,
        85
    ]
}

df = pd.DataFrame(data)

print(df)
print(df.duplicated())
print(df.drop_duplicates())
df.rename(columns ={
    'Student':'praticipant'
},
inplace=True  
)
print(df)