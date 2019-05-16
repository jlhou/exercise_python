import random
compute = random.randint(1, 3)
player = int(input("请玩家出拳(1)拳头(2)剪刀(3)布"))
if ((player == 1 and compute == 2)
        or (player == 2 and compute == 3)
        or (player == 3 and compute == 1)):

    print("玩家赢")
elif compute == player:
    print("平局")
else:
    print("电脑赢")


