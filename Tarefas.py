from tkinter import *
from tkinter import messagebox
import ttkbootstrap as boots
from ttkbootstrap.constants import *

window = boots.Window(themename="vapor")

window.iconbitmap("gatin.ico")
window.title("Tarefas")
window.resizable(False, False)

larguraJanela = 250
alturaJanela = 300

larguraTela = window.winfo_screenwidth()
alturaTela = window.winfo_screenheight()

posx = (larguraTela // 2) - (larguraJanela // 2)
posy = (alturaTela // 2) - (alturaJanela // 2)

# Define a posição da janela
window.geometry('{}x{}+{}+{}'.format(larguraJanela, alturaJanela, posx, posy))

""" Background """
backg = PhotoImage(file="backg.png")
Label(image=backg).place(x=0, y=0, relwidth=1.0, relheight=1.0)


""" Confirmações """
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
        label.place(x=202, y=40)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=40)


def display2() -> None:
    if y.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=75)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=75)


def display3() -> None:
    if z.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=109)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=109)


def display4() -> None:
    if a.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=177)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=177)


def display5() -> None:
    if b.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=211)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=211)


def display6() -> None:
    if c.get():
        label = boots.Label(image=checkimg)
        label.pack()
        label.place(x=202, y=245)
        messagebox.showinfo(title='Parabéns!!', message="Boa :D", icon="warning")
    else:
        label = boots.Label(image=checkimg2)
        label.pack()
        label.place(x=202, y=245)


listaDisplay = [display1, display2, display3, display4, display5, display6]

# icon = PhotoImage(file=)
# window.iconphoto(True, icon)
# window.config(background="blue")

label1 = Label(window, text="Design Patterns", font=("Gothan", 15, "bold"),
               relief=SUNKEN, bd=5, padx=0, pady=0, borderwidth=5)
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
        label.place(x=202, y=40)
        self.checkbutton.pack(pady=2)


if __name__ == '__main__':
    for i in range(1, 7):
        if i == 4:
            label2 = Label(window, text="After Effects", font=("Helvetica", 15, "bold"),
                           relief=SUNKEN, bd=5, padx=0, pady=0)
            label2.pack()

        Button(f'Aula{str(i)}', listaVar[i - 1], listaDisplay[i - 1])

window.mainloop()
