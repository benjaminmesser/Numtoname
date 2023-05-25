

def generate_name_fixed(num: int, char_order: str, char_length: int):
    if num < 1 or char_order is None or len(char_order) < 1 or char_length < 1:
        return ''
    
    name_string = ""
    running_length = num
    char_num = len(char_order)
    for i in range(char_length):
        if running_length > 1 and running_length > (char_num ** (char_length - i - 1)):
            for j in range(char_num):
                if running_length > ((char_num - j - 1) * (char_num ** (char_length - i - 1))):
                    name_string += char_order[(char_num - j - 1)]
                    running_length -= ((char_num - j - 1) * (char_num ** (char_length - i - 1)))
                    break
        else:
            name_string += char_order[0]
    
    return name_string


def generate_names_fixed(start_num: int, end_num: int, char_order: str, char_length: int):
    if start_num < 1 or start_num > end_num or char_order is None or len(char_order) < 1 or char_length < 1:
        return []
    
    names = []
    for i in range(start_num, end_num + 1):
        names.append(generate_name_fixed(i, char_order, char_length))
    
    return names


def generate_name(num: int, char_order: str):
    if num < 1 or char_order is None or len(char_order) < 1:
        return ''

    char_length = 0
    running_total = 0
    last_running_total = 0
    while True:
        if num > running_total:
            char_length += 1
            last_running_total = running_total
            running_total += len(char_order) ** char_length
        else:
            break
    
    return generate_name_fixed(num - last_running_total, char_order, char_length)


def generate_names(start_num: int, end_num: int, char_order: str):
    if start_num < 1 or start_num > end_num or char_order is None or len(char_order) < 1:
        return []
    
    names = []
    for i in range(start_num, end_num + 1):
        names.append(generate_name(i, char_order))
    
    return names


def generate_name_fixed_alpha(num: int, char_length: int):
    char_order = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name_fixed(num, char_order, char_length)


def generate_names_fixed_alpha(start_num: int, end_num: int, char_length: int):
    char_order = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names_fixed(start_num, end_num, char_order, char_length)
    

def generate_name_alpha(num: int):
    char_order = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name(num, char_order)


def generate_names_alpha(start_num: int, end_num: int):
    char_order = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names(start_num, end_num, char_order)


def generate_name_fixed_alpha2(num: int, char_length: int):
    char_order = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name_fixed(num, char_order, char_length)


def generate_names_fixed_alpha2(start_num: int, end_num: int, char_length: int):
    char_order = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names_fixed(start_num, end_num, char_order, char_length)
    

def generate_name_alpha2(num: int):
    char_order = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name(num, char_order)


def generate_names_alpha2(start_num: int, end_num: int):
    char_order = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names(start_num, end_num, char_order)


