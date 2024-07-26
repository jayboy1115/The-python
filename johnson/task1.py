# write out the pi value
# prompt the user to enter the radius and length of the cylinder
# calculate the area
# calculate the volume
# Print the area
# print the volume

pi = 3.14159

radius = float(input("Enter the radius of the cylinder: "))
length = float(input("Enter the length of the cylinder: "))

area = pi * (radius ** 2)
volume = area * length


print(f"The area of the cylinder is: {area:.2f}")
print(f"The volume of the cylinder is: {volume:.2f}")

