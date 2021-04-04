'''
Since the coords for PYautoGUI differ for each OS, I created this program to easily find coords.
'''
import pyautogui, time
print("Press \"CTRL + C\" when you want to quit the program")
while True:
    print(pyautogui.position())
    time.sleep(1.5)