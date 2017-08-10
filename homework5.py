# ，利用课堂给的代码，比较采用二分法求立方根和采用立方根逼近公式两种计算的操作效率。定义函数对给定范围中等差的值检查它们的迭代次数，并生成出比较结果的表格。

from math import fabs


def cbrt1(x):
    ite = 0
    y = fabs(x)
    a, b = 0.0, y
    m = (a + b) / 2
    while fabs(m ** 3 - y) > 0.001:
        if m ** 3 > y:
            b = m
        else:
            a = m
        m = (b + a) / 2
        ite += 1
    return -m if x < 0.0 else m, ite


def cbrt2(x):
    ite = 0
    if x == 0.0:
        return 0.0
    x1 = x
    x2 = (2.0 * x1 + x / x1 / x1) / 3
    while fabs((x2 - x1) / x1) >= 1E-6:
        x1 = x2
        x2 = (2.0 * x1 + x / x1 / x1) / 3
        ite += 1
    return x2, ite


a = float(input('The minimum number to be solved:'))
b = float(input('The maximum number to be solved:'))
sep = float(input('Step-size:'))
print('Number', '\t', 'Function_1(result and iterating times)', '\t\t', 'Function_2(result and iterating times)\t')
count = a
while a <= count <= b + sep:
    print('{0:.8}'.format(count), end=' ')
    print('\t', cbrt1(count), '\t\t\t', cbrt2(count))
    count += sep
# 2，修改递归的 fib 函数，使之能借助一个全局变量（或非局部变量）统计出在计算 fib(n) 的过程中函数调用的总次数。
# 请写另一个函数，它用一些正整数值调用修改后的 fib，输出相应的斐波那契项的值和相应的函数递归调用次数。你看到了什么情况，请在程序文件里用注释说明？
count = 0


def fib(n):
    global count
    if n < 1:
        count += 1
        return 0
    if n == 1:
        return 1
        count += 1
    else:
        return fib(n - 1) + fib(n - 2)
        count += 1


def output(n):
    print(n, fib(n), count)


for i in range(30):
    output(i)


# 3，写函数 draw_4square(m, n)，它输出用字符 "-", "|", "+" 拼出的“田”字，四个小方块的长度和宽度分别为 m 和 n 个字符或行数。例如，drawTian(4, 2) 输出下面的“田”字：

# +----+----+
# |    |    |
# |    |    |
# +----+----+
# |    |    |
# |    |    |
# +----+----+
# 基于你完成上面函数的认识定义另一个函数 draw_board(m, n)，它能生成用同样三个字符拼出的 m * n 个格子的棋盘（例如 8*8 个格子的国际象棋棋盘）。
# 请注意在工作中定义有用的辅助函数。注意，为了保证空格和各种字符宽度相同，以便输出字符对齐，应该把 Python Shell 的窗口设置为采用某种等宽字体输出
# （在 Options 菜单里的 configure IDLE下设置字体，例如用 consolas。苹果机在 File 菜单的 preferences 菜单项下）。

def draw_4square(m, n):
    for i in range(2):
        print('+' + m * '-' + '+' + m * '-' + '+')
        for i in range(n):
            print('|' + m * ' ' + '|' + m * ' ' + '|')
    print('+' + m * '-' + '+' + m * '-' + '+')


draw_4square(2, 3)


def draw_board(m, n):
    for i in range(8):
        for j in range(8):
            print('+' + m * '-', end='')
        print('+')
        for j in range(n):
            for k in range(8):
                print('|' + m * ' ', end='')
            print('|')
    for i in range(8):
        print('+' + m * '-', end='')
    print('+')


draw_board(23, 33)
