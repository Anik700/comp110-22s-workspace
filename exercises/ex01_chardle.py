"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730243145"

# instantiate variables that accept user input
word: str = input("Enter a 5-character word:")
# Checking that user input abides by set constraints
if (len(word) == 5):
    character: str = input("Enter a single character:")
    if (len(character) == 1):
        print("Searching for " + character + " in " + word)
        # Number of occurances 
        count = 0
# Searching string for inputed character acorss indexes
        if (word[0] == character):
            print(character + " found at index 0")
            count = count + 1

        if (word[1] == character):
            print(character + " found at index 1")
            count = count + 1

        if (word[2] == character):
            print(character + " found at index 2")
            count = count + 1

        if (word[3] == character):
            print(character + " found at index 3")
            count = count + 1

        if (word[4] == character):
            print(character + " found at index 4")
            count = count + 1

        if count == 0: 
            print("No instances of" + character + " in " + word)
        if count > 1:
            print(str(count) + " instances of " + character + " found in " + word)
        else:
#Program output
            print(str(count) + " instance of " + character + " found in " + word)

#Error messages if contraints not met
    else: 
        print("Error: Character must be a single character")
        quit()

else:
    print("Error: Word must contain 5 characters")
    quit()