from Specs import *
from ProgramInternalForm import ProgramInternalForm
from Scanner import tokenize, isIdentifier, isConstant
from SymbolTable import SymbolTable


fileName = "p1.txt"
file = open(fileName, 'r')

symbolTable = SymbolTable()
indetifierTable=SymbolTable()
pif = ProgramInternalForm()

with open(fileName, 'r') as file:
    lineNo = 0
    for line in file:
        lineNo += 1
        for token in tokenize(line[0:-1], separators):
            if token in toEncode[2:]:
                pif.add(codification[token], -1)
            elif isIdentifier(token):
                uid = indetifierTable.add(token)
                pif.add(codification['identifier'], uid)
            elif isConstant(token):
                uid = symbolTable.add(token) if token.replace('\'', '').replace('-', '').replace('+', '').isdigit()\
                    else symbolTable.add(token)
                pif.add(codification['constant'], uid)
            else:
                raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

print('\nProgram Internal Form: \n', pif)
print('\nConstant Table: \n', symbolTable)
print('\nIdentifier Table: \n', indetifierTable)

print('\n\nCodification table: ')
for e in codification:
    print(e, " -> ", codification[e])
