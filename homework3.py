import math
from time import time


# 1，请定义一个函数 prime_factors(n)，它确定正整数 n 的所有素因子，并调用 print 逐个输出，重复的因子重复输出。
# 请在函数开始检查参数情况，只对满足要求的参数计算。
def prime_factors(n):
    if n > 0:
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, int(n / i))
    else:
        print('Input error.')


n = int(input('Input positive integar:'))
prime_factors(n)


# 2，请利用（修改/使用）课堂上讨论的有关 Collatz 猜想的函数，定义三个函数：
# 第一个函数返回（注意，不是输出）对正整数 n 做 Collatz 计算的过程中历经的最大值。
# 第二个函数检查 m 到 n 的所有正整数，输出其中造成 Collatz 函数迭代次数最多的数 k 以及它的迭代次数；
# 第三个函数检查从 m 到 n 的所有正整数，找出其中的 k，在对 k 的迭代中历经的最大整数值比其他数都大，输出 k 和对它的迭代中达到的最大数值。
def collatz(n):
    num = n
    count = 0
    while n != 1:
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = n * 3 + 1
        count += 1
    print("For integer " + str(num) + " iterating " +
          str(count) + " times.")


def max_in_process(n):
    num = n
    max = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if max <= n:
            max = n
    return max


def most_iterating_times(m, n):
    max_count = 0
    max_i = m
    for i in range(m, n + 1):
        num = i
        count = 0
        while i != 1:
            if i % 2 == 0:
                i = i // 2
            else:
                i = i * 3 + 1
            count += 1
        if max_count <= count:
            max_count = count
            max_i = num
    print('Number ' + str(max_i) + ' iterates ' + str(max_count) + ' times.')


def max_in_multiple_process(m, n):
    max_in_array = 0
    max = 0
    max_num = m
    for i in range(m, n + 1):
        max = max_in_process(i)
        if max_in_array <= max:
            max_in_array = max
            max_num = i
    print('Number ' + str(max_num) + ' has reached ' + str(max_in_array) + ' in the iterating process.')


max_in_multiple_process(2, 7)

# 3，用下面方法可以为一段计算计时：

# from time import time
# t = time()
# ... ... # 你的计算
# t = time() - t
# 这时变量 t 的值是两次调用 time() 之间经过的时间，以秒计。
# 请写程序计算调和级数的部分和，检查这个“和”在你机器上达到 10, 11，..., 16, 17, 18 时所用的时间，输出这些结果。你看到了什么情况？
# （请在你的程序文件里用注释的方式说明试验的情况）

t0 = time()
sum = 0
i = 1
while i > 0:
    sum_before = sum
    sum += 1 / i
    i = i + 1
    for j in range(10, 20):
        if sum_before <= j and sum > j:
            t = time()
            print(t - t0, sum)
    if sum > 19:
        break
