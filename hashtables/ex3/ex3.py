def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # dict to count the number of times we encounter a given number
    d = {}

    # list to nums that exist in every sub array
    result = []

    # loop through the arrays and count all the occurances of each num
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            # if we haven't seen this num before
            if arrays[i][j] not in d:
                # init its count to 0
                d[arrays[i][j]] = 0

            # increase the count each time we encounter this num
            d[arrays[i][j]] += 1

    # look through the d and find all nums that occur in all arrays
    for k in d.keys():
        if d[k] == len(arrays):
            # add these to the results list
            result.append(k)

    return result


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
