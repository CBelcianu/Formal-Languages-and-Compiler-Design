separators = ['[', ']', '{', '}', '(', ')', ';', ' ']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=', '++', '--']
reservedWords = ['int', 'char', 'while', 'if', 'else', 'printf', 'scanf', 'return', 'for', 'main']

toEncode = ['identifier', 'constant'] + separators + operators + reservedWords
codification = dict([(toEncode[i], i) for i in range(len(toEncode))])
