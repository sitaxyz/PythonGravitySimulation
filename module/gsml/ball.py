from numba import njit
import numpy as np
from .constants import *

#Класс объектов с их логикой
class Ball:
    #ООП функция для создания объектов
    def __init__(self, x, y, col, r = 4, mass = 4, vx = 0, vy = 0):
        self.x = x  
        self.y = y
        self.r = r
        self.col = col
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.fuel = 0
        self.speed = 1
    
    #Функция для возвращения характеристик объекта в виде кортежа
    def feats(self):
        return self.x, self.y, self.r, self.col, self.vx, self.vy, self.mass, self.fuel, self.speed

    #Функция для выведения скорости спутника относительно точки отсчёта
    def font(self):
        return f'Скорость: {round((self.vx**2+self.vy**2)**0.5, 2)} км/c'

    def speed_reduction(self):
        self.speed -= 0.01 if self.speed >= 0.01 else 0

    def speed_boost(self):
        self.speed += 0.01 if self.speed <= 1 else 0


    #Функции для управления, со сменой режима управления 
    def move_down(self):
        self.vy += 0.01 * self.speed
        self.fuel += 2.5 / FPS * self.speed

    def move_up(self):
        self.fuel += 2.5 / FPS * self.speed
        self.vy -= 0.01 * self.speed

    def move_left(self):
        self.vx -= 0.01 * self.speed
        self.fuel += 2.5 / FPS * self.speed

    def move_right(self):
        self.vx += 0.01 * self.speed
        self.fuel += 2.5 / FPS * self.speed


    #функция для расчёта физики
    def force(self, ind, B):
        ox = B[ind].x
        oy = B[ind].y
        m = B[ind].mass
        if m < 0.01 and self.mass < 0.01:
            return 0
        vx = B[ind].vx
        vy = B[ind].vy
        dist = np.sqrt((self.x - ox)**2 + (self.y - oy)**2)
        min_dist = (self.r + B[ind].r) * ResDist
        f = 0
        m_relative = self.mass / B[ind].mass
        if dist <= min_dist:
            newVx = (vx * m + self.vx * self.mass) / (m + self.mass)
            newVy = (vy * m + self.vy * self.mass) / (m + self.mass)
            self.vx = (newVx + k * self.vx) / (k + 1)
            B[ind].vx = (newVx + k * B[ind].vx) / (k + 1)
            self.vy = (newVy + k * self.vy) / (k + 1)
            B[ind].vy = (newVy + k * B[ind].vy) / (k + 1)
            f -= antiG * min(abs(min_dist - dist), min(m, self.mass) * 3)
        else:
            f += min(self.mass * B[ind].mass * G  / (dist ** zg), G / 10)
            mf = MagnConst * self.mass / (dist ** zm)
            f += mf
        fx = f * ((ox - self.x) / dist)
        fy = f * ((oy - self.y) / dist)
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax
        self.vy += ay
        B[ind].vx -= ax * m_relative
        B[ind].vy -= ay * m_relative


    #Функция отскока или отзеркаливания объекта
    def move(self, Walls, WIN_WIDTH, WIN_HEIGHT, ofs_x, ofs_y):
        if Walls:
            x = self.x - ofs_x
            y = self.y - ofs_y
            if x <= 0 and self.vx < 0:
                if Mirror:
                    self.vx = -self.vx
                else:
                    self.x += WIN_WIDTH
                self.vx, self.vy = self.v_norm(self.vx, self.vy)
            if x >= WIN_WIDTH and self.vx > 0:
                if Mirror:
                    self.vx = -self.vx
                else:
                    self.x -= WIN_WIDTH
                self.vx, self.vy = self.v_norm(self.vx, self.vy)
            if y <= 0 and self.vy < 0:
                if Mirror:
                    self.vy = -self.vy
                else:
                    self.y += WIN_HEIGHT
                self.vx, self.vy = self.v_norm(self.vx, self.vy)
            if y >= WIN_HEIGHT and self.vy > 0:
                if Mirror:
                    self.vy = -self.vy
                else:
                    self.y -= WIN_HEIGHT
                self.vx, self.vy = self.v_norm(self.vx, self.vy)
            
        self.x += self.vx
        self.y += self.vy


    @staticmethod
    @njit
    def v_norm(vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        if v > max_speed:
            vx = max_speed * (vx / v)
            vy = max_speed * (vy / v)
        return vx, vy
    
def custom_pos():
    '''Сюда можно добавлять объекты по правилу: x, y, col, r, vx, vy, mass '''
    B.append(Ball(200, 500, GREEN, r=15, mass=198))
    B.append(Ball(200, 200, GREY, r=4, mass=2.5, vx=(198 * G / 300)**0.5))
    B.append(Ball(200, 475, YELLOW, r=1, mass=2.3 * 10 ** -20, vx=(198 * G / 25)**0.5))