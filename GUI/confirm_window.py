import customtkinter as ctk

class ConfirmationWindow:
    def __init__(self, message):
        self.window = ctk.CTk()
        self.window.title("Подтверждение")
        self.window.geometry('350x100')
        self.window.resizable(False, False)
        self.window.wm_geometry("+%d+%d" % (((self.window.winfo_screenwidth()) / 2)-self.window.winfo_width()/2,
                                            ((self.window.winfo_screenheight()) / 2)-self.window.winfo_height()/2))
        
        label = ctk.CTkLabel(self.window, text=message)
        label.pack(padx=10, pady=10)
        
        button_frame = ctk.CTkFrame(self.window)
        button_frame.pack(padx=10, pady=10)
        
        confirm_button = ctk.CTkButton(button_frame, text="Да", command=self.confirm)
        confirm_button.pack(side="left", padx=5)
        
        cancel_button = ctk.CTkButton(button_frame, text="Отмена", command=self.cancel)
        cancel_button.pack(side="left", padx=5)
        
        self.result = None
        
        self.window.protocol("WM_DELETE_WINDOW", self.cancel)
        self.window.mainloop()
    
    def confirm(self):
        self.result = True
        self.window.destroy()
    
    def cancel(self):
        self.result = False
        self.window.destroy()