x = input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要1or不需要2？')
if x == 1:
    y = int(print('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    if y == 2:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        z = input('请问您需要兑换多少金加隆呢？')
        print('好的，我知道了，您需要兑换（你说的数字{}n）金加隆。'.format(z))
        print('那么，您需要付给我（你说的数字N*51.3）人民币。')
else:
    print('好的，再见。')



