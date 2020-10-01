def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(length):
        # store each weight's value as key and index as its value
        cache[weights[i]] = i
        
    # loop through list again, calc the value we need to meet limit
    for j in range(length):
        v = limit - weights[j]
        # check to see if the hash table contains an entry for v
        if v in cache:
            return [cache[v], j]

    return None

print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))