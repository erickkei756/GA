#homework 3, problem 1


characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]
for string in characters:
  if 'u' in string:
    print(string + " " + "U are so Uniquely U!")
  elif 'i' in string:
    print(string + " " + "I bet you're Impressively Intelligent!")
  elif 'o' in string:
    print(string + " " + "O My! How Original!")
  else:
    print(string + " " + "Ehh, a's and e's are so ordinary.")
