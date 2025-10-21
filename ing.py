text=input("Enter a string:")
if len(text)>=3:
    if text.endswith("ing"):
        text=text+"ly"
    else:
        text=text+"ing"
print("Modified string:",text)
