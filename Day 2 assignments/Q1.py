"""Q 1 -write a python program thatinitializers with 5 number add 
 a new number to the array and prints the updated array"""
import numpy as np

list=[1,2,3,4,5]
arr=np.array(list)

print(type(arr))

new_number=10
new_arr=np.append(arr,new_number)
print("old array",list)
print("new array",new_arr)


