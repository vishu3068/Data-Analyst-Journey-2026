import pandas as pd
data = {
    "Name":["Vishwanth","Abhi","Sai","Ravi"],
    "Department":["AIML","CSE","IT","ECE"],
    "Salary":[30000,25000,40000,28000]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[2])
df['role']= ['analyst','trainee','sr.executive','associate']
print(df)
add_row = pd.DataFrame([{'Name':'lasya','Department':'b.arch','Salary':'30000','role':'junior artitect'}])
df=pd.concat([df,add_row])
print(df)
print(df.shape)
print(df.info())
print(df.columns)
print(df.describe())
