import pyautogui
from time import sleep
from random import randint

def move_mouse():
    screen_width, screen_height = pyautogui.size()
    x, y = randint(300, screen_width - 300), randint(300, screen_height - 300)
    current_x, current_y = pyautogui.position()
    speed_x = randint(40, 80)
    if x < current_x:
        speed_x = -speed_x
    speed_y = round(speed_x * (current_y - y) / abs(current_x - x))
    while current_x not in range(x - abs(speed_x), x + abs(speed_x)) and current_y not in range(y - abs(speed_y), y + abs(speed_y)):
        current_x += speed_x
        current_y += speed_y
        pyautogui.moveTo(current_x, current_y)

# example usage
if __name__ == '__main__':
    while True:
        move_mouse()
        sleep(randint(1, 3))