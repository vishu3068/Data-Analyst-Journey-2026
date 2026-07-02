import pandas as pd

data = {
    "Name": [
        "Vishwanth", "Abhi", "Sai", "Ravi", "Karthik",
        "Lasya", "Anjali", "Rahul", "Priya", "Nikhil"
    ],
    "Age": [
        22, 34, 31, 25, 43,
        32, 26, 24, 41, 57
    ],
    "Salary": [
        30000, 45000, 28000, 50000, 35000,
        32000, 55000, 40000, 29000, 60000
    ]
}

df = pd.DataFrame(data)

print(df)
#print(df.sort_values('Salary'))  # ascending order 
#print(df.sort_values('Salary', ascending=False)) #descending

#filtering
print(df[df['Salary']>40000])
print(df[df['Salary']<30000])
print(df[df['Salary']==30000])

#multi conditioning

print(df[(df['Salary']>40000)&     #and
         (df['Age']>30)])

print(df[(df['Salary']<30000)|(df["Age"]<20)])    #or
