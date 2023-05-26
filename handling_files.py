with open("text.txt", "r") as file:
    var = file.read()
    print(var)

with open("text.txt", "r") as file:
    var = file.read()
    split_var = var.split(".")
    print(split_var[2])

with open("text.txt", "r") as file:
    var = file.readlines()
    print(var)

with open("text.txt", "r") as file:
    var = file.read()
    split_var = var.split(".")
    for x in split_var:
        print(x)

with open("text.txt", "a") as file:
    var = file.write("This is the last sentence")
    print(var)


with open("new_file.txt", "w") as file:
    var = file.write("This is my new file")
    print(var)
    file.close()
