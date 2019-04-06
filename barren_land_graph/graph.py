from barren_land_graph.barren_land import BarrenLand
from barren_land_graph.barren_land_intersection import BarrenIntersection
from collections import Counter

class BarrenLandGraph:

    def __init__(self, coords_arr: list):
        self.cycles = []
        self.nodes = self.create_nodes(coords_arr)
        self.edges, self.adjacency_list = self.create_edges_and_adj_list()
        self.cycle_search()

    def create_nodes(self, coords_arr: list) -> list:
        """
        Given a long string of raw barren land rectangle coordinates of
        form {"x0 y0 x1 y1", "x0..."}, creates an array of BarrenLand
        objects to be used as the nodes of our graph

        :param raw_coord_str: string of form {"x0 y0 x1 y1", "x0..."}
        :return: array of BarrenLand objects
        """
        nodes = []
        for rectangle in coords_arr:
            nodes.append(BarrenLand(rectangle, len(nodes)))
        return nodes

    def create_edges_and_adj_list(self) -> (dict, dict):
        """
        Given the list of BarrenLand objects, checks for intersections
        between all nodes (O(V^2) operation) and creates a dictionary
        of form {(index1, index2): BarrenIntersection Object}
        While doing this calculation, the adjacency list of all nodes
        is created and returned. Form of
        {index: [adjindex1, adjindex2,..]}

        :return: dict of edges, dict of adjacency list
        """
        edges, adj_list = {}, {}
        for node in self.nodes:
            adj_list[node.index] = []
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                test_edge = BarrenIntersection(self.nodes[i], i,
                                               self.nodes[j], j)
                if test_edge.intersects:
                    edges.update({(i, j): test_edge})
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        return edges, adj_list

    def cycle_search(self):
        for edge in self.edges.keys():
            for node in edge:
                self.findNewCycles([node])

    def findNewCycles(self, path):
        start_node = path[0]
        next_node = None

        for edge in self.edges.keys():

            if start_node in edge:
                if edge[0] == start_node:
                    next_node = edge[1]
                else:
                    next_node = edge[0]

            if next_node and next_node not in path:
                sub = [next_node]
                sub.extend(path)
                self.findNewCycles(sub)

            elif len(path) > 2 and next_node == path[-1]:
                p = self.rotate_to_smallest(path)
                inv = self.rotate_to_smallest(path[::-1])
                if not p in self.cycles and not inv in self.cycles:
                    self.cycles.append(p)

    #  rotate cycle path such that it begins with the smallest node
    @staticmethod
    def rotate_to_smallest(path):
        n = path.index(min(path))
        return path[n:] + path[:n]


if __name__ == "__main__":
    BarrenLandGraph(["48 192 351 207",
                     "48 392 351 407",
                     "120 52 135 547",
                     "260 52 275 547"])