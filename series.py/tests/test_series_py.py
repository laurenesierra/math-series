from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_one_pass_fib():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_one_fail_fib():
    actual = fibonacci(1)
    expected = 2
    assert actual != expected

def test_two_pass_fib():
    actual = fibonacci(16)
    expected = 987
    assert actual == expected

def test_two_fail_fib():
    actual = fibonacci(16)
    expected = 937
    assert actual != expected

def test_one_pass_luc():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_one_fail_luc():
    actual = lucas(1)
    expected = 2
    assert actual != expected

def test_one_pass_sum():
    actual = sum_series(9)
    expected = 34
    assert actual == expected

def test_two_pass_sum():
    actual = sum_series(8, 2, 1)
    expected = 47
    assert actual == expected

def test_one_fail_sum():
    actual = sum_series(9)
    expected = 37
    assert actual != expected

def test_two_fail_sum():
    actual = sum_series(8, 2, 1)
    expected = 45
    assert actual != expected









