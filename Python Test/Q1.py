"""Q1. Write a Python program that defines a function called "add_numbers" that takes two
arguments (i.e.,
numbers) and returns their sum. Within the function, add the two numbers together and return
the result
using the return statement. Call the function with the values 5 and 6, and print out the returned
result.
This will result in the addition of 5 and 6, with the output of the program being the sum of these
two
numbers."""

def add_numbers(num1,num2):
    result = num1+num2
    return result

result = add_numbers(5,6)
print("The sum of two number will be ",result)


#Output -: The sum of two number will be  11