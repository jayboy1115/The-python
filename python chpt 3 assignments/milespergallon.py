print("WELCOME TO JOHNSON WORLD")

total_miles = 0
total_gallons = 0

while True:
    gallons = float(input("Enter gallons used (-1 to end): "))
    if gallons == -1:
        break

    miles = float(input("Enter miles driven: "))

    mpg = miles / gallons
    print(f"The miles/gallon for this tank was {mpg:.6f}")

    total_miles += miles
    total_gallons += gallons

combined_mpg = total_miles / total_gallons
print(f"The overall average miles/gallon was {combined_mpg:.6f}")



