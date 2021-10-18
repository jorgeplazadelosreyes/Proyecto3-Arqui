from opcodes import allOpcodes

instructions = ["MOV", "ADD", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV", "CALL", "RET", "POP", "PUSH"]
jumps = ["JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV"]
specs = ["CALL", "RET", "POP", "PUSH"]

labels = []
variables = []
salidaMem = []
opcodesList = []

basics = {1: ['A,A', 'A,B', 'B,A', 'B,B'], 2: ['B'], 3: ['A,B', 'B,A', 'A,Lit', 'B,Lit']}
basics1 = ['NOT', 'SHL', 'SHR']
basics2 = ['INC']
basics3 =  ['MOV','ADD','SUB','AND','OR','XOR']

directions = {1: ['A,(Dir)', 'B,(Dir)', 'A,(B)', '(Dir)'], 2:['(Dir),A', '(Dir),B', '(B)'], 3: ['A,(Dir)', 'B,(Dir)', '(Dir),A', '(Dir),B'
, 'A,(B)', 'B,(B)','(B),A'], 4:['(B)', '(Dir)']}
directions1 = ['ADD','SUB','OR','XOR']
directions2 = ['NOT', 'SHL', 'SHR']
directions3 = 'MOV'
directions4 = ['INC','RST']

specials = ['A','B','Dir']

justLetters = ['A,(B)', '(B)', 'B,(B)', '(B),A'] 

cmp = {1:['A,B', 'A,Lit', 'B,Lit'], 2:['A,(Dir)', 'B,(Dir)', 'A,(B)']}

## SE CONSIDERA INDENTACION EN ESTE ASSEMBLER DE DOS ESPACIOS PARA OPERACIONES Y DEFINICION DE VARIABLES
## CAPS SENSITIVE

def leerCodigo(data):
    archivo = open(data, 'r')
    line = archivo.readline()
    counter = 1
    while line:
        line =line.replace("\n","")
        if line == "CODE:":
            break
        line = archivo.readline()
        counter += 1 
    line = archivo.readline()
    counter += 1  
    error = False           ## flag global, depende de flag por linea
    while(line):
        flag = False      
        parsed = line.split(" ")
        if len(parsed) > 1:
            flag = checkOpcodes(parsed, counter)
        if flag:
            error = True
        line = archivo.readline()
        counter += 1
    archivo.close()
    return error, counter

def readData(data):
    arch = open(data,'r')
    line = arch.readline()
    line = arch.readline()
    counter = 2
    error = False
    while line:
        flag = False
        line =line.replace("\n","")
        if line == "CODE:":
            break
        flag = getVariables(line, counter)
        if flag:
            error = True
        line = arch.readline()
        counter += 1
    arch.close()
    return error, (counter-2)
    
def getVariables(line, counter):
    parsed = line.split(" ")
    if len(parsed) != 4:
        print(f"Error: syntax error. Linea: {counter}")
        return True
    if parsed[0] != '' and parsed[1] != '':
        print(f"Error: Error de identacion. Linea: {counter}")
        return True
    nombre = parsed[2]
    lit = parsed[3]
    if nombre == '' or lit == '':
         print(f"Error: syntax error. Linea: {counter}")
         return True
    variables.append(nombre)
    flag,lit = readlit(lit, counter)
    if not flag:
        litToBinary(lit)
    return False

def litToBinary(lit):
    if lit >= 0:
        salidaMem.append(str(format(lit,'08b')))
    else:
        salidaMem.append(str(bin((1<<8) - (lit*-1))[2:]))

def checkFunciones(data):   ## crea lista con funciones presentes en el archivo 
    archivo = open(data, 'r')
    line = archivo.readline()
    counter = 1
    while line:
        line =line.replace("\n","")
        if line == "CODE:":
            break
        line = archivo.readline()
        counter += 1
    line = archivo.readline()
    counter += 1
    flag = False
    while (line):
        error = False
        parsed = line.split(" ")
        if len(parsed) == 1:
            call = parsed[0].replace("\n", "")
            if call[-1] != ':':             ##revisa si tiene : al final
                print(f"Error: Syntax error. Linea: {counter} ")
                flag = True
                error = True
            call = call.replace(':','')
            if call in labels:
                print(f"Error: Redefinicion de funcion {call}. Linea: {counter} ") 
                flag = True 
                error = True
            if not error:
                labels.append(call)      ##añade a functions
        line = archivo.readline()
        counter += 1
    archivo.close()
    return flag

def checkOpcodes(parsed, counter):
    parsed[-1] = parsed[-1].replace('\n','')
    if parsed[0] != '' and parsed[1] != '':  ## revisa identacion
        print(f"Error: Error de identacion. Linea: {counter}")
        return True
    if parsed[2] not in instructions:             ## revisa instrucciones 
        print(f"Error: Instruccion {parsed[2]} no existe. Linea: {counter}")
        return True
    if parsed[2] in jumps:
        return checkJumps(parsed[2],parsed[3:], counter)
    operator = uniteString(parsed[3:])
    if parsed[2] == 'CMP':
        return checkCMP(parsed[2], operator, counter)
    if parsed[2] in specs:
        return checkSpecials(parsed[2], parsed[3:], counter)
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
        getOpcode(str(signal)+' '+str(operator),0)
        return False
    if signal in basics2:
        where = 2
        if operator not in basics[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        getOpcode(str(signal)+' '+str(operator),0)
        return False
    if signal in basics3:
        where = 3
        aux = transformLit(operator)
        if aux not in basics[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        if "Lit" in aux:
            numb = operator.split(',')[1]
            flag,lit = readlit(numb, counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
            return flag
        else:
            getOpcode(str(signal)+' '+str(aux),0)
            return False
    else:
        print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
        return True

def readlit(operator, counter):
    lit = operator
    if '#' in lit:
        lit = lit.replace('#','')
        if not lit.isalnum():
            print(f"Error: Literal invalido. Linea: {counter}")
            return True,0
        numb = int(lit,16)
    else:
        aux = lit.replace("-","")
        if not aux.isnumeric():
            print(f"Error: Literal invalido. Linea: {counter}")
            return True,0
        numb = int(lit)
    if numb < -256 or numb > 256:
        print(f"Error: Literal {numb} invalido. Linea: {counter}")
        return True,0
    return False,numb

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
            return True
        if aux not in justLetters:
            lit = parseDir(operator)
            flag,lit = checkVariables(lit, counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
            return flag
        else:
            getOpcode(str(signal)+' '+str(aux),0)
    if signal in directions2:
        where = 2
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        if aux not in justLetters:
            lit = parseDir(operator)
            flag,lit = checkVariables(lit, counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
            return flag
        else:
            getOpcode(str(signal)+' '+str(aux),0)
    if signal in directions3:
        where = 3
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        if aux not in justLetters:
            lit = parseDir(operator)
            flag,lit = checkVariables(lit, counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
            return flag
        else:
            getOpcode(str(signal)+' '+str(aux),0)
    if signal in directions4:
        where = 4
        if aux not in directions[where]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        if aux not in justLetters:
            lit = parseDir(operator)
            flag,lit = checkVariables(lit, counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
            return flag
        else:
            getOpcode(str(signal)+' '+str(aux),0)
    return False

def checkCMP(signal, operator, counter):
    direction = False
    if '(' in operator or ')' in operator:
        direction = True
    splitted = operator.split(',')
    if not direction:
        aux = transformLit(operator)
        if aux not in cmp[1]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        if splitted[1] != 'B':
            flag,lit = readlit(splitted[1], counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
            return flag
        return False
    else:
        if not checkBrackets(splitted[1]):
            print(f"Error: Syntax error. Linea: {counter}")
            return True
        aux = transformDir(operator)
        if aux not in cmp[2]:
            print(f"Error: Expresion {str(signal)+' '+str(operator)} no existe. Linea: {counter}")
            return True
        if aux not in justLetters:
            lit = parseDir(operator)
            flag,lit = checkVariables(lit, counter)
            if not flag:
                getOpcode(str(signal)+' '+str(aux),lit)
                return flag
            else:
                getOpcode(str(signal)+' '+str(aux),0)
        return False

def checkSpecials(signal, operator, counter):
    if signal == "RET":
        if len(operator) > 0:
            print(f"Error: Expresion invalida. Linea: {counter}")
            return True
        getOpcode(str(signal),0)
    if signal == "POP" or signal == "PUSH":
        if operator != 'A' and operator != 'B':
            print(f"Error: Expresion {str(signal)+' '+str(operator[0])} no existe. Linea: {counter}")
            return True
        getOpcode(str(signal)+' '+str(operator),0)
    if signal == "CALL":
        if len(operator) > 1:
            print(f"Error: Muchos argumentos. Linea: {counter}")
            return True
        flag,lit = readlit(operator[0], counter)        
        if not flag:
            getOpcode(str(signal)+' '+"Dir",lit)
        return flag
    return False

def transformDir(operator):
    count = 0
    index = 'False'
    splitted = operator.split(',')
    for i in splitted:
        if checkBrackets(i) and i != '(A)' and i != '(B)':
            index = count
        count += 1
    if index == 'False':
        return operator
    if len(splitted) == 1 and checkBrackets(splitted[0]):
        new = '(Dir)'
        return new
    else:
        if index == 0:
            new = '(Dir),'+str(splitted[1])
        else:
            new = str(splitted[0]) +',(Dir)'
    new = new.replace(" ","")
    return new

def transformLit(args):
    splitted = args.split(',')
    if splitted[0] != 'A' and splitted[0] != 'B':
        return 'Error'
    if (splitted[0] == 'A' and splitted[1] == 'B') or (splitted[0] == 'B' and splitted[1] == 'A'):
        return args
    new = str(splitted[0]) + ',Lit'
    return new

def parseDir(args):
    lit = ''
    splitted = args.split(',')
    for i in splitted:
        if checkBrackets(i):
            noBrackets = i.replace("(","").replace(")","")
            for char in noBrackets:
                lit+=char
    return lit

def checkBrackets(args):
    if args[0] == '(' and args[-1] == ')':
        return True

def checkJumps(signal, args, counter):
    if len(args) > 1:
        print(args)
        print(f"Error: Muchos argumentos. Linea: {counter}")
        return True
    flag,lit = checkLabels(args[0], counter)        
    if not flag:
        getOpcode(str(signal)+' '+"Dir",lit)
    return flag

def getOpcode(arg,lit): 
    if (not "Lit" in arg) and (not "Dir" in arg):
        opcodesList.append(str(allOpcodes[arg])+"00000000")
    else:
        if lit >= 0:
            opcodesList.append(str(allOpcodes[arg])+str(format(lit,'08b')))
        else:
            opcodesList.append(str(allOpcodes[arg])+str(bin((1<<8) - (lit*-1))[2:]))

def archivoOut(data):
    arch = open(str(data)[:-3]+".out", 'w')
    for opcode in opcodesList:
        arch.write(opcode+str('\n'))
    arch.close()

def archivoMem(data):
    arch = open(str(data)[:-3]+".mem", 'w')
    for data in salidaMem:
        arch.write(data+str('\n'))
    arch.close()

def checkLabels(operator, counter):
    lit = operator
    flag = False
    numb = 0
    if '#' in lit:
        lit = lit.replace('#','')
        if not lit.isalnum():
            flag = True
        else:
            numb = int(lit,16)
    else:
        aux = lit.replace("-","")
        if not aux.isnumeric():
            flag = True
        else:
            numb = int(lit)
    if numb < -256 or numb > 256:
        print(f"Error: Literal {numb} invalido. Linea: {counter}")
        return True,numb
    if flag:
        if operator not in labels:
            print(f"Error: Etiqueta {operator} invalida. Linea: {counter}")
            return True,numb
        else:
            return False,numb
    else:
        return flag,numb

def checkVariables(operator, counter):
    lit = operator
    flag = False
    numb = 0
    if '#' in lit:
        lit = lit.replace('#','')
        if not lit.isalnum():
            flag = True
        else:
            numb = int(lit,16)
    else:
        aux = lit.replace("-","")
        if not aux.isnumeric():
            flag = True
        else:
            numb = int(lit)
    if numb < -256 or numb > 256:
        print(f"Error: Literal {numb} invalido. Linea: {counter}")
        return True,numb
    if flag:
        if operator not in variables:
            print(f"Error: Data {operator} invalida. Linea: {counter}")
            return True,numb
        else:
            return False,numb
    else:
        return flag,numb

def main():
    data =  "palindromo.ass" ##input("Ingrese archivo .ass: ")
    flag0,count1 = readData(data)
    flag1 = checkFunciones(data)
    flag2,counter = leerCodigo(data)
    if not flag1 and not flag2 and not flag0:
        print("Archivo original valido")
        print(f"Numero de lineas en archivo original: {counter-1}")
        print(f"Numero de lineas de data: {count1}")
        print(f"Numero de lineas en codigo: {counter-3-count1-len(labels)}")
        archivoOut(data)
        archivoMem(data)
    

main()