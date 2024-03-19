import tkinter, tkinter.messagebox

class KilloConvert:
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)
        self.prompt_lable = tkinter.Label(self.top_frame, text='Введите расстояние в километрах: ')
        self.desc_lable = tkinter.Label(self.mid_frame, text='Преобразовано в мили')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        self.value = tkinter.StringVar()
        self.prompt_lable.pack(side='left')
        self.desc_lable.pack(side='left')
        self.miles_lable = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.miles_lable.pack(side='left')
        self.kilo_entry.pack(side='left')
        self.calc_button = tkinter.Button(self.bot_frame, text='Преобразовать', command=self.convert)
        self.quit_button = tkinter.Button(self.bot_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(miles)

if __name__ == '__main__':
    kilo_conv = KilloConvert()