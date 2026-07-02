import pandas as pd

data = {
    "Student": ["Vishwanth", "Abhi", "Sai", "Ravi", "Karthik"],
    "Marks": [85, None, 78, None, 92],
    "City": ["Hyderabad", "Warangal", None, "Vijayawada", "Karimnagar"]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())
#df['Marks'] = df['Marks'].fillna(0)
#df['City']=df['City'].fillna('unknown')
print(df.dropna())


