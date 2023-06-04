i1=float(input("Enter the price of the first item\n"))
i2=float(input("Enter the price of the second item\n"))
total=i1+i2
print("Your total is: ",total)
paid=float(input("\nEnter the amount you are going to pay "))
if(total>paid):
    dues=total-paid
    print("\nThe amount due is :",dues)
else:
    print("\nThankyou for your payment")
    change=paid-total
    print("\nChange you receive : ",change)
    
