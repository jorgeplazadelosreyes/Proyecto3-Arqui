opcodes = ["MOV", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV", "CALL", "RET", "POP", "PUSH"]
jumps = ["JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV"]
functions = []

def leerCodigo(data):
    archivo = open(data, 'r')
    line = archivo.readline()
    counter = 1             ## Contador de lineas
    flag = False            ## flag si hay errores en el archivo 
    while(line):
        parsed = line.split(" ")
        if len(parsed) == 1:
            flag = checkFunciones(parsed, counter)
        else:
            flag = checkOpcodes(parsed, counter)
        line = archivo.readline()
        counter += 1
    archivo.close()


def leerData():
    pass

def checkFunciones(parsed, counter):
    call = parsed[0].replace('\n','')
    if call[-1] != ':':             ##revisa si tiene : al final
        print(f"Error: Syntax error, linea: {counter} ")
        return True
    call = call.replace(':','')
    if call in functions:
        print(f"Error: Redefinicion de funcion {call}, linea: {counter} ")
        return True     
    else:
        functions.append(call)      ##añade a functions
    return False

def checkOpcodes(parsed, counter):
    parsed[-1] = parsed[-1].replace('\n','')
    print(parsed)
    if parsed[0] != '' and parsed[1] != '':  ## revisa identacion
        print(f"Error: Error de identacion, linea: {counter}")
        return True
    if parsed[2] not in opcodes:             ## revisa instrucciones 
        print(f"Error: Instruccion {parsed[2]} no existe, linea: {counter}")
        return True
    return False
            

def archivoOut():
    print("hola")
    pass

def main():
    data =  "p3F_1.ass" ##input("Ingrese archivo .ass: ")
    leerCodigo(data)

main()