"""Q8.Write a program for reversing the given number 5436 and the output should be 6345."""

num  = 5436
new_number = 0

while num>0:
    digit = num%10
    num = num//10
    new_number = new_number*10+digit
else:
    print("Reverse number will be :",new_number)

#Output -: Reverse number will be : 634