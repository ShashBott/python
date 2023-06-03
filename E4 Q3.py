str1=input("Enter a String ")
counts={}
str2=str1.upper()
for i in str2:
    counts[i] = str2.count(i)
 
for k in counts.keys():
    print(str(counts[k]) + k)
