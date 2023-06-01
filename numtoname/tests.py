import functions


alphabet1 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
alphabet2 = 'abcdefghijklmnopqrstuvwxyz'
alphabet3 = 'abcdefgh'


def test_generate_name_fixed():
    assert functions.generate_name_fixed(123123, alphabet1, 10) == 'aaaaaaaWNt'
    assert functions.generate_name_fixed(1, alphabet1, 10) == 'aaaaaaaaaa'
    assert functions.generate_name_fixed(1313142525, alphabet1, 10) == "aaaaBLPAqw"
    assert functions.generate_name_fixed(12, alphabet1, 10) == 'aaaaaaaaaF'
    assert functions.generate_name_fixed(52, alphabet1, 10) == 'aaaaaaaaaZ'
    assert functions.generate_name_fixed(54, alphabet1, 10) == 'aaaaaaaaAA'
    assert functions.generate_name_fixed(2, alphabet1, 10) == 'aaaaaaaaaA'
    assert functions.generate_name_fixed(104, alphabet1, 10) == 'aaaaaaaaAZ'
    assert functions.generate_name_fixed(105, alphabet1, 10) == 'aaaaaaaaba'
    assert functions.generate_name_fixed(53, alphabet1, 10) == 'aaaaaaaaAa'
    assert functions.generate_name_fixed(2704, alphabet1, 10) == 'aaaaaaaaZZ'
    assert functions.generate_name_fixed(2705, alphabet1, 10) == 'aaaaaaaAaa'
    assert functions.generate_name_fixed(2709, alphabet1, 10) == 'aaaaaaaAac'
    assert functions.generate_name_fixed(676, alphabet2, 5) == 'aaazz'
    assert functions.generate_name_fixed(677, alphabet2, 5) == 'aabaa'
    assert functions.generate_name_fixed(0, alphabet2, 5) == ''
    assert functions.generate_name_fixed(50, alphabet2, 0) == ''
    assert functions.generate_name_fixed(-5, alphabet2, 5) == ''
    assert functions.generate_name_fixed(50, '', 5) == ''
    assert functions.generate_name_fixed(50, None, 5) == ''


def test_generate_name():
    assert functions.generate_name(2, alphabet3) == 'b'
    assert functions.generate_name(1, alphabet3) == 'a'
    assert functions.generate_name(9, alphabet3) == 'aa'
    assert functions.generate_name(11, alphabet3) == 'ac'
    assert functions.generate_name(73, alphabet3) == 'aaa'
    assert functions.generate_name(0, alphabet3) == ''
    assert functions.generate_name(-6, alphabet3) == ''
    assert functions.generate_name(5, '') == ''
    assert functions.generate_name(5, None) == ''


def test_generate_names_fixed():
    assert functions.generate_names_fixed(alphabet3, 5, start_num = 1, end_num = 5) == ['aaaaa', 'aaaab', 'aaaac', 'aaaad', 'aaaae']
    assert functions.generate_names_fixed(alphabet3, 5, num_list = [11, 12, 13, 14]) == ['aaabc', 'aaabd', 'aaabe', 'aaabf']
    assert functions.generate_names_fixed(alphabet2, 5, num_list = [2, 9, 14, 15]) == ['aaaab', 'aaaai', 'aaaan', 'aaaao']
    assert functions.generate_names_fixed(alphabet3, 5, start_num = 5, end_num = 14, num_list = [1, 2, 3, 5, 7]) == []
    assert functions.generate_names_fixed(alphabet3, 5, start_num = 14, end_num = 13) == []
    assert functions.generate_names_fixed(alphabet2, 5, num_list = [0, 9, 14, 15]) == ['', 'aaaai', 'aaaan', 'aaaao']
    assert functions.generate_names_fixed(alphabet3, 5, start_num = -5, end_num = 14) == []
    assert functions.generate_names_fixed(alphabet3, 0, start_num = 10, end_num = 14) == []
    assert functions.generate_names_fixed('', 5, start_num = 10, end_num = 14) == []
    assert functions.generate_names_fixed(None, 5, start_num = 10, end_num = 14) == []


