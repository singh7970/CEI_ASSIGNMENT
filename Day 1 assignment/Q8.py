# This is the content of Q8.py
# Q8 . Write a Python program that iterates through numbers 1 to 10 and prints each number. Use the
# continue statement to skip numbers that are divisible by 3.


for i in range(1, 11):
    if i % 3 == 0:
        continue  
    print(i)
