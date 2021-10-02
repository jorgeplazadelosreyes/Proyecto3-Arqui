opcodes = ["MOV", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV", "CALL", "RET", "POP", "PUSH"]
functions = []

def leerCodigo(data):
    archivo = open(data, 'r')
    line = archivo.readline()
    counter = 1             ## Contador de lineas
    flag = False            ## flag si hay errores en el archivo 
    while(line):
        parsed = line.split(" ")
        print(parsed)
        if len(parsed) == 1:
            call = parsed[0].replace('\n','').replace(':','')
            if call not in functions:
                functions.append(call)
            else:
                print(f"Error: Redefinicion de funcion {call}, linea: {counter} ")
                flag = True

        line = archivo.readline()
        counter += 1
    archivo.close()


def leerData():
    pass

def error():
    pass

def archivoOut():
    print("hola")
    pass

def main():
    data =  "p3F_1.ass" ##input("Ingrese archivo .ass: ")
    leerCodigo(data)

main()