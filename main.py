import pyautogui
import os
import datetime
import time

Desktoppath = os.path.join((os.environ['USERPROFILE']),'Desktop')
# print(Desktoppath) 
sspath = os.path.join(Desktoppath,'Screenshot')
# print(sspath)

def ssfolder():

    if os.path.isdir(sspath) == True:
        print("ssfolder  exists")
    else:
        os.mkdir(sspath)
        print("ssfolder created")

ssfolder()



def datefolder():
    
    datefoldername = time.strftime("%d-%m-%Y")
    datefolderpath =  os.path.join(sspath,datefoldername)
    # print(datefolderpath)


    if os.path.isdir(datefolderpath) == True:
        print("datefolder exists")
    
    else:
        os.mkdir(datefolderpath)
        print("datefolder created")

datefolder()
