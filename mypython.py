# #BlackJack Game

#Make a random generator
import random

score = 0

def drawCard():
    answer = random.randint(2,11)
    return answer

#Give a result
def drawResult(card):
    print("You a drew a: " + str(card))

while True:
    option = raw_input("Draw a card? ")
    if option == "y":
        card = drawCard()
        drawResult(card)
        score = score + card
        if score > 21:
            print("Get busted!")
            break
        else:
            print("Current Score: " + str(score))
    elif option == "n":
        print("Final Score: " + str(score))
        break
