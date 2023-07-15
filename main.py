"""
LABEL:
    parameter -> bootstyle=""
    aceita: default, primary, secundary, success, info, warning, danger, light and dark.
    e um segundo parâmetro: inverse

BUTTON:
    mesma coisa, só muda que aceita um parâmetro "command=" e no bootstyle aceita o segundo argumento como um link pra
    uma página
    tem que criar um estilo pra colocar no botão a parte
    my_style = boots.Style()
    my_style.configure('nomedoestilodottkbootstrap.nomequalquerparachamardps', font=('nomefonte', tamanho))
"""

from tkinter import *
from tkinter import messagebox
import ttkbootstrap as boots
from ttkbootstrap.constants import *

window = boots.Window(themename="solar")

window.iconbitmap("gatin.ico")
window.geometry("250x300")
window.title("Tarefas")

checkimg = PhotoImage(file="check.png")
checkimg2 = PhotoImage(file="check2.png")
x = BooleanVar()
y = BooleanVar()
z = BooleanVar()
a = BooleanVar()
b = BooleanVar()
c = BooleanVar()
listaVar = [x, y, z, a, b, c]


def display1() -> None:
    if x.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=52)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=52)


def display2() -> None:
    if y.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=83)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=83)


def display3() -> None:
    if z.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=118)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=118)


def display4() -> None:
    if a.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=196)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=196)


def display5() -> None:
    if b.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=230)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=230)


def display6() -> None:
    if c.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=265)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=265)


listaDisplay = [display1, display2, display3, display4, display5, display6]

# icon = PhotoImage(file=)
# window.iconphoto(True, icon)
# window.config(background="blue")

label1 = Label(window, text="<<Curso1>>", font=("Gothan", 15, "bold"),
               relief=SUNKEN, bd=5, padx=5, pady=5)
label1.pack()

my_style = boots.Style()
my_style.configure('default.Outline.TButton', font=('Gothan', 10))


class Button:
    def __init__(self, nome, variavel, display) -> None:
        self.texto = nome
        self.variavel = variavel
        self.display = display
        self.checkbutton = boots.Checkbutton(window, text=self.texto, variable=variavel, onvalue=True, offvalue=False,
                                             command=display, bootstyle="success-outline-toolbutton", width=20,
                                             style='default.Outline.TButton')
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=50)
        self.checkbutton.pack(pady=2)


if __name__ == '__main__':
    for i in range(1, 7):
        if i == 4:
            label2 = Label(window, text="<<Curso2>>", font=("Helvetica", 15, "bold"),
                           relief=SUNKEN, bd=5, padx=5, pady=5)
            label2.pack()

        Button(f'Aula{str(i)}', listaVar[i - 1], listaDisplay[i - 1])

window.mainloop()
