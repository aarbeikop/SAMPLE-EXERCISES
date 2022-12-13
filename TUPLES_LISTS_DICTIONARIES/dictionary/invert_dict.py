# create an inverted dictionary from a given dictionary
# the inverted dictionary should have the values of the original dictionary as keys
# the values of the inverted dictionary should be lists of keys from the original dictionary
#

def invert(d):
    inv = {}
    for k, v in d.items():
        if v not in inv:
            inv[v] = [k] # create a list with the key
        else:
            inv[v].append(k) # append the key to the list
    return inv

d = {'a': 1, 'b': 2, 'c': 3}
print(invert(d)) # prints {1: ['a'], 2: ['b'], 3: ['c']}