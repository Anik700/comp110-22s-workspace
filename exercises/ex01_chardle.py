"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730243145"

# instantiate variables that accept user input

WORD: str = input("Enter a 5-character word:")

# Checking that user input abides by set constraints

if (len(WORD) == 5):
    CHARACTER: str = input("Enter a single character:")
    if (len(CHARACTER) == 1):
        print("Searching for " + CHARACTER + " in " + WORD)

        # Number of occurances 

        COUNT = 0

# Searching string for inputed CHARACTER acorss indexes

        if (WORD[0] == CHARACTER):
            print(CHARACTER + " found at index 0")
            COUNT = COUNT + 1

        if (WORD[1] == CHARACTER):
            print(CHARACTER + " found at index 1")
            COUNT = COUNT + 1

        if (WORD[2] == CHARACTER):
            print(CHARACTER + " found at index 2")
            COUNT = COUNT + 1

        if (WORD[3] == CHARACTER):
            print(CHARACTER + " found at index 3")
            COUNT = COUNT + 1

        if (WORD[4] == CHARACTER):
            print(CHARACTER + " found at index 4")
            COUNT = COUNT + 1

        if COUNT == 0: 
            print("No instances of" + CHARACTER + " in " + WORD)
        if COUNT > 1:
            print(str(COUNT) + " instances of " + CHARACTER + " found in " + WORD)

# Error messages if constraints not met

        if COUNT < 1:
            print("No instances of " + CHARACTER + " found in " + WORD)
        else:


            print(str(COUNT) + " instance of " + CHARACTER + " found in " + WORD)


    else: 
        print("Error: Character must be a single Character")
        quit()

else:
    print("Error: WORD must contain 5 characters")
    quit()