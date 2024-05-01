#Find the max number of two numbers.

var1 = int(input("Insert your first number: "))
var2 = int(input("Insert your second number "))
var3 = int(input("Insert your third number "))


def maximumof3(var1,var2,var3):
    if var1>=var2:
        if var1>=var3:
            return var1
    if var2>=var1:
        if var2>=var3:
            return var2
    if var3>=var1:
        if var3>=var2:
            return var3

#print("The max between your three numbers is: ", max(var1, var2, var3))
print("The max between your three numbers is: ", maximumof3(var1, var2, var3))
