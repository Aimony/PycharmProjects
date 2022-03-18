# import random
# operator = ["+", "-", "*", "/"]
# print(type(random.choice(operator)))
#
# print(type(1+2))



while True:
    a = [ '+','-','*','/' ]
    import random
    Fuhao = random.choice(a)
    if Fuhao == '/':
        Num1 = random.randint(0, 10)
        Num2 = random.randint(1, 10)
        print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
        Answer = input('请输入答案【有小数请保留小数点后三位】: ')
        Correct_Answer = float(Num1 / Num2)
    if Fuhao == '*':
        Num1 = random.randint(0, 10)
        Num2 = random.randint(0, 10)
        print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
        Answer = float(input('请输入答案: '))
        Correct_Answer = Num1 * Num2
    if Fuhao == '+':
        Num1 = random.randint(0, 10)
        Num2 = random.randint(0, 10)
        print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
        Answer = float(input('请输入答案: '))
        Correct_Answer = Num1 + Num2
    if Fuhao == '-':
        Num1 = random.randint(0, 10)
        Num2 = random.randint(0, 10)
        print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
        Answer = float(input('请输入答案: '))
        Correct_Answer = Num1 - Num2
    if Fuhao == '/':
        if Correct_Answer % 1 != 0:
            Correct_Answer = ('%.3f' %Correct_Answer)
    if Answer == Correct_Answer:
        print('正确！')
    else:
        print('错误！')

