"""
This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5

"""
class PrefixMapSum:
    def __init__(self):
        self.mapping = {}

    def insert(self, key: str, value: int):
        self.mapping[key] = value

    def sum(self, prefix: str) -> int:
        return sum(map(lambda x: x[1], 
            filter(lambda x: x[0].find(prefix) == 0, self.mapping.items())))


if __name__ == '__main__':
    mapsum = PrefixMapSum()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
