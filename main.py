import pyautogui
from time import sleep
from screenshots import Screenshots

# creating a screen capturer
screencap = Screenshots('Kick Ya Chop | Addicting Games - Google Chrome')

# defining each side click positions, using the same cords as the screenshots
right = (screencap.right[0], screencap.right[1])
left = (screencap.left[0], screencap.left[1])

# debug counter for while loop. too afraid of True yet
count = 0
# debug timer
for n in range(3, 0, -1):
    print('Starting in %ss' % n)
    sleep(1)
print('GO!')




# Start at right side. then check for branch at actual side
interval = 0.08
side = 'left'

while (count < 400):
    count += 1
    ss = screencap.get_screenshot(side)
    if ss[0][0][0] < 100:
        if side == 'right':
            side = 'left'
            pyautogui.click(left[0], left[1])
        else:
            side = 'right'
            pyautogui.click(right[0], right[1])
        
    else:
        if side == 'right':
            pyautogui.click(right[0], right[1])
            sleep(interval)
        else:
            pyautogui.click(left[0], left[1])
            sleep(interval)
