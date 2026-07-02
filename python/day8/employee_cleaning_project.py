import pandas as pd
df=pd.read_csv('D:\Data_analyst_journey2026\projects\employee_cleaning_project\employee_cleaning.csv')
print(df.isnull().sum())
df['Salary']=df['Salary'].fillna(0)
df['Department']=df['Department'].fillna('unknown')
print(df.drop_duplicates())
print(df)
print('highest salary: ',df['Salary'].max())
print('lowest salary: ', df['Salary'].min())
print('Average salary: ', df['Salary'].mean())
print(df.sort_values('Salary',ascending=False))
print(df[df['Salary']>40000])


df.to_csv(
    "clean_employee_data.csv",
    index=False
)
