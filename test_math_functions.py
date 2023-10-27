import pytest
from math_functions import Math_Functions



@pytest.fixture
def function_tests():
    return Math_Functions



def test_to_add(function_tests):
    number1 = 10
    number2 = 5
    #function_test = Math_Functions()
    assert function_tests.to_add(function_tests, number1, number2) == 15



def test_to_add_no_numeric(function_tests):
    number1 = 4
    number2 = 'r'
    #function_test = Math_Functions()
    with pytest.raises(TypeError):
        function_tests.to_add(function_tests, number1, number2)



@pytest.mark.parametrize(
    ['input_1', 'input_2', 'output_1'],
    [
        (1, 2, 3),
        (2, 1, 3),
        (2, 4, 6),
        (-1, 2, 1),
        (2, -1, 1),
        (0, 3, 3),
        (4, 0, 4),
        (0, 0, 0)
    ]
)
def test_to_add_multiple(function_tests, input_1, input_2, output_1):
    #function_test = Math_Functions()
    assert function_tests.to_add(function_tests, input_1, input_2) == output_1
    


@pytest.mark.parametrize(
    ['input_1', 'input_2'],
    [
        ('q', 2),
        (5, '3'),
        ("", 2),
        (3, "")
    ]
)
def test_to_add_multiple_no_numeric(function_tests, input_1, input_2):
    #function_test = Math_Functions()
    with pytest.raises(TypeError):
        function_tests.to_add(function_tests, input_1, input_2)



def test_to_subtract(function_tests):
    number1 = 8
    number2 = 2
    #function_test = Math_Functions()
    assert function_tests.to_subtract(function_tests,number1, number2) == 6



def test_to_subtract_no_numeric(function_tests):
    number1 = 4
    number2 = 'r'
    #function_test = Math_Functions()
    with pytest.raises(TypeError):
        function_tests.to_subtract(function_tests, number1, number2)



@pytest.mark.parametrize(
    ['input_1', 'input_2', 'output_1'],
    [
        (1, 2, -1),
        (2, 1, 1),
        (2, 4, -2),
        (-1, 2, -3),
        (2, -1, 3),
        (0, 3, -3),
        (4, 0, 4),
        (0, 0, 0)
    ]
)
def test_to_subtract_multiple(function_tests, input_1, input_2, output_1):
    assert function_tests.to_subtract(function_tests,input_1, input_2) == output_1



@pytest.mark.parametrize(
    ['input_1', 'input_2'],
    [
        ('q', 2),
        (5, '3'),
        ("", 2),
        (3, "")  
    ]
)
def test_to_subtract_multiple_no_numeric(function_tests, input_1, input_2):
    with pytest.raises(TypeError):
        function_tests.to_subtract(function_tests, input_1, input_2)



def test_to_multiply(function_tests):
    number1 = 7
    number2 = 11
    #function_test = Math_Functions()
    assert function_tests.to_multiply(function_tests, number1, number2)==77
    


def test_to_multiply_no_numeric(function_tests):
    number1 = 4
    number2 = 'r'
    with pytest.raises(TypeError):
        function_tests.to_multiply(function_tests, number1, number2)

  
  
@pytest.mark.parametrize(
    ['input_1', 'input_2', 'output_1'],
    [
        (1, 2, 2),
        (2, 1, 2),
        (2, -4, -8),
        (-1, 2, -2),
        (1, 3, 3),
        (4, 0, 0),
        (0, 4, 0),
        (0, 0, 0)
    ]
)
def test_to_multiply_multiple(function_tests, input_1, input_2, output_1):
    assert function_tests.to_multiply(function_tests,input_1, input_2) == output_1


"""
@pytest.mark.parametrize(
    ['input_1', 'input_2'],
    [
        ('q', 2),
        (5, '3'),
        ("", 2),
        (3, "")
        
    ]
)
def test_to_multiply_multiple_no_numeric(function_tests, input_1, input_2):
    with pytest.raises(TypeError):
        function_tests.to_multiply(function_tests, input_1, input_2)

    

    
def test_to_divide():
    number1 = 8
    number2 = 4
    function_test = Math_Functions()
    assert function_test.to_divide(number1, number2) ==2    
"""

