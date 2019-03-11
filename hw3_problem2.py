#homework 3, problem 2

temp = 90
while temp > 75:
  temp = temp -3
  action = print(f"The temperature is {temp} - crank the AC!")
  if temp == 75:
    print(f"{temp}. Ah, Much better!")
    break
