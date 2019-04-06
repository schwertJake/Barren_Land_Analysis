class BarrenLand:

    _coord_map = {
        "x0": 0,
        "y0": 1,
        "x1": 2,
        "y1": 3
    }

    _plotly_viz_attr = {
        'type': 'rect',
        'line': {
            'color': 'rgba(255, 69, 0, 1)',
            'width': 2,
        },
        'fillcolor': 'rgba(255, 69, 0, 0.7)'
    }

    def __init__(self, coord_arr: list, index):
        self.coord_dict = self._assign_coordinates(coord_arr)
        self.index = index  # index in list of barren land object
        self.area = (self.coord_dict['x1'] - self.coord_dict['x0'])  * \
                    (self.coord_dict['y1'] - self.coord_dict['y0'])

    def _assign_coordinates(self, coord_arr: list) -> dict:
        """
        Takes the raw input string of form "X0 Y0 X1 Y1"
        for the rectangle, and assigns to self.coord_dict via
        self.coord_map

        :param coord_str: string of coordinates
        :return: none
        """
        ret_dict = {}
        for key, val in self._coord_map.items():
            ret_dict[key] = coord_arr[val]
        ret_dict['x1'] += 1
        ret_dict['y1'] += 1
        return ret_dict

    def display(self):
        """
        Returns a dictionary with coordinates and visualization
        properties to be displayed via Plotly

        :return:
        """
        return self.coord_dict.update(self._plotly_viz_attr)
