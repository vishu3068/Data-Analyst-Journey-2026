highest=0
with open("D:\Data_analyst_journey2026\Python\day6\student_marks.txt", 'r') as cf:
    for line in cf:
        data =line.split()


        if len(data)>=2 and data[1].isdigit():
            marks = int(data[1])


            if marks> highest:
                highest = marks
print('highest marks: ',data[2])


# average
highest=0
total=0
count=0
with open("D:\Data_analyst_journey2026\Python\day6\student_marks.txt", 'r') as cf:
    for line in cf:
        data =line.split()


        if len(data)>=2 and data[1].isdigit():
            marks = int(data[1])
            total= total+marks
            count = count +1

            if marks> highest:
                highest = marks
average= total/count
print('average marks: ',average)
                


            