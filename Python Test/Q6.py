"""Q6. How can you create a program that determines whether a given number (in this case, 98) is
even or
odd? The program should be designed to take the number as input and perform the necessary
calculations to determine whether it is divisible by two. If the number is divisible by two without
leaving a
remainder, it is an even number, and if there is a remainder, it is an odd number. The output of
the
program should indicate whether the given number is even or odd."""

number = int(input('Enter the number :'))

if number%2==0:
    print('Even Number')
else:
    print('Odd Number')

#Output -:number = 21  Odd Number