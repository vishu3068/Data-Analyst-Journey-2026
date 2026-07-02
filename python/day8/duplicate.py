import pandas as pd
data = {
    "Name":["A","B","C","A","B"],
    "Salary":[100,200,300,100,200]
}
df = pd.DataFrame(data)
print(df)
print(df.duplicated())
print(df.drop_duplicates())
df.rename(columns ={
    'Salary': 'Monthly Salary'
},
inplace= True
)
print(df)