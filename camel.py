# Converts a file name in camelCase format to snake_case

def main():
    # get input from user in camel case format
    camel = input("camelCase: ")
    # print output of snake format conversion function
    print(snake_case(camel))
    
def snake_case(c):
    # s is a blank string that c will be converted over to, letter by letter
    s = ""
    # looks at string c (letter by letter) looking for upper case letters
    for letter in c:
        if letter.isupper():
            # when upper is found, add an underscore + lower case version of letter to s
            s = s + "_" + letter.lower()
            #print(letter)  // Checkpoint Tests
            #print(s)
        else:
            # when lower is found, add letter as is to s
            s = s + letter
            #print(s)  // Checkpoint Test
    return s

main()