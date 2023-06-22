# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

#     If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#     If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#     If the guess is the same as that integer, the program should output Just right! and exit.


def main():
    import random
    
    level = set_level("Level: ")

    random_int = random.randint(1, level)

    guess = validate_guess("Guess: ")

    if guess == random_int:
        print("Just right!")
    elif guess < random_int:
        print("Too small!")
    else:
        print("Too large!")

def set_level(l):
    l = 0
    while l < 1:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
    return l

def validate_guess(g):
    g = 0
    while g < 1:
        try:
            g = int(input("Guess: "))
        except ValueError:
            pass
    return g

if __name__ == "__main__":
    main()