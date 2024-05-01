# Swap two variables.

# To swap two variables: the value of the first variable will become the value of the second variable. 
# On the other hand, the value of the second variable will become the value of the first variable.

var1 = int(input("Insert you first number "))
var2 = int(input("Insert your second number "))

print("Variable 1: ", var1, "\nVariable2: " , var2)
#temporaryvar = var1
#var1 = var2
#var2= temporaryvar

#Shortcut:
var1, var2 = var2, var1

print("Variable 1: ", var1, "\nVariable2: " , var2)
