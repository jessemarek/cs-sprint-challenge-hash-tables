#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # dict to store the tickets source and destination
    d = {}

    # list of the route order
    route = []

    # fill the dict with the source - destination key - value pairs
    for i in range(length):
        if tickets[i].source not in d:
            d[tickets[i].source] = tickets[i].destination

    # add the origin to the route list
    route.append(d["NONE"])

    # build the chain of tickets in order
    for i in range(1, length):
        route.append(d[route[i-1]])

    return route
