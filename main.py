import pyautogui as pg
import webbrowser as wb
from os import path
import sys



def resourse_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath('.')
    
    return path.join(base_path, relative_path)

def start() -> None: 
    pg.alert('Программа для автоматического входа на платформу\nНеобходимо после ввода логина и пароля подождать несколько секунд (8-10) и не трогать мышь и клавиатуру.', button='Перейти')
    login = pg.prompt('Введите ваш логин:')
    password = pg.prompt('Введите пароль (как правило это 4 цифры):')
    wb.open('http://mars.algoritmika.org')
    pg.sleep(2)
    exit_account()
    pg.sleep(1)
    sign_account(login, password)

def exit_account() -> None:
    log_in = pg.locateCenterOnScreen(resourse_path('img\\swap.png'))
    if log_in:
        pg.moveTo(log_in[0], log_in[1], duration=0.5)
        pg.click()
        pg.sleep(1)
        logout = pg.locateCenterOnScreen(resourse_path('img\\logout.png'))
        pg.moveTo(logout[0], logout[1], duration=0.5)
        pg.click()

def sign_account(login, password) -> None: 
    try:
        input_log = pg.locateCenterOnScreen(resourse_path('img\\input_login.png'))
        if input_log:
            pg.moveTo(input_log[0], input_log[1], duration=0.5)
            pg.click()
            pg.write(login, interval=0.2)
            skip = pg.locateCenterOnScreen(resourse_path('img\\next.png'))
            pg.moveTo(skip[0], skip[1], duration=0.2)
            pg.click()
            pg.sleep(1)
            pg.write(password, interval=0.2)
            pg.sleep(0.3)
            sign_in = pg.locateCenterOnScreen(resourse_path('img\\sign_in.png'))
            pg.moveTo(sign_in[0], sign_in[1], duration=0.3)
            pg.click()
    except TypeError:
        pg.alert('Простите, бот не нашел одно из окошек :(')
    finally:
        pg.sleep(0.5)
        pg.alert('Бот завершил свою работу.')

if __name__ == '__main__':
    start()
