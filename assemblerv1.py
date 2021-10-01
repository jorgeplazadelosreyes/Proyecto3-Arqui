opcodes = ["MOV", "SUB", "AND", "OR", "NOT", "XOR", "SHL", "SHR", "INC", "RST", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "JGE", "JLE", "JCR", "JOV"]
functions = []

def leerArchivo(data):
    archivo = open(data, 'r')
    line = archivo.readline()
    while(line):
        parsed = line.split(" ")
        if '' in parsed:
            parsed.remove('')
        print(parsed)
        line = archivo.readline()
    archivo.close()


def parser():
    pass

def error():
    pass

def archivoOut():
    print("hola")
    pass

def main():
    data =  "p3F_1.ass" ##input("Ingrese archivo .ass: ")
    leerArchivo(data)

main()