import ivsmath


def test_get_infix():
    string = "55+5-10"
    infix = ivsmath.get_infix(string)
    assert infix == [55.0, '+', 5.0, "-", 10.0]

    string = "55+5*10-50/2"
    infix = ivsmath.get_infix(string)
    assert infix == [55.0, '+', 5.0, "*", 10.0, "-", 50.0, "/", 2.0]


def test_get_postfix():
    infix = [55.0, '+', 5.0, "-", 10.0]
    postfix = ivsmath.get_postfix(infix)
    assert postfix == [55.0, 5.0, "+", 10.0, "-"]

    infix = [55.0, '+', 5.0, "*", 10.0, "-", 50.0, "/", 2.0]
    postfix = ivsmath.get_postfix(infix)
    assert postfix == [55.0, 5.0, 10.0, "*", "+", 50.0, 2.0, "/", "-"]

    infix = [3.0, "!", "^", 3.0, "+", 2.0, "r", 4.0]
    postfix = ivsmath.get_postfix(infix)
    assert postfix == [3.0, "!", 3.0, "^", 2.0, 4.0, "r", "+"]


def test_evaluate_expression():
    expr = "5!"
    result = ivsmath.evaluate_expression(expr)
    assert result == 120.0

    expr = "5!*10"
    result = ivsmath.evaluate_expression(expr)
    assert result == 1200.0

    expr = "5*5-10*20/2-9"
    result = ivsmath.evaluate_expression(expr)
    assert result == -84.0

    expr = "-5+(-5)"
    result = ivsmath.evaluate_expression(expr)
    assert result == -10.0

    expr = "2r4"
    result = ivsmath.evaluate_expression(expr)
    assert result == 2.0


def test_evaluate_expression_errors():
    expr = "5/0"
    result = ivsmath.evaluate_expression(expr)
    assert result == "Math Error"

    expr = "2r(-1)"
    result = ivsmath.evaluate_expression(expr)
    assert result == "Math error - invalid radical function" 


def test_evaluate_expression_parenthersis():
    expr = "2*(4+5)"
    result = ivsmath.evaluate_expression(expr)
    assert result == 18.0

    expr = "2*(-2)"
    result = ivsmath.evaluate_expression(expr)
    assert result == -4.0

    expr = "(6-4)r4"
    result = ivsmath.evaluate_expression(expr)
    assert result == 2.0

    expr = "(2*3)!"
    result = ivsmath.evaluate_expression(expr)
    assert result == 720.0

def test_evaluate_expression_sinus():
    expr = "(180)s"
    result = ivsmath.evaluate_expression(expr)
    assert result == 0
    expr = "5!s"
    result = ivsmath.evaluate_expression(expr)
    assert result == str(0.8660254038)

def test_evaluate_expression_hardcore():
    expr = "(5*2)^2+((179+15/3)*2r(5!)+5/3)*s0.76"
    result = ivsmath.evaluate_expression(expr)
    assert round(float(result),4) == 126.7575

    expr = "((2r((5+5)-(2^8)*0.5)/1.5)-420"
    result = ivsmath.evaluate_expression(expr)
    assert result == "Math error - invalid radical function"

    expr = "2/(3.9*(2r(4+(s(5+5.3)*2.7)/79)))"
    result = ivsmath.evaluate_expression(expr)
    assert round(float(result),4) == 0.2562
