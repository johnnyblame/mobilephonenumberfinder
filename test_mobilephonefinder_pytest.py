from mobilephonefinder import read_file, TrieNode, items
import pytest
@pytest.fixture()
def test_put():
    root = TrieNode()
    res = root.put('38067')
    assert res is None


def test_search1():
    root = read_file()
    root.search('380')
    expected = ['380675674432', '380672832500', '380676767676', '380699999999', '380698989898', '380690000090',
                '380600000000', '380623213123', '380623412515', '380654234235']
    assert items[:10] == expected


def test_search2():
    number = ''
    root = TrieNode()
    res = root.put(number)
    assert res is None
