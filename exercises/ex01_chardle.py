"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730243145"

word: str = input("Enter a 5-character word:")
if (len(word) == 5):
    character: str = input("Enter a single character:")
    if (len(character) == 1):
        print("Searching for " + character + " in " + word)
        count = 0

        if (word[0] == character):
            print(character + " found at index 0")
            count =+ 1

        if (word[1] == character):
            print(character + " found at index 1")
            count =+ 1

        if (word[2] == character):
            print(character + " found at index 2")
            count =+ 1

        if (word[3] == character):
            print(character + " found at index 3")
            count =+ 1

        if (word[4] == character):
            print(character + " found in index 4")
            count =+ 1

        if count == 0: 
            print(character + " not found")

        print(str(count) + " instance of " + character + " found in " + word)
    else: print("Error: Character must be a single character")

else:
    print("Error: Word must contain 5 characters")