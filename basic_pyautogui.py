import pyautogui
import time
import pyscreeze
#pyautogui.FAILSAFE = True  # Enable fail-safe feature
#pyautogui.PAUSE = 0.5  # Set a pause duration between actions   
#print("PyAutoGUI is working!")

#mouse operations
#pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second
#pyautogui.click(100, 100)  # Click the mouse at (100, 100)

#pyautogui.typewrite("Hello, World!")  # Type "Hello, World!"
#pyautogui.rightClick(100, 100)  # Right-click at (100, 100)
#pyautogui.leftClick(100, 100)  # Left-click at (100, 100)
#pyautogui.scroll(-500)  # Scroll up 500 units
#pyautogui.scroll(500)  # Scroll down 500 units
screenshot = pyautogui.screenshot()
screenshot.save("first_screenshot.png")  # Save the screenshot as "first_screenshot.png"