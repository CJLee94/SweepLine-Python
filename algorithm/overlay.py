from find_intersection import SweepLine
def mapoverlay(s_1, s_2):
    """

    :param s_1: a planar subdivisions stored in doubly connected edge lists.
    :param s_2: a planar subdivisions stored in doubly connected edge lists.
    :return:
        The overlay of s_1 and s_2 stored in doubly-connected edge list D.
    """

    # TODO:Copy the doubly-connected edge list for s_1 and s_2 to a new doubly-connected edge list D
    D = []
    D.append(s_1.edge_list)
    D.append(s_2.edge_list)

    # TODO: Compute all intersections between edges from s_1 and s_2 with the plane sweep algorithm of section 2.1
    sweep_line = SweepLine(D, draw=False, verbose=False)
    sweep

