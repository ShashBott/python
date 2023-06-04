class Employee:

  First_name = ''

  Last_name = ''

  Pay = 0

data = Employee()

data.First_name = input("First name is : ")

data.Last_name = input("Last name is : ")

data.Pay = int(input("Pay is : "))

print("Email : "+data.First_name+'.'+data.Last_name+"@company.com")

