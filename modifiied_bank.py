# Only use modified_bank.py to run  test_bank.py successfully.

def main():
    
    greeting = input("Type your greeting here: ")
    print(value(greeting))
    

def value(greet):
    greet = greet.strip().lower()

    if greet.startswith("hello"):
        return "$0"
    elif greet.startswith("h"):
        return "$20"
    else:
        return "$100"
    

if __name__ == "__main__":
    main()