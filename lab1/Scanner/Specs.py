separators = ['[', ']', '{', '}', '(', ')', ';', ' ',',','<<','>>','#']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=', '++', '--','++']
reservedWords = ['int', 'char', 'while', 'if', 'else', 'cout', 'cin', 'return', 'for', 'main','include','iostream','cmath','using','namespace','std']

toEncode = ['identifier', 'constant'] + separators + operators + reservedWords
codification = dict([(toEncode[i], i) for i in range(len(toEncode))])
