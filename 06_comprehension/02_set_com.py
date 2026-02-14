favourite_chais = [
    "Masala Chai",
    "Ginger Chai",  
    "Cardamom Chai",
    "Tulsi Chai",
    "Masala Chai"
]

unique_chais = {item for item in favourite_chais} # Automatically removes duplicates
print(unique_chais)

recipes = {
    "Masala Chai":["ginger" , "cardamom" , "cloves" , "cinnamon"],
    "Ginger Chai":["ginger"],
    "Cardamom Chai":["cardamom"],
    "Tulsi Chai":["tulsi"]
}

unique_spices = { i for item in recipes.values() for i in item if i == "ginger"} # Flattening the list of lists and creating a set
print(unique_spices)

