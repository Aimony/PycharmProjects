try:
    x = input('被除数')
    y = input('除数')
    z = float(x) / float(y)
except ZeroDivisionError:
    print('123')
except TypeError:
    print('456')
except NameError:
    print('789')
else:
    print(x, '/',y,'=',z)

