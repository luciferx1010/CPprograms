def compute_polynomial(coefficients, x):
    """
    Compute the value of a polynomial equation given its coefficients and an input value.
    """
    result = 0

    for i in range(len(coefficients)):
        result += coefficients[i] * (x ** i)

    return result


# Example usage
coefficients = [2, -3, 1]  # Polynomial equation: 2x^2 - 3x + 1
input_value = 5
result = compute_polynomial(coefficients, input_value)
print(f"The result of the polynomial equation is: {result}")
