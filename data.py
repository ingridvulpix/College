grade_curricular = {
    'Matemática básica':{'Periodo':1,'Sigla':'MB','Horas':60,'Requisito':None}, 
    'Construção de páginas da web':{'Periodo':1,'Sigla':'CPW','Horas':40,'Requisito':None},
    'Inglês Instrumental':{'Periodo':1,'Sigla':'II','Horas':40,'Requisito':None},
    'Introdução a Informática':{'Periodo':1,'Sigla':'IAI','Horas':80,'Requisito':None},
    'Projeto e Desenvolvimento de Algortimos':{'Periodo':1,'Sigla':'PDA','Horas':80,'Requisito':None},
    'Fundamentos de Algoritmos de Computação':{'Periodo':2,'Sigla':'FAC','Horas':80,'Requisito':'MB'},
    'Organização de Computadores':{'Periodo':2,'Sigla':'ODC','Horas':80,'Requisito':'IAI'},
    'Algebra Linear':{'Periodo':2,'Sigla':'ALGLIN','Horas':80,'Requisito':None},
    'Fundamentos de Programação':{'Periodo':2,'Sigla':'FP','Horas':80,'Requisito':'PDA'},
    'Matemática para Computação':{'Periodo':3,'Sigla':'MATCOMP','Horas':80,'Requisito':'FAC'},
    'Física para Computação':{'Periodo':3,'Sigla':'FISCOMP','Horas':80,'Requisito':None},
    'Estrutura de Dados':{'Periodo':3,'Sigla':'ED','Horas':80,'Requisito':'PDA'},
    'Programação com Interfaces Gráficas':{'Periodo':3,'Sigla':'PIG','Horas':80,'Requisito':'FP'},
    'Probabilidade e Estatística':{'Periodo':4,'Sigla':'PE','Horas':80,'Requisito':'MATCOMP'},
    'Modelagem de Informação':{'Periodo':4,'Sigla':'MDI','Horas':80,'Requisito':None},
    'Sistemas Operacionais':{'Periodo':4,'Sigla':'SO','Horas':80,'Requisito':'ODC'},
    'Banco de Dados':{'Periodo':4,'Sigla':'BD','Horas':80,'Requisito':'ED'},
    'Programação Orientada a Objetos':{'Periodo':4,'Sigla':'POO','Horas':80,'Requisito':'FP'},
    'Engenharia de Software':{'Periodo':5,'Sigla':'EDS','Horas':80,'Requisito':'MDI'},
    'Redes de Computadores I':{'Periodo':5,'Sigla':'RC1','Horas':120,'Requisito':'SO, FISCOMP'},
    'Análise de Sistemas':{'Periodo':5,'Sigla':'AS','Horas':80,'Requisito':'BD'},
    'Programação de Aplicações Web':{'Periodo':5,'Sigla':'PAW','Horas':80,'Requisito':'BD, FP'},
    'Empreendedorismo e Ética':{'Periodo':6,'Sigla':'EE','Horas':80,'Requisito':None},
    'Tese de Conclusão de Curso':{'Periodo':6,'Sigla':'TCC','Horas':120,'Requisito':None},
    'Redes de Computadores II':{'Periodo':6,'Sigla':'RC2','Horas':120,'Requisito':'RC1'},
    'Arquitetura e Projeto de Sistemas':{'Periodo':6,'Sigla':'APS','Horas':80,'Requisito':'AS'},
    'Computação Gráfica':{'Periodo':6,'Sigla':'CG','Horas':80,'Requisito':'PIG, ALGLIN'}
    }

cronograma_periodo = {
    'Modelagem de Informação':{'Periodo':4,'Sigla':'MDI','Horas':80,'Requisito':None},
    'Sistemas Operacionais':{'Periodo':4,'Sigla':'SO','Horas':80,'Requisito':'ODC'},
    'Banco de Dados':{'Periodo':4,'Sigla':'BD','Horas':80,'Requisito':'ED'}
}

cronograma_provas = {
    'Banco de Dados':{'AP1':'Módulo 1 ao 4','AP2':'Módulo 5 ao 8','AP3':'Módulo 1 ao 8',\
        'Bibliografia':"'Elmasri, Navathe. Sistemas de Banco de Dados','HEUSER, C.A. Projeto de Banco de Dados'"},
    'Modelagem de Informação':{'AP1':'Aula 1 a 12 e 15','AP2':'Aula 16 a 23','AP3':'Aula 1 a 23',\
        'Bibliografia':"'HEUSER, C.A. Projeto de Banco de Dados','FLOWER. UmL Essencial'"},
    'Sistemas Operacionais':{'AP1':'Aula 1 a 6','AP2':'Aula 7 a 12','AP3':'Aula 1 a 12',\
        'Bibliografia':"'Tanenbaum, Woodhull. Sistemas Operacionais:\
            Projeto e Implementação'"}
}

cronograma_materia = {
    'Banco de Dados':{'Módulo 1':{'Semana 1':"'Aula 1: Introdução','Aula 2:'Conceitos'",\
        'Semana 2':"'Aula 3: Exercícios','Aula 4: SGBDs e Modelos de Dados'"},
        'Módulo 2':{'Semana 3':"'Aula 5: Introdução a Modelagem Conceitual','Aula 6: Modelo Entidade-Relacionamento'",\
            'Semana 4':"'Aula 7: Modelo ER - Cardinalidades e Identificadores',\
                'Aula 8: Modelo ER - Generalização, Especialização e outros conceitos'",\
                'Semana 5':"'Aula 9: Construindo o Modelo ER', \
                    'Aula 10: Verificação de modelos, Estabelecimentos de padrões e estratégias de modelagem'"},\
        'Módulo 3':{'Semana 6':"Aula 11: Arquiteturas"},
        'Módulo 4':{'Semana 7':"'Aula 12: Modelo Relacional','Aula 13: Modelo Relacional '",'Semana 8':"'Aula 14: Álgebra Relacional',\
            'Aula 15: Álgebra Relacional','Aula 16: Fixação Álgebra Relacional'"},
        'Módulo 5':{'Semana 9':"'Aula 17: Mapeamento ER-Relacional','Aula 18: Mapeamento ER-Relacional: Mapeamento de Generalização/Especialização'"},
        'Módulo 6':{'Semana 10':"'Aula 27: Normalização de BD – 1FN e 2FN','Aula 28: Normalização de BD – 3FN e 4FN'"},
        'Módulo 7':{'Semana 11':"'Aula 19: SQL – Linguagem de Definição de Dados','Aula 20: SQL – Linguagem de Consulta','Aula 21: SQL – União'",\
            'Semana 12':"'Aula 22: SQL – EXISTS','Aula 23: SQL – Funções de agregação e agrupamento','Aula 24: Atualizações em SQL','Aula 25: Visões em SQL'"},
        'Módulo 8':{'Semana 13':"Aula 29: Evolução dos modelos, visão geral dos modelos hierárquicos e de redes"}},
    'Modelagem de Informação':{'Semana 1':'','Semana 2':'','Semana 3':'','Semana 4':'','Semana 5':'',\
        'Semana 6':'','Semana 7':'','Semana 8':'','Semana 9':'','Semana 10':'','Semana 11':'',\
            'Semana 12':''},
    'Sistemas Operacionais':{'Semana 1':'','Semana 2':'','Semana 3':'','Semana 4':'','Semana 5':'',\
        'Semana 6':'','Semana 7':'','Semana 8':'','Semana 9':'','Semana 10':'','Semana 11':'',\
            'Semana 12':''}
}