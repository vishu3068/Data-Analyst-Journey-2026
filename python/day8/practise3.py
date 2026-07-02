import pandas as pd

data = {
    "Student_ID": [
        "S001","S002","S003","S004","S005",
        "S006","S007","S008","S009","S010",
        "S011","S012","S013","S014","S015",
        "S016","S017","S018","S019","S020"
    ],

    "Name": [
        "Vishwanth","Abhi","Sai","Ravi","Karthik",
        "Lasya","Anjali","Rahul","Priya","Nikhil",
        "Harsha","Pavan","Teja","Rohit","Sneha",
        "Ajay","Charan","Keerthi","Vamsi","Akhil"
    ],

    "Department": [
        "AIML","CSE","IT","ECE","AIML",
        "CSE","IT","ECE","AIML","CSE",
        "IT","ECE","AIML","CSE","IT",
        "ECE","AIML","CSE","IT","ECE"
    ],

    "Maths": [
        85,72,91,68,79,
        88,74,95,82,67,
        90,71,84,77,69,
        93,81,75,87,80
    ],

    "Science": [
        78,81,89,70,85,
        92,73,88,79,76,
        84,69,91,72,83,
        95,80,74,86,77
    ],

    "English": [
        88,75,84,72,90,
        86,79,92,81,73,
        87,78,89,76,85,
        91,80,74,88,82
    ],
    "Total_Marks": [
        251,228,264,210,254,
        266,226,275,242,216,
        261,218,264,225,237,
        279,241,223,261,239
    ]
}

df = pd.DataFrame(data)

print(df)

print('highest marks: ', df[['Maths','Science','English']].max())
print('lowest marks: ',df[['Maths','Science','English']].min())
print(df.sort_values('Maths', ascending= False))
print(df[df["Total_Marks"]>250])
print(df[df["Total_Marks"]<250])

print(df[(df["Total_Marks"]>220)& 
         (df["Total_Marks"]<260)])

print(df[(df['Department']=='AIML')&
         (df["Total_Marks"]>250)])