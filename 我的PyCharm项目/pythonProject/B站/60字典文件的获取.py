scores={'张三':100,'李四':98,'王五':45}
'''第一种，使用[]'''
print(scores['张三'])
# print(scores['陈六'])     #KeyError: '陈六'


'''第二种，使用get()'''
print(scores.get('张三'))
print(scores.get('陈六'))              #None
print(scores.get('老七',99))           #99是在查找‘老七’所对应的value不存在时提供的一个默认值
