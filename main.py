from time import time
from input_robot import InputRobot
from simple_bfs import BarrenLandSimple
from barren_land_graph.field import Field


if __name__ == '__main__':
    params = InputRobot()

    print("--- Using Simple Algo ---")
    start = time()
    bfs = BarrenLandSimple(params.coordinates,
                           params.x, params.y)
    result = bfs.find_all_fertile_areas()
    end = time()
    print("Fertile Land Plots:")
    for plot in result:
        print(plot, end=" ")
    print("\nProcess Time (ms): {0:.15f}".format((end - start)*1000))
    print()

    print("--- Using Graphing Algo ---")
    start = time()
    graph = Field(params.coordinates,
                  max_x=params.x-1, max_y=params.y-1)
    result = graph.find_all_fertile_areas()
    end = time()
    print("Fertile Land Plots:")
    for plot in result:
        print(plot, end=" ")
    print("\nProcess Time (ms): {0:.15f}".format((end - start)*1000))
