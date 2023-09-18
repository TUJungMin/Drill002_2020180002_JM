from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x = 0
y = 90
angle = 0
center_x = 400
center_y = 345

while True:
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 5
        delay(0.01)

    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 5
        delay(0.01)

    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 5
        delay(0.01)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 5
        delay(0.01)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 5
        delay(0.01)

    while (angle < 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = 400 + math.cos(math.radians(angle)) * 255
        y = 355 + math.sin(math.radians(angle)) * 255
        character.draw_now(x, y)
        angle += 5
        delay(0.01)
    angle = 0  # 들여쓰기가 올바르게 수정되었습니다.

close_canvas()
