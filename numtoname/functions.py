# A python module to convert a number or list of numbers into a variable name or list of variable names

def generate_name_fixed(num: int, alphabet: str, name_length: int):
    if num < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return ''
    
    name_string = ""
    running_length = num
    alphabet_size = len(alphabet)
    for i in range(name_length):
        if running_length > 1 and running_length > (alphabet_size ** (name_length - i - 1)):
            for j in range(alphabet_size):
                if running_length > ((alphabet_size - j - 1) * (alphabet_size ** (name_length - i - 1))):
                    name_string += alphabet[(alphabet_size - j - 1)]
                    running_length -= ((alphabet_size - j - 1) * (alphabet_size ** (name_length - i - 1)))
                    break
        else:
            name_string += alphabet[0]
    
    return name_string


def generate_names_fixed(alphabet: str, name_length: int, start_num: int = -1, end_num: int = -1, num_list: list[int] = None):
    if alphabet is None or len(alphabet) < 1 or name_length < 1:
        return []
    
    if (start_num < 1 or start_num > end_num) and (num_list is None or len(num_list) < 1):
        return []
    
    if num_list is not None and (start_num != -1 or end_num != -1):  # Ensure that we have either start_num and end_num or num_list, not both
        return []
    
    names = []
    if num_list is None:
        for i in range(start_num, end_num + 1):
            names.append(generate_name_fixed(i, alphabet, name_length))
    else:
        for num in num_list:
            names.append(generate_name_fixed(num, alphabet, name_length))
    
    return names


def generate_name(num: int, alphabet: str):
    if num < 1 or alphabet is None or len(alphabet) < 1:
        return ''

    name_length = 0
    running_total = 0
    last_running_total = 0
    while True:
        if num > running_total:
            name_length += 1
            last_running_total = running_total
            running_total += len(alphabet) ** name_length
        else:
            break
    
    return generate_name_fixed(num - last_running_total, alphabet, name_length)


def generate_names(start_num: int, end_num: int, alphabet: str):
    if start_num < 1 or start_num > end_num or alphabet is None or len(alphabet) < 1:
        return []
    
    names = []
    for i in range(start_num, end_num + 1):
        names.append(generate_name(i, alphabet))
    
    return names


def generate_name_fixed_alpha(num: int, name_length: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name_fixed(num, alphabet, name_length)


def generate_names_fixed_alpha(start_num: int, end_num: int, name_length: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names_fixed(start_num, end_num, alphabet, name_length)
    

def generate_name_alpha(num: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name(num, alphabet)


def generate_names_alpha(start_num: int, end_num: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names(start_num, end_num, alphabet)


def generate_name_fixed_alpha2(num: int, name_length: int):
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name_fixed(num, alphabet, name_length)


def generate_names_fixed_alpha2(start_num: int, end_num: int, name_length: int):
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names_fixed(start_num, end_num, alphabet, name_length)
    

def generate_name_alpha2(num: int):
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name(num, alphabet)


def generate_names_alpha2(start_num: int, end_num: int):
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names(start_num, end_num, alphabet)


def num_from_name_fixed(name: str, alphabet: str, name_length: int):
    if name is None or len(name) < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return -1
    
    if len(name) != name_length:  # Verify that name is as long as name_length
        return -1
    
    for char in name:  # Verify that all chars in name are in alphabet
        if char not in alphabet:
            return -1

    num = 1
    for i in range(len(name)):
        magnitude = len(alphabet) ** (len(name) - i - 1)
        num += magnitude * (alphabet.index(name[i]))

    return num


def nums_from_names_fixed(names: list[str], alphabet: str, name_length: int):
    if names is None or len(names) < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return []
    
    nums = []
    for name in names:
        nums.append(num_from_name_fixed(name, alphabet, name_length))
    
    return nums


def num_from_name(name: str, alphabet: str):
    if name is None or len(name) < 1 or alphabet is None or len(alphabet) < 1:
        return -1
    
    for char in name:  # Verify that all chars in name are in alphabet
        if char not in alphabet:
            return -1

    num = 0
    for i in range(len(name)):
        magnitude = len(alphabet) ** (len(name) - i - 1)
        num += magnitude * (alphabet.index(name[i]) + 1)

    return num


def nums_from_names(names: list[str], alphabet: str):
    if names is None or len(names) < 1 or alphabet is None or len(alphabet) < 1:
        return []
    
    nums = []
    for name in names:
        nums.append(num_from_name(name, alphabet))
    
    return nums


