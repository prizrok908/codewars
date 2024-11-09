def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    parts = []
    
    for i, digit in enumerate(num_str):
        if digit != '0':
            parts.append(digit + '0' * (length - i - 1))
    
    return ' + '.join(parts)