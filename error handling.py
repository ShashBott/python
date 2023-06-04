
import math

n=int(input("Enter a Number \n"))

      
try:

    m=int(input("Enter its power \n"))
    
    p=math.pow(n,m)
    
    print("Operation performed successfully \n")
    
except ValueError:
    
    print("Values invalid \n")
    
except:
    
    print("OOPS some exception raised ! \n")
    
else:
    
    print("The result of the operation is : ",p)
    
finally:
    
    print("END OF PROGRAM \n")
