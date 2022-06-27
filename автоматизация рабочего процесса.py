import threading
import time

import pyautogui as pg

work = True


def check_working():
    global work
    while work:
        if pg.position() == pg.Point(x=0, y=0):
            work = False
            break


def working():
    while work:

        time.sleep(0.5)
        pg.doubleClick(x=761, y=307)                    #переход на первый акт
        if not work:
            break
        time.sleep(1)
        pg.doubleClick(x=601, y=537)
        #кнопка файлы

        if not work:
            break
        time.sleep(0.5)
        pg.click(x=428, y=619)                  #переход на Pdf
        if not work:
            break
        time.sleep(3)
        pg.doubleClick(x=1910, y=971)    #пролистали страницу вниз
        if not work:
            break
        time.sleep(3)
        pg.click(x=307, y=25)               #переход обратно к актам
        if not work:
            break
        time.sleep(0.5)
        pg.click(x=737, y=22)           #закрытие страницы с файлами
        if not work:
            break
        time.sleep(0.5)
        pg.click(x=348, y=878)      #Нажатие кнопки "Подтвердить"
        if not work:
            break
        time.sleep(0.5)
        pg.click(x=895, y=611)          #нажатие кнопки "Да"
        if not work:
            break
        time.sleep(0.5)
        pg.click(x=989, y=885)          #закрытие акта сверки
        if not work:
            break
        time.sleep(1)                   #обновление страницы
        pg.click(x=284, y=999)
        if not work:
            break
        time.sleep(1)
        pg.click(x=421, y=632)


def main():
    pg.FAILSAFE = False         #дает возможность останавливать программу

    time.sleep(2)
    pg.click(x=771, y=1041)

    t1 = threading.Thread(target=check_working)
    t2 = threading.Thread(target=working)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()