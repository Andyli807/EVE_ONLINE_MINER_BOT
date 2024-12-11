import pynput.mouse
from pynput import keyboard
import pyautogui


last_x = 0
last_y = 0
count = 0

def keyboard_release_1(key):
    if(key == pynput.keyboard.Key.ctrl_l):
        x, y = pyautogui.position()
        print(x,y)
        return False
       
    if key == pynput.keyboard.Key.esc:
        return False
    
    with pynput.keyboard.Listener(
                on_release=keyboard_release_1) as listener:
        listener.join()

def keyboard_release_2(key):
    global last_y
    global last_x
    global count
    if(count == 2):
        return False
    if(key == pynput.keyboard.Key.ctrl_l):
        x, y = pyautogui.position()
        count += 1
        if(last_x==0 and last_y==0):
            last_x = x
            last_y = y 
        elif(x-last_x<0 or y-last_y<0):
            if(x-last_y<0):
                print(x,y,0,y-last_y)
            elif(y-last_y<0):
                print(x,y,x-last_x,0)
            else:
                print(x,y,0,0)
            return False
        else:
            print(x,y,x-last_x,y-last_y)
            return False
        
    if key == pynput.keyboard.Key.esc:
        return False
    
    with keyboard.Listener(on_press=keyboard_release_2) as listener:
        listener.join()

def test(bool):
    if(bool == True):
        keyboard_release_1(pynput.keyboard.Key)
    elif(bool == False):
        keyboard_release_2(pynput.keyboard.Key)
    else:
        return 0

    