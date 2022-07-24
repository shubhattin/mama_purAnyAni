from tkinter import Tk, mainloop, Entry, StringVar, OptionMenu, IntVar, LEFT
from tkinter.font import Font
from json import load, dump
from copy import deepcopy


class nirmANa:
    def __init__(self):
        self.__root = Tk()
        self.__achara = StringVar(self.__root, value='')
        self.__praNAli = IntVar(self.__root, 1)
        OptionMenu(self.__root, self.__praNAli, *['1', '2', '3'],
                   ).pack(side=LEFT)
        Entry(self.__root, width=40, textvariable=self.__achara,
              font=Font(size=20, weight='bold', family='Sanskrit Text',),
              fg='red').pack(side=LEFT)
        self.__root.resizable(False, False)
        self.__root.bind('<Return>', self.__add)
        self.__file = open('shabdānām arthaḥ.json', mode='r', encoding='utf-8')
        self.__json_obj = load(self.__file)
        self.__file.close()
        self.__root.protocol('WM_DELETE_WINDOW', self.__save_data)
        self.__password_status = False
        self.__root.mainloop()

    def __add(self, event):
        data = self.__achara.get()
        if not self.__password_status:
            val = 'truṭi!'
            if data == 'aum' or data == 'अउम्':
                self.__password_status = True
                val = 'ok'
            elif data == 'व्यवस्थित':
                self.__prevent_dublicates()
                self.__save_data()
                return
            self.__achara.set(val)
            self.__root.after(500, lambda: self.__achara.set(''))
            return
        if '/' not in data or data[0] not in self.__json_obj['1']:
            self.__achara.set('truṭi')
            self.__root.after(500, lambda: self.__achara.set(''))
            return
        if data[-1] in ',।':
            a = [1, 2, 3]
            a.remove(self.__praNAli.get())
            if data[-1] == ',':
                st = str(a[0])
            else:
                st = str(a[1])
        else:
            st = str(self.__praNAli.get())
        data = data.split('/')
        extra = ''
        if data[0] in self.__json_obj[st][data[0][0]]:
            extra = self.__json_obj[st][data[0][0]].get(data[0])+' ~`\n'
        self.__json_obj[st][data[0][0]][data[0]
                                        ] = extra+data[1]
        self.__achara.set('अस्तु'+st)
        self.__root.after(100, lambda: self.__achara.set(''))

    def __save_data(self):
        self.__file = open('shabdānām arthaḥ.json', mode='w', encoding='utf-8')
        dump(self.__json_obj, self.__file, ensure_ascii=False, indent=4)
        self.__file.close()
        self.__root.destroy()

    def __prevent_dublicates(self):
        s = self.__json_obj
        y=deepcopy(s)
        for samkhya in s:
            for varNa in s.get(samkhya):
                for shabda in s.get(samkhya).get(varNa):
                    a = check(shabda, s, samkhya, varNa)
                    if a:
                        for c in a:
                            z = s.get(c).get(varNa).get(shabda)
                            del y[c][varNa][shabda]
                            y[c][varNa][shabda+c] = z
        s=y
        res = {}
        for samkhya in s:
            k={}
            for akshara in s.get(samkhya):
                sarve = sorted(s[samkhya][akshara])
                j = {}
                for x in sarve:
                    j[x] = s[samkhya][akshara].get(x)
                k[akshara]=j
            res[samkhya] = k
        self.__json_obj = res


def check(shabda, hj, samkhya, varNa):
    arr = [samkhya]
    if samkhya == '1':
        if shabda in hj['2'][varNa]:
            arr.append('2')
        if shabda in hj['3'][varNa]:
            arr.append('3')
    elif samkhya == '2':
        if shabda in hj['3'][varNa]:
            arr.append('3')
    if arr == [samkhya]:
        return False
    else:
        return arr


if __name__ == '__main__':
    nirmANa()
