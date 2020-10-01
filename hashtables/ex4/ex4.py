def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    positives = []
    result = []

    # iterate through numbers in array
    for num in a:
        # if num is positive
        if num >= 0:
            # make it negative and add it to positive array
            num = -1 * num
            positives.append(num)
        # otherwise add the negatives to cache
        else:
            cache[num] = 0
    
    # iterate through numbers in "positives"
    for num in positives:
        # if num exists in cache
        if num in cache:
            # convert back to positive
            num = -1 * num 
            # then add it to results array
            result.append(num)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
