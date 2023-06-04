def nat(n):
    
    sum=0
    for i in range(n+1):

        sum=sum+i

    print("The sum is: ",sum)


def fib(n):

       if n <= 1:
          return n

       else:
          return(fib(n-1) + fib(n-2))
 




num=int(input("Enter a number "))
nat(num)

nterms=int(input("Enter a number upto which you want to print the fibonacci series "))
if nterms <= 0:
   print("Plese enter a positive integer ")
else:
   print("Fibonacci sequence: ")
   for i in range(nterms):
       print(fib(i))
