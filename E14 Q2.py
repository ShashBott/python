import numpy as np
num1 =int(input("Enter a number "))
num2 =int(input("Enter a number "))
print ("1st Input  number : ",num1)
print ("2nd Input  number : ",num2)
num = np.add(num1,num2) 
print ("output number after addition :", num)


print("\n")
lst=[0,0,0,0,0,0,4]
arr=np.array(lst)
print("Checking if the array contains 0 or not, true=doesn't contains, false=contains \n")
print(np.all(arr))


print("\n")
print("Checking if the array contains non zero number or not, false=doesn't contains, true=contains \n")
print(np.any(arr))


print("\n")
num = np.random.normal(size=15)
print("15 random numbers from a standard normal distribution: \n")
print(num)



