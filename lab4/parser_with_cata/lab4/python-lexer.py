import re
from slextree import Slextree
import sys

class Token:
    def __init__(self, ttype, value, lineno, index):
        self.ttype = ttype
        self.value = value
        self.lineno = lineno
        self.index = index

    def __str__(self):
        return f'Token(type=\'{self.ttype}\', value=\'{self.value}\', lineno={self.lineno}, index={self.index})'

def parse(line, lineno):
    keywords = ["if", "else", "while", "for", "def", "input", "print", "range", "true", "false", "and", "or", "not", "in", "range"]
    regex_expressions = {
        "COMMENT":  r'#.*',
        "STRING":   r'"[^\"]*|"[^\"]*"|\'[^\']*|\'[^\']*\'',
        "ID":       r'[a-zA-Z_][a-zA-Z0-9_]*',
        "NUMBER":   r'-?[1-9][0-9]*',
        "DIGIT":    r'-?[0-9]',
        "EQEQ":     r'\=\={0,1}',
        "LTE":      r'\<\={0,1}',
        "GTE":      r'\>\={0,1}',
        "EQ":       r'\=',
        "LT":       r'\<',
        "GT":       r'\>',
        "+":        r'\+',
        "-":        r'\-',
        "*":        r'\*',
        "/":        r'\/',
        "(":        r'\(',
        ")":        r'\)',
        "[":        r'\[',
        "]":        r'\]',
        ",":        r'\,',
        ":":        r'\:',
        "TAB":      r'\t',
        "SPACE":    r' ',
        "NEWLINE":  r'\n',
        ";":        r'\;',
        ".":        r'\.'
    }
    strict_regex_expressions = {
        "STRING":   r'"[^\"]*"|\'[^\']*\'',
        "EQEQ":     r'\=\=',
        "EQ":       r'\=',
        "ID":       r'[a-zA-Z_][a-zA-Z0-9_]{0,7}'
    }

    left = 0; right = 1; tokens = []
    while right <= len(line):
        found = False
        for rgx in regex_expressions:
            if re.fullmatch(regex_expressions[rgx], line[left:right]) is not None :
                while right <= len(line) and re.fullmatch(regex_expressions[rgx], line[left:right]) is not None :
                    right += 1

                # validate the regex with a more strict version, then either go back or signal an error
                validate = False
                new_regex = ""
                if rgx in strict_regex_expressions and re.fullmatch(strict_regex_expressions[rgx], line[left:right-1]) is None :
                    for strict_rgx in strict_regex_expressions:
                        if re.fullmatch(strict_regex_expressions[strict_rgx], line[left:right-1]) is not None :
                            validate = True; new_regex = strict_rgx
                    if validate: tokens.append(Token(new_regex, line[left:right-1], lineno, left))
                    else: tokens.append(Token("RLEXER ERROR", line[left:right-1], lineno, left))
                else:
                    if rgx == "ID" and line[left:right-1] in keywords:
                        tokens.append(Token("KEYWORD", line[left:right-1], lineno, left))
                    else: tokens.append(Token(rgx, line[left:right-1], lineno, left))
                left = right - 1; right = left + 1
                found = True; break
        if not found :
            tokens.append(Token("UNIDENTIFIED", line[left:right], lineno, left))
            left += 1; right = left + 1
    return tokens

def command_line():
    tokens = []
    line = ""
    lineno = 1
    while line != "exit":
        line = input("python > ")
        for token in parse(line, lineno):
            print(token)
            tokens.append(token)
        lineno += 1
    return tokens

def read_file(filename):
    tokens = []
    file = open(filename, "r")
    lineno = 1
    for line in file:
        for token in parse(line, lineno):
            print(token)
            tokens.append(token)
        lineno += 1
    return tokens

def write_pif(pif, filename):
    file = open(filename, "w")
    for p in pif:
        file.write(str(p))
        file.write("\n")
    file.close()

def write_symboltable(symt, filename):
    file = open(filename, "w")
    for s in symt.v[1:]:
        file.write(str(s))
        file.write("\n")
    file.close()

