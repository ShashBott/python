n = int(input('Enter Number of students : '))
student_marks = {}
for i in range(n):
    lst = list(input().split())
    name = lst[0]
    m1 = int(lst[1])
    m2 = int(lst[2])
    m3 = int(lst[3])    
    scores = [m1,m2,m3]
    student_marks[name] = scores
query_name = input('Enter Name to find Average : ')
print(round(sum(student_marks[query_name])/3,2))

