#Virtual Dice Game,
#Win if you roll a 6, lose a life if you don't
#You have 3 lives

from random import randint

lives = 100
while True: # Sort of infinite Loop
    diceroll = randint(1, 6)
    if diceroll==6:
        print("Congrats, You win")
        break
    else:
        lives = lives - 1 #You lose a life
        print(f"You rolled a {diceroll}, You lose a life, lives left: {lives}")
        if lives == 0:
            print("you lost!")
            break
print("Thanks for playing")