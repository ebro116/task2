import random

def toss_coin():
    num = random.randint(0,1)
    if num == 1:
        return "Head"
    else:
        return "Tail"
