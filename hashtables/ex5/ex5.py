# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # dict of filepaths - filenames
    d = {}

    # list to store results
    result = []

    # look through list of files and paths
    for i in range(len(files)):
        filename = files[i].split('/')[-1]
        filepath = files[i]

        # if the filepath isn't already listed add it to the dict
        if filename not in d:
            # key is the filename and the value will be a list of filepaths
            d[filename] = []

        # store a list of the paths this filename is at
        d[filename].append(filepath)

    # for each file query see if we have an entry in our dict
    for filename in queries:
        if filename in d:
            for filepath in d[filename]:
                result.append(filepath)

    return result


# if __name__ == "__main__":
#     files = [
#         '/bin/foo',
#         '/bin/bar',
#         '/usr/bin/baz'
#     ]
#     queries = [
#         "foo",
#         "qux",
#         "baz"
#     ]
#     print(finder(files, queries))
