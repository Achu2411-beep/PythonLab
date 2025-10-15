colors=input("Enter colors name separted by commas:")
colors_list=[color.strip()for color in colors.split(",")]
print("color list:",colors_list)
print("First color:",colors_list[0])
print("Last color:",colors_list[-1])
