
import random
n=  random.randint(1,9)
guess=int(input("Enetr a numbe between 1 to 9 "))
while n !="guess":
    print
    if guess < n:
        print("guess is low")
        guess=int(input("Enetr a numbe between 1 to 9 "))
    elif guess > n:
        print("guess is high ")
        guess=int(input("Enetr a numbe between 1 to 9 "))
    else:
        print(" You have guessed it ")
        break 
    print 




