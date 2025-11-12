s=input("Enter a string:")
first_char=s[0]
modified_part=s[1:].replace(first_char,'$')
result=first_char+modified_part
print("Output:",result)
