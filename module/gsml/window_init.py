import pygame
from .constants import *
from .physics import get_offset
from .renderGUI import *
from .physics import *
from .controller import smooth_control, events
from .monitor import get_monitors

class Window:

    def __init__(self, height=None, width=None, Logger=False, Trajectories=False, FPS=None, fullsc=True,
                 Pause=False, ControlMode=False, objects=None, monitor='1'):
        if FPS != int:
            FPS = 61
        self.fullscreen = fullsc
        self.fps = FPS
        if self.fullscreen:
            self.monitor = get_monitors(int(monitor[0]))
            self.win_width = self.monitor[0]
            self.win_height = self.monitor[1]
        else:
            self.win_width = int(width)
            self.win_height = int(height)
        self.logging = Logger
        self.pause = Pause
        self.flag = True
        self.controlmode = ControlMode
        self.track = Trajectories
        self.savelog = []
        self.ticks = 0
        self.objects = objects
        self.prerender = False

        pygame.init()
        text_prerender()
        B.clear()
        T.clear()
        if self.objects in [None, (), []]:
            custom_pos()
        else:
            for object in self.objects:
                B.append(Ball(x=object[1], y=object[2], col=object[7], r=object[3], mass=object[4], vx=object[5], vy=object[6]))


        self.clock = pygame.time.Clock()

        if self.fullscreen:
            self.sc = pygame.display.set_mode((0,0), pygame.FULLSCREEN, display=int(monitor[0])-1)
        else:
            self.sc = pygame.display.set_mode((self.win_width, self.win_height))


    def gameloop(self):
        while self.flag:
            self.update()
        

    def update(self):

        ofs_x, ofs_y = get_offset(B, self.win_width, self.win_height)

        self.sc.fill(darkblue)
        self.calcupdate(ofs_x, ofs_y)
        self.renderupdate(ofs_x, ofs_y)

        #Обновление дисплея
        pygame.display.update()
        self.clock.tick(int(self.fps))


    def calcupdate(self, ofs_x: int, ofs_y: int):

        #Обработка ивентов
        self.fps, self.win_height, self.win_width, self.logging, self.pause, self.flag, self.controlmode, self.track, self.prerender = events(self.fps, self.win_height, self.win_width, self.logging,
                                                                                                                                            self.pause, self.flag, self.controlmode, self.track, self.prerender)
        if self.flag:
            #Ведение логов
            if not self.pause:
                self.ticks += 1/FPS
                if self.logging:
                    self.savelog.append([Ball.feats(B[2])[4], Ball.feats(B[2])[5], self.ticks, Ball.feats(B[2])[0], Ball.feats(B[2])[1]])
                
            smooth_control(self.controlmode)

            #Математический расчёт
            prerender(self.sc, ofs_x, ofs_y, self.pause, self.track, self.win_width, self.win_height)


    def renderupdate(self, ofs_x: int, ofs_y: int):
        if self.flag:
            #Рендер текста
            rendertext_active(self.sc, Ball.feats(B[2])[7], "FPS: {:.1f}".format(self.clock.get_fps()),
                            self.logging, self.win_width, self.win_height, self.ticks)

            #Рендер Объектов
            visBalls(self.sc, B, ofs_x, ofs_y, self.win_width, self.win_height)

            #Рендер GUI элементов
            rendergui(self.sc, ofs_x, ofs_y, self.win_width, self.win_height)
    
    def quit(self):
        pygame.quit()
