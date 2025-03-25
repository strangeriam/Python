import pyautogui
import time

def f_mouseMove(x, y):
	pyautogui.click(x,y, button='left', duration=0.25)

print('Step 1: Move to Normal')
f_mouseMove(100, 100)
print('Step 2: Read Position')
print(pyautogui.position())

print('Step 3: Wait 2 seconds')
time.sleep(2)

print('Step 4: Move to Active')
f_mouseMove(100, 200)
print('Step 5: Read Position')
print(pyautogui.position())

print('Step 6: Wait 2 seconds')
time.sleep(2)

print('Step 7: Exit')
f_mouseMove(330, 100)
