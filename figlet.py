def main():
    import sys
    import random
    from pyfiglet import Figlet
    f = Figlet()

    # for len(sys.argv) == 1 set random font
    if len(sys.argv) == 1: 
        random_font = random.choice(f.getFonts())
        f.setFont(font = random_font)

    # for len(sys.argv) == 3 validate/set requested font
    elif len(sys.argv) == 3:
        valid_font = validate_font(sys.argv[1], sys.argv[2])
        f.setFont(font = valid_font)

    # len(sys.argv) was neither 1 or 3    
    else:
        sys.exit("Invalid usage")

    # obtain input from user and print
    string = input("Input: ")
    print(f.renderText(string))
    

def validate_font(argv1, argv2):
    import sys
    from pyfiglet import Figlet
    f = Figlet()

    # if 1st input is NOT -f or --font then exit with error msg
    if argv1 != "-f" and argv1 != "--font":
        sys.exit("Invalid usage")
    
    # invalid font request
    elif argv2 not in f.getFonts():
        sys.exit("Invalid usage")

    # requested font was valid
    else:
        return argv2

    
if __name__ == "__main__":
    main()