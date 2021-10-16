import pyautogui
import os
import time

# For getting desktop path
Desktoppath = os.path.join((os.environ['USERPROFILE']),'Desktop')
# print(Desktoppath) 

# For get Screenshot folder path
sspath = os.path.join(Desktoppath,'Screenshot')
# print(sspath)

# For make folder named Screenshot in desktop
def ssfolder():
    if os.path.isdir(sspath) == True:
        # print("ssfolder  exists")
        pass
    else:
        os.mkdir(sspath)
        # print("ssfolder created")


# for get datewise folder path
datefoldername = time.strftime("%d-%m-%Y")
datefolderpath =  os.path.join(sspath,datefoldername)
# print(datefolderpath)


# for make datewise folder in screenshot folder
def datefolder():
    if os.path.isdir(datefolderpath) == True:
        # print("datefolder exists")
        pass
    else:
        os.mkdir(datefolderpath)
        # print("datefolder created")


# for each image name with time
imagename = time.strftime(r"%H-%M-%S.png")
# print(imagename)

# for each image path
imagepath = os.path.join(datefolderpath,imagename)
# print(imagepath)

# for create screenshot in store in spacif location
def makescreenshot():
    pyautogui.screenshot(imagepath)




ssfolder()
datefolder()
makescreenshot()
