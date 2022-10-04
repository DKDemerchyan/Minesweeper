import tkinter as tk


class Minesweeper:

    window = tk.Tk()
    ROW = 10
    COLUMNS = 7

    def __init__(self):
        self.buttons = []
        for i in range(self.ROW):
            interim = []
            for j in range(self.COLUMNS):
                btn = tk.Button(self.window, width=3, font='Calibri 15 bold')
                interim.append(btn)
            self.buttons.append(interim)

    def create_widgets(self):
        for i in range(self.ROW):
            for j in range(self.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.print_buttons()
        self.window.mainloop()

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)


game = Minesweeper()
game.start()
