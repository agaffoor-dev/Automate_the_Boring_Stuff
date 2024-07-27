path = "append_test.txt" # Specifiy path of text file
with open(path, "w") as file:# Open text file for ability to write to
    file.write("tester\n")
    file.close()
