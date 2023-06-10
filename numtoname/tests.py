import numtoname.functions as functions
import numtoname.helpers  as helpers

import sys
from tqdm import tqdm, trange


alphabet1 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
alphabet2 = 'abcdefghijklmnopqrstuvwxyz'
alphabet3 = 'abcdefgh'
alphabet4 = 'abc'


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

    assert functions.generate_name_fixed(676, alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', 'aaaaa', 'aaaaz', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabaf']) == 'aabag'
    assert functions.generate_name_fixed(676, alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', 'aaaa', 'aaaz', 'aagg', 'aaaaa', 'aabaa', 'aabab', 'aabac']) == 'aabad'
    assert functions.generate_name_fixed(676, alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', '', '', '', 'aaaaa', 'aabaa', 'aabab', 'aabac']) == 'aabad'
    assert functions.generate_name_fixed(676, alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', 'A', '', 'B', 'aaaaa', 'aabaa', 'aabab', 'aabac']) == 'aabad'
    assert functions.generate_name_fixed(676, alphabet2, 5, invalid_names = []) == 'aaazz'

    assert functions.generate_name_fixed(2, alphabet4, 10, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'bbbbbbbbbb'
    assert functions.generate_name_fixed(3, alphabet4, 8, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'cccccccc'
    assert functions.generate_name_fixed(4, alphabet4, 8, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'cccccccc'
    assert functions.generate_name_fixed(999, alphabet4, 8, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'cccccccc'
    assert functions.generate_name_fixed(1, alphabet4, 10, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'bbbbbbbbbb'
    assert functions.generate_name_fixed(2, alphabet4, 10, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'cccccccccc'


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

    assert functions.generate_name(702, alphabet2, invalid_names = ['dfg', 'qwe', 'a', 'z', 'gg', 'aaaaaaaaaa', 'aaa', 'aab', 'aae']) == 'aaf'
    assert functions.generate_name(702, alphabet2, invalid_names = ['dfg', 'qwe', 'a', 'z', '', 'aaaaaaaaaa', 'aaa', 'aab', 'aad']) == 'aae'
    assert functions.generate_name(702, alphabet2, invalid_names = ['dfg', 'qwe', 'a', 'z', 'A', 'aaaaaaaaaa', 'aaa', 'aab', 'aad']) == 'aae'
    assert functions.generate_name(73, alphabet3, invalid_names = []) == 'aaa'

    assert functions.generate_name(2, alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'b'
    assert functions.generate_name(27, alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'ccccccccc'
    assert functions.generate_name(28, alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'aaaaaaaaaa'
    assert functions.generate_name(26, alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'bbbbbbbbb'
    assert functions.generate_name(16, alphabet4, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'cccccccc'
    assert functions.generate_name(13, alphabet4, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 'bbbbbbb'


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

    assert functions.generate_names_fixed(alphabet2, 5, start_num = 676, end_num = 680, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaaa', 'aaaaz', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabaf', 'aabaj']) == ['aabag', 'aabah', 'aabai', 'aabak', 'aabal']
    assert functions.generate_names_fixed(alphabet2, 5, start_num = 676, end_num = 680, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaa', 'aaaz', 'aagg', 'aaaaa', 'aabaa', 'aabab', 'aabac', 'aabag']) == ['aabad', 'aabae', 'aabaf', 'aabah', 'aabai']
    assert functions.generate_names_fixed(alphabet2, 5, start_num = 676, end_num = 680, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaaB', 'aaazA', 'aagg', 'aaaaa', 'aabaa', 'aabab', 'aabac', 'aabag']) == ['aabad', 'aabae', 'aabaf', 'aabah', 'aabai']
    assert functions.generate_names_fixed(alphabet2, 5, num_list = [2, 9, 14, 15], invalid_names=[]) == ['aaaab', 'aaaai', 'aaaan', 'aaaao']

    assert functions.generate_names_fixed(alphabet4, 5, start_num = 2, end_num = 3, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == ['bbbbb', 'ccccc']
    assert functions.generate_names_fixed(alphabet4, 5, start_num = 2, end_num = 6, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == ['bbbbb', 'ccccc', 'ccccc', 'ccccc', 'ccccc']
    assert functions.generate_names_fixed(alphabet4, 5, start_num = 1, end_num = 3, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == ['bbbbb', 'ccccc', 'ccccc']


def test_generate_names():
    assert functions.generate_names(alphabet3, start_num = 1, end_num = 5) == ['a', 'b', 'c', 'd', 'e']
    assert functions.generate_names(alphabet3, num_list = [11, 12, 13, 14]) == ['ac', 'ad', 'ae', 'af']
    assert functions.generate_names(alphabet2, num_list = [2, 9, 14, 15]) == ['b', 'i', 'n', 'o']
    assert functions.generate_names(alphabet3, start_num = 14, end_num = 13) == []
    assert functions.generate_names(alphabet2, num_list = [0, 9, 14, 15]) == ['', 'i', 'n', 'o']
    assert functions.generate_names(alphabet3, start_num = 0, end_num = 5) == []
    assert functions.generate_names('', num_list = [2, 9, 14, 15]) == []
    assert functions.generate_names(None, start_num = 1, end_num = 5) == []

    assert functions.generate_names(alphabet2, start_num = 702, end_num = 705, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', 'gg', 'aaaaaaaaaa', 'aaa', 'aab', 'aae', 'aah']) == ['aaf', 'aag', 'aai', 'aaj']
    assert functions.generate_names(alphabet2, start_num = 702, end_num = 705, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', '', 'aaaaaaaaaa', 'aaa', 'aab', 'aad', 'aag']) == ['aae', 'aaf', 'aah', 'aai']
    assert functions.generate_names(alphabet2, start_num = 702, end_num = 705, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', 'A', 'aaaaaaaaaa', 'aaa', 'aab', 'aad', 'aag']) == ['aae', 'aaf', 'aah', 'aai']
    assert functions.generate_names(alphabet3, num_list = [11, 12, 13, 14], invalid_names = []) == ['ac', 'ad', 'ae', 'af']

    assert functions.generate_names(alphabet4, start_num = 2, end_num = 3, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == ['b', 'c']
    assert functions.generate_names(alphabet4, start_num = 17, end_num = 19, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == ['bbbbbb', 'cccccc', 'aaaaaaa']
    assert functions.generate_names(alphabet4, start_num = 13, end_num = 16, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == ['bbbbbbb', 'ccccccc', 'bbbbbbbb', 'cccccccc']


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

    assert functions.num_from_name_fixed('aaazz', alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', 'aaaaa', 'aaaaz', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabaf']) == 672
    assert functions.num_from_name_fixed('aaazz', alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', 'aaaaa', '', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabae']) == 673
    assert functions.num_from_name_fixed('aaazz', alphabet2, 5, invalid_names = ['aadfg', 'aaqwe', 'aaaaa', 'aaaaZ', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabae']) == 673
    assert functions.num_from_name_fixed('abc', alphabet2, 3, invalid_names = []) == 29

    assert functions.num_from_name_fixed('bbbbbbbbbb', alphabet4, 10, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 2
    assert functions.num_from_name_fixed('cccccccc', alphabet4, 8, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 3
    assert functions.num_from_name_fixed('abababab', alphabet4, 8, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == -1
    assert functions.num_from_name_fixed('bbbbbbba', alphabet4, 8, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == -1
    assert functions.num_from_name_fixed('bbbbbbbbbb', alphabet4, 10, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 1
    assert functions.num_from_name_fixed('cccccccccc', alphabet4, 10, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 2


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

    assert functions.num_from_name('zz', alphabet2, invalid_names = ['dfg', 'qwe', 'a', 'z', 'gg', 'aaaaaaaaaa', 'aaa', 'aab', 'aae']) == 699
    assert functions.num_from_name('zz', alphabet2, invalid_names = ['dfg', 'qwe', 'a', 'z', '', 'aaaaaaaaaa', 'aaa', 'aab', 'aad']) == 700
    assert functions.num_from_name('zz', alphabet2, invalid_names = ['dfg', 'qwe', 'aA', 'z', 'gg', 'aaaaaaaaaa', 'aaa', 'aab', 'aad']) == 700
    assert functions.num_from_name('bbd', alphabet2, invalid_names = []) == 1408

    assert functions.num_from_name('b', alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 2
    assert functions.num_from_name('ccccccccc', alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 27
    assert functions.num_from_name('aaaaaaaaaa', alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 28
    assert functions.num_from_name('bbbbbbbbb', alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 26
    assert functions.num_from_name('cccccccc', alphabet4, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 16
    assert functions.num_from_name('bbbbbbb', alphabet4, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) == 13


def test_nums_from_names_fixed():
    assert functions.nums_from_names_fixed(['aaaaa', 'aaaab', 'aaaac', 'aaaad', 'aaaae'], alphabet2, 5) == [1, 2, 3, 4, 5]
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], alphabet2, 2) == [3, 4, 27, 29]
    assert functions.nums_from_names_fixed(['acb', 'ad', 'ba', 'b'], alphabet2, 2) == [-1, 4, 27, -1]
    assert functions.nums_from_names_fixed(['ac', 'zz', 'ba', 'bc'], alphabet3, 2) == [3, -1, 9, 11]
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], alphabet2, -5) == []
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], '', 2) == []
    assert functions.nums_from_names_fixed([], alphabet3, 2) == []

    assert functions.nums_from_names_fixed(['aabag', 'aabah', 'aabai', 'aabak', 'aabal'], alphabet2, 5, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaaa', 'aaaaz', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabaf', 'aabaj']) == [676, 677, 678, 679, 680]
    assert functions.nums_from_names_fixed(['aabad', 'aabae', 'aabaf', 'aabah', 'aabai'], alphabet2, 5, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaa', 'aaaz', 'aagg', 'aaaaa', 'aabaa', 'aabab', 'aabac', 'aabag']) == [676, 677, 678, 679, 680]
    assert functions.nums_from_names_fixed(['aabad', 'aabae', 'aabaf', 'aabah', 'aabai'], alphabet2, 5, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaaB', 'aaazA', 'aagg', 'aaaaa', 'aabaa', 'aabab', 'aabac', 'aabag']) == [676, 677, 678, 679, 680]
    assert functions.nums_from_names_fixed(['aabag', 'aabah', 'aaagg', 'aabak', 'aabal'], alphabet2, 5, \
        invalid_names = ['aadfg', 'aaqwe', 'aaaaa', 'aaaaz', 'aaagg', 'aaaaa', 'aabaa', 'aabab', 'aabaf', 'aabaj']) == [676, 677, -1, 679, 680]
    assert functions.nums_from_names_fixed(['ac', 'ad', 'ba', 'bc'], alphabet2, 2, invalid_names = []) == [3, 4, 27, 29]

    assert functions.nums_from_names_fixed(['bbbbb', 'ccccc'], alphabet4, 5, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == [2, 3]
    assert functions.nums_from_names_fixed(['bbbbb', 'ccccc', 'bbbbc', 'ababa'], alphabet4, 5, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == [2, 3, -1, -1]
    assert functions.nums_from_names_fixed(['bbbbb', 'ccccc'], alphabet4, 5, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == [1, 2]


def test_nums_from_names():
    assert functions.nums_from_names(['a', 'b', 'c', 'd', 'e'], alphabet2) == [1, 2, 3, 4, 5]
    assert functions.nums_from_names(['ac', 'ad', 'ba', 'bc'], alphabet2) == [29, 30, 53, 55]
    assert functions.nums_from_names(['ac', 'zz', 'ba', 'bc'], alphabet3) == [11, -1, 17, 19]
    assert functions.nums_from_names(['ac', 'ad', 'ba', 'bc'], '') == []
    assert functions.nums_from_names([], alphabet3) == []

    assert functions.nums_from_names(['aaf', 'aag', 'aai', 'aaj'], alphabet2, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', 'gg', 'aaaaaaaaaa', 'aaa', 'aab', 'aae', 'aah']) == [702, 703, 704, 705]
    assert functions.nums_from_names(['aae', 'aaf', 'aah', 'aai'], alphabet2, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', '', 'aaaaaaaaaa', 'aaa', 'aab', 'aad', 'aag']) == [702, 703, 704, 705]
    assert functions.nums_from_names(['aae', 'aaf', 'aah', 'aai'], alphabet2, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', 'A', 'aaaaaaaaaa', 'aaa', 'aab', 'aad', 'aag']) == [702, 703, 704, 705]
    assert functions.nums_from_names(['aaf', 'aag', 'aai', 'aaj'], alphabet2, \
        invalid_names = ['dfg', 'qwe', 'a', 'z', 'gg', 'aaaaaaaaaa', 'aaa', 'aab', 'aae', 'aah', 'aai']) == [702, 703, -1, 704]
    assert functions.nums_from_names(['ac', 'ad', 'ba', 'bc'], alphabet2, invalid_names = []) == [29, 30, 53, 55]

    assert functions.nums_from_names(['b', 'c'], alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == [2, 3]
    assert functions.nums_from_names(['bbbbbb', 'cccccc', 'aaaaaaa'], alphabet4, invalid_names = ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == [17, 18, 19]
    assert functions.nums_from_names(['bbbbbbb', 'ccccccc', 'bbbbbbbb', 'cccccccc'], alphabet4, invalid_names = ['a', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'], invalid_contained = True) \
          == [13, 14, 15, 16]


def test_get_permutations_containing_name():
    name = 'bob'
    name_length = 5
    assert len(helpers.get_permutations_containing_name(alphabet3, name, name_length)) == (name_length - len(name) + 1) * (len(alphabet3) ** (name_length - len(name)))
    name_length = 7
    assert len(helpers.get_permutations_containing_name(alphabet3, name, name_length)) == (name_length - len(name) + 1) * (len(alphabet3) ** (name_length - len(name)))
    name = 'bb'
    name_length = 4
    assert len(helpers.get_permutations_containing_name(alphabet3, name, name_length)) == (name_length - len(name) + 1) * (len(alphabet3) ** (name_length - len(name)))
    assert len(helpers.get_permutations_containing_name(alphabet2, name, name_length)) == (name_length - len(name) + 1) * (len(alphabet2) ** (name_length - len(name)))


if __name__ == '__main__':
    tests = [test_generate_name_fixed, test_generate_name, 
             test_generate_names_fixed, test_generate_names, 
             
             test_num_from_name_fixed, test_num_from_name,
             test_nums_from_names_fixed, test_nums_from_names,
             
             test_get_permutations_containing_name]
    
    for i in trange(len(tests)):
        tests[i]()
        print(f'\n{i + 1} / {len(tests)} tests passed.\n')

    print('\n\nAll tests passed successfully!')

