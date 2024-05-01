#Find the max number of two numbers.

var1 = int(input("Insert your first number: "))
var2 = int(input("Insert your second number "))

# Another alternative: find a functions to find the maximum of 2 number

def maximum(var1,var2):
    if var1>=var2:
        return var1
    else:
        return var2
    
#print("The max between your two numbers is: ", max(var1, var2))
print("The max between your two numbers is: ", maximum(var1, var2))
