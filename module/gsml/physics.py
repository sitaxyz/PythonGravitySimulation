from .constants import B, T, Walls
from .ball import *
from .point import Point
from pygame import draw

# Функция расчета физики для рендера (математический пре-рендер)
def prerender(screen, ofs_x, ofs_y, pause, track, width, height):
    if not pause:
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                B[i].force(j, B)
            B[i].move(Walls, width, height, ofs_x, ofs_y)
    for t in T:
        try:
            t.vis(screen, ofs_x, ofs_y, track)
        except IndexError:
            pass

# Функция нахождения центра масс для централизации камеры
def get_offset(B, width, height):
    sum_x, sum_y = 0, 0
    m = 0
    for ball in B:
        sum_x += ball.x * ball.mass
        sum_y += ball.y * ball.mass
        m += ball.mass
        
    return sum_x / m - width // 2, sum_y / m - height // 2

# Функция рендера всех объектов
def visBalls(screen, B, ofs_x, ofs_y, width, height):
    for ball in B:
        if 0 < ball.x - ofs_x < width and -20 < ball.y - ofs_y < height:
            draw.circle(screen, ball.col, (round(ball.x - ofs_x),
                                           round(ball.y - ofs_y)), ball.r)
        T.append(Point(ball.x, ball.y, ball.col))