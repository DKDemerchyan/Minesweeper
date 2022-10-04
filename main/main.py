import tkinter as tk


win = tk.Tk()
photo = tk.PhotoImage(file=r'C:\Dev\Minesweeper\main\icon.png')


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty value')


def delete_entry():
    name.delete(0, 'end')


def submit():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, tk.END)



win.title('Мое приложение')
win.iconphoto(False, photo)
win.config(bg='#C5C9C7')
win.geometry("500x600+100+100")


tk.Label(win, text='Имя').grid(row=0, column=0, stick='we')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='we')

name = tk.Entry(win)
name.grid(row=0, column=1)
password = tk.Entry(win, show='*')
password.grid(row=1, column=1)


tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, stick='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text='submit', command=submit).grid(row=3, column=0, stick='we')
tk.Button(win, text='insert', command=lambda : name.insert(1, 'hello'))\
    .grid(row=2, column=2, stick='we')


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
