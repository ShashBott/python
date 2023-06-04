score_sheet =[]
st_numbers = int(input("the number of students: "))
for i in range(st_numbers):
    data = int(input())
    score_sheet.append(data)
    score_sheet.sort(reverse=True)
print("runner up:",score_sheet[1])
