print("WELCOME TO JOHNSON TAXATION OFFICE")

def compute_tax(filing_status, taxable_income):
    if filing_status == 0:  # Single filers
        if taxable_income <= 8350:
            return taxable_income * 0.10
        elif taxable_income <= 33950:
            return 8350 * 0.10 + (taxable_income - 8350) * 0.15
        elif taxable_income <= 82250:
            return 8350 * 0.10 + 25000 * 0.15 + (taxable_income - 33950) * 0.25
        elif taxable_income <= 171550:
            return 8350 * 0.10 + 25000 * 0.15 + 48800 * 0.25 + (taxable_income - 82250) * 0.28
        elif taxable_income <= 372950:
            return 8350 * 0.10 + 25000 * 0.15 + 48800 * 0.25 + 89400 * 0.28 + (taxable_income - 171550) * 0.33
        else:
            return 8350 * 0.10 + 25000 * 0.15 + 48800 * 0.25 + 89400 * 0.28 + 201400 * 0.33 + (taxable_income - 372950) * 0.35

    elif filing_status == 1:  # Married filing jointly
        if taxable_income <= 16700:
            return taxable_income * 0.10
        elif taxable_income <= 67900:
            return 16700 * 0.10 + (taxable_income - 16700) * 0.15
        elif taxable_income <= 137050:
            return 16700 * 0.10 + 51200 * 0.15 + (taxable_income - 67900) * 0.25
        elif taxable_income <= 208850:
            return 16700 * 0.10 + 51200 * 0.15 + 70050 * 0.25 + (taxable_income - 137050) * 0.28
        elif taxable_income <= 372950:
            return 16700 * 0.10 + 51200 * 0.15 + 70050 * 0.25 + 71800 * 0.28 + (taxable_income - 208850) * 0.33
        else:
            return 16700 * 0.10 + 51200 * 0.15 + 70050 * 0.25 + 71800 * 0.28 + 164100 * 0.33 + (taxable_income - 372950) * 0.35

    elif filing_status == 2:  # Married filing separately
        if taxable_income <= 8350:
            return taxable_income * 0.10
        elif taxable_income <= 33950:
            return 8350 * 0.10 + (taxable_income - 8350) * 0.15
        elif taxable_income <= 68525:
            return 8350 * 0.10 + 25575 * 0.15 + (taxable_income - 33950) * 0.25
        elif taxable_income <= 104425:
            return 8350 * 0.10 + 25575 * 0.15 + 35175 * 0.25 + (taxable_income - 68525) * 0.28
        elif taxable_status <= 186475:
            return 8350 * 0.10 + 25575 * 0.15 + 35175 * 0.25 + 81850 * 0.28 + (taxable_income - 104425) * 0.33
        else:
            return 8350 * 0.10 + 25575 * 0.15 + 35175 * 0.25 + 81850 * 0.28 + 90250 * 0.33 + (taxable_income - 186475) * 0.35

    elif filing_status == 3:  # Head of Household
        if taxable_income <= 11950:
            return taxable_income * 0.10
        elif taxable_income <= 45500:
            return 11950 * 0.10 + (taxable_income - 11950) * 0.15
        elif taxable_income <= 117450:
            return 11950 * 0.10 + 33550 * 0.15 + (taxable_income - 45500) * 0.25
        elif taxable_income <= 190200:
            return 11950 * 0.10 + 33550 * 0.15 + 72150 * 0.25 + (taxable_income - 117450) * 0.28
        elif taxable_income <= 372950:
            return 11950 * 0.10 + 33550 * 0.15 + 72150 * 0.25 + 72650 * 0.28 + (taxable_income - 190200) * 0.33
        else:
            return 11950 * 0.10 + 33550 * 0.15 + 72150 * 0.25 + 72650 * 0.28 + 182750 * 0.33 + (taxable_income - 372950) * 0.35

    else:
        return "Invalid filing status"

print("Enter filing status:")
print("0 for single filers")
print("1 for married filing jointly")
print("2 for married filing separately")
print("3 for head of household")

filing_status = int(input("Enter filing status: "))
taxable_income = float(input("Enter taxable income: "))

tax = compute_tax(filing_status, taxable_income)

print("Tax:", tax)

