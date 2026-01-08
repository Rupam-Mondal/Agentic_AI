class Chai:
    def __init__(self , milk_level , sweetness):
        self.milk_level = milk_level
        self.sweetness = sweetness

    def add_suger(self , suger):
        print("Added sugar")


my_chai = Chai(100 , 200);
my_chai.add_suger(5);