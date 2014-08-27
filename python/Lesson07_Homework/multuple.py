"""Program takes as data a tuple of two-element tuples and prints out the results of multiplying each pair."""

multuple = [(1,1),(2,2),(12,13),(4,4),(99,99)]

for a, b in multuple:
    print("{2:4} = {0} x {1}".format(a, b, a*b))