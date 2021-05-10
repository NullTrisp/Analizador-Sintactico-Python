from LEX.Lex import Lex
from LEX.Lex import identifiers


class Synx:
    def __init__(self, lex):
        self.lex = lex
        lex.iterateString().iterateStates()

    def iterateIdent(self):
        idents = self.lex.getIdent()
        for index, token in enumerate(idents):
            if token == identifiers[0]:
                if index != len(idents) - 1:
                    raise TypeError("\n\nInvalid instruction!")
                else:
                    print("EOF")
            if token == identifiers[2] and idents[index + 1] == identifiers[1]:
                raise TypeError("\n\nInvalid instruction!")

        return self


try:
    Syntax = Synx(Lex(input("Please input string to check: "))).iterateIdent()

except TypeError as err:
    print(err)
