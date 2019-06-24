```
This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
```

def count(lst):
    count_store = {}
    for num in lst:
        if num in count_store:
            count_store[num] += 1
        else:
            count_store[num] = 1
    return count_store
            
def lists_are_equal(lst1, lst2):
    return count(lst1) == count(lst2)

def concatenation_match(substring, words, word_length):
    substring_words = [substring[i: i + word_length] for i in range(0, len(substring), word_length)]
    return lists_are_equal(substring_words, words)
    
    
def find_indices(s, words):
    word_length = len(words[0])
    substring_length = word_length * len(words)
    indices_list = []
    for i in range(len(s) - substring_length + 1):
        if concatenation_match(s[i: i + substring_length], words, word_length):
            indices_list.append(i)
    return indices_list

if __name__ == '__main__':
    s = input('Enter a string: ')
    words = input('Enter some words: ').split(' ')
    print(find_indices(s, words))
