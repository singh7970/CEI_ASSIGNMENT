for i in range(1, 12):
    filename = f"Q{i}.py"
    with open(filename, 'w') as file:
        file.write("# This is the content of " + filename + "\n")
    print(f"{filename} created.")
    