from grammar import ContextFreeGrammar
from parser import Lr0Parser

grammar = ContextFreeGrammar("input.json", "example")
parser = Lr0Parser(grammar)

def display_cannonical_states():
    print("\nBelow is the cannonical collection: ")
    state_index = 0
    cannonical_collection = parser.get_canonical_collection()
    for state in cannonical_collection:
        print('s' + str(state_index) + ' = ' + str([x[0] + '->' + str(''.join(x[1])) for x in state]))
        state_index += 1

def parsing_an_input_sequence(sequence):
    print("\nParsing the input sequence: " + str(sequence))
    out = parser.parse(sequence)
    res = ""
    for i in out:
        aux = ""
        for c in grammar.production_rules[int(i)][1]:
            aux += c
        if res == "":
            res += grammar.production_rules[int(i)][0] + '->' + aux
        else:
            res += ', ' + grammar.production_rules[int(i)][0] + '->' + aux

    print("\nHow we got there: ")
    for production in res.split(", "):
        print(production)


all_good = True
print("\nAC Grammar Homework:\n1. Simple grammar from seminar:")
display_cannonical_states()
parsing_an_input_sequence(['a','b','b','c'])

try:
    print("\n2. Our grammar:")
    grammar = ContextFreeGrammar("input.json", "alex's grammar")
    parser = Lr0Parser(grammar)

    # # a = 2
    # parsing_an_input_sequence(['0', '18', '1', '40'])

    # # b = 1 + 2
    # parsing_an_input_sequence(['0', '18', '1', '21', '1', '40'])

    # # b = 1 + 2 - 10
    # parsing_an_input_sequence(['0', '18', '1', '21', '1', '22', '1', '40'])

    # # print(a)
    # parsing_an_input_sequence(['8', '25', '0', '26', '40'])

    # # print("ana are mere")
    # parsing_an_input_sequence(['8', '25', '1', '26', '40'])

    # # for a in_range(4): 
    # #   print(a)
    # parsing_an_input_sequence(['5', '0', '41', '9', '25', '1', '26', '40', '31', '8', '25', '0', '26', '40'])

    # # while a > 1: print(a)
    # parsing_an_input_sequence(['4', '0', '15', '1', '30', '31', '8', '25', '0', '26', '40'])

    # # if a > 1: print(a)
    # parsing_an_input_sequence(['2', '0', '15', '1', '30', '31', '8', '25', '0', '26', '40'])

    # # def foobar(): 
    # #   for a in range 4: 
    # #   print(a)
    # # foobar()
    # parsing_an_input_sequence(['6', '0', '25', '26', '30', '40', '31', '5', '0', '41', '9', '25', '1', '26', '30', '40', '31', '8', '25', '0', '26', '40', '0', '25', '26', '40'])

    input_sequence_line = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2']
    parsing_an_input_sequence(['5', '0', '41', '9', '25', '1', '26', '30', '40', '31', '8', '25', '0', '26', '40'])
    for x in parser.get_table():
        print(x)


except Exception as exc:
    print(exc)
    index_in_additional_info = str(exc).split('shift: ')[1]
    print("Symbol position in input stack: " + index_in_additional_info)
    print("Lexical error at line: " + 
            str(input_sequence_line[int(index_in_additional_info)]))
    all_good = False

if all_good:
    print("\n\n{'status': 'good'}")
