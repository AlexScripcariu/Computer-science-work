path = "D:\\git-projects\\Computer-science-work\\projects\\file-handling\\challenge-106\\"


with open(path + "Names.txt", "a") as file:
	new_name = input("Please enter a new name: ")
	file.write(new_name + "\n")
