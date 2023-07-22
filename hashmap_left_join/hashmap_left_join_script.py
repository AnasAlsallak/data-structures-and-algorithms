from hash.hash_table import HashTable

def left_join(hashmap1, hashmap2):
    """
    Function that takes in two hashmaps and returns a list of lists containing the keys and values
    from hashmap1 and hashmap2. If a key from hashmap1 is not present in hashmap2, the value will be
    None.
    """
    output = []
    if not isinstance(hashmap1, HashTable) or not isinstance(hashmap2, HashTable):
        raise TypeError("Both inputs must be hashmaps")        
    
    for key in hashmap1.keys():
            if hashmap2.has(key):
                output.append([key, hashmap1.get(key), hashmap2.get(key)])
            else:
                output.append([key, hashmap1.get(key), None])
    return output