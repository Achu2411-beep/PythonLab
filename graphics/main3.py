from graphicss .rectangle import area as rect_area, perimeter as rect_perimeter
from graphicss .circle import area as circle_area, perimeter as circle_perimeter
from graphicss .graphicss_3d.cuboid import area as cuboid_area, perimeter as cuboid_perimeter
from graphicss .graphicss_3d.sphere import area as sphere_area, perimeter as sphere_perimeter

print("Rectangle Area:", rect_area(8, 4))
print("Rectangle Perimeter:", rect_perimeter(8, 4))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_perimeter(7))

print("Cuboid Area:", cuboid_area(2, 3, 4))
print("Cuboid Perimeter:", cuboid_perimeter(2, 3, 4))

print("Sphere Area:", sphere_area(6))
print("Sphere Perimeter:", sphere_perimeter(6))

