path = "test.txt"

with open(path, "a") as file:
    while True:
        prompt = input("Text to add: ")
        if prompt == "stop":
            break
        file.write("[[" + prompt + "]]" + "\n")
