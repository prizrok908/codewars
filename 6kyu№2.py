def expanded_form(num):
    num_str = str(num)
    if '.' in num_str:
        integer_part, fractional_part = num_str.split('.')
    else:
        integer_part, fractional_part = num_str, ''

    length = len(integer_part)
    parts = []
    for i, digit in enumerate(integer_part):
        if digit != '0':
            parts.append(digit + '0' * (length - i - 1))

    for i, digit in enumerate(fractional_part):
        if digit != '0':
            parts.append(f"{digit}/{10**(i+1)}")

    return ' + '.join(parts)