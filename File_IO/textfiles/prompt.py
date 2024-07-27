path = "another.txt"
with open(path, "a") as file:
    prompt=""
    if prompt != "stop":
        prompt = input("Append to text file: ")
        file.write("[[" + prompt + "]]" + "\n")
    else:
        break
