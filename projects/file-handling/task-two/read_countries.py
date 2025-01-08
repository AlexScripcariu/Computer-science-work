from pathlib import Path

path = Path("D:\\git-projects\\Computer-science-work\\projects\\file-handling\\task-two\\read_countries.py").parent.absolute()

with open(str(path) + "\\Countries.txt", "w") as file:
  file.writelines(["Romania\n", "Belgium\n", "France\n", "Netherlands\n"])


with open(str(path) + "\\Countries.txt", "r") as file:
  print(file.read())

