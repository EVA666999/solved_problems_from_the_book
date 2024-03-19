import tkinter

class AVG:
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)
        self.prompt_lable1 = tkinter.Label(self.top_frame, text='Введите оценку ученика 1: ')
        self.prompt_lable2 = tkinter.Label(self.top_frame, text='Введите оценку ученика 2: ')
        self.prompt_lable3 = tkinter.Label(self.top_frame, text='Введите оценку ученика 3: ')
        self.avg_lable = tkinter.Label(self.mid_frame, text='Средний балл')
        self.ball_entry1 = tkinter.Entry(self.top_frame, width=10)
        self.ball_entry2 = tkinter.Entry(self.top_frame, width=10)
        self.ball_entry3 = tkinter.Entry(self.top_frame, width=10)
        self.value = tkinter.StringVar()
        self.prompt_lable1.grid(row=0, column=0)
        self.prompt_lable2.grid(row=1, column=0)
        self.prompt_lable3.grid(row=2, column=0)
        self.avg_lable.grid(row=0, column=0)
        self.balls_lable = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.balls_lable.grid(row=0, column=1)
        self.calc_button = tkinter.Button(self.bot_frame, text='Усреднить', command=self.convert)
        self.quit_button = tkinter.Button(self.bot_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.grid(row=0, column=0)
        self.quit_button.grid(row=0, column=1)
        self.ball_entry1.grid(row=0, column=1)
        self.ball_entry2.grid(row=1, column=1)
        self.ball_entry3.grid(row=2, column=1)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()
        tkinter.mainloop()

    def convert(self):
        ball1 = float(self.ball_entry1.get())
        ball2 = float(self.ball_entry2.get())
        ball3 = float(self.ball_entry3.get())
        result = (ball1 + ball2 + ball3) / 3
        self.value.set(result)

if __name__ == '__main__':
    kilo_conv = AVG()