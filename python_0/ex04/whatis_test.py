import os

print("Test 1: Even number")
os.system("python3 ex04/whatis.py 4")

print("\nTest 2: Odd number")
os.system("python3 ex04/whatis.py 5")

print("\nTest 3: Odd number")
os.system("python3 ex04/whatis.py -8")

print("\nTest 4: Too many arguments")
os.system("python3 ex04/whatis.py 1 2")

print("\nTest 5: No arguments")
os.system("python3 ex04/whatis.py")

print("\nTest 6: Not an integer")
os.system("python3 ex04/whatis.py hello")
