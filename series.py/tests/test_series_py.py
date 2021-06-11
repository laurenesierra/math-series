from math_series import __version__
from math_series.series import fibonacci
# from math_series.series import lucas



def test_version():
    assert __version__ == '0.1.0'


def test_one_pass():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_one_fail():
    actual = fibonacci(1)
    expected = 2
    assert actual != expected

def test_two_pass():
    actual = fibonacci(16)
    expected = 987
    assert actual == expected

def test_two_fail():
    actual = fibonacci(16)
    expected = 937
    assert actual != expected

def test_three_pass():
    actual = fibonacci(14)
    expected = 377
    assert actual == expected


def test_three_fail():
    actual = fibonacci(14)
    expected = 338
    assert actual != expected

    
# def lucas_test_one_pass():
#     actual = lucas(5)
#     expected = 11
#     assert actual == expected

# def lucas_test_one_fail():
#     actual = lucas(5)
#     expected = 12
#     assert actual != expected







