# 1，修改课堂介绍的统计文本中单词出现频率的程序，设法去掉各种标点符号等不属于单词的字符，使之能更好完成统计工作。
# 建议把矫正被统计单词的功能定义为函数 clarify(word)，它处理直接切分得到的 word，返回矫正后的单词，这样可使对原程序的直接修改最少，
# 也更容易改变单词的矫正方法。原程序文件见课件页，这里有一个试验数据文件（海明威的《太阳照常升起》book 1 文本）。
# 编程中可能用到一些字符串操作，请参考课题幻灯片和 Python 文档。修改函数行为方式，如果调用时给了统计文件名参数，函数就将统计数据存入文件；
# 否则这个函数返回做出的字典。请另外定义一个函数，它调用上述统计函数，并在屏幕上输出（用print）这篇文章中使用最多的20个单词及其使用次数。请考虑如何利用系统函数sorted完成这一工作。

def judge_str(c):
    judge = 1
    if ord(c) in range(32, 39):
        judge = 0
    elif ord(c) in range(40, 48):
        judge = 0
    elif ord(c) in range(58, 64):
        judge = 0
    elif ord(c) in range(91, 97):
        judge = 0
    elif ord(c) in range(123, 126):
        judge = 0
    else:
        judge = 1
    return judge


def clarify(s):
    s = s.lower()
    list_singleword = []
    for i in range(len(s)):
        list_singleword.append(s[i])
    for i in range(len(s)):
        if (i == 0 and s[i] == '\'') or judge_str(s[i]):
            continue
        else:
            list_singleword[i] = ''
    return ''.join(list_singleword)


def textstat(infname, statfile='|'):
    worddict = {}
    textfile = open(infname)

    for line in textfile:
        wordlist = line.split()
        for word in wordlist:
            word = clarify(word)
            if word == '':
                continue
            elif word in worddict:
                worddict[word] += 1
            else:
                worddict[word] = 1
    textfile.close()

    wordlist = [[x, y] for (y, x) in list(worddict.items())]
    wordlist.sort(reverse=True)  # [[747, 'the'], [509, 'I'], [437, 'to'], [436, 'and'], [402, 'a'], [265, '...
    dict_display = {}
    for item in wordlist:
        if item[1] in dict_display:
            dict_display[item[1]] += 1
        else:
            dict_display[item[1]] = 1
    for i in range(20):
        print(wordlist[i][1], wordlist[i][0])
    if statfile != '|':
        outfile = open(statfile, "w")
        for item in wordlist:
            outfile.write(str(item[1]) + "\t" + str(item[0]) + "\n")
    if not statfile != '|':
        return dict_display


textstat('sun1.txt', 'stst_sun.txt')

# 2，请开发一个猜单词游戏程序：程序启动后从一个事先准备好的文件里读入一组单词（用一个单词表），然后进入游戏状态。
# 做每轮游戏时程序从这些单词里随机选出一个。一轮游戏包含若干回合，每个回合程序从单词中随机选出一个字母，输出该字母及其在单词里的位置作为提示。
# 如果用户认为已经猜到，就输入所猜的单词，前面写一个叹号“!”，程序评判其对错并记录有关信息。如果用户觉得无法猜出结果，
# 可以输入一个单独的问号“?”要求程序继续给出提示。基于提示次数和单词长度设置一种失败阈值，要求提示的次数超过这个值即认为本轮游戏失败，
# 程序输出被猜单词后结束本轮。一轮游戏结束后用户输入命令“quit”时程序结束，此时输出一组统计信息：本次游戏共猜了几个单词，正确和错误统计，平均每个单词要求了几次提示。

from random import *

print('The game started!')
flag = 'not quit'
wordfile = open('word_list.txt', 'r')
wordlist = wordfile.readlines()
for i in range(len(wordlist)):
    if wordlist[i][-1] == '\n':
        wordlist[i] = wordlist[i][0:-1]
# print(wordlist)
number_guessed = 0  # 猜过的单词次数。
right_number = 0  # 猜正确的单词。
wrong_number = 0  # 猜错的单词。
hint_times_sum = 0  # 总共的提示次数。
hint_times = 0  # 单个单词的提示次数。
while flag != 'quit':
    word_number = randint(1, len(wordlist))  # 随机选中的单词编号。
    word_guess = wordlist[word_number]  # 随机选中的单词。
    while (hint_times / len(word_guess)) <= 1 / 3:
        hint_letter_number = randint(1, len(word_guess))  # 随机选中的字母编号。
        hint_times += 1
        hint_times_sum += 1
        print(
            'letter: {}, place: {}, please try. If you have known the answer, start your answer with "!". Otherwise, input "?" for more help.'.format(
                word_guess[hint_letter_number - 1], hint_letter_number))
        guess = input()
        if guess[0] == '!':
            guess = guess[1:]
            if guess == word_guess and (hint_times / len(word_guess)) <= 1 / 3:
                print('Success!')
                right_number += 1
                break
            else:
                print('Failed.')
        elif guess == '?':
            print('You have lost a chance.')
        else:
            continue
    if (hint_times / len(word_guess)) > 1 / 3:
        print('Using too many hints, the word is : {}'.format(word_guess))
        wrong_number += 1
    hint_times = 0
    number_guessed += 1
    flag = input('Would you like to quit?')

print('You have tried {} words'.format(number_guessed))
print('You succeeded {} times and failed {} times.'.format(right_number, wrong_number))
print('The average hints you used in each word is {0:.4f}'.format(hint_times_sum / number_guessed))
