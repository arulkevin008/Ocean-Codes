def remove_key(d, key):
    try:
        del d[key]
    except KeyError:
        print(f"Key '{key}' not found.")
    return d

print(remove_key({'a': 1, 'b': 2}, 'b'))  
print(remove_key({'a': 1, 'b': 2}, 'c'))  
