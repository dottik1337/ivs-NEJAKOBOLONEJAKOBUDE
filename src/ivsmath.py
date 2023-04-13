##
# @file ivsmath.py
# @authors
# @brief Handling of math expressions

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
    SIN = 4


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
        elif self.char == "s":
            return Precedence.SIN
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
            print("Error get_infix")
            raise ValueError
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
        print("Division by zero")
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
    if b%2 == 0 and a < 0:
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

def sin(x):
    """
    @brief The function calculates the sine of an angle in degrees using the Taylor series approximation.
    
    @param x The input angle in degrees for which the sine value needs to be calculated.
    @return the sine value of the input angle in radians, rounded to 10 decimal places.
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
    elif operator == "s":
        tmp = sin(stack.pop())
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

def format_expr(x):
    """
    @brief The function formats a given number by limiting the number of digits before and after the decimal
    point and converting it to scientific notation if necessary.
    
    @param x The input value that needs to be formatted
    
    @return The function `format_expr` returns a formatted version of the input `x`
    """
    MAX_N_LEN=3
    MAX_DEC_LEN=7
    try:
        dec_len=len(str(x).split(".")[1])
        dec=str(x).split(".")[1]
    except:
        if(len(str(x)) > MAX_N_LEN):
            return f'{x:e}'
        return int(x)
    
    zero_len=0
    for i in dec:
        if(i == "0"):
            zero_len+=1
        else:
            break

    if((zero_len == dec_len)): #ak je za bodkou iba nula
        return int(x)
    elif(zero_len > MAX_DEC_LEN):
        return f'{x:e}'
    else:
        return x


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
    except ZeroDivisionError:
        return "Division by zero"
    except:
        return "Math Error"
    return format_expr(eval)

if __name__ == "__main__":
    expression = "s5*5" #input()
    print("print:", evaluate_expression(expression))
