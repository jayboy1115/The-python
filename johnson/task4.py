# prompt the user to enter the subtotal
# prompt the user to enter the the gratuity rate in percentage
# calculate for gratuity
# calculate for total
# print the results


subtotal = float(input("Enter the subtotal: "))
gratuity_rate = float(input("Enter the gratuity rate (in %): "))

gratuity = subtotal * (gratuity_rate / 100)
total = subtotal + gratuity

print(f"Gratuity ({gratuity_rate}%): {gratuity:.2f}")
print(f"Total: {total:.2f}")

