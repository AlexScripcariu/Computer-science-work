file_prefix = "C:\\Users\\21scripcariua-wes\\Computer-science-work\\projects\\file-handling\\"

# file = open(file_prefix + "countries.txt", "w")
# file.write("Italy\n")
# file.write("Poland\n")
# file.write("Germany\n")
# file.write("Spain\n")
# file.write("Greece\n")
# file.close()

with open(file_prefix + "countries.txt", "r") as file:
    print(file.read())