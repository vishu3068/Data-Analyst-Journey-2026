import pandas as pd
df=pd.read_csv("D:\Data_analyst_journey2026\employee_data.csv")
print(df['name'])
print(df['salary'])
print(df[['name','salary']])

print(df.loc[9])