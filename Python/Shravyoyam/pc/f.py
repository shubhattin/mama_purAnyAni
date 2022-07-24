from pynput.keyboard import Key,Listener
import ctypes
from os import system 
from threading import Thread
from win32gui import GetWindowText, GetForegroundWindow
from pywinauto.application import Application
from WConio2 import getkey,setcursortype,clrscr
system('mode 55,10')
system('color 04')
print('svasti')
ctypes.windll.kernel32.SetConsoleTitleW('vināsho\'sti')

class run():
    def __init__(self):
        self.__active_status = False
        self.__index = 0
        self.__th =Thread(target=self.__change)
        self.__th.daemon=True
        self.__th.start()       
        self.start_file = []
        self.__active_status = False
        self.__pass = False
        with Listener(on_press=self.__wait) as shrotA:
            shrotA.join()
        if self.__active_status:
            self.__dig.close()
    def __wait(self,key):
        try:
            key = key.name
        except AttributeError:
            key = key.char
        if 'end' in key or 'esc' in key:
            return False
        elif 'shift' in key and self.__pass:
            self.__play()
  
    def __change(self): 
        setcursortype(0)
        a = 'hariom'
        index = 0
        while index != len(a):
            b = getkey()
            if b == a[index]:
                index += 1
            else:
                index = 0
        print('susvasti')
        self.__pass = True
        system('color b')

            
         
    def __play(self):
        a = GetWindowText(GetForegroundWindow())
        app = Application().connect(title=a)
        self.__dig=app[a]
        clrscr()
        print(a)
        self.__active_status = True
run()
