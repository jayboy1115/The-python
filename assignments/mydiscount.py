def my_discount(price, discount):
    discount_amount = (discount / 100) * price
    return price - discount_amount
print(my_discount(100, 15))