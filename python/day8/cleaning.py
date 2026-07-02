import pandas as pd

data = {
    "Name":["Vishwanth","Sai",None,"Abhi"],
    "Salary":[30000,40000,35000,None],
    "Department":["AIML","IT","CSE",None]
}

df = pd.DataFrame(data)

print(df)
print(df.isnull())      #prints missing values
print(df.isnull().sum())  #counts missing values
# print(df.dropna())    #removes missing values
df['Salary'] = df['Salary'].fillna(0) #filling missing value in salary
df['Department'] = df['Department'].fillna("unknown")# is department
df['Name'] = df['Name'].fillna("unknown")
print(df)