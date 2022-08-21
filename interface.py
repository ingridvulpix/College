from data import *
import pandas as pd
from tkinter import *
from pandastable import *

#TO DO Terminar cronograma materia no data

class Display():
    def __init__(self, root):
        self.main = root
        options_menu = [
            'Escolha uma opção',
            'Grade curricular',
            'Cronograma do Período 2022.2',
            'Cronograma de Provas 2022.2',
            'Cronograma das Matérias de 2022.2'
        ]

        self.options_menu = options_menu

        self.create_canvas()

    def create_canvas(self):
        self.main.title('Tecnologia em Sistemas de Computação/UFF')
        self.main.geometry('750x600+200+100')
        self.frame = Frame(self.main)
        self.frame.pack()
        self.df_frame = Frame(self.main)
        self.menu()

    def menu(self):
        label= Label(self.frame, text= "O que deseja saber do curso?", font= ("", 10))
        label.pack(pady=30)
        self.var= StringVar(self.frame)
        self.drop = OptionMenu(self.frame, self.var, *self.options_menu )
        self.drop.pack()
        self.button = Button(self.frame, text = "Gerar DataFrame" , command = self.select_df )
        self.button.pack()


    def select_df(self):
        self.choice = self.var.get()

        if self.choice == self.options_menu[1]:
            self.df_grade()

        if self.choice == self.options_menu[2]:
            self.df_periodo()

        if self.choice == self.options_menu[3]:
            self.df_provas()

        if self.choice == self.options_menu[4]:
            self.df_materia()

        self.button.config(state = DISABLED)
        self.reset_button = Button(self.frame, text='Refresh', command= self.reset).pack()


    def df_materia(self):
        self.df_frame.pack(fill=BOTH,expand=1)
        col = ['Materia','Periodo','Sigla','Horas','Requisito']
        df_periodo = pd.DataFrame(cronograma_periodo).T.reset_index().rename(columns={'index':'Materia'})[col]
        self.table = pt = Table(self.df_frame, dataframe=df_periodo,
                                showtoolbar=True, showstatusbar=True)
        pt.show()        

    def df_periodo(self):
        self.df_frame.pack(fill=BOTH,expand=1)
        col = ['Materia','Periodo','Sigla','Horas','Requisito']
        df_periodo = pd.DataFrame(cronograma_periodo).T.reset_index().rename(columns={'index':'Materia'})[col]
        self.table = pt = Table(self.df_frame, dataframe=df_periodo,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

    def df_grade(self):
        self.df_frame.pack(fill=BOTH,expand=1)
        col = ['Materia','Periodo','Sigla','Horas','Requisito']
        df_grade = pd.DataFrame(grade_curricular).T.reset_index().rename(columns={'index':'Materia'})[col]
        self.table = pt = Table(self.df_frame, dataframe=df_grade,
                                showtoolbar=True, showstatusbar=True)
        pt.show()        

    def df_provas(self):
        self.df_frame.pack(fill=BOTH,expand=1)
        col = ['Materia','AP1','AP2','AP3','Bibliografia']# FIXME visualização da coluna Bibliografia
        df_provas = pd.DataFrame(cronograma_provas).T.reset_index().rename(columns={'index':'Materia'})[col]
        self.table = pt = Table(self.df_frame, dataframe=df_provas,
                                showtoolbar=True, showstatusbar=True)
        pt.show()         

    def reset(self):
        self.frame.destroy()
        self.df_frame.destroy()
        self.create_canvas()