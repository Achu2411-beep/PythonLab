def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
n=int(input("Enter the number of terms:"))
sum_series=0
for i in range(1,n+1):
        term=(i**3)/factorial(i)
        sum_series+=term
print("sum of the series:",sum_series)
