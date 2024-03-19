import tkinter, tkinter.messagebox

class MyGUI:
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        self.main_window.title('Мой первый GUI')
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)
        self.lable1 = tkinter.Label(self.top_frame, text='Мигнуть')
        self.lable2 = tkinter.Label(self.top_frame, text='Моргнуть')
        self.lable3 = tkinter.Label(self.top_frame, text='Кивнуть')
        self.lable1.pack(side='top')
        self.lable2.pack(side='top')
        self.lable3.pack(side='top')
        self.lable4 = tkinter.Label(self.bot_frame, text='Мигнуть')
        self.lable5 = tkinter.Label(self.bot_frame, text='Моргнуть')
        self.lable6 = tkinter.Label(self.bot_frame, text='Кивнуть')
        self.lable4.pack(side='left')
        self.lable5.pack(side='left')
        self.lable6.pack(side='left')
        self.my_button = tkinter.Button(self.main_window, text='Выйти', command=self.main_window.destroy)
        self.top_frame.pack()
        self.bot_frame.pack()
        self.my_button.pack()

        tkinter.mainloop()

if __name__ == "__main__":
    my_gui = MyGUI()