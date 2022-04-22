from curriculo_materias import grade_curricular
import pandas as pd
from tkinter import *
from pandastable import *

#TO DO: FIX DROPDOWN
#TO DO: DROPDOWN NEEDS TO BE RESPONSIVE 
#TO DO: CHANGE DF DE ACORDO COM DROPDOWN
global df 

colunas = ['Materia','Periodo','Sigla','Horas','Requisito']
df = pd.DataFrame(grade_curricular).T.reset_index().rename(columns={'index':'Materia'})[colunas]

class Display(Frame, Canvas):
    def __init__(self, parent=None):
        super(Display, self).__init__()
        self.parent = parent
        self.main = self.master
        self.main.geometry('750x600+200+100')
        self.main.title('Tecnologia em Sistemas de Computação/UFF')
        Frame.__init__(self)
        options = [
            'Escolha uma opção',
            'Grade curricular',
            'Matérias de um período específico'
        ]
        self.options = options
        self.menu()


    def create_canvas(self):
        pass

    def menu(self):
        label= Label(self.main, text= "O que deseja saber do curso?", font= ("", 10))
        label.pack(pady=30)
        clicked= StringVar()
        drop = OptionMenu(self.main, clicked, *self.options )
        drop.pack()
        #self.get_choice(clicked)
    
    def get_choice(self, variable):
        choice = variable.get()
        return choice


    def generate_df(self):
        global f
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()
        return


def main():
    try:
        app = Display()
        app.mainloop()
    
    finally:
        print('Its over')

if __name__ == '__main__':
    main()
