from typing import List
from LEX.Lex import Lex
from LEX.Lex import identifiers

"""
<Programa> ::= <Instrucción> | <Programa> <Instrucción>
<Instrucción> ::= <Expresión> <term> | <Término> <term>
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
        self.getInstructions().termChange().compTermChange(
        ).compChange().igualChange().instrucChange().prograChange()
        print(self.result)

    def createInstructions(self, list: List) -> List:
        instructions = []
        instruction = []
        for token in list:
            if token == identifiers[0]:
                instruction.append(token)
                instructions.append(instruction)
                instruction = []
            else:
                instruction.append(token)

        return instructions

    def getInstructions(self):
        self.instructions = self.createInstructions(self.lex.getIdent())
        return self

    def termChange(self):
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
        return self

    def isCompTerm(self, token: str):
        return True if token == identifiers[4] or token == identifiers[5] or token == identifiers[7] or token == identifiers[8] or token == identifiers[9] or token == identifiers[10] else False

    def compTermChange(self):
        auxExpressions = self.expressions.copy()
        self.expressions = []
        auxExpression = []
        for expression in auxExpressions:
            for token in expression:
                if self.isCompTerm(token):
                    auxExpression.append(expressionIdentifies[10])
                else:
                    auxExpression.append(token)
            self.expressions.append(auxExpression)
            auxExpression = []

        return self

    def compChange(self):
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
        return self

    def igualChange(self):
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
        return self

    def instrucChange(self):
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
        return self

    def prograChange(self):
        for i, expresion in enumerate(self.expressions):
            if expresion[0] != expressionIdentifies[1]:
                aux = self.createInstructions(self.lex.getIdent())
                raise TypeError("Error in line " +
                                str(aux.index(aux[i]) + 1) + ": " + str(aux[i]))
        self.result = expressionIdentifies[0]


try:
    Syntax = Synx(Lex(input("Please input string to check: ")))

except TypeError as err:
    print(err)
