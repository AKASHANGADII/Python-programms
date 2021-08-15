from random import *
def guess_num(start,end,n):
    guess_num = " "
    tries=1
    while(guess_num!=n):
        guess_num = int(input("Guess the number>> "))
        if(guess_num>n):
            print("Try again you guessed to high")

        elif(guess_num<n):
            print("Try again you guessed to low")

        elif(guess_num==n):
            print("Congratulations")
            print("You guessed the correct one")
            print("Number of guesses = {}".format(tries))
            exit()

        tries+=1
        

start = int(input("Enter the starting number>> "))
end = int(input("Enter the ending number>> "))
n = randint(start,end)

guess_num(start,end,n)