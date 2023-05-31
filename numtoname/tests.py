import functions


char_order1 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
char_order2 = 'abcdefghijklmnopqrstuvwxyz'
char_order3 = 'abcdefgh'


def test_generate_name_fixed():
    assert functions.generate_name_fixed(123123, char_order1, 10) == 'aaaaaaaWNt'
    assert functions.generate_name_fixed(1, char_order1, 10) == 'aaaaaaaaaa'
    assert functions.generate_name_fixed(1313142525, char_order1, 10) == "aaaaBLPAqw"
    assert functions.generate_name_fixed(12, char_order1, 10) == 'aaaaaaaaaF'
    assert functions.generate_name_fixed(52, char_order1, 10) == 'aaaaaaaaaZ'
    assert functions.generate_name_fixed(54, char_order1, 10) == 'aaaaaaaaAA'
    assert functions.generate_name_fixed(2, char_order1, 10) == 'aaaaaaaaaA'
    assert functions.generate_name_fixed(104, char_order1, 10) == 'aaaaaaaaAZ'
    assert functions.generate_name_fixed(105, char_order1, 10) == 'aaaaaaaaba'
    assert functions.generate_name_fixed(53, char_order1, 10) == 'aaaaaaaaAa'
    assert functions.generate_name_fixed(2704, char_order1, 10) == 'aaaaaaaaZZ'
    assert functions.generate_name_fixed(2705, char_order1, 10) == 'aaaaaaaAaa'
    assert functions.generate_name_fixed(2709, char_order1, 10) == 'aaaaaaaAac'
    assert functions.generate_name_fixed(676, char_order2, 5) == 'aaazz'
    assert functions.generate_name_fixed(677, char_order2, 5) == 'aabaa'
    assert functions.generate_name_fixed(0, char_order2, 5) == ''
    assert functions.generate_name_fixed(50, char_order2, 0) == ''
    assert functions.generate_name_fixed(-5, char_order2, 5) == ''
    assert functions.generate_name_fixed(50, '', 5) == ''
    assert functions.generate_name_fixed(50, None, 5) == ''


def test_generate_name():
    assert functions.generate_name(2, char_order3) == 'b'
    assert functions.generate_name(1, char_order3) == 'a'
    assert functions.generate_name(9, char_order3) == 'aa'
    assert functions.generate_name(11, char_order3) == 'ac'
    assert functions.generate_name(73, char_order3) == 'aaa'
    assert functions.generate_name(0, char_order3) == ''
    assert functions.generate_name(-6, char_order3) == ''
    assert functions.generate_name(5, '') == ''
    assert functions.generate_name(5, None) == ''


def test_generate_names_fixed():
    assert functions.generate_names_fixed(1, 5, char_order3, 5) == ['aaaaa', 'aaaab', 'aaaac', 'aaaad', 'aaaae']
    assert functions.generate_names_fixed(11, 14, char_order3, 5) == ['aaabc', 'aaabd', 'aaabe', 'aaabf']
    assert functions.generate_names_fixed(14, 13, char_order3, 5) == []
    assert functions.generate_names_fixed(0, 14, char_order3, 5) == []
    assert functions.generate_names_fixed(-5, 14, char_order3, 5) == []
    assert functions.generate_names_fixed(10, 14, char_order3, 0) == []
    assert functions.generate_names_fixed(10, 14, '', 5) == []
    assert functions.generate_names_fixed(10, 14, None, 5) == []


def test_generate_names():
    assert functions.generate_names(1, 5, char_order3) == ['a', 'b', 'c', 'd', 'e']
    assert functions.generate_names(11, 14, char_order3) == ['ac', 'ad', 'ae', 'af']
    assert functions.generate_names(14, 13, char_order3) == []
    assert functions.generate_names(0, 14, char_order3) == []
    assert functions.generate_names(-5, 14, char_order3) == []
    assert functions.generate_names(10, 14, '') == []
    assert functions.generate_names(10, 14, None) == []


def test_num_from_name_fixed():
    assert functions.num_from_name_fixed('ac', char_order2, 2) == 3
    assert functions.num_from_name_fixed('bc', char_order2, 2) == 29
    assert functions.num_from_name_fixed('abc', char_order2, 3) == 29
    assert functions.num_from_name_fixed('bbd', char_order2, 3) == 706
    assert functions.num_from_name_fixed('aaaaaaaaZZ', char_order1, 10) == 2704
    assert functions.num_from_name_fixed('aaaaaaaaZZ', char_order1, 9) == -1
    assert functions.num_from_name_fixed('aaaaaaaaZZ', char_order3, 10) == -1
    assert functions.num_from_name_fixed('', char_order1, 10) == -1
    assert functions.num_from_name_fixed(None, char_order1, 10) == -1


def test_num_from_name():
    assert functions.num_from_name('ac', char_order3) == 11
    assert functions.num_from_name('ac', char_order2) == 29
    assert functions.num_from_name('bc', char_order2) == 55
    assert functions.num_from_name('abc', char_order2) == 731
    assert functions.num_from_name('bbd', char_order2) == 1408
    assert functions.num_from_name('aaa', char_order3) == 73
    assert functions.num_from_name('aZZ', char_order3) == -1
    assert functions.num_from_name('', char_order1) == -1
    assert functions.num_from_name(None, char_order1) == -1


def test_nums_from_names_fixed():
    assert functions.nums_from_names_fixed('ac', char_order2, 2) == 3
    assert functions.nums_from_names_fixed('bc', char_order2, 2) == 29
    assert functions.nums_from_names_fixed('abc', char_order2, 3) == 29
    assert functions.nums_from_names_fixed('bbd', char_order2, 3) == 706
    assert functions.nums_from_names_fixed('aaaaaaaaZZ', char_order1, 10) == 2704
    assert functions.nums_from_names_fixed('aaaaaaaaZZ', char_order1, 9) == -1
    assert functions.nums_from_names_fixed('aaaaaaaaZZ', char_order3, 10) == -1
    assert functions.nums_from_names_fixed('', char_order1, 10) == -1
    assert functions.nums_from_names_fixed(None, char_order1, 10) == -1


def test_nums_from_names():
    assert functions.nums_from_names('ac', char_order3) == 11
    assert functions.nums_from_names('ac', char_order2) == 29
    assert functions.nums_from_names('bc', char_order2) == 55
    assert functions.nums_from_names('abc', char_order2) == 731
    assert functions.nums_from_names('bbd', char_order2) == 1408
    assert functions.nums_from_names('aaa', char_order3) == 73
    assert functions.nums_from_names('aZZ', char_order3) == -1
    assert functions.nums_from_names('', char_order1) == -1
    assert functions.nums_from_names(None, char_order1) == -1


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

