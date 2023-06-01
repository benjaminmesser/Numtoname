# A python module to convert a number or list of numbers into a variable name or list of variable names


def base_generate_name_fixed(num: int, alphabet: str, name_length: int) -> str:
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


def generate_name_fixed(num: int, alphabet: str, name_length: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    if invalid_names is not None and len(invalid_names) >= 1:
        deleted_element_count = 0
        for i in range(len(invalid_names)):
            if set(invalid_names[i - deleted_element_count]) <= set(alphabet):
                pass  # invalid_name only contains characters in given alphabet
            else:
                del invalid_names[i - deleted_element_count]
                deleted_element_count += 1
        
        if deleted_element_count > 0:
            if warnings:
                print(f'\n{deleted_element_count} names in invalid_names contained characters outside of the specified alphabet. These were ignored.\n' \
                    'Set warnings = False to not see this message.\n')
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names_fixed(invalid_names, alphabet, name_length)

        # invalid_nums.sort()  # Superfluous

        skipped_name_count = 0
        while True:
            prev_skipped_name_count = skipped_name_count
            deleted_element_count = 0
            for i in range(len(invalid_nums)):
                # print(invalid_nums)
                if (num + skipped_name_count) >= invalid_nums[i - deleted_element_count]:
                    if invalid_nums[i - deleted_element_count] > 0:
                        skipped_name_count += 1

                    del invalid_nums[i- deleted_element_count]
                    deleted_element_count += 1
                else:
                    break
            
            if skipped_name_count == prev_skipped_name_count:
                break
        
        num += skipped_name_count

    return base_generate_name_fixed(num, alphabet, name_length)


def generate_names_fixed(alphabet: str, name_length: int, invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    if alphabet is None or len(alphabet) < 1 or name_length < 1:
        return []
    
    if (start_num < 1 or start_num > end_num) and (num_list is None or len(num_list) < 1):
        return []
    
    if num_list is not None and (start_num != -1 or end_num != -1):  # Ensure that we have either start_num and end_num or num_list, not both
        return []
    
    names = []
    if num_list is None:
        for i in range(start_num, end_num + 1):
            names.append(generate_name_fixed(i, alphabet, name_length, invalid_names = invalid_names, warnings = warnings))
    else:
        for num in num_list:
            names.append(generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, warnings = warnings))
    
    return names


def generate_name(num: int, alphabet: str, invalid_names: list[str] = None, warnings: bool = True) -> str:
    if num < 1 or alphabet is None or len(alphabet) < 1:
        return ''
    
    if invalid_names is not None and len(invalid_names) >= 1:
        deleted_element_count = 0
        for i in range(len(invalid_names)):
            if set(invalid_names[i - deleted_element_count]) <= set(alphabet):
                pass  # invalid_name only contains characters in given alphabet
            else:
                del invalid_names[i - deleted_element_count]
                deleted_element_count += 1
        
        if deleted_element_count > 0:
            if warnings:
                print(f'\n{deleted_element_count} names in invalid_names contained characters outside of the specified alphabet. These were ignored.\n' \
                    'Set warnings = False to not see this message.\n')
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names(invalid_names, alphabet)

        # invalid_nums.sort()  # Superfluous

        skipped_name_count = 0
        while True:
            prev_skipped_name_count = skipped_name_count
            deleted_element_count = 0
            for i in range(len(invalid_nums)):
                # print(invalid_nums)
                if (num + skipped_name_count) >= invalid_nums[i - deleted_element_count]:
                    if invalid_nums[i - deleted_element_count] > 0:
                        skipped_name_count += 1
                        
                    del invalid_nums[i- deleted_element_count]
                    deleted_element_count += 1
                else:
                    break
            
            if skipped_name_count == prev_skipped_name_count:
                break
        
        num += skipped_name_count


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
    
    return base_generate_name_fixed(num - last_running_total, alphabet, name_length)


def generate_names(alphabet: str, invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    if alphabet is None or len(alphabet) < 1:
        return []
    
    if (start_num < 1 or start_num > end_num) and (num_list is None or len(num_list) < 1):
        return []
    
    if num_list is not None and (start_num != -1 or end_num != -1):  # Ensure that we have either start_num and end_num or num_list, not both
        return []
    
    names = []
    if num_list is None:
        for i in range(start_num, end_num + 1):
            names.append(generate_name(i, alphabet, invalid_names = invalid_names, warnings = warnings))
    else:
        for num in num_list:
            names.append(generate_name(num, alphabet, invalid_names = invalid_names, warnings = warnings))
    
    return names


def generate_name_fixed_alpha(num: int, name_length: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, warnings = warnings)


def generate_names_fixed_alpha(name_length: int, invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names_fixed(alphabet, name_length, invalid_names = invalid_names, start_num = start_num, end_num = end_num, num_list = num_list, warnings = warnings)
    

def generate_name_alpha(num: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name(num, alphabet, invalid_names = invalid_names, warnings = warnings)


def generate_names_alpha(invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names(alphabet, invalid_names = invalid_names, start_num = start_num, end_num = end_num, num_list = num_list, warnings = warnings)


def generate_name_fixed_alpha2(num: int, name_length: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, warnings = warnings)


def generate_names_fixed_alpha2(name_length: int, invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_names_fixed(alphabet, name_length, invalid_names = invalid_names, start_num = start_num, end_num = end_num, num_list = num_list, warnings = warnings)
    

def generate_name_alpha2(num: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_name(num, alphabet, invalid_names = invalid_names, warnings = warnings)


def generate_names_alpha2(invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_names(alphabet, invalid_names = invalid_names, start_num = start_num, end_num = end_num, num_list = num_list, warnings = warnings)


def generate_name_fixed_alpha3(num: int, name_length: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, warnings = warnings)


def generate_names_fixed_alpha3(name_length: int, invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names_fixed(alphabet, name_length, invalid_names = invalid_names, start_num = start_num, end_num = end_num, num_list = num_list, warnings = warnings)
    

def generate_name_alpha3(num: int, invalid_names: list[str] = None, warnings: bool = True) -> str:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name(num, alphabet, invalid_names = invalid_names, warnings = warnings)


def generate_names_alpha3(invalid_names: list[str] = None, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, warnings: bool = True) -> list[str]:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names(alphabet, invalid_names = invalid_names, start_num = start_num, end_num = end_num, num_list = num_list, warnings = warnings)


def num_from_name_fixed(name: str, alphabet: str, name_length: int, invalid_names: list[str] = None, warnings: bool = True) -> int:
    if name is None or len(name) < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return -1
    
    if len(name) != name_length:  # Verify that name is as long as name_length
        return -1
    
    for char in name:  # Verify that all chars in name are in given alphabet
        if char not in alphabet:
            return -1
    
    num = 1
    if invalid_names is not None and len(invalid_names) >= 1:
        if name in invalid_names:
            return -1
        deleted_element_count = 0
        for i in range(len(invalid_names)):
            if set(invalid_names[i - deleted_element_count]) <= set(alphabet):
                pass  # invalid_name only contains characters in given alphabet
            else:
                del invalid_names[i- deleted_element_count]
                deleted_element_count += 1
        
        if deleted_element_count > 0:
            if warnings:
                print(f'\n{deleted_element_count} names in invalid_names contained characters outside of the specified alphabet. These were ignored.\n' \
                    'Set warnings = False to not see this message.\n')
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names_fixed(invalid_names, alphabet, name_length)

        # invalid_nums.sort()  # Superfluous

        skipped_name_count = 0
        num_of_name = num_from_name_fixed(name, alphabet, name_length)
        while True:
            prev_skipped_name_count = skipped_name_count
            deleted_element_count = 0
            for i in range(len(invalid_nums)):
                # print(invalid_nums)
                if num_of_name >= invalid_nums[i - deleted_element_count]:
                    if invalid_nums[i - deleted_element_count] > 0:
                        skipped_name_count += 1
                        
                    del invalid_nums[i- deleted_element_count]
                    deleted_element_count += 1
                else:
                    break
            
            if skipped_name_count == prev_skipped_name_count:
                break
        
        num -= skipped_name_count

    for i in range(len(name)):
        magnitude = len(alphabet) ** (len(name) - i - 1)
        num += magnitude * (alphabet.index(name[i]))

    return num


def nums_from_names_fixed(names: list[str], alphabet: str, name_length: int, invalid_names: list[str] = None, warnings: bool = True) -> list[int]:
    if names is None or len(names) < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return []
    
    nums = []
    for name in names:
        nums.append(num_from_name_fixed(name, alphabet, name_length, invalid_names = invalid_names, warnings = warnings))
    
    return nums


def num_from_name(name: str, alphabet: str, invalid_names: list[str] = None, warnings: bool = True) -> int:
    if name is None or len(name) < 1 or alphabet is None or len(alphabet) < 1:
        return -1
    
    for char in name:  # Verify that all chars in name are in given alphabet
        if char not in alphabet:
            return -1
    
    num = 0
    if invalid_names is not None and len(invalid_names) >= 1:
        if name in invalid_names:
            return -1
        deleted_element_count = 0
        for i in range(len(invalid_names)):
            if set(invalid_names[i - deleted_element_count]) <= set(alphabet):
                pass  # invalid_name only contains characters in given alphabet
            else:
                del invalid_names[i - deleted_element_count]
                deleted_element_count += 1
        
        if deleted_element_count > 0:
            if warnings:
                print(f'\n{deleted_element_count} names in invalid_names contained characters outside of the specified alphabet. These were ignored.\n' \
                    'Set warnings = False to not see this message.\n')
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names(invalid_names, alphabet)

        # invalid_nums.sort()  # Superfluous

        skipped_name_count = 0
        num_of_name = num_from_name(name, alphabet)
        while True:
            prev_skipped_name_count = skipped_name_count
            deleted_element_count = 0
            for i in range(len(invalid_nums)):
                # print(invalid_nums)
                if num_of_name >= invalid_nums[i - deleted_element_count]:
                    if invalid_nums[i - deleted_element_count] > 0:
                        skipped_name_count += 1
                        
                    del invalid_nums[i- deleted_element_count]
                    deleted_element_count += 1
                else:
                    break
            
            if skipped_name_count == prev_skipped_name_count:
                break
        
        num -= skipped_name_count

    for i in range(len(name)):
        magnitude = len(alphabet) ** (len(name) - i - 1)
        num += magnitude * (alphabet.index(name[i]) + 1)

    return num


def nums_from_names(names: list[str], alphabet: str, invalid_names: list[str] = None, warnings: bool = True) -> list[int]:
    if names is None or len(names) < 1 or alphabet is None or len(alphabet) < 1:
        return []
    
    nums = []
    for name in names:
        nums.append(num_from_name(name, alphabet, invalid_names = invalid_names, warnings = warnings))
    
    return nums


