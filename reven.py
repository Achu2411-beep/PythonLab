numbers=input("Enter numbers separated by commas:")
num_list=[int(x.strip())for x in numbers.split(",")]
odd_list=[num for num in num_list if num%2!=0]
print("Orginallist:",num_list)
print("List after removing even numbers:",odd_list)
