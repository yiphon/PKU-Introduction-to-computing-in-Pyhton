# 1，考虑下面游戏：n 个人围成一圈，每次游戏随机取两个数 m 和 k。游戏开始，从编号为 m 的人开始计数，数到第 k 个人出列。
# 然后再从出列的人之后数下去，直到圈子里只剩一个人为止。请写一个函数 CGame(n, m, k) 模拟这个游戏：围成一圈可以用计数到最大的编号后重新回到最小编号值来处理。

def CGame(n, m, k):
    a = [i for i in range(1, n + 1)]
    for i in range(1, n):
        j = m + k
        del a[j % (n - i + 1) - 1]
        m = j % (n - i + 1) - 1
        print(a)


CGame(10, 3, 5)

# 2，请定义一个生成器函数，它顺序检查一段文本（一个字符串），挑选出在文本中遇到的所有长度超过 8 个字符的单词，顺序 yield 出这些单词。
# 在定义这个生成器时不使用 split 等函数构造字符串（不调用任何可能构造字符串的函数或操作），
# 只用从字符串中取字符的操作（即，s[i]）检查字符串内容，用 s[i].isspace() 判断是否空白字符（空格，换行等）。
# 也就是说，你的生成器应设法确定字符串中顺序的由空格分隔的段，做出正确切片字符串（单词）。为简单起见，文本中的标点符号也看作单词内容。
# 定义函数后，请用上次课（4.27）代码文件里的 “Python 语言说明”作为例子试验这个函数的功能（拷贝到你的程序文件里）。

s = """Python was created in the early 1990s by Guido van Rossum at
Stichting Mathematisch Centrum (CWI, see http://www.cwi.nl/)
in the Netherlands as a successor of a language called ABC.
Guido remains Python principal author, although it includes
many contributions from others.

In 1995, Guido continued his work on Python at the Corporation
for National Research Initiatives (CNRI,
see http://www.cnri.reston.va.us/) in Reston, Virginia where
he released several versions of the software.

In May 2000, Guido and the Python core development team moved
to BeOpen.com to form the BeOpen PythonLabs team. In October
of the same year, the PythonLabs team moved to Digital Creations
(now Zope Corporation; see http://www.zope.com/). In 2001, the
Python Software Foundation (PSF, see http://www.python.org/psf/)
was formed, a non-profit organization created specifically to
own Python-related Intellectual Property. Zope Corporation is a
sponsoring member of the PSF."""


def selection(s):
    mark = 0
    for i in range(len(s)):
        if s[i].isspace():
            word = ''
            for j in range(mark, i):
                word += s[j]
            if len(word) > 8:
                yield word
            mark = i + 1


for i in selection(s):
    print(i)

# 3，在 Python 标准库的 Program Framework 栏目下有一个图形包 turtle，它模拟了著名的 logo 语言的一些功能。
# 请自己查阅 Python 文档，阅读该程序包的说明，并基于这个包写一点程序，画出（至少）3 个有趣的图形（自选图形）。请在程序文件里用注释的形式说明你做的工作。
from turtle import *

speed(0)
color('#66ccff')
circle(100, 180)
color('#00eeee')
circle(100, 180)
circle(50, 180)
color('#66ccff')
circle(-50, 180)
pu()
goto(0, 50)
pd()
dot(20, '#00eeee')
pu()
goto(0, 150)
dot(20, '#66ccff')

speed(0)
circle(100, 360)
pu()
goto(100, 100)
left(90)
pd()
colormode(255)
for i in range(30):
    color(255, int(255 * i / 30), int(255 * (30 - i) / 30))
    pu()
    goto(100 * math.cos(i / 15 * math.pi), 100 * (1 + math.sin(i / 15 * math.pi)))
    pd()
    fd(50 + i * 5)
    left(12)

ht()
speed(10)
circle(100, 360)
pu()
goto(100, 100)
pd()
colormode(255)
for i in range(360):
    color(255, int(255 * i / 360), int(255 * (360 - i) / 360))
    pu()
    goto(100 * math.cos(i / 180 * math.pi), 100 * (1 + math.sin(i / 180 * math.pi)))
    pd()
    fd(50 * math.sin(i / 180 * math.pi))
    left(1)

mainloop()
