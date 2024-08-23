n=int(input("Enter the Nmber of question"))
for i in range(1,n):
    filename=f"Q{i}.py"
    with open(filename,'w')as file:
        file.write("This is the content of "+filename+"\n")

