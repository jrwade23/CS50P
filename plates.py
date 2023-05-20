    # Determine the validity of a vanity plate that must follow the following rules

    # “All vanity plates must start with at least two letters.”

    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) 
    # and a minimum of 2 characters.”

    # “Numbers cannot be used in the middle of a plate; they must come at the end. 
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
    # The first number used cannot be a ‘0’.”

    # “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_alpha_numeric(s):
        if meet_char_limits(s):
            if start_w_letters(s):
                return only_num_at_end(s)
            else:
                return False
        else:
            return False
    else:
        return False


def is_alpha_numeric(p):
    return p.isalnum()


def meet_char_limits(p):
    return 2 <= len(p) <= 6


def start_w_letters(p):
    return p[0:2].isalpha()

    
def only_num_at_end(p):
    end = ""
    for letter in p:
        if letter.isnumeric():
            start, end = p.split(letter, 1) # 'end' contains all characters after first number
            break
    if letter == "0":   # Is first number 0?
        return False
    elif end == "":     # Are all characters alphabetical?
        return True
    else:               # Does the string end in all numbers (no numbers in middle)
        return end.isnumeric()
    

main()