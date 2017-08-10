import math
from time import time


# 1，哥德巴赫猜想说任一大于等于 6 的偶数可以分解为两个奇素数之和。请利用课堂给出的素数判断函数定义一个函数，它对 6 到 n 的偶数输出其素数分解。请设法保证每个偶数只输出一种分解。
# 请尝试不用素数判断函数，直接写出这个函数的定义。并用注释的形式简单比较这两个函数。

def is_prime(n):
    a = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i != 0:
            a = a * True
        else:
            a = a * False
    return a


n = int(input('Input the maximum number you\'d solve:'))

for i in range(6, n + 1, 2):
    for j in range(3, i - 2, 2):
        a = True
        b = True
        for k in range(2, int(math.sqrt(j)) + 1):
            if j % k != 0:
                a = a * True
            else:
                a = a * False
        for k in range(2, int(math.sqrt(i - j)) + 1):
            if (i - j) % k != 0:
                b = b * True
            else:
                b = b * False
        if a and b:
            print(i, '\t', j, '\t', i - j)
            break


# 2，如果一个正整数 m 的所有因子（包括 1，但不包括 m 自身）之和 s 等于 m，则称 m 为完全数；如果 s < m 称 m 为亏数；如果 s > m 称 m 为盈数。
# 请定义一个函数，在参数 m 为亏数、完全数或盈数时分别返回 -1, 0, 1。
# 基于这个函数定义另一函数，它检查 a 到 b 范围里的整数，统计其中亏数、完全数和盈数的个数并输出。最后调用你定义的函数统计几个范围里的整数的情况。

def judge(n):
    a = 0
    for i in range(1, n):
        if n % i == 0:
            a += i
    if a > n:
        return 1
    elif a == n:
        return 0
    else:
        return -1


def data(a, b):
    neg = pos = ab = 0
    for i in range(a, b + 1):
        if judge(i) == 1:
            pos += 1
        elif judge(i) == 0:
            ab += 1
        else:
            neg += 1
    print('亏数：', '\t', neg)
    print('完全数', '\t', ab)
    print('盈数：', '\t', pos)


data(23, 10000)


# 3，函数 f(n) 由如下规则定义：当 n 小于 3 时，f(n) = n；对于更大的 n，f(n) = f(n-1) + 2 * f(n-2) + 3 * f(n-3)。
# 请采用递归的方式直接定义一个计算 f 的函数，再按照递推的方式用循环结构定义一个计算 f 的函数。

def f1(n):
    if n < 3:
        return n
    else:
        return f1(n - 1) + 2 * f1(n - 2) + 3 * f1(n - 3)


def f2(n):
    if n < 3:
        return n
    else:
        a = 0
        b = 1
        c = 2
        for i in range(3, n + 1):
            f = c + 2 * b + 3 * a
            c, b, a = f, c, b
        return f


n = int(input('Input positive integer n:'))
t1 = time()
f1(n)
print(time() - t1, f1(n))
t2 = time()
f2(n)
print(time() - t2, f2(n))


# 4，假设需要从很长的钢条上剪裁出长度为 5 厘米、8 厘米、17 厘米和 28 厘米的短条。
# 请写一个函数，它计算出从长度为 n 厘米的钢条上裁出这些短条的不同方式的数目，要求浪费的钢条长度不超过 3 厘米。
# （注意：裁短钢条的不同方式与顺序无关。请考虑如下递归看法：从长 n 钢条上剪裁的不同方式等于...）。
# 在上交的程序里用注释形式论述你的做法的正确性。请在你的函数定义之后调用你的函数求出对 100，160 和 240 长的钢条的计算结果，以清晰明了的形式产生输出。

def computing(n):
    for i in range(n - 3, n + 1):
        for a in range(1, i // 28 + 1):
            for b in range(1, i // 17 + 1):
                for c in range(1, i // 8 + 1):
                    for d in range(1, i // 5 + 1):
                        if a * 28 + b * 17 + c * 8 + d * 5 == i:
                            print(a, b, c, d, i)


computing(240)
