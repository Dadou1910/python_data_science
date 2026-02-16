import os

print("---- SOS.PY TESTS ----")

tests = [
    ("SOS", "... --- ..."),
    ("HELLO", ".... . .-.. .-.. ---"),
    ("ABC", ".- -... -.-."),
    ("HI 2", ".... .. / ..---"),
    ("SOS HELP", "... --- ... / .... . .-.. .--."),
]

for i, (inp, expected) in enumerate(tests, 1):
    print(f"\nTest {i}")
    print(f"Input    : {inp}")
    print(f"Expected : {expected}")
    print("Output   :")
    os.system(f"python3 sos.py \"{inp}\"")


