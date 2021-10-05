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
    if len(splitted) == 1:
        new = '(Dir)'
    if index == 0:
        new = '(Dir),'+str(splitted[1])
    else:
        new = str(splitted[0]) +',(Dir)'
    new = new.replace(" ","")
    return new

def checkBrackets(args):
    if args[0] == '(' and args[-1] == ')':
        return True

def parseDir(args):
    lit = ''
    splitted = args.split(',')
    for i in splitted:
        if checkBrackets(i):
            noBrackets = i.replace("(","").replace(")","")
            for char in noBrackets:
                lit+=char
    return lit

def transformLit(args):
    splitted = args.split(',')
    if splitted[0] != 'A' and splitted[0] != 'B':
        return 'Error'
    if (splitted[0] == 'A' and splitted[1] != 'B') or (splitted[0] == 'B' and splitted[1] != 'A'):
        return args
    new = str(splitted[0]) + ',Lit'
    return new



print(parseDir("(FSDF), 4"))
print(transformLit("A,B"))