import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
curr_temp = 95.4999999999

print(f"Ideal Temp {ideal_temp}")
print(f"Curr Temp {curr_temp}")
print(f"Diff Temp {ideal_temp - curr_temp}")

# for precision

print(sys.float_info)
