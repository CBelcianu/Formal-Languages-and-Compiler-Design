from FA import FA
from RG import RG

if __name__ == '__main__':
    def printMenu():
        print("1. Grammar")
        print("2. Finite automaton")
        print("0. Exit")


    def printMenuRG():
        print("\n1. Read grammar from file")
        print("2. Read grammar from console")
        print("3. See the non-terminals of the grammar")
        print("4. See the terminals of the grammar")
        print("5. See the set of productions of the grammar")
        print("6. See the starting symbol of the grammar")
        print("7. See the set of productions for a given non-terminal of the grammar")
        print("8. Check if the grammar is regular")
        print("9. Construct the finite automaton from the given grammar")
        print("0. Back\n")


    def printMenuFA():
        print("\n1. Read finite automaton from file")
        print("2. Read finite automaton from console")
        print("3. See the set of states of the finite automaton")
        print("4. See the alphabet of the finite automaton")
        print("5. See the set of transitions of the finite automaton")
        print("6. See the initial state of the finite automaton")
        print("7. See the set of final states of the finite automaton")
        print("8. Construct the regular grammar from the given finite automaton")
        print("0. Back\n")

    def menuRG(g):
        printMenuRG()
        option = input("Choose a option: ")
        if option == '1':
            filename = input("Give the filename: ")
            g = RG.readFromFile(filename)
            menuRG(g)
        elif option == '2':
            g = RG.readFromInput()
            menuRG(g)
        elif option == '3':
            print(g.N)
            menuRG(g)
        elif option == '4':
            print(g.E)
            menuRG(g)
        elif option == '5':
            nonterms = set()
            for production in g.P:
                nonterms.add(production[0])
            for nonterm in nonterms:
                g.showProductionsFor(nonterm)
            menuRG(g)
        elif option == '6':
            print(g.S)
            menuRG(g)
        elif option == '7':
            symbol = input("Give the symbol: ")
            result = g.getProductionsFor(symbol)
            if isinstance(result, list):
                for rule in result:
                    print(rule[0] + " -> " + rule[1])
            else:
                print(result)
            menuRG(g)
        elif option == '8':
            print(g.isRegular())
            menuRG(g)
        elif option == '9':
            fa = FA.translateFromRG(g)
            if isinstance(fa, FA):
                print("Set of states")
                print(fa.Q)
                print("Alphabet")
                print(fa.E)
                print("Set of transitions")
                for transition in fa.S:
                    print('(' + transition[0][0] + ", " + transition[0][1] + ") -> " + transition[1])
                print("Initial state")
                print(fa.q0)
                print("Set of final states")
                print(fa.F)
            else:
                print(fa)
            menuRG(g)
        elif option == '0':
            main()
        else:
            print("No such option")
            menuRG(g)

    def menuFA(fa):
        printMenuFA()
        option = input("Choose a option: ")
        if option == '1':
            filename = input("Give the filename: ")
            fa = FA.readFromFile(filename)
            menuFA(fa)
        elif option == '2':
            fa = FA.readFromInput()
            menuFA(fa)
        elif option == '3':
            print(fa.Q)
            menuFA(fa)
        elif option == '4':
            print(fa.E)
            menuFA(fa)
        elif option == '5':
            for transition in fa.S:
                print('(' + transition[0][0] + ", " + transition[0][1] + ") -> " + transition[1])
            menuFA(fa)
        elif option == '6':
            print(fa.q0)
            menuFA(fa)
        elif option == '7':
            print(fa.F)
            menuFA(fa)
        elif option == '8':
            g = RG.translateFromFA(fa)
            print("Set of non-terminal symbols")
            print(g.N)
            print("Set of terminal symbols")
            print(g.E)
            print("Set of productions")
            for rule in g.P:
                print(rule[0] + " -> " + rule[1])
            print("Starting symbol")
            print(g.S)
            menuFA(fa)
        elif option == '0':
            main()
        else:
            print("No such option")
            menuFA(fa)


    def main():
        rg = RG.readFromFile('rg1.txt')
        fa = FA.readFromFile('fa1.txt')
        printMenu()
        option = input("Choose a option: ")
        if option == '1':
            menuRG(rg)
        elif option == '2':
            menuFA(fa)
        elif option == '0':
            return
        else:
            print("No such option")
            main()

    main()

