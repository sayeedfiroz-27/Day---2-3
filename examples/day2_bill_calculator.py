product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_bill = price * quantity

print("")
print("Bill Summary")
print("------------")
print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Bill:", total_bill)
