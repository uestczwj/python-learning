#下面第一行导入生成随机数的函数包，暂时不用深究
from random import randint
secret = randint (1,10)      #产生一个1~10之间的随机数
COUNT = 5
print("请输入你猜的数字，只有{}次机会喔！".format(COUNT))

for i in range(COUNT):
	guess = int(input())
	if (guess == secret):
		print("你真厉害，被你猜中啦，你是我心里的蛔虫吗？！")
		exit(0)
	else:
		print("不是{}喔!".format(guess))