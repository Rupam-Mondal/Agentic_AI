tea_prices_inr = {
    "Masala Chai": 50,
    "Ginger Chai": 40,
    "Cardamom Chai": 45,
    "Tulsi Chai": 35
}

print(tea_prices_inr.items())

tea_prices_usd = { tea : price / 80 for tea , price in tea_prices_inr.items()}

print(tea_prices_usd)