from tkinter import Tk, Frame, Entry, Listbox, StringVar, NW, \
    Scrollbar, BOTH, LEFT, SINGLE, Label, IntVar, OptionMenu
from tkinter.font import Font
from json import load
from os import startfile


def match(a, b):
    if b[:len(a)] == a:
        return True
    else:
        return False


def antaH_parivartana(a):
    res = {}
    for c in a:
        res[a[c]] = c
    return res


class mukhya:
    def __init__(self):
        self.__root = Tk()
        self.__root.resizable(False, False)
        self.__root.geometry('800x410+180+100')
        self.__root.title('shabdakośaḥ')
        self.__root.iconbitmap('icon.ico')
        self.__shabda = StringVar(master=self.__root)
        self.__surakShita_dashA = True
        en = Entry(master=self.__root, width=17,
                   textvariable=self.__shabda, fg='red', bg='yellow',
                   font=Font(size=19, weight='bold', family='Sanskrit Text'))
        en.grid(row=0, column=0, sticky=NW)
        self.__praNAli = IntVar(self.__root, value=0)
        OptionMenu(self.__root, self.__praNAli, *['0', '1', '2', '3', '4'],
                   command=lambda _: self.__kosha_sUchI(1)).grid(
            row=0, column=1, sticky=NW)
        display_frame = Frame(self.__root)
        self.__list = Listbox(master=display_frame, selectmode=SINGLE,
                              font=Font(size=16, weight='bold', family='Sanskrit Text'), height=11)
        self.__list.pack(side=LEFT, fill=BOTH)

        self.__root.bind('<KeyPress>', self.__kosha_sUchI)
        self.__list.insert(0, 'apariṇāmasya')
        scr = Scrollbar(display_frame)
        scr.pack(side=LEFT, fill=BOTH)
        self.__list.config(yscrollcommand=scr.set)
        self.__root.bind('<Button-1>', self.__pashyatyartha)
        self.__temp = ''
        scr.config(command=self.__list.yview)
        display_frame.grid(row=1, column=0)
        arthaframe = Frame(self.__root)
        self.__selection = 0
        self.__list.select_set(self.__selection)
        self.__word = StringVar(self.__root, value='')
        self.__meaning = StringVar(self.__root, value='')
        Label(arthaframe, textvariable=self.__word,
              font=Font(size=20, weight='bold', family='Sanskrit Text'),
              fg='green').grid(row=0, column=0, sticky=NW)
        Label(arthaframe, textvariable=self.__meaning,
              font=Font(size=17, weight='bold', family='Sanskrit Text'),
              fg='purple', wraplength=480, justify=LEFT).grid(row=2, column=0, sticky=NW)
        arthaframe.grid(row=1, column=1, sticky=NW)
        self.__root.mainloop()

    def __kosha_sUchI(self, event=1):
        if self.__surakShita_dashA:
            a = self.__shabda.get()
            if a == 'hariom' or a == 'हरिओम्':
                startfile('nirmāṇa.exe')
                self.__root.destroy()
                exit()
            elif a == 'AUM' or a == 'ॐ':
                startfile('shabdānām arthaḥ.json')
                self.__root.destroy()
                exit()
            elif a == 'aum' or a == 'अउम्':
                self.__surakShita_dashA = False
                self.__shabda.set('')
            return
        if event != 1:
            if 'Up' == event.keysym:
                self.__OnEntryUp()
                return
            elif 'Down' == event.keysym:
                self.__OnEntryDown()
                return
        khojavarNani = self.__shabda.get()
        if khojavarNani == self.__temp and event != 1:
            return
        else:
            self.__temp = khojavarNani
        self.__word.set('')
        self.__meaning.set('')
        antima = []
        self.__list.delete(0, 'end')
        if khojavarNani == '':
            self.__list.insert(0, 'apariṇāmasya')
            return
        varNa = khojavarNani
        if varNa[-1] in '्॒':
            varNa = varNa[:-1]
        if self.__praNAli.get() == 4:
            for c in sarvashabda:
                b = 0
                f = sarvashabda.get(c)
                f_opp = antaH_parivartana(f)
                for s in f.values():
                    if varNa in s:
                        antima.append((f_opp.get(s), s))
                    b += 1
            if antima == []:
                self.__list.insert(0, 'apariṇāmasya')
                return
            c = 0
            for x in antima:
                self.__list.insert(c, x[0]+'~'+x[1])
                c += 1
            return
        if self.__praNAli.get() == 0:
            kl = sarvashabda
        else:
            kl = koshaH[str(self.__praNAli.get())]
        if varNa[0] not in kl:
            self.__list.insert(0, 'apariṇāmasya')
            return
        f = kl.get(varNa[0])
        for x in f.keys():
            if len(x) >= len(varNa):
                if match(varNa, x):
                    antima.append((x, f[x]))
        c = 0
        if antima == []:
            self.__list.insert(0, 'apariṇāmasya')
            return
        for x in antima:
            self.__list.insert(c, x[0]+'    ||~'+x[1])
            c += 1

    def __pashyatyartha(self, event=None):
        if self.__list.get(0) == 'apariṇāmasya':
            return
        try:
            val = self.__list.get(self.__list.curselection()[0])
        except IndexError:
            return
        val = val[:val.find('~')]
        self.__selection = self.__list.curselection()[0]
        if self.__praNAli.get() < 4:
            val = val[:-6]
        self.__word.set(val)
        val = sarvashabda.get(val[0]).get(val)
        self.__meaning.set(val)

    def __OnEntryDown(self):
        if self.__selection < self.__list.size()-1:
            self.__list.select_clear(self.__selection)
            self.__selection += 1
            self.__list.select_set(self.__selection)
        self.__pashyatyartha()

    def __OnEntryUp(self):
        if self.__selection > 0:
            self.__list.select_clear(self.__selection)
            self.__selection -= 1
            self.__list.select_set(self.__selection)
        self.__pashyatyartha()


file = open('shabdānām arthaḥ.json', encoding='utf-8')
koshaH = load(file)
file.close()


def join(a, b):
    return dict(a, **b)


sarvashabda = {}
for b in koshaH["1"].keys():
    sarvashabda[b] = join(koshaH["1"][b],
                          join(koshaH["2"][b], koshaH["3"][b]))
res = {}
d=sarvashabda
for akshara in d:
    sarve = sorted(d[akshara])
    j = {}
    for x in sarve:
        j[x] = d[akshara].get(x)
    res[akshara]=j
sarvashabda=res
mukhya()
