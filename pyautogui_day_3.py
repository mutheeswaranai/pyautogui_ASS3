import pyautogui
import pyperclip
import time
import re
from datetime import datetime

# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Current date and time
now = datetime.now()

date = now.strftime("%d-%m-%Y")
time_now = now.strftime("%H:%M:%S")

print("Date :", date)
print("Time :", time_now)


# --------------------------------------------------
# STEP 1 - OPEN CHROME
# --------------------------------------------------

print("Step 1: Opening Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome", interval=0.05)
pyautogui.press("enter")

time.sleep(4)


# --------------------------------------------------
# STEP 2 - OPEN ACCUWEATHER
# --------------------------------------------------

print("Step 2: Opening AccuWeather...")

pyautogui.hotkey("ctrl", "l")

pyautogui.write(
    "https://www.accuweather.com/en/in/chennai/206671/current-weather/206671",
    interval=0.01
)

pyautogui.press("enter")

time.sleep(7)


# --------------------------------------------------
# STEP 3 - COPY WEATHER PAGE
# --------------------------------------------------

print("Step 3: Copying weather information...")

# Select all webpage text
pyautogui.hotkey("ctrl", "a")
time.sleep(1)

pyautogui.hotkey("ctrl", "c")
time.sleep(2)


# Get copied text
weather_text = pyperclip.paste()

print("\nWeather text copied successfully.")


# --------------------------------------------------
# STEP 4 - FIND REALFEEL
# --------------------------------------------------

print("Step 4: Finding RealFeel...")

# Example text:
# RealFeel® 37°
# RealFeel 37°

match = re.search(
    r"RealFeel(?:®)?\s*([0-9]+)\s*°",
    weather_text,
    re.IGNORECASE
)

if match:
    realfeel = match.group(1) + "°C"
    print("RealFeel :", realfeel)

else:
    print("RealFeel not found!")
    print("Please check copied weather text.")

    # Stop program
    exit()


# --------------------------------------------------
# STEP 5 - OPEN EXCEL
# --------------------------------------------------

print("Step 5: Opening Excel...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("excel", interval=0.05)
pyautogui.press("enter")

time.sleep(5)


# --------------------------------------------------
# STEP 6 - OPEN BLANK WORKBOOK
# --------------------------------------------------

print("Step 6: Opening Blank Workbook...")

# Excel start screen -> Blank Workbook
pyautogui.press("enter")

time.sleep(5)


# --------------------------------------------------
# STEP 7 - CREATE NEW SHEET
# --------------------------------------------------

print("Step 7: Creating new sheet...")

# Shift + F11 creates a new worksheet
pyautogui.hotkey("shift", "f11")

time.sleep(2)


# --------------------------------------------------
# STEP 8 - ENTER HEADERS
# --------------------------------------------------

print("Step 8: Entering weather data...")

# A1 = Date
pyautogui.write("Date")
pyautogui.press("tab")

# B1 = Time
pyautogui.write("Time")
pyautogui.press("tab")

# C1 = RealFeel
pyautogui.write("RealFeel")

# Move to A2
pyautogui.press("home")
pyautogui.press("down")


# --------------------------------------------------
# STEP 9 - ENTER VALUES
# --------------------------------------------------

# A2 = Date
pyautogui.write(date)
pyautogui.press("tab")

# B2 = Time
pyautogui.write(time_now)
pyautogui.press("tab")

# C2 = RealFeel
pyautogui.write(realfeel)

time.sleep(4)

# --------------------------------------------------
# STEP 10 - SAVE EXCEL
# --------------------------------------------------

print("Step 10: Saving Excel file...")

pyautogui.hotkey("fn", "f12")  # Save As

time.sleep(2)


# File name
filename = (
    "Weather_"
    + date
    + "_"
    + time_now.replace(":", "-")
    + ".xlsx"
)

pyautogui.write(filename, interval=0.03)

time.sleep(1)

pyautogui.press("enter")

time.sleep(5)

# Handle possible Excel confirmation
pyautogui.press("enter")

time.sleep(3)


print("--------------------------------")
print("Weather saved successfully!")
print("Date     :", date)
print("Time     :", time_now)
print("RealFeel :", realfeel)
print("File     :", filename)
print("--------------------------------")