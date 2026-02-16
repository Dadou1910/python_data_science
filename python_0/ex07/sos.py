import sys

def translate(text):
    """Translate text into morse"""
    NESTED_MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    ' ': '/'
    }
    return " ".join(NESTED_MORSE.get(c, '?') for c in text.upper())

def isalphanum(text):
    """checks if text only contains chars, nums and spaces"""
    return all(c.isalnum() or c.isspace() for c in text)

def main(argv):
    """
    Docstring for main
    
    :string argv: string to be translated to morse code
    """
    try:
        if len(argv) != 2 or not isalphanum(argv[1]):
            raise AssertionError("The arguments are bad")
        print(translate(argv[1]))
        
    except AssertionError as error:
        print(AssertionError, __name__, error)

if __name__ == '__main__':
    main(sys.argv)