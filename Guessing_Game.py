import random

num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

main = input("Pick a number 1 through 10: ")

answer = random.choice(num_list)


if main == answer:
    print("You Win!")
else:
    print("You Lose!")




