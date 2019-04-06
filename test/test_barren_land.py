import unittest
from barren_land_graph.barren_land import BarrenLand

class TestAssignCoordinates(unittest.TestCase):

    def test_normal_ints(self):
        BL = BarrenLand([0, 1, 2, 3], 0)
        self.assertEqual(BL.coord_dict,
                         {
                             "x0": 0,
                             "y0": 1,
                             "x1": 3,
                             "y1": 4
                         })

    def test_string_values_exception(self):
        with self.assertRaises(TypeError):
            BarrenLand("0 1 2 3", 0)


class TestArea(unittest.TestCase):

    def test_area_arithmetic(self):
        BL = BarrenLand([0, 0, 5, 5], 0)
        self.assertEqual(BL.area, 36)
