path = "D:\\git-projects\\Computer-science-work\\projects\\file-handling\\challenge-106\\"

selected_name = ""

with open(path + "Names.txt", "r") as file:
    lines = file.readlines()
    selected_name = input("Please enter the name to delete: ")

with open(path + "Names.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != selected_name:
            f.write(line)