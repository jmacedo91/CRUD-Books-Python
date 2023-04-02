# Importando Tkinter
from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# Criando Janela ###############

janela = Tk()
janela.title("")
janela.geometry('1043x513')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE) # Bloqueia a alteração do geometry

################# Dividindo a Janela ###############

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=463, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=463, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

################# Label Cima ###############

app_nome = Label(frame_cima, text="Johnny's Library", anchor=NW, font='Ivy 13 bold', bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

################# Configurando Frame Baixo ###############

# Livro
label_livro = Label(frame_baixo, text='Livro *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_livro.place(x=10, y=10)

entry_livro = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_livro.place(x=15, y=40)

# Autor
label_autor = Label(frame_baixo, text='Autor *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_autor.place(x=10, y=70)

entry_autor = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_autor.place(x=15, y=100)

# Editora
label_editora = Label(frame_baixo, text='Editora *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_editora.place(x=10, y=130)

entry_editora = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_editora.place(x=15, y=160)

# Gênero
label_genero = Label(frame_baixo, text='Gênero *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_genero.place(x=10, y=190)

entry_genero = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_genero.place(x=15, y=220)

# País
label_pais = Label(frame_baixo, text='País *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_pais.place(x=10, y=250)

entry_pais = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_pais.place(x=15, y=280)

# Data
label_data = Label(frame_baixo, text='Data *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_data.place(x=10, y=310)

entry_data = DateEntry(frame_baixo, width=42, background='darkblue', foreground='white', borderwidth=2)
entry_data.place(x=15, y=340)

janela.mainloop()




