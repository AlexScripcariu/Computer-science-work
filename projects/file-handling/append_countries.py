from pathlib import Path

path = Path("D:\\git-projects\\Computer-science-work\\projects\\file-handling\\task-two\\read_countries.py").parent.absolute()

with open(str(path) + "\\Countries.txt", "a") as file:
  file.write("France\n")

  