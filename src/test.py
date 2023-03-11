import math_1


def test_get_infix():
    string = "55+5-10"
    infix = math_1.get_infix(string)
    assert infix == [55.0, '+', 5.0, "-", 10.0]

    string = "55+5*10-50/2"
    infix = math_1.get_infix(string)
    assert infix == [55.0, '+', 5.0, "*", 10.0, "-", 50.0, "/", 2.0]


def test_get_postfix():
    infix = [55.0, '+', 5.0, "-", 10.0]
    postfix = math_1.get_postfix(infix)
    assert postfix == [55.0, 5.0, "+", 10.0, "-"]

    infix = [55.0, '+', 5.0, "*", 10.0, "-", 50.0, "/", 2.0]
    postfix = math_1.get_postfix(infix)
    assert postfix == [55.0, 5.0, 10.0, "*", "+", 50.0, 2.0, "/", "-"]

    infix = [3.0, "!", "^", 3.0, "+", 2.0, "r", 4.0]
    postfix = math_1.get_postfix(infix)
    assert postfix == [3.0, "!", 3.0, "^", 2.0, 4.0, "r", "+"]
