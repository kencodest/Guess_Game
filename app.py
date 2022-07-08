#This is a guess the number game made by Ken Muia

#import the random module to generate random numbers
import random 

print('Hello, what is your name?')
name = input()
print('Well, '+name+' I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)
trials = len(list(range(1,6))) #length of the list of range elements is 5

while(True):
    try:
        for guessesTaken in range(1,trials+1): #added 1 to trials so that the range is from 1 to 5 as intended
            print('Take a Guess!! You have trials ('+str(trials)+') left')
            trials -= 1
            guess = int(input())
            if guess < secretNumber:
                print('Nop! Guess too low!')
            elif guess > secretNumber:
                print('Nop! Guess too high!')
            else:
                break

        if guess == secretNumber:
            print('You got it! Took you '+str(guessesTaken)+' guess(es) to hack') 
            break
        else:
            print('Well, the number I was thinking of is '+str(secretNumber))
            break
    except:
        print('You did not enter a number. Try again')
    if trials == 0:
        break