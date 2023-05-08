from GUI.menu_window import CreateGUI
from module.gsml.window_init import Window
from module.graphics.graph_module import create_graphs
from GUI.confirm_window import ConfirmationWindow

if __name__ == '__main__':
    # Создание GUI-окна
    gui = CreateGUI()
    gui.mainloop()


    #logger, trajectories, fps, pause, control_mode, objects, monitor_val, Height, Width, FullScreen
    # Получение данных из GUI-окна
    Settings = gui.get()

    confirm = ConfirmationWindow('Вы уверены, что хотите запустить симуляцию?')
    while confirm.result:
        # Созадник окна симуляции
        app_window = Window(
        Logger=Settings[0], 
        Trajectories=Settings[1],
        FPS=Settings[2], 
        Pause=Settings[3], 
        ControlMode=Settings[4], 
        objects=Settings[5],
        monitor=Settings[6],
        height=Settings[7],
        width=Settings[8], 
        fullsc=Settings[9]
    )
        # Запуск цикла симуляции
        app_window.gameloop()
        # Закрытие приложения
        app_window.quit()
        # Создание графика при наличии данных
        if app_window.savelog:
            confirm = ConfirmationWindow('Создать графики скорости и историю траектории?')
            if confirm.result:
                create_graphs(app_window.savelog)
        
        confirm = ConfirmationWindow('Вы хотите повторить сценарий?')