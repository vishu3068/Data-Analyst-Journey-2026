import pandas as pd
data =[90,98,88,78,96,69,58,95,60,78]
marks = pd.Series(data)
print(marks)
print(marks.loc[8])
print(marks.iloc[9])
print(marks[marks<=80])
print('maximum marks: ',marks.max())
print('minimum marks: ', marks.min())
print('average marks: ',marks.mean())