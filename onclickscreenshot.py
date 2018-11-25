from pynput import keyboard
import pyautogui

def on_press(key):
    global i
    try: k = key.char
    except: k = key.name 
    if key == keyboard.Key.esc: return False
    s = str(i)+'.png'
    screenshot = pyautogui.screenshot(s) 
    i = i + 1

i = 0 
lis = keyboard.Listener(on_press=on_press)
lis.start() 
lis.join() 
