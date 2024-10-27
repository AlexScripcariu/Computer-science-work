first_line = input("Please enter the first line of a nursery rhyme: ")
print(len(first_line))
start = int(input("Please enter a starting number: "))
end = int(input("Please enter an ending number: "))

print(first_line[start - 1:end])