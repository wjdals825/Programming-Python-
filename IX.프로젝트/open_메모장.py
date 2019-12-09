import pyautogui as pag
import time

if __name__ == '__main__':
    pag.moveTo (18,1060)
    pag.click()
    pag.press("hangul")
    pag.typewrite("apahwkd")
    pag.press("enter")
    time.sleep(2)
    pag.typewrite("hello world")
    pag.press("enter")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    pag.hotkey('ctrl','s')
    time.sleep(1)
    pag.press("hangul")
    pag.typewrite("C:\\Users\\LG\\")
    pag.press("hangul")
    pag.typewrite("vkdlTjsdnjfem")
    pag.press("enter")



    #메모장 프로그램 실행하지
    #hello world 치자
    #두번 내리자
    #반갑구나 세상아 치자
    #저장하자
    #파이썬월드