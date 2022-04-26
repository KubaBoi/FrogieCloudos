import subprocess
import pyautogui
import time

class PropertiesOpener:

    @staticmethod
    def open(file):
        subprocess.Popen(f"explorer /select,\"{file}\"")
        time.sleep(1)
        pyautogui.hotkey("alt", "enter")
        time.sleep(0.5)
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.5)
        pyautogui.hotkey("alt", "F4")