def pifify(tokens):
    codification = {
        "ID"        : 0, # idenfitier
        "STRING"    : 1, # all of them are constants
        "NUMBER"    : 1, # .
        "DIGIT"     : 1, # .
        "if"        : 2, 
        "else"      : 3,
        "while"     : 4, 
        "for"       : 5, 
        "def"       : 6, 
        "input"     : 7,
        "print"     : 8,
        "range"     : 9,
        "true"      :10,
        "false"     :11,
        "and"       :12,
        "or"        :13,
        "not"       :14,
        "EQEQ"      :15,
        "LTE"       :16,
        "GTE"       :17,
        "EQ"        :18,
        "LT"        :19,
        "GT"        :20,
        "+"         :21,
        "-"         :22,
        "*"         :23,
        "/"         :24,
        "("         :25,
        ")"         :26,
        "["         :27,
        "]"         :28,
        ","         :29,
        ":"         :30,
        "TAB"       :31,
        "SPACE"     :32,
        ";"         :33,
        "."         :34,
        "COMMENT"   :35,
        "UNIDENTIFIED": 36,
        "RLEXER ERROR": 37,
        "\'"        :38,
        "\""        :39,
        "NEWLINE"   :40,
        "in"        :41  
    }

    pif = []
    identifier_symbol_table = Slextree()
    constant_symbol_table = Slextree()
    for token in tokens:
        if token.ttype == "KEYWORD":
            pif.append({codification[token.value]: -1})
        else:
            if token.ttype == "ID":
                identifier_symbol_table.append(token)
                pos = identifier_symbol_table.search(token)
                pif.append({codification[token.ttype]: pos})
            elif token.ttype == "STRING" or token.ttype == "NUMBER" or token.ttype == "DIGIT":
                constant_symbol_table.append(token)
                pos = constant_symbol_table.search(token)
                pif.append({codification[token.ttype]: pos})
            else:
                if not token.ttype == "SPACE":
                    pif.append({codification[token.ttype]: -1})
    
    return pif, identifier_symbol_table, constant_symbol_table

def pifify2(tokens):
    codification = {
        "ID"        : 0, # idenfitier
        "STRING"    : 1, # all of them are constants
        "NUMBER"    : 1, # .
        "DIGIT"     : 1, # .
        "if"        : 2, 
        "else"      : 3,
        "while"     : 4, 
        "for"       : 5, 
        "def"       : 6, 
        "input"     : 7,
        "print"     : 8,
        "range"     : 9,
        "true"      :10,
        "false"     :11,
        "and"       :12,
        "or"        :13,
        "not"       :14,
        "EQEQ"      :15,
        "LTE"       :16,
        "GTE"       :17,
        "EQ"        :18,
        "LT"        :19,
        "GT"        :20,
        "+"         :21,
        "-"         :22,
        "*"         :23,
        "/"         :24,
        "("         :25,
        ")"         :26,
        "["         :27,
        "]"         :28,
        ","         :29,
        ":"         :30,
        "TAB"       :31,
        "SPACE"     :32,
        ";"         :33,
        "."         :34,
        "COMMENT"   :35,
        "UNIDENTIFIED": 36,
        "RLEXER ERROR": 37,
        "\'"        :38,
        "\""        :39,
        "NEWLINE"   :40,
        "in"        :41
    }

    pif = []
    identifier_symbol_table = Slextree()
    constant_symbol_table = Slextree()
    for token in tokens:
        if token.ttype == "KEYWORD":
            pif.append(codification[token.value])
        else:
            if token.ttype == "ID":
                identifier_symbol_table.append(token)
                pos = identifier_symbol_table.search(token)
                pif.append(codification[token.ttype])
            elif token.ttype == "STRING" or token.ttype == "NUMBER" or token.ttype == "DIGIT":
                constant_symbol_table.append(token)
                pos = constant_symbol_table.search(token)
                pif.append(codification[token.ttype])
            else:
                if not token.ttype == "SPACE":
                    pif.append(codification[token.ttype])
    
    return pif, identifier_symbol_table, constant_symbol_table

def main():
    method = input("method: ")
    if method == "cmd" :
        tokens = command_line()
    else:
        print(sys.argv[0])
        tokens = read_file(sys.argv[1])
    pif, identifier_symbol_table, constant_symbol_table = pifify2(tokens)
    write_pif(pif, "pif.txt")
    write_symboltable(identifier_symbol_table, "identifiers.txt")
    write_symboltable(constant_symbol_table, "constants.txt")

main()
