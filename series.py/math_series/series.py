def fibonacci(n):

  """
  this function has one parameter (n).
  this function should return the nth value
  in the fibonacci series.
  the function is implemented using recursion.

  each number in the fibonacci sequence 
  is the sum of the two numbers that precede it. 
  
  the sequence goes: 
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

  """

  if n < 0:
    print("Incorrect")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

  """
  this function has one parameter (n).
  this function should return the nth value
  in the fibonacci series.
  the function is implemented using recursion.

  The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.
  The first few Lucas numbers are:

  2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, ....
  """
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, a = 0, b = 1):

  """
  Both the fibonacci series and the lucas numbers are based on an identical formula. Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

  """
  if n == 0:
    return a
  elif n == 1:
    return b
  else:
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
      


