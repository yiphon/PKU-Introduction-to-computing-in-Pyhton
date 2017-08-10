import random
import math


# 1，请设法找到辛普森（数值）积分公式，并定义一个基于辛普森公式做数值积分的函数，
# 其中采用课堂提出的逐步加细划分的方法，通过多次求数值积分逼近函数的实际积分值。
# 请写出几个用你的函数完成积分的实例。

def simpson(f, a, b, div):
    sum = 0
    d = (b - a) / div
    for i in range(div):
        t = a + i * d
        sum += 1 / 6 * f(t) + 2 / 3 * f(t + 0.5 * d) + 1 / 6 * f(t + d)
    return sum * d


def integrate(f, a, b, div):
    if a > b:
        a, b = b, a
    i = 0
    sum_1 = 0
    sum_2 = 1
    while math.fabs(sum_1 - sum_2) > 1e-6:
        sum_1 = simpson(f, a, b, div)
        sum_2 = simpson(f, a, b, 2 * div)
        print(sum_1, sum_2)
        div *= 2
    return sum_2


integrate(lambda x: math.sin(x), 0, math.pi / 2, 10)


# 2，蒙特卡罗积分是利用随机试验求函数的数值积分的方法。请考虑定义一个蒙特卡罗积分函数 mt_int，通过生成平面上区域 [x1,x2] * [y1,y2] 里的随机点数据，
# 检查其位于被积函数 f 的值之下的比率，得到函数积分的近似值。

def test(f, x1, x2, y1, y2):
    passed = 0
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    x_ran = random.uniform(x1, x2)
    y_ran = random.uniform(y1, y2)
    if (0 <= y_ran <= f(x_ran)):
        passed += 1
    if (0 >= y_ran >= f(x_ran)):
        passed -= 1
    return passed


def mt_int(f, x1, x2, y1, y2, num):
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    spot = 0
    for i in range(num):
        spot += test(f, x1, x2, y1, y2)
    return spot / num * (x2 - x1) * (y2 - y1)


print(mt_int(lambda x: math.cos(x), 0, math.pi, -3, 3, 1000000))


# 3，赌场有一种游戏称为“幸运七”，说你丢两个骰子，如果它们点数之和为 7 你就赢 4 元，如果不是 7 你输 1 元。
# 请定义一个函数模拟这种游戏，看看赌场的规则是否“公平”。另外，请定义一个函数 lucky7(a, b)，其中 a 表示你的初始赌资，b 是你准备见好就收的款额。
# 函数模拟“幸运七”游戏，直至你的赌资输光或者你手头的钱超过 b。函数结束之前打印出过程中的投骰子次数，曾经达到的最高和最低款额。
def test():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a + b == 7


def mt_lucky7(num):
    m = 0
    for i in range(num):
        if test():
            m += 4
        else:
            m -= 1
    return m


def lucky7(a, b):  # 0<a<b
    money = a
    count = 0
    max = min = a
    while not (math.fabs(money) <= 1e-3 or money - b >= 1e-3):
        if test():
            money += 4
            count += 1
        else:
            money -= 1
            count += 1
        if money >= max:
            max = money
        if money <= min:
            min = money
    print(count, min, max)


lucky7(50, 100)
