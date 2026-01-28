def update_order():
    chai_type = "Latte"
    def kitchen():
        nonlocal chai_type
        chai_type = "Cappuccino"
    kitchen()
    print(f"Updated chai type to {chai_type}")

update_order()

# nonlocal just see one scope above it, so it cannot access global variables.
# global is used to access global variables.