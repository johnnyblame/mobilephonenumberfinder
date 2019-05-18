from mobilephonefinder import TrieNode, items


def test_read_file():
    with open('test.txt', 'r') as f:
        root = TrieNode()
        line = str(f.readline().strip('\r\n'))
        while line != '':
            root.put(line)
            line = str(f.readline().strip('\r\n'))
        return root


def test():
    root = test_read_file()
    root.search('380')
    expected = ['380675674432', '380672832500', '380983567721']
    assert items == expected

def test2():
    items.clear()
    root = test_read_file()
    root.search('3806')
    expected = ['380675674432', '380672832500']
    assert items == expected

def test3():
    items.clear()
    root = test_read_file()
    root.search('380983')
    expected = ['380983567721']
    assert items == expected
