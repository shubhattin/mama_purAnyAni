from resources import locate, setcursortype, clrscr, control, textcolor

def main():
    x = '\0'
    while True:
        clrscr()
        locate(1, 1)
        textcolor(12)
        print('    Decimal To Binary')
        textcolor(11)
        print('    Binary To Decimal')
        textcolor(10)
        print('    Exit')
        x = control()
        if x is None:
            return


setcursortype(0)
main()
