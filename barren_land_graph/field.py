from barren_land_graph.graph import BarrenLandGraph

class Field:

    def __init__(self,  coords_arr: list, min_x=0, max_x=399,
                 min_y=0, max_y=599):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        edge_nodes = [
            [min_x, min_y, min_x-1, max_y],
            [max_x+1, min_y, max_x, max_y],
            [min_x, min_y, max_x, min_y-1],
            [min_x, max_y+1, max_x, max_y],
        ]
        self.graph = BarrenLandGraph(edge_nodes + coords_arr)
        self.total_barren = \
            sum([x.area for x in self.graph.nodes]) - \
            sum([x.intersection_area for x in self.graph.edges.values()])
        self.total_area = (max_x + 1 - min_x) * (max_y + 1 - min_y)
        self.total_usable = self.total_area - self.total_barren
        self.cycle_areas = self.find_cycle_area()
        self.fertile_plots = self.find_all_fertile_areas()

    def find_cycle_area(self):
        areas = {}
        for cycle in self.graph.cycles:
            if len(cycle) > 4:
                print("Can't compute, cycle is too big!")
                return None

            coord_list = []
            for i in cycle:
                coord_list.append(self.get_coord_dict(i))
            parallel_nodes = [(coord_list[0],coord_list[2]),
                             (coord_list[1], coord_list[3])]

            for n1, n2 in parallel_nodes:
                if n1["x0"] <= n1["x1"] < n2["x0"] <= n2["x1"]:
                    x_range = n2["x0"] - n1["x1"]
                elif n2["x0"] <= n2["x1"] < n1["x0"] <= n1["x1"]:
                    x_range = n1["x0"] - n2["x1"]
                elif n1["y0"] <= n1["y1"] < n2["y0"] <= n2["y1"]:
                    y_range = n2["y0"] - n1["y1"]
                elif n2["y0"] <= n2["y1"] < n1["y0"] <= n1["y1"]:
                    y_range = n1["y0"] - n2["y1"]
                else:
                    print("Something went wrong, rectangles aren't parrallel")
                    return None

            cycle_name = ",".join([str(x) for x in cycle])
            areas.update({cycle_name: (x_range * y_range)})
        return areas

    def get_coord_dict(self, index):
        return self.graph.nodes[index].coord_dict

    def find_all_fertile_areas(self):
        results = []
        for name, area in self.cycle_areas.items():
            if area != self.total_area:
                results.append(area)
        if sum(results) != self.total_usable:
            results.append(self.total_usable - sum(results))
        return sorted(results)

    def describe_graph(self):
        print("Nodes")
        for node in self.graph.nodes:
            print("\t Index:", node.index, "Area:", node.area)
            print("\t\t Coordinates:", node.coord_dict)
        print("Edges")
        for key,val in self.graph.edges.items():
            print("\t", key, "| Intersection Area:", val.intersection_area)
            print("\t\t", val.coord_dict)
        print("Adjacency List:")
        for key,val in self.graph.adjacency_list.items():
            print("\t", key, ":", val)
        print("Cycles:")
        for cycle in self.graph.cycles:
            print("\t "+", ".join([str(x) for x in cycle]))
        print("Total Area:")
        print("\t", self.total_area)
        print("Total Barren Area:")
        print("\t", self.total_barren)
        print("Total Usable Area:")
        print("\t", self.total_usable)
        print("Cycle Areas:")
        for name, area in self.cycle_areas.items():
            print("\t", name, ":", area)
        print("Fertile Plots:")
        print("\t", self.fertile_plots)


if __name__ == "__main__":

    Field([[0, 292, 399, 307]]).describe_graph()
    print('\n------------------------------------------\n')
    Field([[48, 192, 351, 207],
           [48, 392, 351, 407],
           [120, 52, 135, 547],
           [260, 52, 275, 547]]).describe_graph()
