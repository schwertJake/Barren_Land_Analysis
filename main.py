from input_robot import InputRobot
from simple_bfs import BarrenLandSimple

if __name__ == '__main__':
    params = InputRobot()

    if params.simple_algo:
        bfs = BarrenLandSimple(params.coordinates,
                               params.x, params.y)
        print("Fertile Land Plots:")
        for plot in bfs.find_all_fertile_areas():
            print(plot, end=" ")
