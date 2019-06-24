```
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

```
def count(cont):
    cont_map = {}
    for char in cont:
        if char in cont_map:
            cont_map[char] += 1
        else:
            cont_map[char] = 1
    return cont_map

def lists_are_equal(lst1, lst2):
    return count(lst1) == count(lst2) 

def exists_one_to_one_character_mapping(s1, s2):
    s1_map = count(s1)
    s2_map = count(s2)
    return lists_are_equal(s1_map.values(), s2_map.values())
    

if __name__ == '__main__':
    s1 = input('Enter the first string: ')
    s2 = input('Enter the second string: ')
print(exists_one_to_one_character_mapping(s1, s2))
