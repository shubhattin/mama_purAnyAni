from WConio2 import getch, gotoxy, setcursortype, highvideo, clrscr, textcolor, getkey
import ctypes


def locate(xy, yx): return gotoxy(yx - 1, xy - 1)


def title(st):
    ctypes.windll.kernel32.SetConsoleTitleW(st)
    return


def control():
    title('Decimal-Binary Conversions')
    locate(1, 1)
    textcolor(15)
    print('>>>')
    f = 1
    a = '\0'
    while True:
        a = '\0'
        a = getkey()
        if a == '\x1b':
            return None
        elif f == 1:
            if a == 'down':
                f = 2
                setl(1, f)
            elif a == 'up':
                f = 3
                setl(1, f)
            elif a == '\r':
                binr()
                return 0
        elif f == 2:
            if a == 'down':
                f = 3
                setl(2, f)
            elif a == 'up':
                f = 1
                setl(2, f)
            elif a == '\r':
                decm()
                return 0
        elif f == 3:
            if a == 'down':
                f = 1
                setl(3, f)
            elif a == 'up':
                f = 2
                setl(3, f)
            elif a == '\r':
                return None


def setl(vb, bv):
    locate(vb, 1)
    print('   ')
    textcolor(15)
    locate(bv, 1)
    print('>>>')


def entr():
    vbn = 0
    textcolor(15)
    print('\nPress Enter Key to Continue')
    while vbn != 13:
        vbn = getch()[0]


def ckeck(bn):
    for j in bn:
        if j in '23456789':
            return 1
    return 0


def binr():
    title('Conversion From Decimal To Binary')
    clrscr()
    textcolor(11)
    setcursortype(1)
    try:
        num = int(input('Enter a Decimal Number = '))
    except ValueError:
        num = 0
    num = abs(num)
    clrscr()
    print('Decimal Form = '+str(num))
    setcursortype(0)
    c = 0
    n = 0
    d = 0
    textcolor(4)
    print('\nBinary Conversion:\nSolution:-\n')
    textcolor(10)
    if num == 0:
        print('2 | 0 - 0')
    while num != 0:
        c = num % 2
        print(({True: '2', False: ' '}[num != 1]+' | '+str(num)+' - '+str(c)))
        num = (num-c)//2
        d += c*10**n
        n = n+1
    textcolor(14)
    print('\nConverted Binary Form = '+str(d))
    entr()


def decm():
    title('Conversion From Binary To Decimal')
    clrscr()
    textcolor(11)
    setcursortype(1)
    try:
        nm = int(input('Enter a Binary Number = '))
    except ValueError:
        nm = 0
    setcursortype(0)
    a = str(nm)
    if ckeck(a):
        textcolor(14)
        print('\n'+str(nm)+' is Not a Binary Number')
        entr()
        return
    a = str(abs(nm))
    clrscr()
    print('Binary Form = '+str(a))
    b, c, d = len(a), 0, 0
    textcolor(4)
    print('\nDecimal Conversion:\nSolution:-\n')
    textcolor(10)
    for n in range(0, b):
        c = int(a[n])*2**(b-n-1)
        d += c
        print(a[n]+'*2^'+str(b-n-1)+' = '+str(c))
    textcolor(14)
    print('\nConverted Decimal Form = '+str(d))
    entr()
