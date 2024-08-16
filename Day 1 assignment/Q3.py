# This is the content of Q3.py
# Loop through numbers 1 to 10
for i in range(1, 11):
    
    # Create a filename with the format "Q1.py", "Q2.py", ..., "Q10.py"
    filename = f"Q{i}.py"
    
    # Open the file in write mode ('w'). If the file doesn't exist, it will be created.
    with open(filename, 'w') as file:
        
        # Write a comment inside the file indicating its filename
        file.write("# This is the content of " + filename + "\n")
    
    # Print a message to the console confirming that the file was created
    print(f"{filename} created.")
