def square_digits(num):
    result = ''.join(str(int(digit) ** 2) for digit in str(num))
    return int(result)