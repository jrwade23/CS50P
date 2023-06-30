# Only use modified_twttr.py to run  test_twttr.py successfully.

# Removes all vowels from input string and prints result

def main():
    word = input("Input: ")

    print(shorten(word))

def shorten(w):
    new = ""
    for letter in w:
        match letter.lower():
            case "a" | "e" | "i" | "o" | "u":
                None
            case _:
                new = new + letter
    return new

if __name__ == "__main__":
    main()
