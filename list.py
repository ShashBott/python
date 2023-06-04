list=[1,2,3,4,5]
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

print("original list ",list)
list1.reverse()
print("reversed list ",list1)

print("\nconcatenation of lists= ",list+list2)

x=zip(list,list2)
print("\niteration of both lists simultaneously: ",tuple(x))

new_item=11
list2.append(new_item)
print("\nadding 11 to the list2 it becomes= ",list2)

list3 =["a", "b", ["c", ["d", "e", ["f", "g"], "k"]]]
sub_list = ["h", "i", "j"]
list3[2][1][2].extend(sub_list)
print("\nExtend nested list by adding the sublist is: ",list3)

list4=[1,4,5,1,6,1,7,1]
print("\noriginal list :",list4)
for i in list4:
    if(i==1):
       list4.remove(1)
print("after removing 1 from list: ",list4)
