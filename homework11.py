# 1，写一个程序（其中定义适当函数）统计你本学期至今总共写了多少行 Python 代码，包含多少注释行，多少空白行。写了多少非注释的非空白字符，及使用各 Python 关键字的使用情况。
# 程序最后输出非注释且非空白的 Python 程序行数，非注释的非空白字符数，以及程序里使用各 Python 关键字的次数（请注意哪些关键字还没用过）。
# 注意：标准库包 os 里有一个函数 listdir，调用它能返回一个目录（默认为 “当前目录”）下所有文件名的表，这是一个字符串的表。
# 利用它就不需要自己写具体文件名了（如需要请查 Python 文档等）；另外 s.endswith(".py") 检查串 s 是否以 ".py" 结尾。
# 把你的 .py 文件和这个程序放在同一目录下，程序运行时这些都在“当前目录”下，工作比较方便。请先检查原有的程序代码，尽量使统计结果准确。
# 统计结果用注释形式包含在上交的程序文件里。如果程序里有中文应注意文件打开方式。
# 再用你的程序处理一下 IDLE 的所有源文件，做同样统计。这些源文件在 Python 系统目录的 Lib 子目录下，自己设法找一找。
# 用标准库库 os 里的函数 chdir(path) 可以把当前目录转到用“path”指定的目录下，然后事情就很简单了。
# 注意，在用字符串描述 Windows 的文件目录路径时，作为路径分隔符的反斜线字符需要双写，因为反斜线符是 Python 字符串里的特殊字符，
# 要在字符串里写它就必须双写。例如 c:\python34\Lib 可以写 "c:/python34/Lib"。

import os
import keyword
import math


def count_file(fname):
    global keyword_dict
    code_line = 0  # 代码行数
    note_line = 0  # 注释行数
    blank_line = 0  # 空白行数
    str_number = 0  # 非注释非空白字符数
    flag = 0
    try:
        file = open(fname, 'r', encoding='utf-8')
        linelist = file.readlines()
    except OSError:
        print('Cannot open', fname)
        raise
    tri_note_list = []

    for i in range(len(linelist)):
        linelist[i] = linelist[i].strip()
        if linelist[i].find('"""') != -1:
            tri_note_list.append(i)
    for i in range(len(linelist)):
        for j in range(int(len(tri_note_list) / 2)):
            if tri_note_list[2 * j] <= i <= tri_note_list[2 * j + 1]:
                flag = 1
        if flag:
            code_line += 1
        elif linelist[i] == '':
            blank_line += 1
        elif linelist[i][0] == '#':
            note_line += 1
        else:
            code_line += 1
            for j in range(len(keyword.kwlist)):
                if linelist[i].find(keyword.kwlist[j]) != -1:
                    keyword_dict[keyword.kwlist[j]] += 1
            for j in range(len(linelist[i])):
                if (not linelist[i][j].isspace()) and linelist[i][j] != '#':
                    str_number += 1
                if linelist[i][j] == '#':
                    break
        flag = 0
    return code_line, note_line, blank_line, str_number


code_line = 0
note_line = 0
blank_line = 0
str_number = 0
keyword_dict = {}
for j in range(len(keyword.kwlist)):
    keyword_dict[keyword.kwlist[j]] = 0

a = []
for item in os.listdir("D://python36//Lib"):
    if item.endswith('.py'):
        a.append("D://python36//Lib//" + item)

for i in range(len(a)):
    code_line += count_file(a[i])[0]
    note_line += count_file(a[i])[1]
    blank_line += count_file(a[i])[2]
    str_number += count_file(a[i])[3]

print(
    'You have written {} code lines, {} note lines, {} blank lines, {} characters in code.'.format(code_line, note_line,
                                                                                                   blank_line,
                                                                                                   str_number))
print(keyword_dict)

# 2，请为浮点数矩阵设计一种对象表示的形式，针对这种形式定义两个函数，一个求矩阵的行列式值，另一个求两个矩阵的乘积。
# 设有正文文件里保存着两个浮点数矩阵的数据，文件里的一行对应矩阵一行（一串浮点数，两个浮点数之间用空格分隔），
# 两个矩阵之间用一个空行分隔（如 示例文件 data2.dat）。请写一段程序，它从指定文件读入两个矩阵，求出它们各自的行列式值，并求出两个矩阵的乘积。
# 还请另定义一个检查矩阵表示的正确性的函数。在提交的作业文件里，请用注释说明你采用的矩阵表示形式（例如是一个表，或者其他复合对象等）。
# 注意，直接按矩阵行列式求值的基本数学定义，会得到一种非常慢的算法（请估算一下，在计算一个10*10矩阵的行列式时，将构造出多少个9*9行列式，多少个8*8行列式等等），
# 一种合理算法是采用高斯消元法（请顺便估算一下计算10*10矩阵的行列式，需要做多少次加减和乘除）。

import numpy as np


def matrix_forming(fname):
    f = open(fname, 'r')
    matrix = f.readlines()
    matrix1 = []
    matrix2 = []
    for i in range(matrix.index('\n')):
        matrix1.append(matrix[i].strip().split())
    for i in range(matrix.index('\n') + 1, 2 * matrix.index('\n') + 1):
        matrix2.append(matrix[i].strip().split())
    return matrix1, matrix2


def det(a):
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

                # print(a)
    for i in range(n):
        det *= a[i][i]
    return det


def matrix_muiltiply(a, b):
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


matrix_muiltiply(matrix_forming('data2.txt')[0], matrix_forming('data2.txt')[1])
