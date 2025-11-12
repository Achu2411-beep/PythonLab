n=int(input("Enter the number of element:"))
lst=[]
for i in range(n):
    value=int(input(f"Enter a element{i+1}:"))
    lst.append(value)
    sum=0
    for num in lst:
        sum=sum+num
        print("The sum of all items in the list is:",sum)
