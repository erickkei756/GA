
angry = True
bored = True
hungry = False
tired = False

# Example `if` statement:
if angry and hungry and bored:
  print("Eat the Triceratops.")
elif tired and hungry:
  print("Eat the Iguanadon.")
elif hungry and bored:
  print("Eat the Stegasaurus.")
elif tired:
  print("Go to bed.")
elif angry and bored:
  print("Fight the Velociraptor.")
elif angry or bored:
  print("Roar.")
else:
  print("Give a toothy smile.")
