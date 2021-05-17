from LEX.LexError import LexError
from SynxError import SynxError
from LEX.Lex import Lex
from LEX.Lex import identifiers

"""
<Programa> ::= <Instrucción> | <Programa> <Instrucción>
<Instrucción> ::= <Igualdad> <term> | <Comparación> <term> | <Término> <term>
<Igualdad> ::= <var> <eqTo> <Término>
<Comparación> ::= <Término> <compOp> <Término>
<Término> ::= <num> | <Comparación> | <var> 


(1) <var> | <num> -> <Término>      *<var> <eqTo> | <var> <TERM> (do not change)
(2) <eqTo> | <GreatT> | <LessT> | <EqualT> | <GreEqT> | <LesEqT> | <DiffT> -> <compOp>
(3) <Término> <copmOp> <Término> -> <Comparación>

(4) <var> <eqTo> <Término> | <var> <eqTo> <Comparación> -> <Igualdad>
(5) <Igualdad> <term> | <Comparación> <term> -> <Instrucción>

jsf3=43;df5=17;dsfa=jsf3>=df5;var;;

"""

expressionIdentifies = ["<Programa>",
                        "<Instrucción>",
                        "<Expresión>",
                        "<TERM>",
                        "<Expresión>",
                        "<Igualdad>",
                        "<Comparación>",
                        "<var>",
                        "<eqTo>",
                        "<Término>",
                        "<compOp>",
                        "<num>",
                        ]


