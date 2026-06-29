#method1 to read file
f = open('D:\Data_analyst_journey2026\Python\day6\student_marks.txt', 'r')
content_file = f.read()
print(content_file)

f.close()

#method 2 using with not neede to close

with open('D:\Data_analyst_journey2026\Python\day6\student_marks.txt', 'r') as f:
    content = f.read()
    print(content)
# to read line by line 
with open('D:\Data_analyst_journey2026\Python\day6\student_marks.txt', 'r') as f:
    content = f.readline(0)
    #to print all lines
    for lines in f:
        print(lines, end = '')