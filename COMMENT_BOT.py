import time
import pyautogui as pg
counter  = 772
for i in range(999):
    pg.click(x=136, y=236)
    time.sleep(1)
    pg.typewrite("This is my " )
    pg.typewrite(str(counter))
    pg.typewrite(" comment, So good luck repliers. Comment Written #SHOUTOUT #PLEASE")
    time.sleep(1)
    pg.click(x=867, y=277)
    time.sleep(3)
    print(counter )
    time.sleep(1)
    counter += 1