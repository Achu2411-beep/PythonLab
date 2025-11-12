n=int(input("Enetr a number:"))
temp=n
digits=len(str(n))
sum=0
while temp>0:
    rem=temp%10
    sum=sum+(rem**digits)
    temp=temp//10
if sum==n:
    print(n,"is a Armstrong number.")
else:
    print(n,"is not  an Armstrong numbers.")
