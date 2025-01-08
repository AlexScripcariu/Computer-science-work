path = "D:\\git-projects\\Computer-science-work\\projects\\file-handling\\challenge-109\\"

code = ""
val = 0

try: 
  print("1) Create a new file")
  print("2) Display the file")
  print("3) Add a new item to the file") 
  val = int(input("Please write 1, 2 or 3: "))
except ValueError:
  print("Please type in a number between 1-3!")
else:
  if not(1 <= val <= 3):
    print("Please enter a number between 1-3!!!")

match val:
  case 1:
    code = "w"
  case 2:
    code = "r"
  case 3:
    code = "a"


def gen_result():
  with open(path + "Subject.txt", code) as file:
    if code == "r":
      print(file.read())
      return

    subject = input("Please enter a school subject: ")
    file.write(subject + "\n")


gen_result()