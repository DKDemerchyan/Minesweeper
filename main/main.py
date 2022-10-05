import tkinter as tk
from random import shuffle


class CustomButton(tk.Button):
    """Переопределение стандартной кнопки."""

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(CustomButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'New Button{self.x} {self.y} {self.number} {self.is_mine}'


class Minesweeper:
    """Основной класс реализующий работу программы."""

    window = tk.Tk()
    ROW = 5
    COLUMNS = 5
    MINES = 5

    def __init__(self):
        self.buttons = []
        for i in range(self.ROW + 2):
            interim = []
            for j in range(self.COLUMNS + 2):
                btn = CustomButton(
                    self.window, x=i, y=j,
                    width=3, font='Calibri 15 bold'
                )
                btn.config(command=lambda button=btn: self.click(button))
                interim.append(btn)
            self.buttons.append(interim)

    def click(self, clicked_button: CustomButton):
        if clicked_button.is_mine:
            clicked_button.config(
                text='*', background='red',
                disabledforeground='black'
            )
        else:
            clicked_button.config(
                text=clicked_button.number, disabledforeground='black'
            )
        clicked_button.config(state='disabled')

    def create_widgets(self):
        for i in range(self.ROW+2):
            for j in range(self.COLUMNS+2):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(self.ROW+2):
            for j in range(self.COLUMNS+2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(
                        text='*', background='red',
                        disabledforeground='black'
                    )
                else:
                    btn.config(
                        text=btn.number, disabledforeground='black'
                    )
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.plant_mines()
        self.print_buttons()
        self.open_all_buttons()
        self.window.mainloop()

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def get_mines_places(self):
        indexes = list(range(1, self.ROW * self.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:self.MINES]

    def plant_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, self.ROW+1):
            for j in range(1, self.COLUMNS+1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1


game = Minesweeper()
game.start()
