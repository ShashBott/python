x = int(input("How many times do you want to perform division "));
for i in range(x):
    try:
        a, b = input("input two numbers to divide ").split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code: ",e);
    except ValueError as v:
        print("Error Code: ",v);
