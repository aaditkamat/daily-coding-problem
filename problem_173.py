```
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```
def not_a_nested_dict(dictionary):
    return len(list(filter(lambda x: type(x) == dict, dictionary.values()))) == 0

def flatten(dictionary):
    if not_a_nested_dict(dictionary):
        return dictionary
    new_dictionary = {}
    for key in dictionary:
        if not type(dictionary[key]) == dict:
            new_dictionary[key] = dictionary[key]
        else:
            flattened_dictionary = flatten(dictionary[key])
            for namespaced_key in flattened_dictionary:
                new_dictionary[f"{key}.{namespaced_key}"] = flattened_dictionary[namespaced_key]
    return new_dictionary
    

if __name__ == '__main__':
    dictionary = {
                    "key": 3,
                    "foo": {
                        "a": 5,
                        "bar": {
                            "baz": 8
                        }
                     }
                }
    print(flatten(dictionary))
