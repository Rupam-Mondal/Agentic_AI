staff = [("Amit" , 16) , ("Zara" , 17)]

for name , age in staff:
    if age < 18:
        print("Hi")
        break
else:
    print("No one")