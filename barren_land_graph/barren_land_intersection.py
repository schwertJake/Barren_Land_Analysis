"""
barren_land_intersection.py
This module is the edge object for the graph of barren land
plots. It takes two barren land (vertex) objects, checks for
an intersecting area, and stores the intersection area if there
is one.
"""
from barren_land_graph.barren_land import BarrenLand


class BarrenIntersection:

    def __init__(self, land0: BarrenLand, index0: int,
                 land1: BarrenLand, index1: int):
        self.land_indexes = (index0, index1)
        self._land0 = land0
        self._land1 = land1
        self.coord_dict = {}  # corner coords of intersection rectangle
        self.intersection_area, self.intersects = \
            self._compute_intersection_2d()

    def _compute_intersection_2d(self) -> (int, bool):
        """
        Computes the total area of intersection of two rectangles
        given their x and y min/max coordinates. It does this by
        first finding the total distance of intersection in the x and
        y dimension individually, then combining them to get the product.

        :return: (int, bool), when int is the total area of intersection
            and the bool is whether or not the two rectangles intersect
        """
        x_max, x_min, x_inter_bool = self._compute_intersection_1d('x')
        y_max, y_min, y_inter_bool = self._compute_intersection_1d('y')
        self.coord_dict = {
            "x0": x_min,
            "y0": y_min,
            "x1": x_max,
            "y1": y_max
        }
        return (x_max - x_min) * (y_max - y_min), \
               x_inter_bool and y_inter_bool

    def _compute_intersection_1d(self, dimension_mask: str) -> (int, int, bool):
        """
        Computes the distance of intersection of two lines in one
        dimension. Does this by first making sure the min and max of
        each line is known and correct, then running through different
        cases of how two lines may intersect, and computing the answer given
        that case.

        :param dimension_mask: mask of dimension of lines, 'x' or 'y'
        :return: (int, bool)
        """
        l0_min = self._land0.coord_dict[dimension_mask+'0']
        l0_max = self._land0.coord_dict[dimension_mask+'1']
        l1_min = self._land1.coord_dict[dimension_mask+'0']
        l1_max = self._land1.coord_dict[dimension_mask+'1']

        # Make sure coordinates are in the right order:
        if l0_min > l0_max:
            l0_min, l0_max = l0_max, l0_min
        if l1_min > l1_max:
            l1_min, l1_max = l1_max, l1_min

        # If the Lines do not intersect at all
        if l0_max < l1_min or l0_min > l1_max:
            return 0, 0, False

        if l0_max == l1_min:
            return l0_max, l1_min, True
        if l0_min == l1_max:
            return l0_min, l1_max, True

        # If one line is fully within the other line:
        if l0_min < l1_min and l0_max > l1_max:
            return l1_max, l1_min, True
        if l1_min <= l0_min and l1_max >= l0_max:
            return l0_max, l0_min, True

        # If one line is partially within the other:
        if l0_min < l1_min < l0_max < l1_max:
            return l0_max, l1_min, True
        if l1_min < l0_min < l1_max < l0_max:
            return l1_max, l0_min, True

        # If we got here, something went horribly wrong
        raise Exception("Couldn't compute intersection of",
                        self.land_indexes)
