# Importando Tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

################# cores ###############
co0 = "#f0f3f5"  # cinza
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue
co10 = "#000000"  # preta

################# Criando Janela ###############

janela = Tk()
janela.title("Johnny's Library")
janela.geometry('1043x543')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE) # Bloqueia a alteração do geometry

################# Dividindo a Janela ###############

frame_cima = Frame(janela, width=310, height=50, bg=co10, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=493, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=493, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

################# Label Cima ###############

app_nome = Label(frame_cima, text="Johnny's Library", anchor=NW, font='Ivy 13 bold', bg=co10, fg=co1, relief='flat')
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

# Consulta

label_consulta = Label(frame_baixo, text='Consulta *', anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4, relief='flat')
label_consulta.place(x=10, y=370)

entry_consulta = Entry(frame_baixo, width=45, justify='left', relief='solid')
entry_consulta.place(x=15, y=400)

################# Botões do Frame Baixo ###############

insert_button = Button(frame_baixo, text="Inserir", width=10, font='Ivy 9 bold', bg=co6, fg=co1, relief='raised',
                       overrelief='ridge')
insert_button.place(x=15, y=440)

update_button = Button(frame_baixo, text="Atualizar", width=10, font='Ivy 9 bold', bg=co2, fg=co1, relief='raised',
                       overrelief='ridge')
update_button.place(x=112, y=440)

delete_button = Button(frame_baixo, text="Deletar", width=10, font='Ivy 9 bold', bg=co7, fg=co1, relief='raised',
                       overrelief='ridge')
delete_button.place(x=209, y=440)

################# Frame Direita ###############

tabela_header = ['ID', 'Livro', 'Autor', 'Editora', 'Gênero', 'Data', 'País']

tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_header, show='headings')

# Vertical Scroll Bar
vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)

# Horizontal Scroll Bar
hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_direita.grid_rowconfigure(0, weight=12)

hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw', 'nw']
h = [30, 170, 140, 140, 100, 120, 100]
n = 0

for col in tabela_header:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n], anchor=hd[n])
    n += 1

janela.mainloop()


