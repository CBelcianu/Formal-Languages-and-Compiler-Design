from Specs import operators


def isIdentifier(token):
    return token[0].isalpha() and len(token) < 8


def isConstant(token):
    return token.isdigit() or (token[0] == '\'' and token[-1] == '\'') or (token[0] == '-' or token[0] == '+' and token[1:].isdigit())


def isPartOfOperator(char):
    for op in operators:
        if char in op:
            return True
    return False


def fetchToken(line, index):
    token = ''
    quoteCount = 0

    while index < len(line) and quoteCount < 2:
        if line[index] == '"':
            quoteCount += 1
        token += line[index]
        index += 1

    return token, index


def fetchOperator(line, index):
    token = ''

    while index < len(line) and isPartOfOperator(line[index]):
        token += line[index]
        index += 1

    return token, index


def tokenize(line, separators):
    token = ''
    index = 0

    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = fetchToken(line, index)
            yield token
            token = ''

        elif isPartOfOperator(line[index]):
            if line[index-1].isdigit():
                yield token
                token = ''
            index1 = index
            spaceCnt = 0
            if line[index1] == '+' or line[index1] == '-':
                if line[index1+1].isdigit():
                    spaceCnt = 1
                while (line[index1].isdigit() or line[index1] == ' ' or isPartOfOperator(line[index1])) and spaceCnt < 2:
                    if line[index1].isdigit() or isPartOfOperator(line[index1]):
                        token += line[index1]
                        index1 += 1
                    elif line[index1] == ' ':
                        spaceCnt += 1
                        index1 += 1
                index = index1
                spaceCnt = 0
            else:
                if token:
                    yield token
                token, index = fetchOperator(line, index)
                yield token
                token = ''

        elif line[index] in separators:
            if token:
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''

        else:
            token += line[index]
            index += 1
    if token:
        yield token
