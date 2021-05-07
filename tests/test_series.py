from math_series.series import fibonacci

def test_fibonacci_1 () :
    n = 0
    expected = 0
    actual = fibonacci(n)
    assert expected is actual , "The result of " + str(n) + " as input should be " + str(expected) + " , but The actual output is : " + str(actual)


def test_fibonacci_2 () :
    n = 1
    expected = 1
    actual = fibonacci(n)
    assert expected is actual , "The result of " + str(n) + " as input should be " + str(expected) + " , but The actual output is : " + str(actual)


def test_fibonacci_3 () :
    n = 2
    expected = 1
    actual = fibonacci(n)
    assert expected is actual , "The result of " + str(n) + " as input should be " + str(expected) + " , but The actual output is : " + str(actual)


def test_fibonacci_4 () :
    n = 3
    expected = 2
    actual = fibonacci(n)
    assert expected is actual , "The result of " + str(n) + " as input should be " + str(expected) + " , but The actual output is : " + str(actual)


def test_fibonacci_5 () :
    n = 7
    expected = 13
    actual = fibonacci(n)
    assert expected is actual , "The result of " + str(n) + " as input should be " + str(expected) + " , but The actual output is : " + str(actual)