from curriculo_materias import grade_curricular
import pandas as pd

#TO DO:Colocar cronograma de cada disciplina
#TO DO:Identificar a semana do cronograma atrás do input do usuário

class Grade:
    def __init__(self,periodo):
        self.periodo = periodo
        global df 
        df = pd.DataFrame.from_dict(grade_curricular, orient='index')

    def mostrar_materias(self):#mostra todas as matérias do curriculo
        print(df)
    def materias_periodo(self,periodo):#mostra matérias do período selecionado
        result_df = df.loc[df['periodo']== periodo]
        print(result_df)


#p1 = Grade(1)
#p1.mostrar_materias()
#p1.materias_periodo(5)
