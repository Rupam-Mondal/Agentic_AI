def vat(price , vat_rate):
    return price * (vat_rate + 100) / 100

order = [100 , 200 , 300]

for price in order:
    final_price = vat(price , 15)
    print(final_price)

