#challange 1 print only names

with open('D:\Data_analyst_journey2026\Python\day6\student_marks.txt', 'r') as cf:
    for line in cf:
        marks = line.split()

        if len(marks)>=2 and marks[1].isdigit():
            print(marks[0])

##challange 2 print only marrks

with open('D:\Data_analyst_journey2026\Python\day6\student_marks.txt', 'r') as cf:
    for line in cf:
        marks = line.split()

        if len(marks)>=2 and marks[1].isdigit():
            print(marks[1])