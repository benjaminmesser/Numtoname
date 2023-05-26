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


if __name__ == '__main__':
    test_generate_name_fixed()
    test_generate_name()
    test_generate_names_fixed()
    test_generate_names()

    print('All tests passed successfully!')

