import helpers


# A python module to convert a number or list of numbers into a variable name or list of variable names (or vice versa)


def generate_name_fixed(num: int, alphabet: str, name_length: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    if num < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return ''
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
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
        
        if invalid_contained:
            for invalid_name in invalid_names:  # Just remove single characters from alphabet if single characters in invalid_names and invalid_contained is True
                if len(invalid_name) == 1:
                    alphabet.replace(invalid_name, '')
            
            new_invalid_names = invalid_names
            current_name_length = 3
            while True:  # Continue generating longer permutations of each invalid_name until we are sure that we have enough
                if (num + len(new_invalid_names) + 1) >= (len(alphabet) ** current_name_length):
                    for invalid_name in invalid_names:
                        new_invalid_names += helpers.get_permutations_containing_name(alphabet, invalid_name, current_name_length)
                        new_invalid_names = list(set(new_invalid_names))  # Remove duplicates on each iteration to reduce memory

                    new_invalid_names = list(set(new_invalid_names))  # Remove duplicates

                    current_name_length += 1
                else:
                    invalid_names = new_invalid_names
                    del new_invalid_names  # Reduce memory
                    break

        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names_fixed(invalid_names, alphabet, name_length)

        # invalid_nums.sort()  # Superfluous

        skipped_name_count = helpers.get_skipped_name_count(num = num, invalid_nums = invalid_nums)
        
        num += skipped_name_count
    

    return helpers.base_generate_name_fixed(num, alphabet, name_length)


def generate_names_fixed(alphabet: str, name_length: int, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    if alphabet is None or len(alphabet) < 1 or name_length < 1:
        return []
    
    if (start_num < 1 or start_num > end_num) and (num_list is None or len(num_list) < 1):
        return []
    
    if num_list is not None and (start_num != -1 or end_num != -1):  # Ensure that we have either start_num and end_num or num_list, not both
        return []
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
        return []
    
    names = []
    if num_list is None:
        for i in range(start_num, end_num + 1):
            names.append(generate_name_fixed(i, alphabet, name_length, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings))
    else:
        for num in num_list:
            names.append(generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings))
    
    return names


def generate_name(num: int, alphabet: str, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    if num < 1 or alphabet is None or len(alphabet) < 1:
        return ''
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
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
        
        if invalid_contained:
            for invalid_name in invalid_names:  # Just remove single characters from alphabet if single characters in invalid_names and invalid_contained is True
                if len(invalid_name) == 1:
                    alphabet.replace(invalid_name, '')
            
            new_invalid_names = invalid_names
            current_name_length = 3
            while True:  # Continue generating longer permutations of each invalid_name until we are sure that we have enough
                if (num + len(new_invalid_names) + 1) >= (len(alphabet) ** current_name_length):
                    for invalid_name in invalid_names:
                        new_invalid_names += helpers.get_permutations_containing_name(alphabet, invalid_name, current_name_length)
                        new_invalid_names = list(set(new_invalid_names))  # Remove duplicates on each iteration to reduce memory

                    new_invalid_names = list(set(new_invalid_names))  # Remove duplicates

                    current_name_length += 1
                else:
                    invalid_names = new_invalid_names
                    del new_invalid_names  # Reduce memory
                    break
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names(invalid_names, alphabet)

        # invalid_nums.sort()  # Superfluous

        skipped_name_count = helpers.get_skipped_name_count(num = num, invalid_nums = invalid_nums)
        
        num += skipped_name_count


    # Figure out name_length

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
    
    return helpers.base_generate_name_fixed(num - last_running_total, alphabet, name_length)


def generate_names(alphabet: str, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    if alphabet is None or len(alphabet) < 1:
        return []
    
    if (start_num < 1 or start_num > end_num) and (num_list is None or len(num_list) < 1):
        return []
    
    if num_list is not None and (start_num != -1 or end_num != -1):  # Ensure that we have either start_num and end_num or num_list, not both
        return []
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
        return []
    
    names = []
    if num_list is None:
        for i in range(start_num, end_num + 1):
            names.append(generate_name(i, alphabet, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings))
    else:
        for num in num_list:
            names.append(generate_name(num, alphabet, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings))
    
    return names


def generate_name_fixed_alpha(num: int, name_length: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_names_fixed_alpha(name_length: int, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names_fixed(alphabet, name_length, start_num = start_num, end_num = end_num, num_list = num_list, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)
    

def generate_name_alpha(num: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_name(num, alphabet, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_names_alpha(start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return generate_names(alphabet, start_num = start_num, end_num = end_num, num_list = num_list, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_name_fixed_alpha2(num: int, name_length: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_names_fixed_alpha2(name_length: int, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_names_fixed(alphabet, name_length, start_num = start_num, end_num = end_num, num_list = num_list, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)
    

def generate_name_alpha2(num: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_name(num, alphabet, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_names_alpha2(start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return generate_names(alphabet, start_num = start_num, end_num = end_num, num_list = num_list, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_name_fixed_alpha3(num: int, name_length: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name_fixed(num, alphabet, name_length, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_names_fixed_alpha3(name_length: int, start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names_fixed(alphabet, name_length, start_num = start_num, end_num = end_num, num_list = num_list, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)
    

def generate_name_alpha3(num: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> str:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_name(num, alphabet, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def generate_names_alpha3(start_num: int = -1, end_num: int = -1, num_list: list[int] = None, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[str]:
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    return generate_names(alphabet, start_num = start_num, end_num = end_num, num_list = num_list, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings)


def num_from_name_fixed(name: str, alphabet: str, name_length: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> int:
    if name is None or len(name) < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return -1
    
    if len(name) != name_length:  # Verify that name is as long as name_length
        return -1
    
    for char in name:  # Verify that all chars in name are in given alphabet
        if char not in alphabet:
            return -1
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
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
                
        if invalid_contained:
            for invalid_name in invalid_names:  # Just remove single characters from alphabet if single characters in invalid_names and invalid_contained is True
                if len(invalid_name) == 1:
                    alphabet.replace(invalid_name, '')
            
            new_invalid_names = invalid_names
            for invalid_name in invalid_names:
                new_invalid_names += helpers.get_permutations_containing_name(alphabet, invalid_name, len(name))
                new_invalid_names = list(set(new_invalid_names))  # Remove duplicates on each iteration to reduce memory

            invalid_names = list(set(new_invalid_names))  # Remove duplicates
            del new_invalid_names  # Reduce memory
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names_fixed(invalid_names, alphabet, name_length)

        # invalid_nums.sort()  # Superfluous

        num_of_name = num_from_name_fixed(name, alphabet, name_length)
        skipped_name_count = helpers.get_skipped_name_count_from_name(num = num, invalid_nums = invalid_nums, num_of_name = num_of_name)
        
        num -= skipped_name_count
    

    for i in range(len(name)):
        magnitude = len(alphabet) ** (len(name) - i - 1)
        num += magnitude * (alphabet.index(name[i]))

    return num


def nums_from_names_fixed(names: list[str], alphabet: str, name_length: int, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[int]:
    if names is None or len(names) < 1 or alphabet is None or len(alphabet) < 1 or name_length < 1:
        return []
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
        return []
    
    nums = []
    for name in names:
        nums.append(num_from_name_fixed(name, alphabet, name_length, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings))
    
    return nums


def num_from_name(name: str, alphabet: str, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> int:
    if name is None or len(name) < 1 or alphabet is None or len(alphabet) < 1:
        return -1
    
    for char in name:  # Verify that all chars in name are in given alphabet
        if char not in alphabet:
            return -1
        
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
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
                
        if invalid_contained:
            for invalid_name in invalid_names:  # Just remove single characters from alphabet if single characters in invalid_names and invalid_contained is True
                if len(invalid_name) == 1:
                    alphabet.replace(invalid_name, '')
            
            new_invalid_names = invalid_names
            for invalid_name in invalid_names:
                new_invalid_names += helpers.get_permutations_containing_name(alphabet, invalid_name, len(name))
                new_invalid_names = list(set(new_invalid_names))  # Remove duplicates on each iteration to reduce memory

            invalid_names = list(set(new_invalid_names))  # Remove duplicates
            del new_invalid_names  # Reduce memory
        
        # Sort invalid_names by alphabet, then by length
        invalid_names = sorted(sorted(invalid_names, key=lambda word: [alphabet.index(c) for c in word]), key = len)

        invalid_nums = nums_from_names(invalid_names, alphabet)

        # invalid_nums.sort()  # Superfluous

        num_of_name = num_from_name(name, alphabet)
        skipped_name_count = helpers.get_skipped_name_count_from_name(num = num, invalid_nums = invalid_nums, num_of_name = num_of_name)
        
        num -= skipped_name_count
    

    for i in range(len(name)):
        magnitude = len(alphabet) ** (len(name) - i - 1)
        num += magnitude * (alphabet.index(name[i]) + 1)

    return num


def nums_from_names(names: list[str], alphabet: str, invalid_names: list[str] = None, invalid_contained: bool = False, warnings: bool = True) -> list[int]:
    if names is None or len(names) < 1 or alphabet is None or len(alphabet) < 1:
        return []
    
    if len(set(alphabet)) < len(alphabet):
        print(f'\nThe given alphabet contains duplicate characters! Please give a proper alphabet.\n')
        return []
    
    nums = []
    for name in names:
        nums.append(num_from_name(name, alphabet, invalid_names = invalid_names, invalid_contained = invalid_contained, warnings = warnings))
    
    return nums


