#hw11_problem5

# problem 5

# Add your own! :)
tv_characters = ["Will Byers", "Tyrion Lannister", "Oliver Queen", "Jean Luc Picard", "Malcom Reynolds", "The Doctor", "Sam Winchester", "Sherlock Holmes"]

# Write out my character list to a file called "text"
for index, character in enumerate(tv_characters):
  f = open("text", "a") # use "a" instead of "w to append instead of write"
  f.write("{0}: {1}\n".format(index+1, character))
  f.close()
