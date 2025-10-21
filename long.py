words=input("Enter words separated by spaces:").split()
longest_length=len(max(words,key=len))
print("Length of the longest word:",longest_length)
