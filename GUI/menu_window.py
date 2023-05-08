import customtkinter as CTk
import tkinter
from tkinter import *
from module.gsml.constants import *
from .add_ball_window import WindowAddBall
import screeninfo
from sys import exit

class CreateGUI(CTk.CTk):
    def __init__(self):
        self.Logger = False
        self.Trajectories = False
        self.Helper = False
        self.FPS = True
        self.Pause = False
        self.ControlMode = False
        self.objects = []
        self.monitors_val = None
        self.fullscreen = False
        self.custom_height = None
        self.custom_width = None
        

        def saves():
            self.FPS = fps.get() if fps.get() == '' else 61
            self.Helper = helper.get()
            self.Logger = log.get()
            self.Pause = pause.get()
            self.Trajectories = track.get()
            self.ControlMode = control.get()
            self.custom_height = width_val.get()
            self.custom_width = height_val.get()
        
        def push():
            saves()
            self.destroy()
        
        def enhancedFunction():
            if enhfun.get():
                self.geometry('500x400')
            else:
                self.geometry('250x400')
            
        def full_screen_get():
            self.fullscreen = fullscreen_val.get()
            if self.fullscreen:
                monitor_value.pack(pady=5)
                width_val.place_forget()
                height_val.place_forget()
            else:
                monitor_value.pack_forget()
                width_val.place(relx=0.71, rely=0.7, anchor=tkinter.CENTER)
                height_val.place(relx=0.29, rely=0.7, anchor=tkinter.CENTER)
            
        def addBall():
            self.objects = WindowAddBall()

        def find_screens():
            screens = screeninfo.get_monitors()
            screen_names = []
            for i, screen in enumerate(screens):
                screen_name = f"{i+1}) {screen.width}x{screen.height}"
                screen_names.append(screen_name)

            monitor_value.configure(values=screen_names)
            
        def combobox_callback(choise):
            self.monitors_val = choise

        super().__init__()

        self.protocol("WM_DELETE_WINDOW", exit)

        self.geometry('250x400')
        self.resizable(False, False)
        self.wm_geometry("+%d+%d" % (((self.winfo_screenwidth()) / 2)-200,
                                    ((self.winfo_screenheight()) / 2)-250))
        self.title('Настройки')


        button = CTk.CTkButton(master=self, text="Запустить", command=push)
        button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        button_add = CTk.CTkButton(master=self, text="Добавить", command=addBall)
        button_add.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        option = CTk.CTkFrame(self, width=230, height=250)
        option.pack(pady=5, )

        fps = CTk.CTkEntry(master=option,
                            placeholder_text="FPS",
                            width=50,
                            height=25,
                            border_width=2,
                            corner_radius=10)
        fps.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)

        log = CTk.CTkSwitch(master=option, text="Логгер", command=saves,
                                 onvalue=True, offvalue=False)
        log.place(relx=0.1, rely=0.20)

        helper = CTk.CTkSwitch(master=option, text="Подсказки", command=saves,
                                 onvalue=True, offvalue=False)
        helper.place(relx=0.1, rely=0.30)

        pause = CTk.CTkSwitch(master=option, text="Пауза в начале", command=saves,
                                 onvalue=True, offvalue=False)
        pause.place(relx=0.1, rely=0.40)

        track = CTk.CTkSwitch(master=option, text="Траектория", command=saves,
                                 onvalue=True, offvalue=False)
        track.place(relx=0.1, rely=0.50)

        control = CTk.CTkSwitch(master=option, text="Контроль управления", command=saves,
                                 onvalue=True, offvalue=False)
        control.place(relx=0.1, rely=0.60)

        fullscreen_val = CTk.CTkSwitch(master=option, text="Полн. экран", command=full_screen_get,
                                 onvalue=True, offvalue=False)
        fullscreen_val.place(relx=0.1, rely=0.70)

        enhfun = CTk.CTkSwitch(master=option, text="Доп. настройки", command=enhancedFunction,
                                 onvalue=True, offvalue=False)
        enhfun.place(relx=0.1, rely=0.80)

        height_val = CTk.CTkEntry(master=self,
                            placeholder_text="Высота",
                            width=100,
                            height=25,
                            border_width=2,
                            corner_radius=10)
        height_val.place(relx=0.29, rely=0.7, anchor=tkinter.CENTER)

        width_val = CTk.CTkEntry(master=self,
                            placeholder_text="Ширина",
                            width=100,
                            height=25,
                            border_width=2,
                            corner_radius=10)
        width_val.place(relx=0.71, rely=0.7, anchor=tkinter.CENTER)


        monitor_value = CTk.CTkComboBox(master=self, variable='', values=[],
                                        command=combobox_callback, width=150)
        find_screens()
        monitor_value.set('Выберите экран')

    
    def get(self):
        return self.Logger, self.Trajectories, self.FPS, self.Pause, self.ControlMode, self.objects, self.monitors_val, self.custom_height, self.custom_width, self.fullscreen