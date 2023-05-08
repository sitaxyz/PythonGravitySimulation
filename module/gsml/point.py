from pygame import draw
from .constants import *

#Класс создания точек прошедшей траектории
class Point:
    #Функция для сохранения точек траектории, которые в последующем занесутся в список T
    def __init__(self, x, y, col, r = 1, max_age = Track_time):
        self.age = 0
        self.x = x
        self.y = y
        self.col = col
        self.r = r
        self.max_age = max_age
    #Функция змейкоявидного рендера траектории
    def vis(self, screen, ofs_x, ofs_y, track):
        if track:
            draw.circle(screen, self.col, (round(self.x - ofs_x),
                                           round(self.y - ofs_y)), self.r)
        self.age += 1
        if self.age > self.max_age:
            T.remove(self)
