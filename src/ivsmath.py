

expression = "5+5"  # input()


class Precedence():
    PLUS = 1
    MINUS = 1
    MUL = 2
    DIV = 2
    POW = 3
    ROOT = 3
    FAC = 4


class Operator():
    def __init__(self, char):
        self.char = char

    def get_eval(self):
        match self.char:
            case "+":
                return Precedence.PLUS
            case "-":
                return Precedence.MINUS
            case "*":
                return Precedence.MUL
            case "/":
                return Precedence.DIV
            case "^":
                return Precedence.POW
            case "r":
                return Precedence.ROOT
            case "!":
                return Precedence.FAC
            case _:
                print("error Operator.get_eval")
                return 0

    def __le__(self, other):
        return self.get_eval() <= other.get_eval()

    def __ge__(self, other):
        return self.get_eval() >= other.get_eval()


def get_infix(string):
    infix = []
    number = ""
    operators = ["+", "-", "*", "/", "^", "r", "!", "?"]
    for char in string:
        if char.isdigit() or char == '.':
            number += char
        elif char in operators:
            number = float(number)
            infix.append(number)
            number = ""
            infix.append(char)
        else:
            print("Error get_infix")
    infix.append(float(number))
    return infix


def get_postfix(infix):
    postfix = []
    stack = []
    for i in infix:
        if isinstance(i, float):
            postfix.append(i)
        else:
            while (len(stack) != 0 and Operator(stack[-1]) >= Operator(i)):
                postfix.append(stack.pop())
            stack.append(i)
    while len(stack) != 0:
        postfix.append(stack.pop())
    return postfix


def str_to_postfix(string):
    return get_postfix(get_infix(string))


print("print:", str_to_postfix(expression))
