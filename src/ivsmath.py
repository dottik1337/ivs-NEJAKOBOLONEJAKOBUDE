##
# @file ivsmath.py
# @authors
# @brief Handling of math expressions

#expression = 5-1 #input()


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
        if self.char == "+":
            return Precedence.PLUS
        elif self.char == "-":
            return Precedence.MINUS
        elif self.char == "*":
            return Precedence.MUL
        elif self.char == "/":
            return Precedence.DIV
        elif self.char == "^":
            return Precedence.POW
        elif self.char == "r":
            return Precedence.RADICAL
        elif self.char == "!":
            return Precedence.FAC
        else:
            print(self.char)
            print("error Operator.get_eval")
            return 0

    def __le__(self, other):
        return self.get_eval() <= other.get_eval()

    def __ge__(self, other):
        if self.char == "(":
            return False
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
        # zabezpecuje ze minusove cisla budu minusove
        elif char == "-" and (len(infix) == 0 or (infix[-1] == "(" and number == "")):
            number += char
        elif char in operators or char in "()":
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
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
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
        raise ValueError
    else:
        return b/a


def radical(a, b):
    """
    @brief It calculates the radical.

    @param b The index
    @param a The radicand
    @return the @p a root of @p b
    """
    if a < 0:
        print("Value error in radical function")
        raise ValueError
    elif b == 0:
        print("Value error in radical function")
        raise ValueError
    else:
        return a ** (1.0/b)


def factorial(a):
    """
    @brief It calculates the factorial.

    @param a The number to find the factorial of
    @return factorial of @p a
    """
    if a % 1 != 0 or a < 0:
        print("Value error in factorial function")
        raise ValueError
    elif a > 1558:  # max number that can be calculated using this algorithm
        print("Value error in factorial function")
        raise ValueError
    sum = 1
    for i in range(2, int(a)+1):
        sum *= i
    return sum

def power(a,b):
    """
    @brief It returns the value of a to the power of b.
    
    @param a exponent
    @param b the base
    """
    return b**a

def handle_operation(stack, operator):
    """
    @brief It handles the operations for evaluate_postfix

    @param stack a list of numbers
    @param operator The operator to be applied to the stack.
    """
    if operator == "+":
        tmp = stack.pop() + stack.pop()
    elif operator == "-":
        tmp = -stack.pop() + stack.pop()
    elif operator == "*":
        tmp = stack.pop() * stack.pop()
    elif operator == "/":
        tmp = division(stack.pop(), stack.pop())
    elif operator == "^":
        tmp = power(stack.pop(), stack.pop())
    elif operator == "r":
        tmp = radical(stack.pop(), stack.pop())
    elif operator == "!":
        tmp = factorial(stack.pop())
    else:
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
    try:
        infix = get_infix(expression)
        postfix = get_postfix(infix)
        eval = evaluate_postfix(postfix)
    except:
        return "Math Error"
    return eval


#print("print:", evaluate_expression(expression))
