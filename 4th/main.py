import Armstrong
lower=int(input("Enter the lower limits:"))
upper=int(input("Enter the upper limits:"))
print(f"Armstrong numbers between {lower} and {upper} are:")
for num in range(lower,upper+1):
    if Armstrong.is_armstrong(num):
       print(num)
