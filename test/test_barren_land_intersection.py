import unittest
from barren_land_graph.barren_land_intersection import BarrenIntersection
from barren_land_graph.barren_land import BarrenLand


class TestComputeIntersection(unittest.TestCase):

    def setUp(self):
        self.BI_intersect = BarrenIntersection(
            BarrenLand([0, 0, 10, 10,], 0), 0,
            BarrenLand([5, 5, 15, 15], 1), 1)
        self.BI_bordering = BarrenIntersection(
            BarrenLand([0, 0, 10, 10], 2), 2,
            BarrenLand([11, 11, 20, 20], 3), 3)
        self.BI_seperate = BarrenIntersection(
            BarrenLand([0, 0, 10, 10], 4), 4,
            BarrenLand([15, 15, 20, 20], 5), 5)

    def test_intersection(self):
        self.assertEqual(
            self.BI_intersect._compute_intersection_1d('x'),
            (11, 5, True))
        self.assertEqual(
            self.BI_intersect._compute_intersection_1d('y'),
            (11, 5, True))
        self.assertEqual(
            self.BI_intersect._compute_intersection_2d(),
            (36, True))
        self.assertEqual(
            self.BI_intersect.coord_dict,
            {
                "x0": 5,
                "y0": 5,
                "x1": 11,
                "y1": 11
            }
        )

    def test_bordering(self):
        self.assertEqual(
            self.BI_bordering._compute_intersection_1d('x'),
            (11, 11, True))
        self.assertEqual(
            self.BI_bordering._compute_intersection_1d('y'),
            (11, 11, True))
        self.assertEqual(
            self.BI_bordering._compute_intersection_2d(),
            (0, True))
        self.assertEqual(
            self.BI_bordering.coord_dict,
            {
                "x0": 11,
                "y0": 11,
                "x1": 11,
                "y1": 11
            }
        )

    def test_seperate(self):
        self.assertEqual(
            self.BI_seperate._compute_intersection_1d('x'),
            (0, 0, False))
        self.assertEqual(
            self.BI_seperate._compute_intersection_1d('y'),
            (0, 0, False))
        self.assertEqual(
            self.BI_seperate._compute_intersection_2d(),
            (0, False))
        self.assertEqual(
            self.BI_seperate.coord_dict,
            {
                "x0": 0,
                "y0": 0,
                "x1": 0,
                "y1": 0
            }
        )
