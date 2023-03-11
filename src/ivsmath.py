##
# @file ivsmath.py
# @authors
# @brief Handling of math expressions

# expression = input()


class Precedence():
    """
    @brief Precedence enum
    contains operators and their precedence 
    """
    PLUS = 1
    MINUS = 1
    MUL = 2
    DIV = 2
    POW = 3
    RADICAL = 3
    FAC = 4


class Operator():
    """
    @brief Operator class for comparing precedences
    """

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
                return Precedence.RADICAL
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
    """
    @brief It takes a string and returns the infix expression.

    @param string The string to be converted to infix
    @return infix list
    """
    infix = []
    number = ""
    operators = ["+", "-", "*", "/", "^", "r", "!", "?"]
    for char in string:
        if char.isdigit() or char == '.':
            number += char
        elif char in operators:
            if number != "":
                number = float(number)
                infix.append(number)
                number = ""
            infix.append(char)
        else:
            print("Error get_infix")
    if number != "":
        infix.append(float(number))
    return infix


def get_postfix(infix):
    """
    @brief It converts infix to postfix

    @param infix The infix expression to be converted to postfix
    @return postfix list
    """
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


def division(a, b):
    """
    @brief It divides b by a

    @param a The number to divide by
    @param b The first number
    @returns @p b / @p a
    """
    if a == 0:
        print("division by zero in division")
    else:
        return b/a


def radical(a, b):
    """
    @brief It calculates the radical.

    @param b The index
    @param a The radicand
    @return the @p a root of @p b
    """
    if b > 0:
        print("Value error in radical function")
    elif a == 0:
        print("Value error in radical function")
    else:
        return b ** (1.0/a)


def factorial(a):
    """
    @brief It calculates the factorial.

    @param a The number to find the factorial of
    @return factorial of @p a
    """
    if a % 1 != 0 or a < 0:
        print("Value error in factorial function")
    sum = 1
    for i in range(2, int(a)+1):
        sum *= i
    return sum


def handle_operation(stack, operator):
    """
    @brief It handles the operations for evaluate_postfix

    @param stack a list of numbers
    @param operator The operator to be applied to the stack.
    """
    match operator:
        case "+":
            tmp = stack.pop()+stack.pop()
        case "-":
            tmp = -(stack.pop())+stack.pop()
        case "*":
            tmp = stack.pop()*stack.pop()
        case "/":
            tmp = division(stack.pop(), stack.pop())
        case "^":
            tmp = stack.pop()**stack.pop()
        case "r":
            tmp = radical(stack.pop(), stack.pop())
        case "!":
            tmp = factorial(stack.pop())
        case _:
            print("Not implemented yet")
    stack.append(tmp)


def evaluate_postfix(postfix):
    """
    @brief It evaluates a postfix expression.

    @param postfix a list of postfix epression
    @return float result
    """
    stack = []
    for i in postfix:
        if isinstance(i, float):
            stack.append(i)
        else:
            handle_operation(stack, i)
    return stack.pop()


def evaluate_expression(expression):
    """
    @brief It evaluates the expression

    @param expression The math expression to evaluate
    @return result
    """
    infix = get_infix(expression)
    postfix = get_postfix(infix)
    return evaluate_postfix(postfix)


# print("print:", evaluate_expression(expression))
