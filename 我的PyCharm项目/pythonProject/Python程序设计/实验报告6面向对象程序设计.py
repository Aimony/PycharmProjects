# import time
# class Clock_Time(object):
#     # 构造方法
#     def __init__(self, hour, min, second):
#         self.hour = hour
#         self.min = min
#         self.second = second
#     # 定义类方法
#     def go_time(self):
#         # 时间是秒先走 秒走到60分钟+1，分钟走到60 时钟+1
#         # 因此先让秒自加1
#         self.second += 1
#         # 当秒为60时
#         if self.second == 60:
#             # 分钟自加1
#             self.min += 1
#             # 把秒钟重置为0
#             self.second = 0
#         # 当分钟为60时
#         if self.min == 60:
#             # 时钟自加1
#             self.hour += 1
#             # 把分钟重置为0
#             self.min = 0
#         # 当时钟为24时
#         if self.hour == 24:
#             # 把时钟重置为0时
#             self.hour = 0
#
#     def display_time(self):
#         # 引入str.zfill()方法
#         hour_str = str(self.hour)
#         min_str = str(self.min)
#         second_str = str(self.second)
#         print('{}:{}:{}'.format(hour_str.zfill(2), min_str.zfill(2), second_str.zfill(2)))
#         # print('{}:{}:{}'.format(self.hour, self.min, self.second))
#
# if __name__ == "__main__":
#     # 实例化对象
#     clock = Clock_Time(23,59,58)
#     while True:
#         clock.display_time()
#         time.sleep(1)
#         clock.go_time()


# import time
# class Clock:
#     hour = 0
#     min = 0
#     sec = 0
#     def getNow(self):
#         print('当前时间')
#
# c1 = Clock()
# print(c1.hour,c1.min,c1.sec)


# from math import sqrt
#
#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         """
#         构造器
#         :param x:横坐标
#         :param y:纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """
#         移动到指定的位置
#         :param x:
#         :param y:
#         :return:
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """
#         移动指定的增量
#         :param dx:横坐标的增量
#         :param dy:纵坐标的增量
#         :return:
#         """
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """
#         计算与另外一个点的距离
#         :param other:另外一个点
#         :return:
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     # 对这个对象的描写
#     def __str__(self):
#         return '(%s,%s)' % (str(self.x), str(self.y))
#
#
# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     print(p1.distance_to(p2))
#     p1.move_to(1, 2)
#     print(p1)
#     p2.move_by(-1, -2)
#     print(p2)
#
#
# if __name__ == '__main__':
#     main()



from math import sqrt
from time import sleep, time, localtime
from abc import ABCMeta, abstractmethod

"""
# 定义一个类描述数字时钟
使用@property装饰器和property方法实现属性"""


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):  # 初始化方法
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):  # 走字
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):  # 显示
        print("{}:{}:{}".format(self.hour, self.minute, self.second))
        return '%02d:%02d:%02d' % \
               (self.hour, self.minute, self.second)


"""定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法"""

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def move(self, dx, dy):
        self.x += dx;
        self.y += dy;

    def distance_to(self, Point):
        dx = self.x - Point.x
        dy = self.y - Point.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


"""定义一个学生类，并通过继承定义一个研究生类，查看多态性展示效果"""

class Student(object):
    def __init__(self, Sname, Sno, Sage):
        self.Sno = Sno
        self.Sname = Sname
        self.Sage = Sage

    @property
    def Sno(self):
        return self._Sno

    @Sno.setter
    def Sno(self, sno):
        self._Sno = sno

    @property
    def Sname(self):
        return self._Sname

    @Sname.setter
    def Sname(self, sname):
        self._Sname = sname

    @property
    def Sage(self):
        return self._Sage

    @Sage.setter
    def Sage(self, sage):
        self._Sage = sage

    def __str__(self):
        return '我叫%s,学号是%s,年龄为%s,是一名学生' % (str(self.Sname), str(self.Sno), str(self.Sage))

    def run(self):
        return '我叫%s,学号是%s,年龄为%s,是一名学生' % (str(self.Sname), str(self.Sno), str(self.Sage))

class Gra_student(Student):
    def __init__(self, Sno, Sname, Sage, Skey):
        super().__init__(Sno, Sname, Sage)
        self.Skey = Skey

    def __str__(self):
        return '我叫%s,学号是%s,年龄为%s,是一名研究生' % (str(self.Sname), str(self.Sno), str(self.Sage))


"""静态方法和类方法：定义一个“三角形”类"""


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self.b) * (half - self._c))


"""
使用抽象类完成一下任务：

某公司有三种类型的员工 分别是部门经理、程序员和销售员
"""


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法
        :param name:
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        :return:月薪
        """
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = value if value > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def TestSalary():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))

def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print('无法构成三角形')


def main1():
    clock = Clock.now()
    while True:
        clock.show()
        # print(clock.show())
        sleep(1)
        clock.run()


def main2():
    P1 = Point()
    P2 = Point()
    P1.x = 0
    P1.y = 0
    print(P1.x, P1.y)
    P2.move(-1, -1)
    print(P2)
    print(P1)
    P3 = P1.distance_to(P2)
    print(P3)


def main3():
    s1 = Student('小明', 1001, 13)
    print(s1)
    s2 = Gra_student('小刚', 1002, 21, 'c009')
    print(s2)
