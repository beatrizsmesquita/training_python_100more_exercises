# Take numbers from a user and show the average of the numbers the user entered.

numbers_input = input("Write the numbers you want to get the average of, separated by commas: ")

numbers_str = numbers_input.split(',') 
numbers_int=[]

for i in numbers_str:
    numbers_int.append(int(i))

for v in numbers_int:
    if len(numbers_int) != 0:
        avg=sum(numbers_int)/len(numbers_int)
    else:
        avg = 0 #There's no number to calculate

print(f'The average of {numbers_int} is: ', avg)
