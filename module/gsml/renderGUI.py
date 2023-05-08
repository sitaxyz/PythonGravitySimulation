from .constants import WHITE, RED, B
from pygame import font, draw
from .ball import Ball
import datetime

def seconds_to_date(seconds):
    date = datetime.datetime.fromtimestamp(seconds * 127000)
    return date.strftime('%Y:%m:%d:%H:%M:%S')

#На какой высоте
def option(satelite, moon, earth):
    dist_e = ((Ball.feats(earth)[0]-Ball.feats(satelite)[0])**2+(Ball.feats(earth)[1] - Ball.feats(satelite)[1])**2)**0.5
    dist_m = ((Ball.feats(moon)[0]-Ball.feats(satelite)[0])**2+(Ball.feats(moon)[1] - Ball.feats(satelite)[1])**2)**0.5

    if Ball.feats(earth)[6]/dist_e > Ball.feats(moon)[6]/dist_m:
        return f'до Земли: {round(dist_e*425-6374, 2)} км'
    else:
        return f'до Луны: {round(dist_m*425-1700, 2)} км'

def text_prerender():
    global Helper0, Helper1, Helper2, Helper3, Helper4, Helper5, Helper6, Helper7, f1, f2
    #Создание текста
    f1 = font.Font(None, 29)
    f2 = font.Font(None, 22)
    Helper7 = f2.render('Горячие клавиши:', 1, WHITE)
    Helper6 = f2.render('Траектория - t', 1, WHITE)
    Helper5 = f2.render('Время(скорость рендера) - +|-', 1, WHITE)
    Helper4 = f2.render('Пауза - Пробел', 1, WHITE)
    Helper3 = f2.render('Режим управления - r', 1, WHITE)
    Helper2 = f2.render('Управление спутником - стрелочки', 1, WHITE)
    Helper1 = f2.render('Выйти - q', 1, WHITE)
    Helper0 = f2.render('Выключить логи(по умолчанию включены) - l', 1, WHITE)


def rendertext_active(screen, fuel, fps, logging: bool, width, height, time):

    text_fuel = f1.render(f'Потрачено топлива: {fuel:.2f} л', 1, WHITE)
    screen.blit(text_fuel, (20, 75))

    text_logoffon = f1.render(f'Логгер: {logging}', 1, WHITE)
    screen.blit(text_logoffon, (width-140, 40))

    text_fps = f1.render(fps, 1, WHITE)
    screen.blit(text_fps, (width-120, 20))
    
    text_time = f1.render(seconds_to_date(time), 1, WHITE)
    screen.blit(text_time, (20, 140))

    text1 = f1.render(f'{Ball.font(B[2])}', 1, WHITE)
    screen.blit(text1, (20, 20))

    text_timeorbit= f1.render(f'Расстояние {option(B[2], B[1], B[0])}', 1, WHITE)
    screen.blit(text_timeorbit, (20, 50))

    text_boost = f1.render(f'Ускорение: {Ball.feats(B[2])[8]:.2f}', 1, WHITE)
    screen.blit(text_boost, (20, 100))

    for i in range(7):
        screen.blit(globals()[f'Helper{i}'], (20, height - 40 - i*30))

#Рендер GUI элементов
def rendergui(screen, ofs_x, ofs_y, width, height):
    draw.aaline(screen, RED, [ Ball.feats(B[2])[0] - ofs_x, Ball.feats(B[2])[1] - ofs_y], [Ball.feats(B[2])[0] + Ball.feats(B[2])[4] - ofs_x, Ball.feats(B[2])[1]+Ball.feats(B[2])[5] - ofs_y], 2)
    draw.rect(screen, (255, 255, 255), (width-250, height-250, 200, 200))
    draw.line(screen, RED, [width-150, height-150], [(Ball.feats(B[2])[4]*10+width-150), (Ball.feats(B[2])[5]*10+height-150)], 3)
