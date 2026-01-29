def pure_chai(cups):
    return 10 * cups

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += 10 * cups
    return total_chai

