import sys

from ft_filter import ft_filter

def check_length(S, N):
    """
    Accepts 2 arguments:
    
    :str S: The string to break down into words to analyze
    :int N: The min length of words selected from the S string
    """
    text = S.split()
    return list(ft_filter(lambda x: len(x) > N, text))

def main(argv):
    try:
        if len(argv) != 3:
            raise AssertionError("The arguments are bad")
        try:
            n = int(argv[2])
        except:
            raise AssertionError("Arguments should be a string followed by an int")
        print(check_length(argv[1], n))
        
    except AssertionError as error:
        print(AssertionError, __name__, error)

if __name__ == '__main__':
    main(sys.argv)