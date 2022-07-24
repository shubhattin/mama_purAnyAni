from functions import TrigFunc, rnd
from tkinter import Frame, Button, Scale, IntVar, StringVar, Label, Entry,\
    NW, LEFT, Toplevel, HORIZONTAL, Tk, Radiobutton
from tkinter.font import Font
from winregistry import WinRegistry


def set_lang() -> int:
    path = r'HKCU\SOFTWARE\trig_evaluate'
    reg = WinRegistry()
    try:
        a = int(reg.read_value(path, 'language')['data'])
        if a not in (0, 1):
            raise FileExistsError
        return a
    except FileNotFoundError:
        store_lang(0)
        return set_lang()


def store_lang(n) -> None:
    reg = WinRegistry()
    path = r'HKCU\SOFTWARE\trig_evaluate'
    if 'trig_evalutor' not in reg.read_key(r'HKCU\SOFTWARE')['keys']:
        reg.create_key(path)
    reg.write_value(path, 'language', {0: b'0', 1: b'1'}[n], 'REG_BINARY')


hn_lng_db = ('दशमलव सूक्ष्मता', 'भाषा चुनें', 'अनुप्रयोग परिचय', 'रेडियन प्रणाली मे बदले',
             '  डिग्री प्रणाली मे बदलें  ', 'कोण का माप', '', 'अवसर्पक को कर्षित करें',
             'अपनी भाषा चुनें', 'त्रिकोणमितीय अनुपातों के सटीक मान की गणना हेतु यह ऐप है।'
             '\nइसके निर्माण मे किसी वाह्य गणित ग्रंथालय का प्रयोग नहीं हुआ है ।'
             '\nइसके कलन विधि को \'टेलर\' प्रक्रम से निर्मित किया गया है।\nनिर्माता : शुभम आनंद '
             'गुप्ता', 'त्रिकोणमितीय मूल्याङ्कनकर्ता', 'दशमलव सूक्ष्मता निर्धारण', 'भाषा', 'ऐप के बारे मे')
en_lng_data = ('Decimal Precision', ' Language ', 'About', 'Switch to Radian Mode',
               'Switch to Degree Mode', 'Enter Angle', '', 'Drag the Slider',
               'Choose Your Language', 'Application to evaluate exact values of '
               'Trignometric Ratios.\nNo External Mathematical Library has been used.'
               '\nThe Algorithm is made using \'Taylor\' series.\nAuthor : Shubham Anand'
               ' Gupta', 'Trignometric Evaluator', 'Set Decimal Precision', 'Language',
               'About')


