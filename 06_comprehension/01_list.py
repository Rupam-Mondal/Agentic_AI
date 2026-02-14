menu = [
    "Masala Dosa",
    "Idli",
    "Vada",
    "Pongal"

]

# [expression for item in iterable if condition]

pongal = [ item for item in menu if "Pongal" in item]

print(pongal)