opcodes = ["MOV", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV", "CALL", "RET", "POP", "PUSH"]
jumps = ["JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV"]
basics = ["MOV", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC"]
directions = ["MOV", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP"]
functions = []
variables = []

## SE CONSIDERA INDENTACION EN ESTE ASSEMBLER DE DOS ESPACIOS PARA OPERACIONES Y DEFINICION DE VARIABLES
## CAPS SENSITIVE

def leerCodigo(data):
    archivo = open(data, 'r')
    line = archivo.readline()
    line = archivo.readline()
    counter = 1             ## Contador de lineas
    flag = False            ## flag si hay errores en el archivo 
    while(line):
        parsed = line.split(" ")
        if len(parsed) > 1:
            flag = checkOpcodes(parsed, counter)
        line = archivo.readline()
        counter += 1
    archivo.close()
    return flag


def leerData():
    pass

def checkFunciones(data):   ## crea lista con funciones presentes en el archivo 
    archivo = open(data, 'r')
    line = archivo.readline()
    line = archivo.readline()
    counter = 1
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
    ##print(parsed)
    if parsed[0] != '' and parsed[1] != '':  ## revisa identacion
        print(f"Error: Error de identacion, linea: {counter}")
        return True
    if parsed[2] not in opcodes:             ## revisa instrucciones 
        print(f"Error: Instruccion {parsed[2]} no existe, linea: {counter}")
        return True
    if parsed[2] in jumps:
        return checkJumps(parsed[3:], counter)
    operator = uniteString(parsed[3:])
    if '(' in operator or ')' in operator:
        checkDiretionning(operator, counter)
    else:
        checkBasics(operator, counter)

def uniteString(args):
    unite = ''
    for arg in args:
        unite+= arg
    unite.replace(" ","")
    return unite

def checkBasics(args, counter):
    pass

def checkDiretionning(args, counter):
    pass

def checkJumps(args, counter):
    if len(args) > 1:
        print(f"Error: Muchos argumentos. Linea: {counter}")
        return True
    if args[0] not in functions:
        print(f"Error: Funcion {args[0]} no existe. Linea: {counter}") 
        return True
    return False

def archivoOut():
    print("hola")
    pass

def main():
    flag = False
    data =  "p3F_1.ass" ##input("Ingrese archivo .ass: ")
    flag = checkFunciones(data)
    flag = leerCodigo(data)
    print(flag)
    

main()