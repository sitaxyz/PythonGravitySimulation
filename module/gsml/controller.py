import pygame
from .ball import Ball
from .constants import B

#Движение космического аппарата
def smooth_control(controlmode):
    if controlmode:
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP] and pressed[pygame.K_LCTRL]:
            Ball.speed_boost(B[2])
        elif pressed[pygame.K_DOWN] and pressed[pygame.K_LCTRL]:
            Ball.speed_reduction(B[2])
        else:
            if pressed[pygame.K_LEFT]:
                Ball.move_left(B[2])
            elif pressed[pygame.K_RIGHT]:
                Ball.move_right(B[2])

            if pressed[pygame.K_DOWN]:
                Ball.move_down(B[2])
            elif pressed[pygame.K_UP]:
                Ball.move_up(B[2])

def keyevents(i, fps, win_height, win_width, logging, pause, flag, controlmode, track, prerender):
    if i.key == pygame.K_r:
        controlmode = not controlmode
    elif i.key == pygame.K_q:
        flag = not flag
    elif i.key == pygame.K_l:
        logging = not logging
    elif i.key == pygame.K_t:
        track = not track
    elif i.key == pygame.K_SPACE:
        pause = not pause
    elif i.key == pygame.K_MINUS:
        fps -= 5
    elif i.key == pygame.K_EQUALS:
        fps += 5
    elif i.key == pygame.K_p:
        prerender = not prerender
    
    return fps, win_height, win_width, logging, pause, flag, controlmode, track, prerender

def events(fps: int, win_height: int, win_width: int,
           logging: bool, pause: bool, flag: bool,
           controlmode: bool, track: bool, prerender: bool):

    for i in pygame.event.get():
        if i.type == pygame.QUIT or not flag:
            flag = False
        if i.type == pygame.KEYDOWN:
            fps, win_height, win_width, logging, pause, flag, controlmode, track, prerender = keyevents(i,fps, win_height, win_width, logging, pause, flag, controlmode, track, prerender)

    return fps, win_height, win_width, logging, pause, flag, controlmode, track, prerender