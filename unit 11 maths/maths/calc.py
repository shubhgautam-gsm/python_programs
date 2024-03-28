def log10(x):
    """
    Calculate the base-10 logarithm of a number.
    
    Args:
        x (float): The number for which the base-10 logarithm is calculated.
        
    Returns:
        float: The base-10 logarithm of the input number.
    """
    if x <= 0:
        raise ValueError("Input must be positive for logarithm calculation")
    
    result = 0
    while x >= 10:
        x /= 10
        result += 1
    while x < 1:
        x *= 10
        result -= 1
    
    return result

def log20(x):
    """
    Calculate the base-20 logarithm of a number.
    
    Args:
        x (float): The number for which the base-20 logarithm is calculated.
        
    Returns:
        float: The base-10 logarithm of the input number.
    """
    if x <= 0:
        raise ValueError("Input must be positive for logarithm calculation")
    
    result = 0
    while x >= 20:
        x /= 20
        result += 1
    while x < 1:
        x *= 20
        result -= 1
    
    return result

def sqr(x):
    return x*x
 
def sqrt(x, epsilon=1e-6):
    """
    Calculate the square root of a number using the Babylonian method.
    
    Args:
        x (float): The number for which the square root is calculated.
        epsilon (float): The desired level of precision.
        
    Returns:
        float: The square root of the input number.
    """
    if x < 0:
        raise ValueError("Square root is undefined for negative numbers")
    elif x == 0:
        return 0
    
    guess = x / 2
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    
    return guess

def exp(x, terms=100):
    """
    Calculate the value of e raised to the power of x using Maclaurin series expansion.
    
    Args:
        x (float): The exponent.
        terms (int): Number of terms to use in the series expansion.
        
    Returns:
        float: The value of e raised to the power of x.
    """
    result = 1
    factorial = 1
    for n in range(1, terms + 1):
        factorial *= n
        result += (x ** n) / factorial
    return result

def custom_pow(x, y):
    """
    Calculate the power of x raised to the value of y.
    
    Args:
        x (float): The base.
        y (float): The exponent.
        
    Returns:
        float: The result of x raised to the power of y.
    """
    return x ** y

def custom_floor(x):
    """
    Return the floor value of x.
    
    Args:
        x (float): The number for which the floor value is calculated.
        
    Returns:
        int: The floor value of x.
    """
    return int(x) if x >= 0 else int(x) - 1

def custom_ceil(x):
    """
    Return the ceil value of x.
    
    Args:
        x (float): The number for which the ceil value is calculated.
        
    Returns:
        int: The ceil value of x.
    """
    return int(x) + 1 if x != int(x) else int(x)

def custom_fabs(x):
    """
    Return the absolute value of x.
    
    Args:
        x (float): The number for which the absolute value is calculated.
        
    Returns:
        float: The absolute value of x.
    """
    return -x if x < 0 else x

def custom_factorial(x):
    """
    Calculate the factorial of x.
    
    Args:
        x (int): The number for which the factorial is calculated.
        
    Returns:
        int: The factorial of x.
    """
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def custom_modf(x):
    """
    Return the fractional and integer parts of x as a tuple.
    
    Args:
        x (float): The number for which the fractional and integer parts are calculated.
        
    Returns:
        tuple: A tuple containing the fractional and integer parts of x.
    """
    integer_part = int(x)
    fractional_part = x - integer_part
    return fractional_part, integer_part

__all__ = ['log10', 'log20', 'sqr', 'sqrt', 'exp', 'custom_pow', 'custom_floor', 'custom_ceil', 'custom_fabs', 'custom_factorial', 'custom_modf']
