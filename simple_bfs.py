

class BarrenLandSimple:

    def __init__(self, coord_arr: list, x_max=400, y_max=400):
        self.x_max = x_max
        self.y_max = y_max
        self.plot = self._create_plot(x_max, y_max)
        self._coord_list = self._build_coord_list(coord_arr)
        self._populate_barren_land()

    def find_all_fertile_areas(self) -> list:
        """
        This is the callable method of the class to start the
        algorithm. It starts at (0,0) on the array and starts
        incrementing x until it finds a 0 entry (fertile land).
        When it does, it calls a bfs starting at this point.
        It collects the results of each bfs, and sorts them in
        a list to return as the available plot sizes

        :return: list of plot sizes from smallest to largest
        """
        x, y = 0, 0
        result_list = []

        while x < self.x_max and y < self.y_max:
            # if the land is fertile, start a BFS
            if self._get_plot_point(x, y) == 0:
                result_list.append(self._bfs(x, y))

            # Traverse through every entry to find new fertile land
            if x == self.x_max - 1:
                x = 0
                y += 1
            else:
                x += 1

        return sorted(result_list)

    def _bfs(self, x: int, y: int) -> int:
        """
        This is the bulk of the work - a BFS that looks
        at every single entry in the array. If it hasn't been
        seen (value is 0), it marks the entry with a 1 and adds
        all surrounding entries to the queue. Each time it does
        this, it increments the plot_size count.
        Entries with a 1 (already seen) or -1 (barren land) are
        ignored

        :param x: starting x coordinate for the bfs
        :param y: starting y coordinate for the bfs
        :return: size of the plot integer
        """
        queue = []            # queue to hold neighbor nodes
        queue.append((x, y))  # starting node, stored as a tuple (x,y)
        plot_size = 0         # increments to count plot size

        while not queue == []:
            node = queue.pop(0)
            x, y = node

            if self._get_plot_point(x, y) == 0:
                plot_size += 1
                self._put_plot_point(x, y, 1)

                # Add neighbors to the queue if they're in boundaries
                if x > 0:
                    queue.append((x-1, y))
                if x < self.x_max - 1:
                    queue.append((x+1, y))
                if y > 0:
                    queue.append((x, y-1))
                if y < self.y_max - 1:
                    queue.append((x, y+1))

        return plot_size

    def _get_plot_point(self, x: int, y: int) -> int:
        """
        Returns the entry / value at point x,y from the
        2d array of land plots

        :param x: x coordinate of value
        :param y: y coordinate of value
        :return: value at (x,y) in array
        """
        return self.plot[y][x]

    def _put_plot_point(self, x: int, y: int, val: int):
        """
        Sets the entry in the 2d array to val

        :param x: x coordinate of value to set
        :param y: y coordinate of value to set
        :param val: value to set the entry to
        :return: None
        """
        self.plot[y][x] = val

    @staticmethod
    def _create_plot(x_max: int, y_max: int) -> list:
        """
        Static method to create 2d array of size x_max * y_max

        :param x_max: max x value
        :param y_max: max y_value
        :return: list of 2d array size x_max * y_max of all 0's
        """
        return [[0 for x in range(x_max)] for y in range(y_max)]

    def _populate_barren_land(self):
        """
        Marks the land barren (entry of -1) for
        all rectangles input by the user

        :return: None
        """
        for coords in self._coord_list:
            for y in range(coords["y0"], coords["y1"]+1):
                for x in range(coords["x0"], coords["x1"]+1):
                    self._put_plot_point(x, y, -1)  # Mark as barren

    @staticmethod
    def _build_coord_list(raw_coord_list: list) -> list:
        """
        Given a list of strings of form
        "x0 y0 x1 y1", ...
        transforms into a dictionary of form
        {
          "x0": x0,
          "y0": y0,
          ...
        }
        where the values are integers
        and returns a list of dictionaries

        :param raw_coord_list:
        :return:
        """
        coord_list = []
        for coords in raw_coord_list:
            coords = coords.split(" ")
            coord_list.append(
                {
                    "x0": int(coords[0]),
                    "y0": int(coords[1]),
                    "x1": int(coords[2]),
                    "y1": int(coords[3])
                }
            )
        return coord_list


if __name__ == "__main__":
    raw_coords = ["48 192 351 207",
                  "48 392 351 407",
                  "120 52 135 547",
                  "260 52 275 547"]
    land = BarrenLandSimple(raw_coords, 400, 600)
    print("STARTING BFS")
    print("RESULTS:", land.find_all_fertile_areas())
