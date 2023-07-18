def print_map_of_africa():
  for i in range(0, 20):
    for j in range(0, 20):
      if i < 10 and j < 10:
        print("*", end="")
      elif i < 10 and j >= 10:
        print(" ", end="")
      elif i >= 10 and j < 10:
        print(" ", end="")
      else:
        print("*", end="")
  print()

print_map_of_africa()




africa_map = [
    "      **       ",
    "   *******    ",
    " **********   ",
    "************ ",
    "************ ",
    " **********   ",
    "  *********  ",
    "   ********  ",
    "     ******  ",
    "      *****  ",
    "       ****  ",
    "        ***  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "         **  ",
    "             "
]

for row in africa_map:
    print(row)
