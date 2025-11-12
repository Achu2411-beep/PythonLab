def add_numbers(*args):
    """
    This function takes a variable number of integer arguments entered by the user and returns their sum.
    Example:
    add_numbers(2,3,5)->10
    """
    return sum(args)
nums=input("Enter number separated by spaces:")
nums=[int(x) for x in nums.split()]
total=add_numbers(*nums)
print("The sum is :",total)
print("\nFunction description:")
print(add_numbers.__doc__)
