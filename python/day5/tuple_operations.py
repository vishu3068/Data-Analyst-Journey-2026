marks = (85,90,78,90)

#tuple indexing
print(marks[2])
print(marks[-3])

#tuple concatination: add to tuple to gether
marks2 = (89,67,90,58,78,45)

all_marks = marks + marks2

print(all_marks)

#add or change values in tuple using list
marks =(85, 90, 78, 90, 89, 67, 90, 58, 78, 45)
temp= list(marks)
temp.append(99)
temp.pop(3)
temp[4]=79
marks = tuple(temp)
print(marks)