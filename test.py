from typing import Literal


basics = {1: ['A,A', 'A,B', 'B,A', 'B,B'], 2: 'B', 3: ['A,B', 'B,A', 'A,Lit', 'B,Lit'] }
basics1 = ['NOT', 'SHL', 'SHR']
basics2 = 'INC'
basics3 =  ['MOV','ADD','SUB','AND','OR','XOR']
def check(signal, operator):
    where = ''
    if signal in basics1:
        where = 1
        if operator not in basics[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe")
            return True
    if signal == basics2:
        if operator != 'B':
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe")
            return True
    if signal in basics3:
        where = 3
        if operator == 'A,B' or operator == 'B,A':
            return False
        readlit(operator)

def readlit(operator):
    lit = operator.split(',')[1]
    if '#' in lit:
        lit = lit.replace('#','')
        numb = int(lit,16)
    else:
        numb = int(lit)
    if numb < 0 or numb > 256:
        print(f"Error: Literal {numb} invalido")
        return True
    return False
    

check('MOV','A,#10F')