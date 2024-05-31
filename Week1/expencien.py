
import sys
try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("Error value!")
    sys.exit(1)

sum = x + y
print(f"Sum: {sum}")