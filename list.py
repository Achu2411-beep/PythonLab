list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

print("Same length:", len(list1) == len(list2))
print("Same sum:", sum(list1) == sum(list2))
common = False
for x in list1:
    if x in list2:
        print("Common value found:", x)
        common = True
        break

if not common:
    print("No common values")

