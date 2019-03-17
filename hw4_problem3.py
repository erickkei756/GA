user_entry = input("enter a word to be reversed: ")

output = ""
for i in range(len(user_entry)):
  reverse = len(user_entry) - i - 1
  output += user_entry[reverse]

print(output)
