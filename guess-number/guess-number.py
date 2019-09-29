from random import randint     #这一行暂时不用理解

secret = randint (1,10)        #定义小明想的数所在的范围1~10
temp = input("小丽，我已经想好数字了，请在下面输入你猜的数字吧:")
guess = int(temp)

while guess != secret:
    if guess == secret:
        print("你真厉害，被你猜中啦，你是我心里的蛔虫吗？！")
    else:
        if guess > secret:
            print("这个数小于{}喔,，请重新输入吧：".format(guess))
        else:
            print("这个数大于{}喔，请重新输入吧：".format(guess))

    temp = input()
    guess = int(temp)

print("游戏结束，不玩啦^_^")

"""  假设小明想的数是7
小丽，我已经想好数字了，请在下面输入你猜的数字吧:>? 5
这个数大于5喔，请重新输入吧：
8
这个数小于8喔,，请重新输入吧：
6
这个数大于6喔，请重新输入吧：
7
游戏结束，不玩啦^_^
"""