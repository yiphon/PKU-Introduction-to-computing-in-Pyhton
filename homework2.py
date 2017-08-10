import math

# 1，写一个程序，它对 0 到 90 度之间（包括两端点）每隔 5 度的角度，在一行里输出角度值以及其正弦、余弦函数值。
num = []
sinnum = []
cosnum = []
for i in range(0, 19):
    num.append(i * 5 * pi / 180)
    sinnum.append(sin(num[i]))
    cosnum.append(cos(num[i]))
    print(sinnum[i], cosnum[i])
print('Degrees' + '\t' + 'sines' + '\t' + 'cosines')
for i in range(len(num)):
    print(num[i], sinnum[i], cosnum[i])


# 2，写一个程序，它用等差的一系列值比较 math 包的求平方根函数和课堂给出的求平方根程序，
# 在一行里输出一对两个函数值和它们之差的绝对值，并在最后输出误差的平均值。请以比较清晰的方式输出。
def sqrt(x):
    guess = 1.0
    while math.fabs((guess * guess - x)) > 1e-6:
        guess = (guess + x / guess) / 2
    return guess


sum = 0
min = float(input('Input the minimum number you want to compute. (min>0)'))
max = float(input('Input the maximum number you want to compute.'))
common_difference = float(input('Input the common difference you want in the array.'))
print('自变量值' + '\t' + '自定义函数值' + '\t' + '内置函数值' + '\t' + '差的绝对值')
number = min
count = 0
while number <= max:
    result1 = sqrt(number)
    result2 = math.sqrt(number)
    error = math.fabs(result1 - result2)
    sum += error
    print(number, '\t', result1, '\t', result2, '\t', error)
    number += common_difference
    count = count + 1
print('误差平均值：')
print(sum / count)

# 3，写程序计算连分式 1 + 1 / (1 + 1 / (...(1 + 1 / (1 + x))))，是有 n 层嵌套的连分式。其中的 n 和 x 由输入得到。


n = int(input('Input n:'))
x = float(input('Input x:'))
result = 1 + x
for i in range(n):
    result = 1 / result + 1
    print(i, result)

# 4，写一个二进制浮点数转换计算器程序，通过输入送给它任意一个包含（一个）小数点的二进制串，它求出相应的浮点数并输出。
# 该程序应反复读入二进制串并输出，直到人输入特殊的串 end。
# （注意，人输入三个字符 end 并按 Enter 键，input 函数返回的串相当于写 "end"，用 == 运算符可以判断两个字符串是否相等。）
str = input('Input the binary string:')
while not str == 'end':
    if str.find('.') == -1:
        num = 0
        for i in range(len(str)):
            num = num * 2 + int(str[i])
        print(num)
    elif str.find('.') == 0:
        num = 0
        for i in range(1, len(str)):
            num += 2 ** (-i) * int(str[i])
        print(num)
    else:
        num = 0
        for i in range(str.find('.')):
            num += 2 ** (str.find('.') - i - 1) * int(str[i])
        for i in range(str.find('.') + 1, len(str)):
            num += 2 ** (str.find('.') - i) * int(str[i])
        print(num)
    str = input('Input the binary string:')
