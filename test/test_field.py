import unittest
from barren_land_graph.field import Field


class TestFindCycleArea(unittest.TestCase):

    def test_empty_case(self):
        F = Field([])
        self.assertEqual(F.find_all_fertile_areas(), [240000])

    def test_example_case_1(self):
        F = Field([[0, 292, 399, 307]])
        self.assertEqual(F.find_all_fertile_areas(), [116800, 116800])

    def test_example_case_2(self):
        F = Field([[48, 192, 351, 207],
                   [48, 392, 351, 407],
                   [120, 52, 135, 547],
                   [260, 52, 275, 547]])
        self.assertEqual(F.find_all_fertile_areas(), [22816, 192608])