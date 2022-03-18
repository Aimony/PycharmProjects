import random
secretNum = random.randint(1,100)
print("---------------猜年龄（1-100岁之间）------------------------")
print('你只能猜5次哦')
for number in range(1,6):
    print("请输入你猜的年龄：")
    guess = int(input())
    if guess == 0:
        break
    if guess < secretNum:
        print("太小啦")
    elif guess > secretNum:
        print("太大啦")
    else:
        break
if(guess == secretNum):
    print("真厉害，猜对啦，就是",str(guess))
else:
    print("很遗憾，正确的答案应该是",str(secretNum))