import pyautogui

pyautogui.size() #(1280, 720) returns screen resolution

width, height = pyautogui.size()

width #1280

height #720

pyautogui.position() # (324, 270) Tell the mouse position

pyautogui.moveTo(10, 10) # move mouse position to x=10, y=10

# pyautogui.moveTo(10,10, duration=2)
# move mouse position to x=10, y=10 in 2s

# pyautogui.mouseRel(200, 0, duration=2)
# move mouse position relative to original position

# pyautogui.click(339, 38)
# pyautogui.rightClick(339, 38)
# pyautogui.middleClick(339, 38)
# mouse click action at x=339, y=38 if there are no x and y, current position will be click

# pyautogui.doubleClick(339, 39)
# mouse double click action

# pyautogui.displayMousePosition()
# display Mouse position and color
