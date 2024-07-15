print("WELCOME TO JOHNSON WORLD")

principal = float(input("Enter initial investment: "))
rate = float(input("Enter annual interest rate (in %): "))

for year in range(1, 31):
    amount = principal * (1 + rate / 100) ** year
    print(f"Year {year}: ${amount:.2f}")
