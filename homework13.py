# 某个程序的GUI实现。

import tkinter as tk
import math


class prime_factorGUI(tk.Frame):
    @staticmethod
    def prime_factor(n):
        def is_prime(n):
            a = True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i != 0:
                    a = a * True
                else:
                    a = a * False
            return a

        if is_prime(n):
            return str(n) + ' is not a composite number'
        else:
            dic_factor = {}
            count = n
            for i in range(n, 1, -1):
                if n % i == 0 and is_prime(i):
                    count = count / i
                    times = 1
                    while True:
                        if count % i == 0:
                            times += 1
                            count = count / i
                        else:
                            dic_factor[str(i)] = str(times)
                            break
            return dic_factor

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('Prime factors decomposition')
        self.grid()
        self._guide = tk.Label(self, font=('Times New Roman', 15), text='Input number:')
        self._guide.grid(row=0, column=0, sticky=tk.W)
        self._input_line = tk.Entry(self, width=20, )  # width 为字符宽度
        self._input_line.grid(row=1, column=0, sticky=tk.W)
        self._button = tk.Button(self, text='Get prime factors decomposition', anchor=tk.CENTER,
                                 command=self.calculation)
        self._button.grid(row=1, column=1)
        self.mainloop()

    def calculation(self):

        self._num = self._input_line.get()
        self._num = int(self._num)
        self._result = prime_factorGUI.prime_factor(self._num)
        if isinstance(self._result, str):
            self.errlable = tk.Label(self, font=('Times New Roman', 13), text=self._result)
            self.errlable.grid(row=2, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        if isinstance(self._result, dict):
            self._str = '{}='
            self._list = [[y, x] for (y, x) in list(self._result.items())]
            self._list.sort()
            for item in self._list:
                self._str += '\n' + item[0] + '^' + item[1]
            self.outputlable = tk.Label(self, font=('Times New Roman', 13), text=self._str.format(self._num))
            self.outputlable.grid(row=2, column=0, sticky=tk.W + tk.E + tk.N + tk.S)


prime_factorGUI()
