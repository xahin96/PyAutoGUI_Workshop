import pyautogui
import time
import subprocess

# Open the Whiteboard app
subprocess.Popen(["open", "-a", "Whiteboard"])

# Wait for the app to open
time.sleep(5)

# Function to draw each letter
def draw_A(start_x, start_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(start_x, start_y - 50, duration=0.5, button='left')  # Left vertical
    pyautogui.dragTo(start_x + 30, start_y - 50, duration=0.5, button='left')  # Right diagonal
    pyautogui.dragTo(start_x + 60, start_y, duration=0.5, button='left')  # Right vertical
    pyautogui.moveTo(start_x + 15, start_y - 25)
    pyautogui.dragTo(start_x + 45, start_y - 25, duration=0.5, button='left')  # Middle bar

def draw_U(start_x, start_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(start_x, start_y - 50, duration=0.5, button='left')  # Left vertical
    pyautogui.dragTo(start_x + 30, start_y - 50, duration=0.5, button='left')  # Right vertical
    pyautogui.dragTo(start_x + 30, start_y, duration=0.5, button='left')  # Bottom horizontal

def draw_T(start_x, start_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(start_x + 40, start_y, duration=0.5, button='left')  # Top horizontal
    pyautogui.moveTo(start_x + 20, start_y)
    pyautogui.dragTo(start_x + 20, start_y - 50, duration=0.5, button='left')  # Vertical

def draw_O(start_x, start_y):
    pyautogui.moveTo(start_x + 20, start_y)
    pyautogui.dragTo(start_x + 20, start_y - 40, duration=0.5, button='left')  # Left
    pyautogui.dragTo(start_x + 40, start_y - 40, duration=0.5, button='left')  # Top
    pyautogui.dragTo(start_x + 40, start_y, duration=0.5, button='left')  # Right
    pyautogui.dragTo(start_x + 20, start_y, duration=0.5, button='left')  # Bottom

def draw_M(start_x, start_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(start_x, start_y - 50, duration=0.5, button='left')  # Left vertical
    pyautogui.dragTo(start_x + 10, start_y - 40, duration=0.5, button='left')  # Left diagonal
    pyautogui.dragTo(start_x + 20, start_y - 50, duration=0.5, button='left')  # Middle vertical
    pyautogui.dragTo(start_x + 30, start_y - 40, duration=0.5, button='left')  # Right diagonal
    pyautogui.dragTo(start_x + 40, start_y - 50, duration=0.5, button='left')  # Right vertical
    pyautogui.dragTo(start_x + 40, start_y, duration=0.5, button='left')  # Right bottom

def draw_E(start_x, start_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(start_x, start_y - 50, duration=0.5, button='left')  # Left vertical
    pyautogui.dragTo(start_x + 30, start_y, duration=0.5, button='left')  # Top horizontal
    pyautogui.dragTo(start_x + 30, start_y - 25, duration=0.5, button='left')  # Middle horizontal
    pyautogui.dragTo(start_x + 30, start_y - 50, duration=0.5, button='left')  # Bottom horizontal

# Starting positions for each letter
start_x = 570
start_y = 315
spacing = 70

# Draw the word "AUTOMATE"
draw_A(start_x, start_y)
start_x += 60
draw_U(start_x, start_y)
start_x += 60
draw_T(start_x, start_y)
start_x += 60
draw_O(start_x, start_y)
start_x += 60
draw_M(start_x, start_y)
start_x += 60
draw_A(start_x, start_y)
start_x += 60
draw_T(start_x, start_y)
start_x += 60
draw_E(start_x, start_y)
