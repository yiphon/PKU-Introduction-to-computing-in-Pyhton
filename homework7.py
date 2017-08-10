import math

# 1，请用表描述式生成包含下面元素的表：

# 100 以内 7 的所有倍数的平方根。
# 一个半轴长 1，3，6，7，另一半轴长 14，8，9，11 的所有椭圆的面积。
# 类似上表，但只对两个半轴长度之和是偶数的求出面积。
# 对角线元素全为 0 其他元素全为 1 的 20*20 矩阵，用元素是 list 的 list 表示。例如 [[1, 2], [3, 4]] 是一个 2*2 矩阵。

a1 = [math.sqrt(i + 1) for i in range(100) if (i + 1) % 7 == 0]
a2 = [math.pi * a * b for a in [1, 3, 6, 7] for b in [14, 8, 9, 11]]
a3 = [math.pi * a * b for a in [1, 3, 6, 7] for b in [14, 8, 9, 11] if (a + b) % 2 == 0]
a4 = [[int(i + 1 != j) for i in range(20)] for j in range(1, 21)]
print(a4)


# 2，写一个函数 prime_factors(n)，它返回一个表，其中包含正整数 n 的所有素因子（重复的因子在表中重复出现）。
def prime_factors(n):
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
            a.append(int(n / i))
    return a


print(prime_factors(2345))


# 3，请定义函数 rem_duples(lst)，它基于 lst 构造并返回一个新表，其中按 lst 里原来的顺序包含了 lst 的所有元素值，但消除了重复出现。
# 例如，rem_duples([1, 4, 3, 2, 4, 2, 4, 4, 0]) 的结果应该是表 [1, 4, 3, 2, 0]。注意，要求不修改作为实际参数的表。

def rem_duples(lst):
    a = []
    a.append(lst[0])
    for i in range(len(lst)):
        for j in range(i):
            if lst[j] == lst[i]:
                break
            if j == i - 1:
                a.append(lst[i])
    return a


print(rem_duples([1, 3, 2, 4, 5, 2, 3, 5, 2, 6, 4, 7, 4]))


# 4，请开发一个程序包（一个 Python 文件），其中采用课堂上讨论的简单的一元多项式表示法（表示为系数的表），
# 包里除包含多项式的求值函数外，另请定义多项式求和，多项式求乘积，多项式求负，以及多项式输出函数。
# 你可以根据自己的喜好设计多项式的输出形式（假设其自变量是 x），还可以考虑定义其他函数。请在文件里包含几个利用你的函数做多项式计算的例子，在文件最前面用注释的形式说明完成了哪些工作。
def value(p, x):
    val = 0
    for i in range(len(p)):
        val += p[i] * x ** i
    return val


def product(p1, x1, p2, x2):
    val1 = value(p1, x1)
    val2 = value(p2, x2)
    return val1 * val2


def minus(p, x):
    return -value(p, x)


def output(p):
    print('The polynomial is:')
    for i in range(len(p) - 1, 0, -1):
        if i == len(p) - 1:
            if math.fabs(p[i]) <= 1e-6:
                continue
            elif p[i] == 1:
                print('x^', i, end='')
            elif p[i] == -1:
                print('-x^', i, end='')
            else:
                print(p[i], '*x^', i, end='')
        elif i == 1:
            if math.fabs(p[i]) <= 1e-6:
                continue
            elif p[i] == 1:
                print('+' + 'x', end='')
            elif p[i] == -1:
                print('-' + 'x', end='')
            elif p[i] > 0:
                print('+', p[i], '*x', end='')
            elif p[i] < 0:
                print('-', (-p[i]), '*x', end='')
        elif math.fabs(p[i]) <= 1e-6:
            continue
        elif p[i] == 1:
            print('+', 'x^', i, end='')
        elif p[i] == -1:
            print('-', 'x^', i, end='')
        elif p[i] > 0:
            print('+', p[i], '*x^', i, end='')
        elif p[i] < 0:
            print('-', (-p[i]), '*x^', i, end='')

    if math.fabs(p[0]) <= 1e-6:
        pass
    elif p[0] > 0:
        print('+', p[0])
    else:
        print(p[0])


output([0, 1121, 0, 1, -1, -1, 0, 1, 1, -1, 1])
