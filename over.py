numbers=input("Enter a list of integers separated by spaces:")
numbers=[int(x) for x in numbers.split()]
result=[]
for n in numbers:
    if n > 100:
        result.append("over")
    else:
        result.append(n)
    print("Modified list:",result)
