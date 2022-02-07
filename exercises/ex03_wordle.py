"""Ex03 - Structured Wordle."""

__author__ = "730243145"

def contains_char(word: str, index: str) -> bool:
    assert len(index) == 1

    """Defining Character Search."""
    i = 0

    while i < len(word):
        if word[i] == index:
            return True
        i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    """Adding Colored Boxes to Output."""
    i = 0
    returned = ""
    while i < len(guess):
        if(contains_char(secret, guess[i])):
            if(secret[i] == guess[i]):
                returned += GREEN_BOX
            else:
                returned += YELLOW_BOX
        else:
            returned += WHITE_BOX
        i += 1
    return returned


def input_guess(exp_len: int) -> str:

    """Analyzing Expected Length and Guess Length."""
    inp = str(input(f"Enter a {exp_len} character word: "))
    
    while len(inp) != exp_len:
        inp = str(input(f"That wasn't {exp_len} chars! Try again: "))
    
    return inp

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET = "codes"
    GREEN_BOX: str = "\U0001F7E9"
    turns = 1

    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")

        guess = input_guess(len(SECRET))
        emojis = emojified(guess, SECRET)

        if guess != SECRET:
            print(emojis)
        else:
            print(emojis)
            print(f"You won in {turns}/6 turns!")
            turns = 8000000

        turns += 1

    if turns == 7:
        print ("X/6 - Sorry, try again tomorrow!")
