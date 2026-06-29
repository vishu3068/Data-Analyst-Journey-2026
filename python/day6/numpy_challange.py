import numpy as np
salary=[25000,30000,28000,40000,35000]
print('highest salary: ',np.max(salary))
print('lowest salary: ',np.min(salary))
print('sum of salary: ',np.sum(salary))
print('average salary: ',np.sum(salary)/5)
i=0
for i in salary:
    i=i+5000
    print("bonus salary: ",i)