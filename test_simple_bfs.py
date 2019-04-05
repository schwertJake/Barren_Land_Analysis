import unittest
from simple_bfs import BarrenLandSimple

class TestCreatePlot(unittest.TestCase):

    def setUp(self):
        self.BLS = BarrenLandSimple([], 5, 10)

    def test_plot_dimensions(self):
        self.assertEqual(
            (len(self.BLS.plot), len(self.BLS.plot[0])),
            (10,5)
        )

    def test_plot_entries(self):
        self.assertEqual(self.BLS.plot[1:], self.BLS.plot[:-1])
        self.assertEqual(self.BLS.plot[0][0], 0)

class TestBuildCoordList(unittest.TestCase):

    def test_single_coord_list(self):
        BLS = BarrenLandSimple(["0 5 5 10"])
        self.assertEqual(
            BLS._coord_list, [{
                'x0': 0,
                'y0': 5,
                'x1': 5,
                'y1': 10
            }]
        )

    def test_multiple_coord_list(self):
        BLS = BarrenLandSimple(["0 10 10 20",
                                 "5 25 25 50"])
        self.assertEqual(
            BLS._coord_list,[{
                'x0': 0,
                'y0': 10,
                'x1': 10,
                'y1': 20
            },
            {
                'x0': 5,
                'y0': 25,
                'x1': 25,
                'y1': 50
            }]
        )


class TestPopulateBarrenLand(unittest.TestCase):

    def test_barren_land_plotted(self):
        BLS = BarrenLandSimple(["0 2 2 3"], 3, 5)
        self.assertEqual(BLS.plot,
                         [[0]*3, [0]*3, [-1]*3, [-1]*3, [0]*3])


class TestBFS(unittest.TestCase):

    def test_empty_small_plot(self):
        empty_small_BLS = BarrenLandSimple([], 10, 10)
        self.assertEqual(empty_small_BLS._bfs(0,0), 100)

    def test_empty_large_plot(self):
        empty_large_BLS = BarrenLandSimple([], 400, 600)
        self.assertEqual(empty_large_BLS._bfs(0,0), 240000)

    def test_starting_barren_land(self):
        barren_BLS = BarrenLandSimple(["0 3 4 4"], 5, 5)
        self.assertEqual(barren_BLS._bfs(0,3), 0)

    def test_running_into_barren(self):
        barren_BLS = BarrenLandSimple(["0 4 4 5"], 5, 10)
        self.assertEqual(barren_BLS._bfs(0,0), 20)

class TestFindAllFertileArea(unittest.TestCase):

    def test_empty_case(self):
        BLS = BarrenLandSimple([])
        self.assertEqual(BLS.find_all_fertile_areas(), [240000])

    def test_example_case_1(self):
        BLS = BarrenLandSimple(["0 292 399 307"])
        self.assertEqual(BLS.find_all_fertile_areas(), [116800, 116800])

    def test_example_case_2(self):
        BLS = BarrenLandSimple(["48 192 351 207",
                                "48 392 351 407",
                                "120 52 135 547",
                                "260 52 275 547"])
        self.assertEqual(BLS.find_all_fertile_areas(), [22816, 192608])

if __name__ == '__main__':
    unittest.main()
