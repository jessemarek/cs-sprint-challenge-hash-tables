def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # dict to store a count of values
    d = {}

    # list to store results
    result = []

    for i in range(len(a)):
        # get the absolute value of a number
        num = abs(a[i])
        # if the num is not in the dict add it
        if num not in d:
            # init the count to 0
            d[num] = 0

        # increase the count by 1
        d[num] += 1

    # look through dict at all nums listed
    for k, v in d.items():
        # if the count of a num is 2 then we have a number
        # that had a negative in the list as well
        if v == 2:
            # add this number to the results list
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
