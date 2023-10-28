def to_multiply(number1, number2):
    try:
        number1 = float(number1)
        number2 = float(number2)
        resultmultiply = number1 * number2
        return resultmultiply
    except ValueError as err:
        print(err)
        raise
    
resultado = to_multiply('a',4)
print(resultado)