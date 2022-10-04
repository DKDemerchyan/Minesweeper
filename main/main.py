import tkinter as tk


win = tk.Tk()
photo = tk.PhotoImage(file=r'C:\Dev\Minesweeper\main\icon.png')


win.title('Мое приложение')
win.iconphoto(False, photo)
win.config(bg='#C5C9C7')
win.geometry("500x600+100+100")


btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')

btn1.grid()
btn2.grid()


win.mainloop()
