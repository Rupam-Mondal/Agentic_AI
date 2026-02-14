daily_sales = [
    1 , 4 , 9 , 54 , 2
]

sales = sum(sale for sale in daily_sales if sale > 2) # Generator expression to filter sales greater than 10

print(sales) # This will print the generator object