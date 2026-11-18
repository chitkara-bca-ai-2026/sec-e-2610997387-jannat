print("========== DATA CONVERSION UTILITY ==========")

product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total_price = price * quantity
amount_string = str(total_price)

print("\n--- TYPE CASTING SUMMARY ---")
print("product_name:", product_name, type(product_name))
print("price:", price, type(price))
print("quantity:", quantity, type(quantity))
print("total_price:", total_price, type(total_price))
print("amount_string:", amount_string, type(amount_string))

print("\n--- TAX INVOICE ---")
print("Product Name:", product_name)
print("Price per Unit: Rs.", price)
print("Quantity:", quantity)
print("Invoice Total: Rs.", amount_string)