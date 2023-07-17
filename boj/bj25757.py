import sys

inputs = sys.stdin.readlines()

game = inputs[0].split()[1]
if game == "Y":
    game = 1
if game == "F":
    game = 2
if game == "O":
    game = 3


print(len(set(inputs[1:])) // game)
