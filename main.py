# encoding: utf-8

from time import sleep
import CropAndAnalyze
import os
from playsound import playsound

TarGoldCoin = 450000  # 最小目标金币
TarExlixir = 450000  # 最小目标圣水
TarDarkElixirDrill = 0  # 最小目标暗黑重油
SpoilsLoc = (100, 125, 450, 320)  # 进攻时可获取战利品的位置
NextLoc = ("2186", "774")  # 进攻时搜索下一个对手的按钮的坐标
EndLoc = ("210", "797")  # 进攻时结束战斗的坐标(目前暂时没有开发相关功能)
AccessToken = ""  # 百度数字识别APIToken


def YouHaveFindIt():
    print(r'找到目标')
    playsound('FindIt.mp3')


def FirstRun():
    os.system("adb devices")


def check(SpoilsDic, MinGoldCoin=0, MinExlixir=0, MinDarkElixirDrill=0):
    if SpoilsDic["金币"] >= MinGoldCoin and SpoilsDic["圣水"] >= MinExlixir \
            and SpoilsDic["黑油"] >= MinDarkElixirDrill \
            or (MinGoldCoin + MinExlixir) <= (SpoilsDic["金币"] + SpoilsDic["圣水"]):
        return True
    else:
        return False


FirstRun()

while True:
    os.system("adb exec-out screencap -p > screen.png")
    CropAndAnalyze.CropImage("screen.png", SpoilsLoc)
    Base64Str = CropAndAnalyze.LocalImageToBase64("Spoils.png")
    SpoilsDic = CropAndAnalyze.AnalyzeImage(AccessToken, Base64Str)
    if check(SpoilsDic, TarGoldCoin, TarExlixir, TarDarkElixirDrill):
        YouHaveFindIt()
        op = input("Do You Want Attack it?(y/n)")
        if op == 'y' or op == 'Y':
            break
        else:
            print("We will find the next one")
    os.system("adb shell input tap " + NextLoc[0] + ' ' + NextLoc[1])
    sleep(4)
