# 1，定义函数 squeeze(list1, list2)，两个参数都是整数的表。squeeze 从 list1 里删除所有比表 list2 里的某个整数大 1 的数。
# 注意，这个函数不适合采用简单的 for 循环实现（因为删除元素导致被处理表的长度和内容都变了）。如果你想试试，请用一些例子试验，注意观察计算中出现的情况。

def squeeze(a, b):
    c = [0 for i in range(len(a))]
    d = [0 for i in range(len(b))]
    e = []
    for i in range(len(a)):
        c[i] = a[i]
    for i in range(len(b)):
        d[i] = b[i]
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] + 1 == a[i]:
                c[i] = ''
    for i in range(len(c)):
        if c[i] != '':
            e.append(c[i])
    return e


a = [1, 2, 3, 4, 3, 3, 4, 5, 55]
b = [5, 4, 5, 32, 4, 56, 32, 54]
print(squeeze(a, b))


# 2，写一个函数计算并输出直至第 n 行的杨辉三角形。（这里特别的不要求输出形式，但杨辉三角形的一行应输出在一行，整数之间用空格分隔。）

def fact(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * fact(n - 1)


def YangHui(n):  # 第n行，对应下标为（n-1）
    for i in range(0, n):
        for j in range(0, i + 1):
            print(int(fact(i) / (fact(i - j) * fact(j))), end=' ')
        print('\n')


YangHui(30)


# 3，定义函数 disjoins(lst)，其参数是一个表。这种表的元素都是形如 [a, b] 的包含两个整数的表，表示数轴上的一个闭区间。
# disjoins 返回一个表，其中包含从 lst 中选出的一组（最大的）不相交区间（也就是说，如果你选了一个或几个区间，它们应互不相交，
# 而且没选的区间里不存在与它们都不相交的区间。本题目不要求考虑区间的总长度最大等其他问题，可以作为自我练习）。

def disjoins(lst):
    set_lst = []
    set_all = set()
    get_range = []
    for i in range(len(lst)):
        set_lst.append({i for i in range(lst[i][0], lst[i][1])})
    for i in range(len(set_lst)):
        set_all = set_all.union(set_lst[i])
    for i in range(len(set_lst)):
        for item in set_lst[i]:
            for j in range(i + 1, len(set_lst)):
                if item in set_lst[j]:
                    set_all.discard(item)
    for item in set_all:
        get_range.append([item, item + 1])
    return get_range


print(disjoins([[2, 3], [2, 5], [3, 6], [1, 7], [4, 9]]))


# 4，考虑模拟一个金属杆上的热传导过程。杆的左端有一个100度的稳定热源，右端有一个70度的稳定热源。
# 将杆分为10段，除两个端点外，其余分段点的初 始温度都是0度。通过一轮轮计算模拟热传导的过程，每个点的下一时刻温度是其自身与其左右两个相邻点当前温度的平均值。
# (1)，请输出前10轮传导的过程 杆上各分段点的温度情况；(2)，确定通过多少轮传导后杆上各点的最低温度超过了60度，并输出在此期间每5轮传导后的情况。请用 Python 的格式化功能把输出排列整齐。

def conduction(n):
    points = [0 for i in range(11)]
    points[0] = 100
    points[10] = 70
    copylist = []
    for i in range(n):
        copylist = points.copy()
        for j in range(1, 10):
            copylist[j] = (points[j - 1] + points[j + 1]) / 2
        points = copylist.copy()

    return points


for i in range(1, 11):
    print(conduction(i))
for i in range(1, 100):
    if min(conduction(i)) > 60.0:
        break
for j in range(1, i, 5):
    for item in conduction(j):
        print('{:.5f}'.format(item), end=' ')
    print('\n')
