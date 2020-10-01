def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    # iterate through each list in array
    for li in arrays:
        # iterate through each # in that list
        for num in li:
            # if num exists in cache, then increment its value
            if num in cache:
                cache[num] += 1
                # check if the index is equal to len of array
                if cache[num] == len(arrays):
                    # if so, the num exists in all the lists - add to results
                    result.append(num)
            # otherwise add it to cache and set value to 1
            else:
                cache[num] = 1
        
    return result


    # result = set(arrays[0]).intersection(arrays[:1])
    # return result
    

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
