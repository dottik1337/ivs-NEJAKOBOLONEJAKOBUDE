""" Math library for calculator Numbo"""


class InvalidRadical(Exception):
    """Raised when there is number < 0 under even radical"""

class Precedence():
    """Precedence enum
    contains operators and their precedence 
    """
    PLUS = 1
    MINUS = 1
    MUL = 2
    DIV = 2
    POW = 3
    RADICAL = 3
    FAC = 4
    SIN = 4
    BRACKET = 5

class Operator():
    """Operator class for comparing precedences
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
        elif self.char == "s":
            return Precedence.SIN
        elif self.char == "(" or ")":
            return Precedence.BRACKET
        else:
            return 0

    def __le__(self, other):
        return self.get_eval() <= other.get_eval()

    def __ge__(self, other):
        if self.char == "(":
            return False
        return self.get_eval() >= other.get_eval()


def get_infix(string):
    """It takes a string and returns the infix expression.

    Args:
        string (str): The string to be converted to infix

    Returns:
        list: infix list
    """
    infix = []
    number = ""
    operators = ["+", "-", "*", "/", "^", "r", "!", "s"]
    for char in string:
        if char.isdigit() or char == '.':
            number += char
        # zabezpecuje ze minusove cisla budu minusove
        elif char == "-" and ((len(infix) == 0 and number == "") or (len(infix) != 0 and infix[-1] == "(" and number == "")):
            number += char
        elif char in operators or char in "()":
            if number != "":
                number = float(number)
                infix.append(number)
                number = ""
            infix.append(char)
        else:
            raise ValueError
    if number != "":
        infix.append(float(number))
    return infix


def get_postfix(infix):
    """It converts infix to postfix

    Args:
        infix (list): The infix expression to be converted to postfix

    Returns:
        list: postfix list
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
    """It divides b by a

    Args:
        a (float): The number to divide by
        b (float): The first number
    Returns:
        float: Division of the given numbers
    """
    if a == 0:
        raise ValueError
    else:
        return b/a


def radical(a, b):
    """It calculates the radical.

    Args:
        b (float): The index
        a (float): The radicand
    Returns:
        float: The a root of b
    """
    if b%2 == 0 and a < 0:
        raise InvalidRadical
    elif b == 0:
        raise InvalidRadical
    else:
        return a ** (1.0/b)


def factorial(a):
    """It calculates the factorial.

    Args:
        a (float): The number to find the factorial of

    Returns:
        int: Factorial of a
    """
    if a % 1 != 0 or a < 0:
        raise ValueError
    elif a > 170:  # max number that can be calculated using this algorithm
        raise ValueError
    sum = 1
    for i in range(2, int(a)+1):
        sum *= i
    return sum

def power(a,b):
    """It returns the value of a to the power of b.
    
    Args:
        a (float): The exponent
        b (float): The base
    Returns:
        float: a to the power of b
    """
    return b**a

def sin(x):
    """The function calculates the sine of an angle in degrees using the Taylor series approximation.

    Args:
        x (float): The input angle in degrees for which the sine value needs to be calculated.

    Returns:
        float: The sine value of the input angle in radians, rounded to 10 decimal places.
    """
    pi = 3.14159265359
    x = (x * pi) / 180
    term = x
    denominator = 1.0
    result = 0.0
    i = 1.0
    div = 5
    while(abs(div) > 0.00000000001):
        div = term/float(denominator)
        result += div
        term *= -(x*x)
        denominator *= (i+1)*(i+2)
        i += 2

    return round(result,10)

def handle_operation(stack, operator):
    """It handles the operations for evaluate_postfix

    Args:
        stack (list): List of numbers
        operator (list): The operator to be applied to the stack.
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
    elif operator == "s":
        tmp = sin(stack.pop())
    else:
        pass
        #print("Not implemented yet")
    stack.append(tmp)


def evaluate_postfix(postfix):
    """It evaluates a postfix expression.

    Args:
        postfix (str): List of postfix epression

    Returns:
        float: Result
    """
    stack = []
    for i in postfix:
        if isinstance(i, float):
            stack.append(i)
        else:
            handle_operation(stack, i)
    return stack.pop()

def format_expr(x):
    """The function formats a given number by limiting the number of digits before and after the decimal
    point and converting it to scientific notation if necessary.
    
    Args:
        x (float): The input value that needs to be formatted

    Returns:
        str: Formatted version of the input `x`
    """
    MAX_N_LEN=1000000000000000000000
    if(x - int(x) == 0.0):
        if(x > MAX_N_LEN):
            return f'{x:e}'
        return int(x)
    return str(float(x))


def evaluate_expression(expression):
    """It evaluates the expression

    Args:
        expression (str): The math expression to evaluate

    Returns:
        (str): Result
    """
    try:
        infix = get_infix(expression)
        postfix = get_postfix(infix)
        eval = evaluate_postfix(postfix)
    except ZeroDivisionError:
        return "Division by zero"
    except InvalidRadical:
        return "Math error - invalid radical function"
    except:
        return "Math Error"
    return format_expr(eval)

if __name__ == "__main__":
    expression = input() #"2/(3.9*(2r(4+(s(5+5.3)*2.7)/79)))"
    print(evaluate_expression(expression))
