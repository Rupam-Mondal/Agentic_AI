# value = 13
# remainder = value % 5

# if remainder:
#     print("Hi")


value = 13

if (remainder := value % 5):
    print(f"Hi {remainder}")

flavours = ["masala" , "ginger" , "lemon"]

print("Available flavours " , flavours)

while (flavour := input("Enter flavour")) not in flavours:
    print("Sorry no available")