"""Q9.Write a program to check if a given number 371 is an Armstrong number?"""
number = 153
new_number = 0

while number>0:
    digit = number%10
    number=number//10
    new_number+=pow(digit,3)
else:
    if number==new_number:
        print("Armstrong Number")
    else:
        print('Not Armstrong Number')

