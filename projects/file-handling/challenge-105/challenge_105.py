file_ext = "C:\\Users\\21scripcariua-wes\\Computer-science-work\\projects\\file-handling"
folder = "challenge-105\\"
path = file_ext + folder

try:
    with open("C:\\Users\\21scripcariua-wes\\Computer-science-work\\projects\\file-handling\\challenge-105\\Numbers.txt", "w") as file:
        file.write("1, 2, 3, 4, 5")
except FileNotFoundError:
    print("File not Found!")