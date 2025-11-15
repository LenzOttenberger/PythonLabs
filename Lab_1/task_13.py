import random

rand = random.randint(1, 100)

while(True):
    ans = int(input('Enter ans: '))
    if ans > rand:
        print('Lower')
    elif ans < rand:
        print('Higher')
    elif ans == rand:
        print('U won!')
        break