from curriculo_materias import disciplinas

#TO DO:Imprimir a grade de cada período
#TO DO:Pegar Input do terminal
#TO DO:Colocar cronograma de cada disciplina
#TO DO:Identificar a semana do cronograma atrás do input do usuário

class Grade:
    def __init__(self,periodo,verifica):
        self.periodo = periodo
        self.verifica = verifica

          
    def mostra_materias(periodo):#materias para determinado periodo
        print(disciplinas[periodo])

p1 = Grade(1,0)
print(p1.mostra_materias())