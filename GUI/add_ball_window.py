
def WindowAddBall():
    import customtkinter as ctk
    import tkinter as tk
    objects = []

    def add_object():
        name = name_entry.get()
        x = float(x_entry.get())
        y = float(y_entry.get())
        r = float(r_entry.get())
        m = float(m_entry.get())
        vx = float(vx_entry.get())
        vy = float(vy_entry.get())
        object_data = [name, x, y, r, m, vx, vy, color]
        objects.append(object_data)
        objects_listbox.insert(ctk.END, object_data)

    def apply_changes():
        root.destroy()
    
    def choose_color():
        from tkinter import colorchooser
        # Создаем главное окно
        colorch = tk.Tk()
        colorch.withdraw()  # Скрываем окно, чтобы оно не мешало
        colorch.title('Выберите цвет')  # Устанавливаем заголовок окна
        colorch.geometry('300x200')  # Устанавливаем размер окна
        colorch.attributes('-topmost', True)  # Устанавливаем окно поверх других окон

        # Опции для окна выбора цвета
        color = colorchooser.askcolor(parent=colorch, color='#000000')[0]
        colorch.destroy()  # Закрываем окно после выбора цвета
        return color

    def show_color_chooser():
        global color
        color = choose_color()

    root = ctk.CTk()
    root.geometry('500x390')
    root.resizable(False, False)
    root.title("Редактор объектов")
    
    objects = []

    frame1 = ctk.CTkFrame(root)
    frame1.pack(side=ctk.LEFT, padx=5, pady=5)

    objects_listbox = tk.Listbox(frame1, width=40, height=16)
    objects_listbox.pack(side=ctk.TOP)

    buttons_frame = ctk.CTkFrame(frame1)
    buttons_frame.pack(side=ctk.TOP)

    plus_button = ctk.CTkButton(buttons_frame, text="+", width=5, command=add_object)
    plus_button.pack(side=ctk.LEFT, padx=5, pady=5)

    minus_button = ctk.CTkButton(buttons_frame, text="-", width=5, command=lambda: objects_listbox.delete(ctk.ACTIVE))
    minus_button.pack(side=ctk.LEFT, padx=5, pady=5)

    frame2 = ctk.CTkFrame(root)
    frame2.pack(side=ctk.LEFT, padx=5, pady=5)

    name_label = ctk.CTkLabel(frame2, text="Название:")
    name_label.grid(row=0, column=0, sticky=ctk.W)
    name_entry = ctk.CTkEntry(frame2)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    x_label = ctk.CTkLabel(frame2, text="X:")
    x_label.grid(row=1, column=0, sticky=ctk.W)
    x_entry = ctk.CTkEntry(frame2)
    x_entry.grid(row=1, column=1, padx=5, pady=5)

    y_label = ctk.CTkLabel(frame2, text="Y:")
    y_label.grid(row=2, column=0, sticky=ctk.W)
    y_entry = ctk.CTkEntry(frame2)
    y_entry.grid(row=2, column=1, padx=5, pady=5)

    r_label = ctk.CTkLabel(frame2, text="Радиус:")
    r_label.grid(row=3, column=0, sticky=ctk.W)
    r_entry = ctk.CTkEntry(frame2)
    r_entry.grid(row=3, column=1, padx=5, pady=5)

    m_label = ctk.CTkLabel(frame2, text="Масса:")
    m_label.grid(row=4, column=0, sticky=ctk.W)
    m_entry = ctk.CTkEntry(frame2)
    m_entry.grid(row=4, column=1, padx=5, pady=5)

    vx_label = ctk.CTkLabel(frame2, text="Скорость по X:")
    vx_label.grid(row=5, column=0, sticky=ctk.W)
    vx_entry = ctk.CTkEntry(frame2)
    vx_entry.grid(row=5, column=1, padx=5, pady=5)

    vy_label = ctk.CTkLabel(frame2, text="Скорость по Y:")
    vy_label.grid(row=6, column=0, sticky=ctk.W)
    vy_entry = ctk.CTkEntry(frame2)
    vy_entry.grid(row=6, column=1, padx=5, pady=5)

    apply_button = ctk.CTkButton(root, text="Применить", command=apply_changes)
    apply_button.place(relx=0.5, rely=0.98, anchor='s')

    col_label = ctk.CTkLabel(frame2, text="Цвет:")
    col_label.grid(row=7, column=0, sticky=ctk.W)
    col_entry = ctk.CTkButton(frame2, text='Выбрать цвет', command=show_color_chooser)
    col_entry.grid(row=7, column=1, padx=5, pady=5)

    root.mainloop()

    return objects
