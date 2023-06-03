file = open("C:\Users\HP\AppData\Local\Programs\Python\Python310\Hello.txt",'r')

F1 = file.read()

print(F1)

file2 = open("C:\Python\Python310\Hello2.txt",'w')

file2.write(F1.replace('"','\\"'))

F2= open("C:\Python\Python310\Hello2.txt",'r')

F2= file2.read()

print(F2)

file.close()

file2.close()
