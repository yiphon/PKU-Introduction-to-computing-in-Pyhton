# 1，基于你上次有关矩阵的工作定义一个矩阵类，其中定义一组适当的方法。用注释说明所定义的方法，并用几个例子表现该类的使用和效果。

import numpy as np
import datetime
import math


class Matrix:
    def __init__(self, fname):
        if not isinstance(fname, str):
            raise TypeError(fname)
        else:
            self._f = fname

    def fname(self):
        return self._f

    def _matrix_forming(self):
        f = open(self._f, 'r')
        matrix = f.readlines()
        matrix1 = []
        matrix2 = []
        for i in range(matrix.index('\n')):
            matrix1.append(matrix[i].strip().split())
        for i in range(matrix.index('\n') + 1, 2 * matrix.index('\n') + 1):
            matrix2.append(matrix[i].strip().split())
        return matrix1, matrix2

    @staticmethod
    def _det(a):
        n = len(a)
        det = 1
        for i in range(n):
            for j in range(n):
                a[i][j] = float(a[i][j])
        matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = float(a[i][j])
        print(np.linalg.det(matrix))
        for i in range(0, n - 1):  # i为作为减数的行序号
            max = a[i][i]
            index_max = i
            for j in range(i, n):
                if math.fabs(a[j][i]) > math.fabs(max):
                    max = a[j][i]
                    index_max = j
            a[i], a[index_max] = a[index_max], a[i]
            for j in range(i + 1, n):  # j为作为被减数的行序号
                factor = a[j][i] / a[i][i]
                for k in range(i, n):  # k对应每一行参与计算的列
                    a[j][k] = a[j][k] - factor * a[i][k]

        for i in range(n):
            det *= a[i][i]
        print(det)
        return det

    @staticmethod
    def _matrix_muiltiply(a, b):
        row_a = len(a)
        row_b = len(b)
        colomn_a = len(a[0])
        colomn_b = len(b[0])
        for i in range(row_a):
            for j in range(colomn_a):
                a[i][j] = float(a[i][j])
        for i in range(row_b):
            for j in range(colomn_b):
                b[i][j] = float(b[i][j])
        matrix = [[0 for i in range(row_a)] for j in range(colomn_b)]
        if colomn_a != row_b:
            return ''
        else:
            for i in range(row_a):
                for j in range(colomn_b):
                    for k in range(colomn_a):
                        matrix[i][j] += a[i][k] * b[k][j]
            for i in range(len(matrix)):
                print(matrix[i])
            matrix_a = np.zeros((row_a, colomn_a))
            for i in range(row_a):
                for j in range(colomn_a):
                    matrix_a[i][j] = float(a[i][j])
            matrix_b = np.zeros((row_b, colomn_b))
            for i in range(row_b):
                for j in range(colomn_b):
                    matrix_b[i][j] = float(b[i][j])
            matrix_a = np.mat(matrix_a)
            matrix_b = np.mat(matrix_b)
            print(np.dot(matrix_a, matrix_b))


a = Matrix('data2.txt')._matrix_forming()[0]
b = Matrix('data2.txt')._matrix_forming()[1]
Matrix('data.txt')._det(b)


# 2，请基于 Person 类定义几个为公司人员管理系统使用的类，包括一个一般雇员类 Employee，一个工人类 Worker 和一个管理人员类 Manager。
# 写一段代码调用这些类的功能建一个小公司的人员表，并用 print 函数输出一些说明公司情况的信息。

class Person:
    def __init__(self, name, sex, birthday):
        if not (isinstance(name, str) and
                        sex in ("女", "男") and
                    isinstance(birthday, tuple) and
                        len(birthday) == 3):
            raise ValueError(name, sex, birthday)
        birth = datetime.date(*birthday)  # 生成一个日期对象
        self._name = name
        self._sex = sex
        self._birthday = birth

    def set_name(self, name):  # 修改名字
        if not isinstance(name, str):
            raise ValueError
        self._name = name

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return (datetime.date.today().year -
                self._birthday.year)

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise TypeError(another, Person)
        return self._name < another._name

    def __str__(self):
        return " ".join((self._name, self._sex, str(self._birthday)))

    def print(self):
        print((self._name, self._sex, self._birthday))


class Employee(Person):
    def __init__(self, name, sex, birthday, salary, department='df'):
        Person.__init__(self, name, sex, birthday)
        if not (isinstance(salary, int) and isinstance(department, str)):
            raise TypeError
        self._salary = salary
        self._department = department

    def salary(self):
        return self._salary

    def department(self):
        return self._department

    def __str__(self):
        return ' '.join((self._name, self._sex, str(self._birthday), str(self._salary), self._department))

    def _set_salary(self, num):
        if not isinstance(num, int):
            raise TypeError
        else:
            self._salary = num

    def _set_department(self, string):
        if not isinstance(string, str):
            raise TypeError
        else:
            self._department = string

    def print(self):
        print((self._name, self._sex, self._birthday, self._salary, self._department))


class Worker(Employee):
    _id_num = 0

    @classmethod
    def _id_generation(cls, birthday):
        Worker._id_num += 1
        year = datetime.date(*birthday).year
        return '1{0:04}{1:05}'.format(year, Worker._id_num)

    def __init__(self, name, sex, birthday, salary, department):
        Employee.__init__(self, name, sex, birthday, salary, department)
        self._id = Worker._id_generation(birthday)

    def print(self):
        print(self._name, self._sex, self._birthday, str(self._salary), self._department, self._id)

    def __str__(self):
        return ' '.join(
            (self._name, self._sex, str(self._birthday), str(self._salary), self._department, str(self._id)))


class Manager(Employee):
    _id_num = 0

    @classmethod
    def _id_generation(cls, birthday):
        Manager._id_num += 1
        year = datetime.date(*birthday).year
        return '2{0:04}{1:05}'.format(year, Manager._id_num)

    def __init__(self, name, sex, birthday, salary, department):
        Employee.__init__(self, name, sex, birthday, salary, department)
        self._id = Manager._id_generation(birthday)

    def print(self):
        print(self._name, self._sex, self._birthday, self._salary, self._department, self._id)

    def __str__(self):
        return ' '.join(
            (self._name, self._sex, str(self._birthday), str(self._salary), self._department, str(self._id)))


if __name__ == '__main__':
    def test():
        global plist
        print('name\tsex\tdate\tsalary\tdepartment')
        p1 = Manager('曾博', '男', (2012, 12, 20), 150000, 'physics')
        p2 = Manager('徐国曦', '男', (2012, 12, 20), 150000, 'chemistry')
        p3 = Manager('白如冰', '男', (2012, 12, 20), 150000, 'mathematics')
        p4 = Manager('江汉臣', '男', (2012, 12, 20), 150000, 'management')
        p5 = Worker('马可', '男', (2012, 12, 20), 1500, 'mechanics')
        plist = [p1.print(), p2.print(), p3.print(), p4.print(), p5.print()]
        print('Later...')
        p1._set_department('CS')
        p2._set_department('CS')
        p3._set_department('CS')
        p4._set_department('CS')
        p5._set_department('CS')
        p5._set_salary(1500000)
        plist = [p1.print(), p2.print(), p3.print(), p4.print(), p5.print()]


    test()
