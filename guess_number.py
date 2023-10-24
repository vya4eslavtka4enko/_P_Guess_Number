from art import logo
from art import win
from art import lose
import random 
print(logo)
print("Welcom to the number guessing game ")
print("I am thinking of a number between 1 and 100 ")
level = input('Choose a dificulty.Type "easy" or "hard"')
# global variable
lives = 0


# function
def setLevel(level):
    if level == "hard":
        lives = 5
    else:
        lives = 10
    return lives
    
def setNumber():
    guessNumber = random.randint(1,100)
    return guessNumber

lives =setLevel(level)
guessNumber=setNumber()
print(guessNumber)
print(f"You have {lives} attempts remaining to guess a number ")
ChooseNumber = 0
while guessNumber != ChooseNumber:
      ChooseNumber = int(input("Make a guess "))
      if ChooseNumber == guessNumber:
          print(win)
      lives-=1
      print(lives)
      if lives == 0:
        print(lose)
        break
    
    


    
