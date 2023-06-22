# In a file called emojize.py, implement a program that prompts the user for a str in English 
# and then outputs the “emojized” version of that str, converting any codes (or aliases) therein 
# to their corresponding emoji.

# First had to download/install emoji package. <pip install emoji>

def main():
    import emoji

    request = input("Input: ")
    print(emoji.emojize(request, language="alias"))

if __name__ == "__main__":
    main()