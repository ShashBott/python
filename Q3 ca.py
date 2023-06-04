lst=[]
print("Enter 4 test scores\n")
for i in range(0, 4):
    ele = float(input())
    lst.append(ele)
lst.sort()
for i in range(1,4):
    print("Test score: ",lst[i])
    if lst[i]>=90.00:
        
        print("Grade A")
        
    elif lst[i]>80.00 and lst[i]<89.99:
        
        print("Grade B")
        
    elif lst[i]>70.00 and lst[i]<79.99:
        
        print("Grade C")
        
    elif lst[i]>60.00 and lst[i]<69.99:
        
        print("Grade D")
        
    else:
        
        print("Grade F");
        
sum=0
for i in range(1,4):
    sum=sum+lst[i]
avg=sum/3
print("Average of three highest grades ",avg)
