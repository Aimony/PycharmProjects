import time
import random
# 存储用户信息
user_info_dict = {'hades': '13579',
                  'nick': '123',
                  'ruixing': 'a1',
                  'fanping': 'b2'
                  }

# 注册
def register():
    print(f'\n{"注册".center(50,"-")}')
    # 输入用户名
    while True:
        user_name = input("请输入用户名>>>").strip()
        if user_name in user_info_dict:
            print('用户名已存在,请重新注册')
            continue
        # 输入密码
        while True:
            pwd = input('请输入你的密码>>>').strip()
            pwd_again = input('请再次输入你的密码>>>')
            # 判断密码是否一致
            if pwd != pwd_again:
                print("两次密码输入不一致,请重新输入")
                continue
            else:
                user_info_dict[user_name] = pwd
                print('正在注册', end='')
                for i in range(10):
                    print('>', end='')
                    time.sleep(0.5)
                print("\n注册成功")
                break
        break



# 登录
def login():
    print(f'\n{"登录游戏".center(50,"-")}')
    # 输入用户名
    user_name = input('请输入用户名>>>').strip()
    if user_name not in user_info_dict:
        print('用户名不存在,请注册')
    else:
        count = 0
        # 判断密码是否正确
        while count < 3:
            pwd = input('请输入你的密码>>>').strip()
            if pwd != user_info_dict.get(user_name):
                print('密码错误')
                count += 1
            else:
                print('正在登录', end='')
                for i in range(10):
                    print('>', end='')
                    time.sleep(0.5)
                print('\n登录成功,载入游戏', end='')
                for i in range(10):
                    print('>', end='')
                    time.sleep(1)
                game()
                break
            if count == 3:
                print('三次机会用完啦!!!')





# 发奖品
def award():
    # 定义奖品
    prize_dict = {0: '布娃娃',
                  1: '变形金刚',
                  2: '奥特曼',
                  3: '<Python从入门到放弃>'
                  }
    print(f'恭喜你猜对啦!你可以从如下奖品中选择两个奖品\n{prize_dict}\n')
    prize_choice = input(f'是否需要奖品,需要请按"Y"/"y",否则直接退出>>>')
    # 判断是否拿奖品
    if prize_choice == "Y" or prize_choice == "y":
        count = 0
        user_prize_dict = dict()
        # 用户选择奖品
        while count < 2:
            user_prize_choice = int(input('请输入奖品序号>>>').strip())
            # 判断奖品是否存在
            if user_prize_choice not in prize_dict:
                print('你输入的奖品不存在,请重新选择~')
                continue
            prize = prize_dict[int(user_prize_choice)]
            print(f"恭喜你获得了奖品--{prize}")
            # 将用户的获奖信息记录下来
            if user_prize_dict.get(prize):
                user_prize_dict[prize] += 1
            else:
                user_prize_dict[prize] = 1
            count += 1
        print(f"恭喜你获得了奖品{user_prize_dict}!!!")

# 进入游戏
def game():
    print(f'\n{"开始猜年龄游戏".center(50,"-")}\n')
    age = random.randint(0,80)  # 随机年龄
    count = 0  # 统计玩的次数
    while count < 3:
        inp_age = input('请输入你猜的年龄>>>').strip()  # 用户输入年龄
        # 判断输入的是否是数字
        if not inp_age.isdigit():
            print('傻缺,输入数字知道不!!!')
            continue
        inp_age_int = int(inp_age)
        # 核心逻辑
        if inp_age_int == age:
            award()
            break
        elif inp_age_int > age:
            print('猜大了')
        else:
            print('猜小了')
        count += 1
        # 判断用户是否继续游戏
        if count != 3:
            continue
        choice = input('菜鸡,三次机会用完喽~ \n是否还想玩,继续请按"y"/"Y",否则退出>>>').strip()
        if choice == "Y" or choice == "y":
            count = 0
    print(f'\n{"Game Over".center(50,"-")}\n')



# 开始游戏
def run():
    # print(f'{"开始游戏".center(50,"-")}\n')
    while True:
        function_dict = {'1': '注册',
                         '2': '登录',
                         '3': '结束'
                         }
        function_dict1 = {'注册': register,
                          '登录': login,
                          }
        choice = input(f'请选择功能{function_dict}>>>').strip()
        if choice == '3':
            break
        else:
            function_dict1[function_dict[choice]]()
if __name__ == '__main__':
    run()