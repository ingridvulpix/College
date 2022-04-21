from curriculo_materias import grade_curricular
import pandas as pd
from tkinter import *
from pandastable import *


global df 

colunas = ['Materia','Periodo','Sigla','Horas','Requisito']
df = pd.DataFrame(grade_curricular).T.reset_index().rename(columns={'index':'Materia'})[colunas]


class Display(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Grade curricular de Tecnologia em Sistemas de Computação')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()
        return

app = Display()
#launch the app
app.mainloop()

