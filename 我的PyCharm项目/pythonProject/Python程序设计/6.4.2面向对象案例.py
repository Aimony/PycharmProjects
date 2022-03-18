# class Car:
#     price = 100000
#     def __init__(self,c):
#         self.color = c
#
# car1 = Car('Red')
# car2 = Car('Blue')
# print(car1.color,Car.price)
# Car.price = 666666
# Car.__name__ = 'QQ'
# car1.color = 'Yellow'
# print(car2.color,Car.price,Car.__name__)
#
#
# import types
# def setspeed(self,s):
#     self.speed = s

class MyArray:
    '''All the element in this array must be numbers'''

    def __IsNumber__(self,n):
        return isinstance(n,(int,float,complex))

    def __init__(self,*args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber__(arg):
                    raise Exception('All element must be numbers')
            self.__value = list(args)

    #重载运算符+
    def __add__(self,n):
        if self.__IsNumber__(n):
            b = MyArray()
            b.__value = [item + n for item in self.__value]
            return b
        elif isinstance(n,MyArray):
            if len(n.__value) == len(self.__value):
                c = MyArray()
                c.__value = list(map(lambda x,y: x+y,self.__value,n.__value))
                return c
            else:
                print('Length not equal')
        else:
            print('Not supposed')

    #重载运算符—
    def __sub__(self,n):
        if not self.__IsNumber__(n):
            raise Exception('not supposed.')
        b = MyArray()
        b.__value = [item-n for item in self.__value]
        return b

    #重载运算符*
    def __mul__(self, n):
        if not self.__IsNumber__(n):
            raise Exception('not supposed')
        b = MyArray()
        b.__value = [item*n for item in self.__value]
        return b

    #重载运算符/
    def __truediv__(self, n):
        if not self.__IsNumber__(n):
            raise Exception('not supposedf')
        b = MyArray()
        b.__value = [item/n for item in self.__value]
        return b

    #重载运算符//
    def __floordiv__(self, n):
        if not self.__IsNumber__(n):
            raise Exception(n,'is not an integer')
        b = MyArray()
        b.__value = [item//n for item in self.__value]
        return b

    #重载运算符%
    def __mod__(self, n):
        if not self.__IsNumber__(n):
            raise Exception('not supposed')
        b = MyArray()
        b.__value = [item%n for item in self.__value]
        return b

    #重载运算符**
    def __pow__(self, n):
        if not self.__IsNumber__(n):
            raise Exception('not supposed')
        b = MyArray()
        b.__value = [item**n for item in self.__value]
        return b

    def __len__(self):
        return len(self.__value)

    def __repr__(self):
        return repr(self.__value)

    def __str__(self):
        return str(self.__value)


    def append(self,v):
        assert self.__IsNumber__(v),'Only number can be appended'
        self.__value.append(v)

    def __getitem__(self, index):
        length = len(self.__value)

        if isinstance(index,int) and 0 <= index <length:
            return self.__value[index]

        elif isinstance(index,(list,tuple)):
            for i in index:
                if not (isinstance(i,int) and (0 <= i <length)):
                    return 'index error'
            result = []
            for item in index:
                result.append(self.__value[item])
            return result
        else:
            return 'index error'

    def __setitem__(self, index, value):
        length = len(self.__value)
        if isinstance(index,int) and (0 <= index <length):
            self.__value[index] = value
        elif isinstance(index,(list,tuple)):
            for i in index:
                if not (isinstance(i,int) and (0 <= i <length)):
                    raise Exception('index error')
            if isinstance(value,(list,tuple)):
                if len(index) == len(value):
                    for i,v in zip(index,value):
                        self.__value[i] = v
                else:
                    raise Exception('values and index must be the same length')
            elif isinstance(value,(int,float,complex)):
                for i in index:
                    self.__value[i] = value
            else:
                raise Exception('value error')
        else:
            raise Exception('index error')

    def __contains__(self, v):
        return v in self.__value

    def dot(self,v):
        if not isinstance(v,MyArray):
            raise Exception(v,'must be an instance of Myarray.')
        if len(v) != len(self.__value):
            raise Exception('The size must be equal.')
        return sum([i * j for i,j in zip(self.__value,v.__value)])

    def __eq__(self, v):
        assert isinstance(v,MyArray),'wrong type'
        return self.__value == v.__value

    def __It__(self,v):
        assert isinstance(v,MyArray),'wrong type'
        return self.__value < v.__value



if __name__ == '__main__':
    print('Please use me as a module')