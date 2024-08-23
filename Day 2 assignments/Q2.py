
""" Q 2 - Create a program that takes user input to add multiple
 elements to an array ,then print to final array"""

array=[]
ele=int(input("How many element you want to add in Array : "))
for i in range(0,ele):
    user=int(input(f"enter the number of {i} index :"))
    array.append(user)

print("Your final array is",array)    
