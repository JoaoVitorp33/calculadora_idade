from tkinter import *
from tkinter import ttk

# instalar o tkcalendar: pip install tkcalendar
# importando tkcalendar
from tkcalendar import Calendar, DateEntry

# instalar o dateutil: pip install python-dateutil
# importando dateutil
from dateutil.relativedelta import relativedelta

# importando datetime
from datetime import date

# cores
cor1 = "#3b3b3b" # preta/pesado
cor2 = "#333333" # preta/leve
cor3 = "#FFFFFF"  # white / branca
cor4 = "#fcc058"  # orange / laranja
 
janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')
janela.configure(bg=cor1)

# Criando frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief="flat", bg=cor2)
frame_cima.grid(row=0, column=0)
 
frame_baixo = Frame(janela, width=310, height=400, pady=0, padx=0, relief="flat", bg=cor1)
frame_baixo.grid(row=1, column=0, sticky=NW)

def calcular():
    
    inicial = cal_1.get()
    termino = cal_2.get()
    
    # separando os valores e atribuindo em variaveis diferentes
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
 
    # Convertendo os valores em formato  datatime
    data_inicial = date(ano_1, mes_1, dia_1)
 
    # separando os valores e atribuindo em variaveis diferentes
    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]
 
    # Convertendo os valores em formato  datatime
    data_nascimento = date(ano_2, mes_2, dia_2)
    
    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days
    
 
    l_app_1_anos['text'] = anos
    l_app_2_mes['text'] = meses
    l_app_3_dia['text'] = dias

# Botao calcular
 
b_age = Button(frame_baixo, command=calcular, text="Calcular Idade", width=20, height=1, bg=cor1, fg=cor3,font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_age.place(x=60, y=225)

# Criando labels para frame cima
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief="flat", anchor="center", font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)
l_de_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief="flat", anchor="center", font=('Arial 35 bold'), bg=cor2, fg=cor4)
l_de_idade.place(x=0, y=70)

# Criando labels para frame baixo
l_data_inicial = Label(frame_baixo, text="Data Inicial", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor3)
l_data_inicial.place(x=40, y=30)
 
cal_1 = DateEntry(frame_baixo,width=13, background='darkblue',foreground='white', borderwidth=2,date_pattern='mm/dd/y', year=2023)
cal_1.place(x=170, y=30)
 
l_data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor3)
l_data_nascimento.place(x=40, y=70)
 
cal_2 = DateEntry(frame_baixo, width=13, background='darkblue',foreground='white', borderwidth=2,date_pattern='mm/dd/y', year=2023)
cal_2.place(x=170, y=70)

l_app_1_anos = Label(frame_baixo, text="27", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 25 bold'),bg=cor1,  fg=cor3)
l_app_1_anos.place(x=60, y=135)
l_app_anos = Label(frame_baixo, text="Anos", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 11 bold'),bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=175)
 
l_app_2_mes = Label(frame_baixo, text="12", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 25 bold'),bg=cor1,  fg=cor3)
l_app_2_mes.place(x=140, y=135)
l_app_mes = Label(frame_baixo, text="Meses", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 11 bold'),bg=cor1, fg=cor3)
l_app_mes.place(x=140, y=175)
 
l_app_3_dia = Label(frame_baixo, text="27", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 25 bold'),bg=cor1,  fg=cor3)
l_app_3_dia.place(x=220, y=135)
l_app_dia = Label(frame_baixo, text="Dias", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 11 bold'),bg=cor1, fg=cor3)
l_app_dia.place(x=220, y=175)

 
janela.mainloop()