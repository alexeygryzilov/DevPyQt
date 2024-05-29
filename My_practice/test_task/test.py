
import pyautogui

def hot():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('taskschd.msc')
    pyautogui.press('enter')

hot()


