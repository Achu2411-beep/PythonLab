n=int(input("Enter the number of terms:"))
a=0
b=1
if n<=0:
    print("Please enetr a positive number:")
elif n==1:
    print("Fibonacci series:",a)
else:
    print("Fibonacci series:",a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
