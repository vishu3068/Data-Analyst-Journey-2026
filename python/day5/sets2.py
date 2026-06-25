set1 = {1,2,3,4,5,6,7,8,9,10,11,12,}
set2 = {8,9,10,11,12,13,14,15,16,17,18,19,20}

set1.add(17)
print(set1)
set2.remove(9)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set1.issubset(set2))
set1.update(set2)
print(set1)
set2.clear()
print(set2)