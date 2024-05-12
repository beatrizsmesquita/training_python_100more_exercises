# Take numbers from a user and show the average of the numbers the user entered.

len_input = int(input("How many numbers you want to enter?"))

inputs=[]
for i in range(len_input):
    numbers_str=input("Enter one number: ")
    inputs.append(int(numbers_str))

avg = sum(inputs)/len(inputs) if len(inputs) !=0 else 0
print(f'The average of {inputs} is: ', avg)
