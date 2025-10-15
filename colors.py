color_list1=input("Enter colors for list1(comma separated):").split(",")
color_list2=input("Enter colors for list2(comma separated):").split(",")
color_list1=[color.strip() for color in color_list1]
color_list2=[color.strip() for color in color_list2]
result=[color for color in color_list1 if color not in color_list2]
print("colors in list1 not in list2:",result)
