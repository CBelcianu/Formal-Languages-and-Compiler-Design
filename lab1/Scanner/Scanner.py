from Specs import operators


def isIdentifier(token):
    return token[0].isalpha() and len(token) < 8


def isConstant(token):
    return token.isdigit() or (token[0] == '\'' and token[-1] == '\'')


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


def tokenResolver(line, separators):
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
