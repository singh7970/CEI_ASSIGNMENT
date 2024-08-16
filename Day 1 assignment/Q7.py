# This is the content of Q7.py
# Q7 Create a program that prints the multiplication table of a given number using a while loop.


number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
