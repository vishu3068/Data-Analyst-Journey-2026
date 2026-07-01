import pandas as pd
#pandas : is a python library used for dataanalysis, data cleaning, data manipulation
#reading csv and reading excel etc/.
#series: is a one dimentional data labeled array which can stowre any valueof any data typr
#its like a single column in excel
data = [101,102,103,104,150,180,190,200]
series= pd.Series(data)
print(series)
print(series.loc[2]) #locate with index through data
series.loc[3]=110 #updating vaalue
print(series)
print(series[series>=150]) #filtering data
