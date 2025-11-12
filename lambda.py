square_area=lambda side:side*side
rectangle_area=lambda length,breadth:length*breadth
triangle_area=lambda base,height:0.5*base*height
side=float(input("Enter  side of squares:"))
length=float(input("Enter length of rectangle:"))
breadth=float(input("Enter breadth of rectangle:"))
base=float(input("Enter base of triangle:"))
height=float(input("Enter height of triangle:"))
print("Area of square:",square_area(side))
print("Area of rectangle:",rectangle_area(length,breadth))
print("Area of triangle:",triangle_area(base,height))


