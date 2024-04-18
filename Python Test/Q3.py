"""Q3.Write a program that prints all prime numbers between 0 to 50."""

def check_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

for i in range(2,51):
    if check_prime(i)==True:
        print(i)

#Output -: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

