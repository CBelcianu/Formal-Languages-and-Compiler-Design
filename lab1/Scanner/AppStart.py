from Specs import *
from ProgramInternalForm import ProgramInternalForm
from SymbolTable import SymbolTable
from Scanner import tokenize, isIdentifier, isIntConstant, isCharConstant

fileName = 'p1.txt'
file = open(fileName, 'r')
lines = file.readlines()
symbolTable = SymbolTable()
pif = ProgramInternalForm()

counter = 0
for line in lines:
    counter += 1
    tokens = tokenize(line[0:-1], separators)
    i = 0
    while i in range(len(tokens)):
        if tokens[i] in toEncode:
            if tokens[i] == ' ':
                i += 1
            elif tokens[i] != '+' and tokens[i] != '-':
                pif.add(codification[tokens[i]], -1)
                i += 1
            elif (tokens[i] == '-' or tokens[i] == '+') and isIntConstant(tokens[i+1]) and tokens[i-1] in toEncode:
                pos = symbolTable.get(tokens[i]+tokens[i+1])
                if pos is None:
                    pos = symbolTable.add(int(tokens[i+1]), tokens[i]+tokens[i+1])
                pif.add(codification['constant'], pos)
                i += 2
            elif (tokens[i] == '-' or tokens[i] == '+') and isIdentifier(tokens[i+1]) and tokens[i-1] in toEncode:
                pos = symbolTable.get(tokens[i] + tokens[i + 1])
                if pos is None:
                    pos = symbolTable.add(len(tokens[i+1]), tokens[i] + tokens[i+1])
                pif.add(codification['constant'], pos)
                i += 2
            else:
                pif.add(codification[tokens[i]], -1)
                i += 1
        elif isIdentifier(tokens[i]):
            pos = symbolTable.get(tokens[i])
            if pos is None:
                pos = symbolTable.add(len(tokens[i]), tokens[i])
            pif.add(codification['identifier'], pos)
            i += 1
        elif isCharConstant(tokens[i]):
            pos = symbolTable.get(tokens[i])
            if pos is None:
                pos = symbolTable.add(ord(tokens[i].replace('\'','')), tokens[i])
            pif.add(codification['constant'], pos)
            i += 1
        elif isIntConstant(tokens[i]):
            pos = symbolTable.get(tokens[i])
            if pos is None:
                pos = symbolTable.add(ord(tokens[i].replace('\'', '')), tokens[i])
            pif.add(codification['constant'], pos)
            i += 1
        else:
            raise Exception('Unknown token ' + tokens[i] + ' at line ' + str(counter))

print('\nProgram Internal Form: \n', pif)
print('\nSymbol Table: \n', symbolTable)

print('\n\nCodification table: ')
for e in codification:
    print(e, " -> ", codification[e])
