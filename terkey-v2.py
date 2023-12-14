# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2023-04-01 19:37:02.089767
import os
from time import sleep
import socket, struct, time, os, sys

def jalan():
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10 /100)

def tik():
    titik = [
     '   ', '.  ', '.', '..', '...', '...', ',', '[\x1b[1;32m\xe2\x9c\x93\x1b[1;37m]']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;96mPROSESS SEDANG MENG INSTALL  \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.9)


def looding2():
    looding2 = ['[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[/]', '[-]', '[\\]', '[|]', '[\x1b[1;32m\xe2\x9c\x93\x1b[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mTUNGGU SAMBIL NGOPI \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.2)


def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass

    key = "extra-keys = [['KEYBOARD','TAB','exit','HOME','UP','login','PGUP'],['DRAWER','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties', 'w').write(key)
    os.system('termux-reload-settings')


os.system('clear')
print '\t\x1b[1;97mPROGRAM INSTALASI TOMBOL HOME TERMUX \n \t    Code by : Subur Martiana'
ana = raw_input('\x1b[31;1m\n\x1b[37;2mLANJUTKAN TEKAN ENTER \x1b[37;1m : ')
os.system('clear')
looding2()
print ''
tik()
setup()
os.system('clear')
wk = raw_input('\x1b[1;91mSELESAI [\x1b[32;1mCLOSE TEKAN \x1b[33;1m+ \x1b[32;1mENTER\x1b[37;1m]')
os.system('exit')
