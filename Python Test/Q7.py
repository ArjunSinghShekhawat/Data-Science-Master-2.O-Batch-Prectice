"""Q7.Write a program for sum of digits.The digits are 76543 and the output should be 25."""

sum = 0
num = 76543

while num>0:
    digit = num%10
    num = num//10
    sum+=digit
else:
    print("The all digit sum will be : ",sum)

#Output -: The all digit sum will be :  25