def test_generate_names():
    assert functions.generate_names(alphabet3, start_num = 1, end_num = 5) == ['a', 'b', 'c', 'd', 'e']
    assert functions.generate_names(alphabet3, num_list = [11, 12, 13, 14]) == ['ac', 'ad', 'ae', 'af']
    assert functions.generate_names(alphabet2, num_list = [2, 9, 14, 15]) == ['b', 'i', 'n', 'o']
    assert functions.generate_names(alphabet3, start_num = 14, end_num = 13) == []
    assert functions.generate_names(alphabet2, num_list = [0, 9, 14, 15]) == ['', 'i', 'n', 'o']
    assert functions.generate_names(alphabet3, start_num = 0, end_num = 5) == []
    assert functions.generate_names('', num_list = [2, 9, 14, 15]) == []
    assert functions.generate_names(None, start_num = 1, end_num = 5) == []


def test_num_from_name_fixed():
    assert functions.num_from_name_fixed('ac', alphabet2, 2) == 3
    assert functions.num_from_name_fixed('bc', alphabet2, 2) == 29
    assert functions.num_from_name_fixed('abc', alphabet2, 3) == 29
    assert functions.num_from_name_fixed('bbd', alphabet2, 3) == 706
    assert functions.num_from_name_fixed('aaaaaaaaZZ', alphabet1, 10) == 2704
    assert functions.num_from_name_fixed('aaaaaaaaZZ', alphabet1, 9) == -1
    assert functions.num_from_name_fixed('aaaaaaaaZZ', alphabet3, 10) == -1
    assert functions.num_from_name_fixed('', alphabet1, 10) == -1
    assert functions.num_from_name_fixed(None, alphabet1, 10) == -1


def test_num_from_name():
    assert functions.num_from_name('ac', alphabet3) == 11
    assert functions.num_from_name('ac', alphabet2) == 29
    assert functions.num_from_name('bc', alphabet2) == 55
    assert functions.num_from_name('abc', alphabet2) == 731
    assert functions.num_from_name('bbd', alphabet2) == 1408
    assert functions.num_from_name('aaa', alphabet3) == 73
    assert functions.num_from_name('aZZ', alphabet3) == -1
    assert functions.num_from_name('', alphabet1) == -1
    assert functions.num_from_name(None, alphabet1) == -1


def test_nums_from_names_fixed():
    assert functions.nums_from_names_fixed(['aaaaa', 'aaaab', 'aaaac', 'aaaad', 'aaaae'], alphabet2, 5) == [1, 2, 3, 4, 5]
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], alphabet2, 2) == [3, 4, 27, 29]
    assert functions.nums_from_names_fixed(['acb', 'ad', 'ba', 'b'], alphabet2, 2) == [-1, 4, 27, -1]
    assert functions.nums_from_names_fixed(['ac', 'zz', 'ba', 'bc'], alphabet3, 2) == [3, -1, 9, 11]
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], alphabet2, -5) == []
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], '', 2) == []
    assert functions.nums_from_names_fixed([], alphabet3, 2) == []


def test_nums_from_names():
    assert functions.nums_from_names(['a', 'b', 'c', 'd', 'e'], alphabet2) == [1, 2, 3, 4, 5]
    assert functions.nums_from_names(['ac', 'ad', 'ba', 'bc'], alphabet2) == [29, 30, 53, 55]
    assert functions.nums_from_names(['ac', 'zz', 'ba', 'bc'], alphabet3) == [11, -1, 17, 19]
    assert functions.nums_from_names(['ac', 'ad', 'ba', 'bc'], '') == []
    assert functions.nums_from_names([], alphabet3) == []


if __name__ == '__main__':
    test_generate_name_fixed()
    test_generate_name()

    test_generate_names_fixed()
    test_generate_names()



    test_num_from_name_fixed()
    test_num_from_name()

    test_nums_from_names_fixed()
    test_nums_from_names()

    print('All tests passed successfully!')

