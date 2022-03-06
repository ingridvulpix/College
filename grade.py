from curriculo_materias import grade_curricular

#TO DO:Imprimir a grade de cada período
#TO DO:Colocar cronograma de cada disciplina
#TO DO:Identificar a semana do cronograma atrás do input do usuário
#TO DO:Corrigir laço for e mostrar_materias, ultimo None

class Grade:
    def __init__(self,periodo):
        self.periodo = periodo
 
    def mostrar_materias(self):#mostra todas as matérias do curriculo
        for materia in grade_curricular:
            print('\nNome da materia: ', materia)
            print('Periodo: ',grade_curricular[materia]['periodo'])
            print('Sigla: ',grade_curricular[materia]['sigla'])
            print('Horas: ',grade_curricular[materia]['horas'])
            print('Requisitos: ',grade_curricular[materia]['requisito'])
            print('--------------------------------------------')

p1 = Grade('1')
print(p1.mostrar_materias())