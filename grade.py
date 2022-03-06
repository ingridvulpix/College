from curriculo_materias import grade_curricular
import pandas as pd

#TO DO:Imprimir a grade de cada período
#TO DO:Colocar cronograma de cada disciplina
#TO DO:Identificar a semana do cronograma atrás do input do usuário
#TO DO:Corrigir laço for e mostrar_materias, ultimo None

class Grade:
    def __init__(self,periodo):
        self.periodo = periodo
 
    def mostrar_materias(self):#mostra todas as matérias do curriculo
        df = pd.DataFrame.from_dict(grade_curricular, orient='index')
        print(df)


p1 = Grade('1')
print(p1.mostrar_materias())
