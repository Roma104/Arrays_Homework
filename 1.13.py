# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

sum = 0
i = 0
while i < len(product_prices):
    #print(product_prices[i], "*", product_quantities[i])
    sum += product_prices[i] * product_quantities[i]
    i += 1

print("The value of all goods available in the store: ", round(sum, 2))