import keyboard  # parar o loop
import pyautogui  # leitura de tela e captura de screenshot
import win32api  # api windows para clicar
import win32con  # api windows para clicar
import time  # usar o sleep após um click


# função para clicar


def click(x, y):
    # api do windows pois é rápida para clicar
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Descobrir a região da tela através da posição do mouse

'''while True:
    print(pyautogui.position())
    if input() == '1':
        break'''
# rgb(255,219,195) cor do alvo

while not keyboard.is_pressed('c'):
    sc = pyautogui.screenshot(region=(1501, 552, 900, 630))  # print da região onde está o jogo
    width, height = sc.size
    # loop nos pixels da screenshot
    for largura in range(0, width, 10):
        achar = 0
        for altura in range(0, height, 10):
            r, g, b = sc.getpixel((largura, altura))
            if r == 255 and g == 219 and b == 195:  # verificação do rgb
                achar = 1
                click(1501 + largura, 552 + altura)
                time.sleep(0.15)
                break
        if achar == 1:
            break

sc = pyautogui.screenshot(region=(1501, 552, 900, 630))
sc.save('exemplo.png')
