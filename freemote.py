from types import TracebackType
from pynput import keyboard
from pynput.keyboard import Key, Listener
import pyautogui
import csv
import time

# Version 1.5

emote = [""]

emote_dict = {}

# Loads Emotes
with open("freemotes.csv", "r") as f:
    rd = csv.reader(f)

    for row in rd:
        emote_dict[row[0]] = row[1]
        print(f"Emote Loaded: {row[0]}")

    f.close()

# Main func
def on_press(key):
    global emote
    
    if key == Key.shift_r or key == Key.shift_l:
        return
    
    if len(emote) < 1:
        emote = [""]
        return
    
    if emote[0] == ":":
        if key == Key.backspace:
            emote.pop()
            return
    
    if str(key) == "':'":
        if len(emote) == 1:
            emote.clear()
            emote.append(":")
        else:
            emote.append(":")
    elif emote[0] == ":" and emote[-1] == ":" and len(emote) > 2:
        jl = "".join(emote).lower()
        emote = [""]
        print(f"Emote Detected: {jl}")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        try:
            send = emote_dict[jl]
            pyautogui.typewrite(send)
            print(f"Emote Sent: {jl}")
        except:
            print(f"{jl} is not a valid emote")
            pass
    elif emote[0] == ":":
        try:
            if key.char == ";":
                emote.append(":")
            else:
                emote.append(key.char)
        except:
            if key == Key.backspace:
                emote.pop()
            elif key == Key.tab:
                cur = "".join(emote)
                try:
                    fd = [x for x in emote_dict.keys() if x.startswith(cur)][0]
                except:
                    print(f"No emote starts with {cur}")
                    return
                rd = fd[len(cur):len(fd)][:-1]
                pyautogui.typewrite(rd)
                pyautogui.typewrite(":")

# Stuff I don't understand
with Listener(on_press=on_press,on_release=None) as listener:
    listener.join()

# You're probably better off getting Discord Nitro if you're reading this