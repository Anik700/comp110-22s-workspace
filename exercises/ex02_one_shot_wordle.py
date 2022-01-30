"""ex02: One Shot Wordle"""

__author__ = "730243145"


SECRET= "python"
guess = str(input("What is your " + str(len(SECRET)) + "-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index = 0
result = ""

# code that makes sure the length of guess = length of secret word
while len(guess) != len(SECRET):
    guess = str(input("That was not " + str(len(SECRET)) + "-letters! Try again: "))

if guess == SECRET:
    while index < len(SECRET):
        if guess[index] == SECRET[index]:
            result += GREEN_BOX

        index += 1
    print(result)
    print("Woo! You got it!")
else:
    while index < len(SECRET):
        if guess[index] == SECRET[index]:
            result += GREEN_BOX
        else:
# Declaring bool variable as false and alternate index as 0 
            yell = False
            altindex = 0
            while yell == False and altindex < len(SECRET):
                if SECRET[altindex] == guess[index]:
                    yell = True
                else:
                    altindex += 1
# If yell evaluates to True the while loop is closed and a yellow box is printed for that index
            if yell == True:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX

        index += 1
    print(result)
    print("Not quite. Play again soon!")
