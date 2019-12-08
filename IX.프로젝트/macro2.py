import pyautogui as pag
import time             #sleep

if __name__ == '__main__':
    pag.moveTo(200, 200, 2)
    pag.click()
    pag.typewrite("happy birthday to seungyeon!", interval=0.5)
    pag.press("enter")
    pag.typewrite("happy birthday to namkyeoung")
    pag.press("hangul")
    pag.typewrite("skaruddk toddlf cnrgkgo!!!")
    pag.press("hangul")
