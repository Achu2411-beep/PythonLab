import math
lower=int(input("Enter the lower limit(4-digit):"))
upper=int(input("Enter the upper limit(4-digit):"))
print("Four -digit numbers with all even digits and are perfect squares:")
for n in range(lower,upper+1):
    digits_even=all(int(d)%2==0 for d in str (n))
    sqrt_n=int(math.sqrt(n))
    is_square=sqrt_n*sqrt_n==n
    if digits_even and is_square:
        print(n)

