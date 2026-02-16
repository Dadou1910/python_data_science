
import os

print("---- VALID TESTS ----")

tests = [
    ("hello world apple banana", 5),
    ("a bb ccc dddd", 0),
    ("a bb ccc", 10),
    ("one two three four five", 3),
]

for i, (text, n) in enumerate(tests, 1):
    print(f"\nTest {i}")
    print(f"Input string: \"{text}\"")
    print(f"N: {n}")
    os.system(f"python3 filterstring.py \"{text}\" {n}")

print("\n---- ERROR TESTS ----")

print("\nTest E1: missing argument")
os.system("python3 filterstring.py 'hello world'")

print("\nTest E2: too many arguments")
os.system("python3 filterstring.py 'hello world' 3 extra")

print("\nTest E3: non-integer N")
os.system("python3 filterstring.py 'hello world' abc")

print("\nTest E4: empty string")
print("Input string: \"\" | N: 3")
os.system("python3 filterstring.py '' 3")
