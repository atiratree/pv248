def f_to_str(num):
    return '{:.2f}'.format(num)


def generate_alphabet_variables(count):
    next_char_code = 97
    if next_char_code + count > 122:
        raise Exception('Unsupported: only up to 26  alphabet variables supported')

    alphabet = []
    for i in range(0, count):
        alphabet.append(chr(next_char_code))
        next_char_code += 1
    return alphabet
