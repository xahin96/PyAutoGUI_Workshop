import pyautogui
import time

print("Move the mouse to the desired position and wait for 5 seconds...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Mouse position: ({x}, {y})")
