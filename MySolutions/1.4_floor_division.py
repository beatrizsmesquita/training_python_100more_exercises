#Find the floor division of two numbers.

var1 = int(input("Insert your first number: "))
var2 = int(input("Insert your second number "))

#print(f"The floor division between {var1} and {var2} is: ", var1//var2)

## Using flooe method from the math module

import math
print(f"The floor division between {var1} and {var2} is: ", math.floor(var1/var2))
