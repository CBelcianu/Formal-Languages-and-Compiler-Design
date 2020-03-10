import json, copy, re


class ContextFreeGrammar:
    _default_filename = "input.json"
    _starting_symbol = "starting symbol"
    _terminals = "terminals"
    _non_terminals = "non terminals"
    _production_rules = "production rules"
    _command_file_flag = False

    def __init__(self, filename=_default_filename, grammar_name=""):
        self.starting_symbol = None
        self.terminals = []
        self.non_terminals = []
        self.production_rules = []
        self.grammar_name = grammar_name
        self.load(filename)

    def is_non_terminal(self, value):
        return value in self.non_terminals

    def is_terminal(self, value):
        return value in self.terminals

    def get_productions_for(self, non_terminal):
        if not self.is_non_terminal(non_terminal):
            raise Exception('Can only show productions for non-terminals.')
        return [prod for prod in self.production_rules if prod[0] == non_terminal]

    def show_productions_for(self, non_terminal):
        productions = self.get_productions_for(non_terminal)
        print(', '.join([' -> '.join(prod) for prod in productions]))

    def _json(self, p):
        self.starting_symbol = p[ContextFreeGrammar._starting_symbol]
        for terminal in p[ContextFreeGrammar._terminals]: self.terminals.append(terminal)
        for non_terminal in p[ContextFreeGrammar._non_terminals]: self.non_terminals.append(non_terminal)
        for rule in p[ContextFreeGrammar._production_rules]:
            aux = rule[1][0].split(' ')
            reslst = []
            if len(aux)>1:
                for x in aux:
                     reslst.append(x)
                self.production_rules.append((rule[0], reslst))
            else:
                self.production_rules.append((rule[0], [aux[0]]))

    def load(self, filename=_default_filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            self._json(data[self.grammar_name])

    def __str__(self):
        return "\nContextFreeGrammar: { Starting symbol: " + str(self.starting_symbol) + "\n" + \
               "\t\tProduction rules: " + str([str(r) for r in self.production_rules]) + "\n" + \
               "\t\tTerminals: " + str(self.terminals) + "\n" + \
               "\t\tNon-Terminals: " + str(self.non_terminals) + " }\n"
