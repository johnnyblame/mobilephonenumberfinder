items = []
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def put(self, number):
        if len(number) == 0:
            self.end = True
            return
        k = number[0]
        number = number[1:]
        if k in self.children.keys():
            self.children[k].put(number)
        else:
            node = TrieNode()
            self.children[k] = node
            node.put(number)

    def dfs(self, so_far=None):
        if self.children.keys() is []:
            items.append(so_far)
        if self.end is True:
            items.append(so_far)
        for key in self.children.keys():
            self.children[key].dfs(so_far + key)

    def search(self, search_number, so_far=''):
        if len(search_number) > 0:
            k = search_number[0]
            search_number = search_number[1:]
            if k in self.children.keys():
                so_far = so_far + k
                self.children[k].search(search_number, so_far)
            else:
                print('No Match')

        else:
            if self.end is True:
                print(so_far)
            for key in self.children.keys():
                self.children[key].dfs(so_far + key)


def read_file():
    with open('pn.txt', 'r') as f:
        root = TrieNode()
        line = str(f.readline().strip('\r\n'))
        while line != '':
            root.put(line)
            line = str(f.readline().strip('\r\n'))
        return root


if __name__ == "__main__":

    root = read_file()
    print('Input: ')
    inp = input()
    root.search(inp)
    if len(items) == 0:
        print('')
    else:
        print(items[:10])
