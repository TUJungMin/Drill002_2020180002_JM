from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 255
radius = 255  
angle = 0  

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    
   
    x = 400 + math.cos(math.radians(angle)) * radius
    y = 255 + math.sin(math.radians(angle)) * radius
    
    character.draw_now(x, y)
    
    angle += 1  
    
    delay(0.01)
    if(angle == 360):
        x, y = 400, 90
        move_x = 1  # x축 이동 속도
        move_y = 0  # y축 이동 속도

        while True:
            clear_canvas_now()
            grass.draw_now(400, 30)
    
            # x축 음의 방향으로 이동
            x += move_x
    
            # 맵 끝에 도달하면 y축으로 이동
            if x > 799:
                x = 799
                move_x = 0
                move_y = 1
            y +=move_y
            # y축 맨 위로 도달하면 x축 양의 방향으로 이동
            if y > 550:
                y = 550
                move_x = -1
                move_y = 0
            x += move_x
            if x < 0:
             x = 0
             move_x = 0
             move_y = -1
            y += move_y
            character.draw_now(x, y)
    
            delay(0.01)

close_canvas()
