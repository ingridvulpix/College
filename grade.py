from curriculo_materias import grade_curricular

#TO DO:Imprimir a grade de cada período
#TO DO:Pegar Input do terminal
#TO DO:Colocar cronograma de cada disciplina
#TO DO:Identificar a semana do cronograma atrás do input do usuário

class Grade:
    def __init__(self,periodo):
        self.periodo = periodo
 
    def mostrar_materias(self):#mostra todas as matérias do curriculo
        for materia in grade_curricular:
            print('\nNome da materia: ', materia)


p1 = Grade('1')
print(p1.mostrar_materias())