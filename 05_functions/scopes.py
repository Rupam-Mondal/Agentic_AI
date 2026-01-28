def serve_chai():
    chai_type = "masala" # local variable
    print(f"Serving a cup of {chai_type} chai.")

chai_type = "ginger"
serve_chai()
print(f"Outside the function, chai_type is {chai_type}.")

def chai_counter():
    chai_order = "lemon" # Enclosed variable
    def prepare_chai():
        chai_order = "Ginger"
        print(f"Preparing a cup of {chai_order} chai.")
    prepare_chai()
    print(f"Chai order is {chai_order}.")

chai_counter()