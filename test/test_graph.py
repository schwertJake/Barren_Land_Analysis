import unittest
from barren_land_graph.graph import BarrenLandGraph
from barren_land_graph.barren_land import BarrenLand


class TestCreateNode(unittest.TestCase):

    def setUp(self):
        self.BLG_one = BarrenLandGraph([[0, 292, 399, 307]])
        self.BLG_many = BarrenLandGraph(
            [[48, 192, 351, 207],
             [48, 392, 351, 407],
             [120, 52, 135, 547],
             [260, 52, 275, 547]])

    def test_create_node_single(self):
        self.assertEqual(
            [x.coord_dict for x in self.BLG_one.nodes],
            [BarrenLand([0, 292, 399, 307], 0).coord_dict]
        )

    def test_create_node_many(self):
        self.assertEqual(
            [x.coord_dict for x in self.BLG_many.nodes],
            [BarrenLand([48, 192, 351, 207], 0).coord_dict,
             BarrenLand([48, 392, 351, 407], 1).coord_dict,
             BarrenLand([120, 52, 135, 547], 2).coord_dict,
             BarrenLand([260, 52, 275, 547], 3).coord_dict]
        )

class TestCreateEdgesAndAdjList(unittest.TestCase):

    def setUp(self):
        self.BLG_one = BarrenLandGraph([[0, 292, 399, 307]])
        self.BLG_many = BarrenLandGraph(
            [[48, 192, 351, 207],
             [48, 392, 351, 407],
             [120, 52, 135, 547],
             [260, 52, 275, 547]])

    def test_edges_one(self):
        self.assertEqual(self.BLG_one.edges, {})

    def test_adj_list_one(self):
        self.assertEqual(self.BLG_one.adjacency_list, {0: []})

    def test_edges_many(self):
        self.assertEqual(
            list(self.BLG_many.edges.keys()),
            [(0,2), (0,3), (1,2), (1,3)])

    def test_adj_list_many(self):
        self.assertEqual(
            self.BLG_many.adjacency_list,
            {0: [2,3],
             1: [2,3],
             2: [0,1],
             3: [0,1]})

class TestCycleSearch(unittest.TestCase):

    def setUp(self):
        self.BLG_one = BarrenLandGraph([[0, 292, 399, 307]])
        self.BLG_many = BarrenLandGraph(
            [[48, 192, 351, 207],
             [48, 392, 351, 407],
             [120, 52, 135, 547],
             [260, 52, 275, 547]])

    def test_cycles_one(self):
        self.assertEqual(self.BLG_one.cycles, [])

    def test_cycles_many(self):
        self.assertEqual(self.BLG_many.cycles, [[0, 3, 1, 2]])
