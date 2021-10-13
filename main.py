import pyautogui
import os


Desktoppath = os.path.join((os.environ['USERPROFILE']),'Desktop')
print(Desktoppath)

# print(os.getcwd())
sspath = os.path.join(Desktoppath,'Screenshot')
print(sspath)
os.mkdir(sspath)
