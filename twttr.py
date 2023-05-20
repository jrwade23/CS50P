# Removes all vowels from input string and prints result

def main():
    orig = input("Input: ")

    print(remove_vowels(orig))

def remove_vowels(o):
    new = ""
    for letter in o:
        match letter.lower():
            case "a" | "e" | "i" | "o" | "u":
                None
            case _:
                new = new + letter
    return new

main()