class Synx:
    def __init__(self, lex: Lex):
        self.lex = lex
        self.expressions = []
        self.getInstructions().createTermino().createCompOp(
        ).createComparacion().createIgualdad().instrucChange().createPrograma()

    def printLines(self, list: list) -> None:
        for i, tokens in enumerate(list):
            if i < len(list) - 1:
                print(f"line {i+1}: {tokens}")
            else:
                print(f"line {i+1}: {tokens}", end="\n\n")

    def getInstructions(self):
        """metod to slice the lex result into instructions (each instruction ends with <term> token"""
        instructions = []
        instruction = []
        for token in self.lex.getIdent():
            if token == identifiers[0]:
                instruction.append(token)
                instructions.append(instruction)
                instruction = []
            else:
                instruction.append(token)
        self.instructions = instructions
        print("Init instructions: ")
        self.printLines(self.instructions)
        return self

    def createTermino(self):
        """
        method to change from ( <var> | <num> ----> <Término> ) 

        This will not change ( <var> <eqTo> | <var> <TERM> )
        """
        for instruction in self.instructions:
            instrucExpression = []
            for i, token in enumerate(instruction):
                if token == identifiers[2]:
                    instrucExpression.append(expressionIdentifies[9])
                elif token == identifiers[1]:
                    if i != len(instruction) and instruction[i + 1] != identifiers[3]:
                        instrucExpression.append(expressionIdentifies[9])
                    else:
                        instrucExpression.append(expressionIdentifies[7])
                else:
                    instrucExpression.append(token)
            self.expressions.append(instrucExpression)

        print("Instructions with <Término>: ")
        self.printLines(self.expressions)
        return self

    def isCompToken(self, token: str):
        """method to check if token is a <compOp>"""
        return True if token == identifiers[4] or token == identifiers[5] or token == identifiers[7] or token == identifiers[8] or token == identifiers[9] or token == identifiers[10] else False

    def createCompOp(self):
        """method to change from ( <eqTo> | <GreatT> | <LessT> | <EqualT> | <GreEqT> | <LesEqT> | <DiffT> ----> <compOp> )"""
        auxExpressions = self.expressions.copy()
        self.expressions = []
        auxExpression = []
        for expression in auxExpressions:
            for token in expression:
                if self.isCompToken(token):
                    auxExpression.append(expressionIdentifies[10])
                else:
                    auxExpression.append(token)
            self.expressions.append(auxExpression)
            auxExpression = []

        print("Instructions with <compOp>: ")
        self.printLines(self.expressions)
        return self

    def createComparacion(self):
        """method to change from ( <Término> <copmOp> <Término> ----> <Comparación> )"""
        auxExpressions = self.expressions.copy()
        self.expressions = []
        auxExpression = []
        skip = False
        counter = 0
        for expression in auxExpressions:
            for i, token in enumerate(expression):
                if not skip:
                    if i <= len(expression) - 3 and token == expressionIdentifies[9] and expression[i+1] == expressionIdentifies[10] and expression[i+2] == expressionIdentifies[9]:
                        auxExpression.append(expressionIdentifies[6])
                        skip = True
                    else:
                        auxExpression.append(token)
                else:
                    counter += 1
                    if counter == 2:
                        skip = False
                        counter = 0
            self.expressions.append(auxExpression)
            auxExpression = []

        print("Instructions with <Comparación>: ")
        self.printLines(self.expressions)
        return self

    def createIgualdad(self):
        """method to change from ( <var> <eqTo> <Término> | <var> <eqTo> <Comparación> -> <Igualdad> )"""
        auxExpressions = self.expressions.copy()
        self.expressions = []
        auxExpression = []
        skip = False
        counter = 0
        for expression in auxExpressions:
            for i, token in enumerate(expression):
                if not skip:
                    if i <= len(expression) - 3 and token == expressionIdentifies[7] and expression[i + 1] == expressionIdentifies[8] and (expression[i + 2] == expressionIdentifies[9] or expression[i + 2] == expressionIdentifies[6]):
                        auxExpression.append(expressionIdentifies[5])
                        skip = True
                    else:
                        auxExpression.append(token)
                else:
                    counter += 1
                    if counter == 2:
                        skip = False
                        counter = 0
            self.expressions.append(auxExpression)
            auxExpression = []

        print("Instructions with <Igualdad>: ")
        self.printLines(self.expressions)
        return self

    def instrucChange(self):
        """method to change from ( <Igualdad> <term> | <Comparación> <term> -> <Instrucción> )"""
        auxExpressions = self.expressions.copy()
        self.expressions = []
        auxExpression = []
        skip = False
        counter = 0
        for expression in auxExpressions:
            for i, token in enumerate(expression):
                if not skip:
                    if i <= len(expression) - 2 and (token == expressionIdentifies[5] or token == expressionIdentifies[6] or token == expressionIdentifies[9]) and expression[i + 1] == expressionIdentifies[3]:
                        auxExpression.append(expressionIdentifies[1])
                        skip = True
                    else:
                        auxExpression.append(token)
                else:
                    counter += 1
                    if counter == 1:
                        skip = False
                        counter = 0
            self.expressions.append(auxExpression)
            auxExpression = []

        print("Instructions with <Instrucción>: ")
        self.printLines(self.expressions)
        return self

    def createPrograma(self):
        """method check programa"""
        for i, expresion in enumerate(self.expressions):
            if expresion[0] != expressionIdentifies[1]:
                aux = self.instructions
                raise SynxError("Error in line " +
                                str(aux.index(aux[i]) + 1) + ": " + str(aux[i]))
        self.result = expressionIdentifies[0]
        print(
            f"Code has been checked and is valid!: {self.result}", end="\n\n")


exit = False
while(not exit):
    try:
        print("Synx:\n[1] => Analyze string\n[2] => Exit", end="\n\n")
        option = int(input("Please input what to do: "))
        if option == 1:
            Syntax = Synx(Lex(input("Please input string to check: ")))
        elif option == 2:
            exit = True
        else:
            print("SELECT A VALID OPTION!", end="\n\n")

    except SynxError as err:
        print(err, end="\n\n")
    except LexError as err:
        print(err, end="\n\n")
    except ValueError:
        print("SELECT A VALID OPTION!", end="\n\n")
