file = open('E:\dir\city.txt','r')

f1 = file.read()

print("Details of all cities :\n",f1,'\n')

words = f1.split()

print("City names with population more than 10Lakhs : ")

area = 0

for i in range(0,5):

  if i==0:

    L = words[0:i+3]

    area += float(L[2])

    if float(L[1])>10:

      print(L[0])

    else:

      continue

  elif i<=15:

    L = words[i*3:i*3+3]

    area += float(L[2])

    if float(L[1])>10:

      print(L[0])

print("\nTotal area covered by cities : ",area)
