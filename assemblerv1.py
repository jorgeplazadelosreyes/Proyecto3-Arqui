opcodes = ["MOV", "ADD", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV", "CALL", "RET", "POP", "PUSH"]
jumps = ["JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV"]

functions = []
variables = []

basics = {1: ['A,A', 'A,B', 'B,A', 'B,B'], 2: 'B', 3: ['A,B', 'B,A', 'A,Lit', 'B,Lit']}
basics1 = ['NOT', 'SHL', 'SHR']
basics2 = 'INC'
basics3 =  ['MOV','ADD','SUB','AND','OR','XOR']

directions = {1: ['A,(Dir)', 'B,(Dir)', 'A,(B)', '(Dir)'], 2:['(Dir),A', '(Dir),B', '(B)'], 3: ['A,(Dir)', 'B,(Dir)', '(Dir),A', '(Dir),B'
, 'A,(B)', 'B,(B)','(B),A'], 4:['(B)', '(Dir)']}
directions1 = ['ADD','SUB','OR','XOR']
directions2 = ['NOT', 'SHL', 'SHR']
directions3 = 'MOV'
directions4 = ['INC','RST']

cmp = ['A,B', 'A,Lit', 'B,Lit', 'A,(Dir)', 'B,(Dir)', 'A,(B)']

## SE CONSIDERA INDENTACION EN ESTE ASSEMBLER DE DOS ESPACIOS PARA OPERACIONES Y DEFINICION DE VARIABLES
## CAPS SENSITIVE

def leerCodigo(data):
    archivo = open(data, 'r')
    line = archivo.readline()
    line = archivo.readline()
    counter = 2             ## Contador de lineas
    flag = False            ## flag si hay errores en el archivo 
    error = False
    while(line):
        parsed = line.split(" ")
        flag = checkOpcodes(parsed, counter)
        if not flag:
            error = True
        line = archivo.readline()
        counter += 1
    archivo.close()
    return error


def leerData():
    pass

def checkFunciones(data):   ## crea lista con funciones presentes en el archivo 
    archivo = open(data, 'r')
    line = archivo.readline()
    line = archivo.readline()
    counter = 2
    flag = False
    while (line):
        error = False
        parsed = line.split(" ")
        if len(parsed) == 1:
            call = parsed[0].replace("\n", "")
            if call[-1] != ':':             ##revisa si tiene : al final
                print(f"Error: Syntax error, linea: {counter} ")
                flag = True
                error = True
            call = call.replace(':','')
            if call in functions:
                print(f"Error: Redefinicion de funcion {call}, linea: {counter} ") 
                flag = True 
                error = True
            if not error:
                functions.append(call)      ##añade a functions
        line = archivo.readline()
    archivo.close()
    return flag

def checkOpcodes(parsed, counter):
    parsed[-1] = parsed[-1].replace('\n','')
    if parsed[0] != '' and parsed[1] != '':  ## revisa identacion
        print(f"Error: Error de identacion, linea: {counter}")
        return True
    if parsed[2] not in opcodes:             ## revisa instrucciones 
        print(f"Error: Instruccion {parsed[2]} no existe, linea: {counter}")
        return True
    if parsed[2] in jumps:
        return checkJumps(parsed[3:], counter)
    operator = uniteString(parsed[3:])
    if ('(' in operator or ')' in operator):
        return checkDiretionning(parsed[2], operator, counter)
    else:
        return checkBasics(parsed[2],operator,counter)

def uniteString(args):
    unite = ''
    for arg in args:
        unite+= arg
    unite.replace(" ","")
    return unite

def checkBasics(signal, operator, counter):
    where = ''
    if signal in basics1:
        where = 1
        if operator not in basics[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
    if signal == basics2:
        if operator != 'B':
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
    if signal in basics3:
        where = 3
        if operator == 'A,B' or operator == 'B,A':
            return False
        if (operator[0] == 'A' or operator[0] == 'B') and operator[1] == ',':
            operator = operator.split(',')[1]
            return readlit(operator, counter)
        else:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return False

def readlit(operator, counter):
    lit = operator
    if '#' in lit:
        lit = lit.replace('#','')
        if not lit.isalnum():
            print(f"Error: Literal invalido. Linea: {counter}")
            return True
        numb = int(lit,16)
    else:
        if not lit.isnumeric():
            print(f"Error: Literal invalido. Linea: {counter}")
            return True
        numb = int(lit)
    if numb < 0 or numb > 256:
        print(f"Error: Literal {numb} invalido. Linea: {counter}")
        return True
    return False

def checkDiretionning(signal, operator, counter):
    where = 0
    splitted = operator.split(',')
    aux = transformDir(operator)
    if len(splitted) < 1 or len(splitted) > 2:
        print(f"Error: Muchos argumentos. Linea: {counter}")
        return True
    if signal in directions1:
        where = 1
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return False
    if signal in directions2:
        where = 2
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return False
    if signal in directions3:
        where = 3
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return False
    if signal in directions4:
        where = 4
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return False
    return False

def transformDir(operator):
    count = 0
    index = 'False'
    splitted = operator.split(',')
    for i in splitted:
        if checkBrackets(i) and i != 'A' and i != 'B':
            index = count
        count += 1
    if index == 'False':
        return operator
    if len(splitted) == 1:
        new = '(Dir)'
    if index == 0:
        new = '(Dir),'+str(splitted[1])
    else:
        new = str(splitted[0]) +',(Dir)'
    return new

def checkBrackets(args):
    if args[0] == '(' and args[-1] == ')':
        return True

def checkJumps(args, counter):
    if len(args) > 1:
        print(f"Error: Muchos argumentos. Linea: {counter}")
        return True
    return readlit(args[0], counter)

def readDir():
    pass

def archivoOut():
    print("hola")
    pass

def main():
    data =  "incorrecto.ass" ##input("Ingrese archivo .ass: ")
    flag1 = checkFunciones(data)
    flag2 = leerCodigo(data)
    

main()