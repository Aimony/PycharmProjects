def ori2com(ori_str: str):
    """
    将原码字符串 -> 补码字符串
    :param ori_str:原码字符串
    :return:补码字符串
    """
    # 如果符号位为正，则原码与补码相同
    if ori_str[0] == '0':
        return ori_str
    elif ori_str[0] == '1':
        value_str = ""

        # 数值位按位取反
        for i in range(len(ori_str)):
            if i == '1':
                continue
            if ori_str[i] == '0':
                value_str += '1'
            elif ori_str[i] == '1':
                value_str += '0'

        # 数值位加 1
        n = int(value_str, 2) + 1
        com_str = bin(n)[2:]
        if len(com_str) >= len(ori_str):
            # 说明进位到符号位了
            com_str = '0' + com_str[1:]
        else:
            # 0不够，中间填充0
            n = len(ori_str) - len(com_str) - 1
            for i in range(n):
                com_str = '0' + com_str
            com_str = '1' + com_str

        return com_str


def com2ori(com_str: str):
    """
    将补码字符串 -> 原码字符串
    :param com_str: 补码字符串
    :return: 原码字符串
    """
    # 补码再求一次补码，就得到原码
    return ori2com(com_str)


# def ori2dec(bin_str: str):
#     """
#     将原码字符串 -> 十进制数值
#     :param bin_str:原码字符串
#     :return:十进制数值
#     """
#     # 如果为正数
#     if bin_str[0] == '0':
#         return int(bin_str, 2)
#     elif bin_str[0] == '1':
#         return -int(bin_str[1:], 2)

#
# def com2dec(com_str: str):
#     """
#     将补码字符串 -> 十进制数值
#     :param com_str:补码字符串
#     :return:十进制数值
#     """
#     ori_str = com2ori(com_str)
#     return ori2dec(ori_str)


if __name__ == '__main__':
    while True:
        ori_str = input('请输入二进制原码')
    # print("二进制原码：" + ori_str)
        print('补码：' + ori2com(ori_str))
    # print('十进制：', ori2dec(ori_str))
    #
    # print()
    #
    # com_str = '100100100'
    # print("二进制补码：" + com_str)
    # print('原码：' + com2ori(com_str))
    # print('十进制：', com2dec(com_str))