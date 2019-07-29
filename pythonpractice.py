#BMI function

#Ask  user to enter height and weight
height = float(input(" What is your height in meters? "))
weight = float(input(" WHat is your weight in kilograms? "))

#Calculate and report body mass index (BMI)
bmi= weight/(height **2)
print( " Your BMI is", bmi)


#if I want to round BMI number in terms of decimals
print( "Your BMI is", round(bmi, 1))

#Determine if underweight, healthy weight, or overweight
if bmi<25:
    print(" You are a healthy weight ")
else:
    print(" You are overweight ")


# Example While Loop

#Define variable counter
counter=1

while counter<=10:
    print(counter)
    counter= counter+1

#Magic Number program
#Define variable magic_number

magic=7
magic<10
#Ask user for a number
guess=int(input(" Please guess the magic number: "))

while guess!=magic:
    print(" Sorry, that is wrong ")
    guess=int(input("Please try entering another number: "))

print(" Congratulations, that is the magic number! ")
print(" Goodbye ")

#Another way for the number Game

import random
answer= random.randint(1,10)
print(answer)

while True:
    guessString= raw_input("give me a guess: ")
    guess= int(guessString)
    if guess==answer:
        print(" you got it")
else:
    print("You are wrong")
break
