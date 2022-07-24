from pynput.keyboard import Key,Listener
from playsound import playsound
from json import load
import ctypes
from os import system
from threading import Thread
from time import sleep, time
from WConio2 import getkey, setcursortype, kbhit
from subprocess import Popen
path = load(open('s.json'))
system('mode 40,7')
system('color 08')
print('astu')
ctypes.windll.kernel32.SetConsoleTitleW('mahatvapUrNa')


class run():
    def __init__(self):
        self.__active_status = False
        self.__index = 0
        self.__th = Thread(target=self.__play)
        self.__th.daemon = True
        self.__th2 = Thread(target=self.__change)
        self.__th2.daemon = True
        self.__th2.start()
        self.start_file = []
        self.__v_daśā = False
        with Listener(on_press=self.__wait) as shrotA:
            shrotA.join()
        if self.__v_daśā:
            self.__eog.kill()
    def __wait(self,key):
        try:
            key = key.name
        except AttributeError:
            key = key.char
        if 'end' in key or 'esc' in key:
            return False
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
        print('svasti')
        a, b = '', ''
        c = a+b
        while c not in path:
            a = getkey()
            start = time()
            while time()-start <= 0.600:
                if kbhit():
                    b = getkey()
            c = a+b
            a, b = '', ''
        self.start_file = path.get(c)
        print('uttama')
        self.__th.start()

    def __play(self):
        tpe = self.start_file[-1]
        self.start_file = self.start_file[:-1] + \
            {'0': '.mp3', '1': '.m4a', '2': '.mp4','3':''}[tpe]
        if tpe == '0' or tpe == '1':
            while True:
                playsound(self.start_file, block=True)
                sleep(1)
        elif tpe == '2' or  tpe=='3':
            command = '"C:\\Program Files\\VideoLAN\VLC\\vlc.exe"'+self.start_file
            self.__eog = Popen(command)
            self.__v_daśā = True


run()
