import sys

def general_count(text):
    """Counts and prints char types in text"""

    text_len = len(text)
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    digits = sum(1 for char in text if char.isdigit())
    punctuation = sum(1 for char in text if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    space = sum(1 for char in text if char.isspace())
    
    print(f"The text contains {text_len} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")   
    

def main(argv):
    """
    Analyzes the contents of a texting and counts the number
    of different char types.

    The texting is either put as argument in the terminal or
    inputed by the user.
    """
    try:
        if len(argv) < 2:
            try:
                argv = input("What is the text to count?\n")
            except EOFError:
                print("Program has ended.")
                return
        elif len(argv) > 2:
            raise AssertionError("Too many arguments provided")
        general_count(argv[1])
    except AssertionError as error:
        print(AssertionError, __name__, error)


if __name__ == '__main__':
    main(sys.argv)