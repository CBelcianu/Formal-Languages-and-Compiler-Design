class FA:
    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    def isState(self, value):
        return value in self.Q

    @staticmethod
    def parseLineForStatesOrSymbols(line):
        values = []
        for value in line.strip().split('=')[1].strip()[1:-1].strip().split(','):
            values.append(value.strip())
        return values

    @staticmethod
    def parseInputFotStatesOrSymbols(line):
        values = []
        for value in line.strip()[1:-1].strip().split(','):
            values.append(value.strip())
        return values

    @staticmethod
    def readFromFile(filename):
        with open(filename) as file:
            Q = FA.parseLineForStatesOrSymbols(file.readline())
            E = FA.parseLineForStatesOrSymbols(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = FA.parseLineForStatesOrSymbols(file.readline())

            res = ""
            for line in file:
                res += line

            S = FA.parseTransitions(FA.parseLineForStatesOrSymbols(res))

            return FA(Q, E, S, q0, F)

    @staticmethod
    def readFromInput():
        Q = FA.parseInputFotStatesOrSymbols(input('Q = '))
        E = FA.parseInputFotStatesOrSymbols(input('E = '))
        q0 = input('q0 = ')
        F = FA.parseInputFotStatesOrSymbols(input('F = '))

        S = FA.parseTransitions(FA.parseInputFotStatesOrSymbols(input('S = ')))

        return FA(Q, E, S, q0, F)

    @staticmethod
    def parseTransitions(parts):
        result = []
        transitions = []
        index = 0

        while index < len(parts):
            transitions.append(parts[index] + ',' + parts[index + 1])
            index += 2

        for transition in transitions:
            lhs, rhs = transition.split('->')
            state2 = rhs.strip()
            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

            result.append(((state1, route), state2))

        return result

    @staticmethod
    def translateFromRG(rg):
        if not rg.isRegular():
            print("grammar is not regular")
            return
        Q = rg.N + ['K']
        E = rg.E
        q0 = rg.S
        F = ['K']

        S = []

        for production in rg.P:
            state2 = 'K'
            state1, rhs = production
            if state1 == q0 and rhs[0] == 'E':
                F.append(q0)
                state2 = q0

            route = rhs[0]

            if len(rhs) == 2:
                state2 = rhs[1]

            S.append(((state1, route), state2))

        return FA(Q, E, S, q0, F)

    def getTransitionsFor(self, state):
        if not self.isState(state):
            raise Exception('Can only get transitions for states')

        return [trans for trans in self.S if trans[0][0] == state]

    def showTransitionsFor(self, state):
        transitions = self.getTransitionsFor(state)

        print('{ ' + ' '.join([' -> '.join([str(part) for part in trans]) for trans in transitions]) + ' }')

    def __str__(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n'
