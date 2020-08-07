def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # dict to store total weight and which indices
    d = {}

    # store the index numbers for answer
    indices = []

    # loop through list and add each weight to the list
    # along with the index number
    for i in range(length):
        if weights[i] not in d:
            d[weights[i]] = i

    # check each weight. if (limit - weight) is in d we have
    # another weight that adds up to the limit
    for i in range(length):
        if limit - weights[i] in d:
            indices.append(i)

    # if the list is not empty sort it in reverse order
    # and return tuple of index nums
    if len(indices) >= 1:
        indices = sorted(indices, reverse=True)

        return tuple(indices)

    else:
        return None