class Design:
    def __init__(self, r):
        self.__root = r
        self.__root.bind('<KeyPress>', self.__enter_value)
        self.__language = IntVar(self.__root, set_lang())
        self.__l_data = {0: en_lng_data, 1: hn_lng_db}[self.__language.get()]
        self.__root.geometry('618x290+200+100')
        self.__root.resizable(False, False)
        self.__root.iconbitmap(r'icon.ico')
        self.__root.title(self.__l_data[10])
        self.__round_off_index = IntVar(self.__root, 3)
        self.__printing = lambda x=['                     '] * 6: \
            'Sin = {0}\nCos = {1}\nTan = {2}\n Cosec = {3}\nSec = {4}\nCot = {5}' \
            .format(x[1], x[0], x[2], x[3], x[4], x[5])
        self.__angle_mode = IntVar(self.__root, 0)
        self.__print_status = False
        self.__input_text = StringVar(self.__root)
        self.__design_top_frame()
        self.__design_input_frame()
        self.__design___print_frame()

    def __design_top_frame(self) -> None:
        self.__top_frame = Frame(self.__root)
        my_font = Font(size=15, weight='bold')
        decimal_precision_button = Button(self.__top_frame, text=self.__l_data[0],
                                          font=my_font, fg='blue', bg='yellow',
                                          relief='ridge', command=self.__prec_setter)
        decimal_precision_button.grid(row=0, sticky=NW)
        language_button = Button(self.__top_frame, text=self.__l_data[1], font=my_font,
                                 fg='red', bg='yellow', relief='ridge',
                                 command=self.__lang_btn)
        language_button.grid(row=0, column=1, sticky=NW)
        about_button = Button(self.__top_frame, text=self.__l_data[2], font=my_font,
                              fg='green', bg='yellow', relief='ridge',
                              command=self.__about_window)
        about_button.grid(row=0, column=2, sticky=NW)
        self.__mode_button = Button(self.__top_frame, font=my_font, fg='black',
                                    text=self.__l_data[int(
                                        self.__angle_mode.get())+3],
                                    bg='yellow', relief='ridge',
                                    command=self.__mode_select)
        self.__mode_button.grid(row=0, column=3, sticky=NW)
        self.__top_frame.grid(row=0, sticky=NW)

    def __design_input_frame(self) -> None:
        seperator = Label(self.__root, text=' ' * 10)
        seperator.grid(row=1, sticky=NW)
        self.__input_frame = Frame(self.__root)
        my_font2 = Font(size=20, weight='bold')
        enter = Label(self.__input_frame, text=self.__l_data[5],
                      font=my_font2, fg='green')
        enter.pack(side=LEFT)
        value_enter = Entry(self.__input_frame, textvariable=self.__input_text,
                            font=my_font2, width=27, fg='orange')
        value_enter.pack(side=LEFT)
        self.__seperator_label = Label(self.__input_frame, text='⁰',
                                       font=Font(size=18, weight='bold'))
        self.__seperator_label.pack(side=LEFT)
        self.__input_frame.grid(row=2, column=0, sticky=NW)

    def __design___print_frame(self) -> None:
        print_frame = Frame(self.__root)
        my_font2 = Font(size=19, weight='bold')
        self.__print_label = Label(print_frame, text=self.__printing(),
                                   font=my_font2, fg='purple')
        self.__print_label.pack(side=LEFT)
        print_frame.grid(row=3, column=0, sticky=NW)

    def __extract_num(self, s) -> str:
        result = ''
        decimal_status = False
        counter = 1
        for x in s:
            if x == '.' and not decimal_status:
                decimal_status = True
            elif x == '-' and counter == 1:
                first = False
            elif x not in '1234567890':
                continue
            result += x
            counter += 1
        return result

    def __enter_value(self, event=None) -> None:
        try:
            self.__calc_value(float(str(self.__input_text.get())))
            self.__print_status = True
        except ValueError:
            self.__input_text.set(self.__extract_num(
                str(self.__input_text.get())))
            self.__print_status = True
            a = str(self.__input_text.get())
            try:
                self.__calc_value(float(a))
            except ValueError:
                self.__print_label.configure(text=self.__printing())

    def __calc_value(self, angl) -> None:
        val: list = []
        if self.__angle_mode.get() == 0:
            val = TrigFunc(angl).ratios
        else:
            val = TrigFunc(angl, True).ratios
        val = rnd(val, self.__round_off_index.get())
        self.__print_label.configure(text=self.__printing(val))

    def __mode_select(self, x=0) -> None:
        self.__angle_mode.set(abs(self.__angle_mode.get() - 1 + x))
        self.__mode_button.configure(text=self.__l_data[4] if self.__angle_mode.get()
                                     == 1 else self.__l_data[3])
        self.__print_label.configure(text=self.__printing())
        self.__seperator_label.configure(text={1: 'rad', 0: '⁰'}
                                         [self.__angle_mode.get()])
        self.__enter_value()
        self.__print_status = True

    def __prec_setter(self) -> None:
        round_off_window = Toplevel()
        round_off_window.title(self.__l_data[11])
        round_off_window.resizable(False, False)
        round_off_window.iconbitmap(r'Icon.ico')
        round_off_window.geometry('320x92+250+150')
        my_font = Font(size=16, weight='bold')
        display_label = Label(round_off_window, text=self.__l_data[7],
                              font=my_font, fg='green')
        display_label.pack()
        self.scale = Scale(round_off_window, from_=3, to=15, orient=HORIZONTAL,
                           length=330, width=25, variable=self.__round_off_index,
                           command=self.__update_prec_data)
        self.scale.pack()
        round_off_window.mainloop()

    def __update_prec_data(self, event) -> None:
        self.scale.set(self.__round_off_index.get())
        if self.__print_status:
            self.__enter_value()

    def __lang_btn(self) -> None:
        self.__lang_window = Toplevel()
        self.__lang_window.title(self.__l_data[12])
        self.__lang_window.geometry('250x100+300+150')
        self.__lang_window.resizable(False, False)
        self.__lang_window.iconbitmap(r'Icon.ico')
        my_font = Font(size=16, weight='bold')
        self.__lbl = Label(self.__lang_window, text=self.__l_data[8],
                           font=my_font, fg='green')
        self.__lbl.pack()
        l_chooser2 = Radiobutton(self.__lang_window, text='हिन्दी', font=my_font,
                                 value=1, variable=self.__language,
                                 command=self.__update_lang_data)
        l_chooser2.pack()
        l_chooser1 = Radiobutton(self.__lang_window, text='English', font=my_font,
                                 value=0, variable=self.__language,
                                 command=self.__update_lang_data)
        l_chooser1.pack()
        self.__lang_window.mainloop()

    def __update_lang_data(self) -> None:
        self.__l_data = {0: en_lng_data, 1: hn_lng_db}[self.__language.get()]
        store_lang(self.__language.get())
        self.__top_frame.grid_forget()
        self.__input_frame.grid_forget()
        self.__design_input_frame()
        self.__design_top_frame()
        self.__mode_select(1)
        self.__lbl.configure(text=self.__l_data[8])
        self.__root.title(self.__l_data[10])
        self.__lang_window.title(self.__l_data[12])

    def __about_window(self) -> None:
        abt_win = Toplevel()
        abt_win.title(self.__l_data[13])
        abt_win.resizable(False, False)
        abt_win.iconbitmap(r'Icon.ico')
        abt_win.geometry('610x104+220+150')
        my_font = Font(size=16, weight='bold')
        label = Label(abt_win, text=self.__l_data[9], font=my_font, fg='brown')
        label.pack()
        abt_win.mainloop()


if __name__ == "__main__":
    root = Tk()
    App = Design(root)
    root.mainloop()
