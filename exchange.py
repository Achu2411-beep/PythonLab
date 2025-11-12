text=input("Enter a string:")
if len(text)>1:
    swapped=text[-1]+text[1:-1]+text[0]
else:
    swapped=text
print("String after swapping first and last characters:",swapped)
