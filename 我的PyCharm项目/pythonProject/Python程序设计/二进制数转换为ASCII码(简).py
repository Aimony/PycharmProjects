def ori2com(ori_str: str):

    if ori_str[0] == '0':
        return ori_str
    elif ori_str[0] == '1':
        value_str = ""

        for i in range(len(ori_str)):
            if i == '1':
                continue
            if ori_str[i] == '0':
                value_str += '1'
            elif ori_str[i] == '1':
                value_str += '0'

        n = int(value_str, 2) + 1
        com_str = bin(n)[2:]
        if len(com_str) >= len(ori_str):
            com_str = '0' + com_str[1:]
        else:
            n = len(ori_str) - len(com_str) - 1
            for i in range(n):
                com_str = '0' + com_str
            com_str = '1' + com_str
        return com_str
def com2ori(com_str: str):

    return ori2com(com_str)

if __name__ == '__main__':
    while True:
        ori_str = input('请输入二进制原码')
        print('补码：' + ori2com(ori_str))
