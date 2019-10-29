from Specs import operators
import re


def isIdentifier(token):
    return re.match('^([_])?[a-zA-Z]([a-zA-Z]|[0-9]){,7}$', token) is not None


def isCharConstant(token):
    return re.match('^\'([a-zA-Z])\'$', token) is not None


def isIntConstant(token):
    return re.match('^[1-9][0-9]*$', token) is not None or re.match('^0$', token) is not None


def isPartOfOperator(char):
    for op in operators:
        if char in op:
            return True
    return False


def fetchOperator(line, index):
    token = ''

    while index < len(line) and isPartOfOperator(line[index]) and isPartOfOperator(token+line[index]):
        token += line[index]
        index += 1

    return token, index


def fetchString(line, index):
    token = ''
    quote_count = 0

    while index < len(line) and quote_count < 2:
        if line[index] == "'":
            quote_count += 1
        token += line[index]
        index += 1

    return token, index


def tokenize(line, separators):
    token = ""
    index = 0
    tokens = []

    while index < len(line):
        if line[index] == "'":
            if token:
                tokens.append(token)
            token, index = fetchString(line, index)
            tokens.append(token)
            token = ''

        elif isPartOfOperator(line[index]):
            if token:
                tokens.append(token)
            token, index = fetchOperator(line, index)
            tokens.append(token)
            token = ''
        elif line[index] in separators:
            if token:
                tokens.append(token)
            token, index = line[index], index + 1
            tokens.append(token)
            token = ''

        else:
            token += line[index]
            index += 1

    if token:
        tokens.append(token)

    return tokens
