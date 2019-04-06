"""
graph.py
This module contains the Graph object made of Barren Land plots
Including a list of vertexes, edges, and adjacency list. These
are used to find cycles within the graph, which are indicative of
borders or barren land. We'll calculate their area in field.py
"""
from barren_land_graph.barren_land import BarrenLand
from barren_land_graph.barren_land_intersection import BarrenIntersection


class BarrenLandGraph:

    def __init__(self, coords_arr: list):
        self.cycles = []
        self.nodes = self._create_nodes(coords_arr)
        self.edges, self.adjacency_list = self._create_edges_and_adj_list()
        self._cycle_search()

    @staticmethod
    def _create_nodes(coords_arr: list) -> list:
        """
        Given a long list of barren land rectangle coordinates of
        form {[x0 y0 x1 y1], [x0...]}, creates an array of BarrenLand
        objects to be used as the nodes of our graph

        :param coord_str: list of form [x0 y0 x1 y1], [x0...]
        :return: array of BarrenLand objects
        """
        nodes = []
        for rectangle in coords_arr:
            nodes.append(BarrenLand(rectangle, len(nodes)))
        return nodes

    def _create_edges_and_adj_list(self) -> (dict, dict):
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

    def _cycle_search(self):
        """
        Looks for cycles starting at all nodes

        :return: None
        """
        for node in self.nodes:
            self._find_new_cycles([node.index])

    def _find_new_cycles(self, path: list):
        """
        Searches for cycles in graph, if found, returns
        the path of the cycle. Checks for and rules out
        duplicates.
        Algorithm adopted from LetterRip's post found here:
        https://stackoverflow.com/questions/12367801/
            finding-all-cycles-in-undirected-graphs

        :param path: list of node indexes
        :return: None
        """
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
                self._find_new_cycles(sub)

            elif len(path) > 2 and next_node == path[-1]:
                p = self._rotate_to_smallest(path)
                inv = self._rotate_to_smallest(path[::-1])
                if p not in self.cycles and inv not in self.cycles:
                    self.cycles.append(p)

    @staticmethod
    def _rotate_to_smallest(path: list) -> list:
        """
        Rotate cycle path such that it begins with the smallest node

        :param path: list of indexes
        :return: rotated list of indexes
        """
        n = path.index(min(path))
        return path[n:] + path[:n]
