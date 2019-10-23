from Specs import *
from ProgramInternalForm import ProgramInternalForm
from Scanner import tokenize, isIdentifier, isConstant
from SymbolTable import SymbolTable


fileName = "p1.txt"
file = open(fileName, 'r')

symbolTable = SymbolTable()
pif = ProgramInternalForm()

with open(fileName, 'r') as file:
    lineNo = 0
    for line in file:
        lineNo += 1
        for token in tokenize(line[0:-1], separators):
            if token in toEncode[2:]:
                pif.add(codification[token], -1)
            elif isIdentifier(token):
                uid = symbolTable.add(len(token), token)
                pif.add(codification['identifier'], uid)
            elif isConstant(token):
                uid = symbolTable.add(int(token.replace('\'', '').replace('-', '').replace('+', '')), token) if token.replace('\'', '').replace('-', '').replace('+', '').isdigit()\
                    else symbolTable.add(ord(token.replace('\'', '')), token)
                pif.add(codification['constant'], uid)
            else:
                raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

print('\nProgram Internal Form: \n', pif)
print('\nSymbol Table: \n', symbolTable)

print('\n\nCodification table: ')
for e in codification:
    print(e, " -> ", codification[e])
