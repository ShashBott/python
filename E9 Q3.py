try:
    
    file = open("E:\dir\Hello.txt","r")

    F1 = file.read()

except FileNotFoundError as err:

    print("Error code: ",err)
    
else:

    print(F1)

    file2 = open("E:\dir\Hello2.txt","w")

    file2.write(F1.replace('"','\\"'))

finally:
    
    file.close()

try:

    file2= open("E:\dir\Hello2.txt","r")
    F2=file2.read()

except FileNotFoundError as err:

    print("Error code: ",err)
    
else:
    
    print(F2)

finally:
    
   file2.close()
