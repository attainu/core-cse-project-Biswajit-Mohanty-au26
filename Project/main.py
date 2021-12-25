user1 = input("enter your name ")
user2 = input("enter your name ")

ladder = {2:37, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
snake = {32:10, 34:6, 48:26, 62:18, 88:24, 95:56, 97:78}
pos1 = 0
pos2 = 0
import random
def move(pos):
    dice = random.randint(1,6)
    print(f"Dice:{dice}")
    pos = pos + dice
    if pos in snake:
        print("bitten by snake")
        pos = snake[pos]
        print(f"position:{pos}")
    elif pos in ladder:
        print("climmed by ladder")
        pos = ladder[pos]
        print(f"position:{pos}")
    else:
        print(f"position:{pos}")
    return pos
while True:
    print(user1,"enter A to throw the dice :")
    A =input()
    pos1 = move(pos1)
    if pos1 >= 100:
        print(user1, "win the game")
        break
    print(user2,"enter B to throw the dice :")
    B = input()
    pos2 = move(pos2)
    if pos2 >= 100:
        print(user2 ,"win the game")
        break

