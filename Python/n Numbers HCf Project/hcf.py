from WConio2 import textcolor, clrscr, getch, setcursortype
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("n Numbers HCF")


def hcf(n):
    a, b, r = n[0], n[1], 0
    for x in range(0, len(n) - 1):
        while a != 0:
            r = b % a
            b = a
            a = r
        a = b
        if x + 2 == len(n): break
        b = n[x + 2]
    return a


def main():
    textcolor(11)
    clrscr()
    print("\t\tAfter Entering Enough Numbers Enter last Value as 0 to Find HCF\n\n")
    num, x, p, ch = [], 0, [], '\0'
    textcolor(10)
    while True:
        try:
            x = float(input("Enter a Number="))
        except:
            break
        if not x:
            break
        p.append(str(int(x)) if x == int(x) else str(x))
        x = abs(x)
        while x != int(x):
            x *= 10
        num.append(int(x))
    if len(p) == 1 or not len(p):
        return
    setcursortype(0)
    clrscr()
    textcolor(12)
    print("\n\nHCF of These Entered Numbers:")
    textcolor(15)
    print(' , '.join(p))
    textcolor(14)
    print("Is =", hcf(num))
    textcolor(15)
    print('\nPress Enter Key to Continue')
    while ch != '\r':
        ch = getch()[1]
    return


main()