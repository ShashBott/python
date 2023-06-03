def fullname(str1):
    
   lst = str1.split()
   newspace = ""
    
   for i in range(len(lst)-1):
      str1 = lst[i]
   
      newspace += (str1[0].upper()+'.')
  
   newspace += lst[-1].title()
   return newspace 
            
str1=input("Enter Full Name ::>")
print("Short Form of Name Is ::>",fullname(str1)) 
