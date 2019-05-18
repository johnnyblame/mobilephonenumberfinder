from mobilephonefinder import TrieNode, items


def test_search1():
    root = TrieNode()
    root.put('380671234213')
    root.put('380324514313')
    root.put('312453441234')
    root.search('20')
    expected = []
    assert items == expected
