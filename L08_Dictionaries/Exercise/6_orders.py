products = {}
command = input()
while command != "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][1] += quantity
        if products[product][0] != price:
            products[product][0] = price
    command = input()

for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")


# Write a program that keeps the information about products and their prices. Each product has a name, a price, and
# a quantity:
#     • If the product doesn't exist yet, add it with its starting quantity.
#     • If you receive a product, which already exists, increases its quantity by the input quantity and if its price is
# different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep
# adding items. Finally, print all items with their names and the total price of each product.
# Input
#     • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
#     • The product data is always delimited by a single space.
# Output
#     • Print information about each product in the following format:"{product_name} -> {total_price}"
#     • Format the total price to the 2nd digit after the decimal separator.

# Examples
# Input:
#   Beer 2.20 100
#   IceTea 1.50 50
#   NukaCola 3.30 80
#   Water 1.00 500
#   buy
#
# Output:
#   Beer -> 220.00
#   IceTea -> 75.00
#   NukaCola -> 264.00
#   Water -> 500.00
#
# # Input:
#   Beer 2.40 350
#   Water 1.25 200
#   IceTea 5.20 100
#   Beer 1.20 200
#   IceTea 0.50 120
#   buy
#
# Output:
#   Beer -> 660.00
#   Water -> 250.00
#   IceTea -> 110.00
