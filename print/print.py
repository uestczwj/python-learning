#用一个逗号结尾就可以禁止输出换行:
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

