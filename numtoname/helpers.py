# Helper functions, not callable when importing package


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


def get_skipped_name_count(num: int, invalid_nums: list[str]) -> int:
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
    
    return skipped_name_count


def get_skipped_name_count_from_name(num: int, invalid_nums: list[str], num_of_name: int) -> int:
    skipped_name_count = 0
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
    
    return skipped_name_count

