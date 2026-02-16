from NULL_not_found import NULL_not_found
import sys
import io

class DoublePrint:
    def __init__(self, *files):
        self.files = files
    
    def write(self, data):
        for f in self.files:
            f.write(data)
    
    def flush(self):
        for f in self.files:
            f.flush()

buffer = io.StringIO()

DoublePrint = DoublePrint(sys.stdout, buffer)
old_stdout = sys.stdout
sys.stdout = DoublePrint

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

sys.stdout = old_stdout

captured = buffer.getvalue()

test = "Nothing: None <class 'NoneType'>\n\
Cheese: nan <class 'float'>\n\
Zero: 0 <class 'int'>\n\
Empty: <class 'str'>\n\
Fake: False <class 'bool'>\n\
Type not Found\n\
1\n"

print('\n')
print('captured', repr(captured), '\n')
print('test', repr(test))

if captured == test:
    print("\nTEST PASSED")
else:
    print("\nTEST FAILED")





