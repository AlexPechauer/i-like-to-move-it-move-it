

"""
Make a virtual environment, do a pip install pyautogui

Activates by
1: Putting cursor at top of screen where y = 0,
2: By not moving mouse for SET_TIME.

Program runs continuously with terminal window showing "On." Program will crash
when cursor location in top left corner, (0,0), or computer is locked.
Set pyautogui.FAILSAFE = False to disable. Program would then persist after computer
is locked
"""

import pyautogui, time

pyautogui.FAILSAFE = True

SET_TIME = 150

# print("On")

def move_click(num):
  x, y = pyautogui.position()
  pyautogui.moveTo(x+num, y)
  if(y==0):
    pyautogui.click()
    time.sleep(.25)

while(True):

  x, y = pyautogui.position()
  time.sleep(.25) #Required to record that the cursor has moved.
  x2, y2 = pyautogui.position()

  # print('x: ',x, 'y: ', y)

#left x 1080 to 0
#left y 1410 509

#right x 1 to 1919
#right y 1080 0
  ###Main program driver####
  if(y==0):
    move_click(1)
    time.sleep(.25) #Creates 50% duty cycle of cursor movement.
    move_click(-1)

  start_time = time.time()
  stop_watch = 0
  while(y==y2 and y!=0):
    new_time = time.time()
    stop_watch = new_time - start_time
    if(stop_watch >= SET_TIME):
      pyautogui.moveTo(654, 0)
      break
    x, y = pyautogui.position()
    time.sleep(.25)
    x2, y2 = pyautogui.position()

  end_time = time.time()