import tkinter

class ListBoxExample:
    def __init__(self) -> None:
        self.main_winfow = tkinter.Tk()

        self.listbox = tkinter.Listbox(self.main_winfow, height=0, width=0)
        self.listbox.pack(padx=10, pady=10)
        
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница',
                'Суббота', 'Воскресенье']
        
        for day in days:
            self.listbox.insert(tkinter.END, day)

        tkinter.mainloop()

if __name__ == '__main__':
    list_box_exp = ListBoxExample()