from LEX.Lex import Lex
from LEX.LexError import LexError
from Synx import Synx
from SynxError import SynxError

"""
jsf3=43;df5=17;dsfa=jsf3>=df5;var;;
"""
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
