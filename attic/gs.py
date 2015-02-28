#!/usr/bin/python

# get terminal size
# from resize(1)
# it does not work quite properly and there is a simpler way
#
# do not use

import os, time, termios
from termios import ICRNL, IUCLC, ICANON, ECHO, CS8, VMIN, VTIME, TCSANOW, TCSADRAIN, TCSAFLUSH

getsize = "\0337\033[r\033[999;999H\0336n\033[18t"
restoreemu = "\0338"
ttyfd = os.open('/dev/tty', os.O_RDWR)

tioorig = termios.tcgetattr(ttyfd)
tio = tioorig[:]

tio[0] &= ~(ICRNL | IUCLC) # iflag
tio[3] &= ~(ICANON | ECHO) # lflag
tio[2] |= CS8 # cflag
tio[6][VMIN] = 6 # cc
tio[6][VTIME] = 1 # cc
termios.tcsetattr(ttyfd, TCSAFLUSH, tio)
os.write(ttyfd, getsize)
x = os.read(ttyfd, len(getsize))
os.write(ttyfd, restoreemu)
termios.tcsetattr(ttyfd, TCSADRAIN, tioorig)
print `x`
