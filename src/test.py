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

    expr = "-5+-5"
    result = ivsmath.evaluate_expression(expr)
    assert result == 0.0

    expr = "2r4"
    result = ivsmath.evaluate_expression(expr)
    assert result == 2.0


def test_evaluate_expression_errors():
    expr = "5/0"
    result = ivsmath.evaluate_expression(expr)
    assert result == "Math error"

    expr = "2r-1"
    result = ivsmath.evaluate_expression(expr)
    assert result == "Math error"
