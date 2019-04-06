class InputRobot:

    opening_message = \
        "Welcome, fellow farmer!\n" \
        "I'm a robot that will tell you the size of fertile land " \
        "plots available\n" \
        "To start, enter the size of the plot by type the coordinates " \
        "like \"x, y\" then hitting enter"

    barren_land_message = \
        "Great. Now, let's plot the barren land. Do so by entering the " \
        "coordinates of the rectangle\n" \
        "Type the in the form \"x0 y0 x1 y1\" and then hit enter\n" \
        "When you're done, type \"END\""

    visualization_message = \
        "Great. And just for you, we have some extra options\n" \
        "When I finish my calculations, would you like me to draw " \
        "the plots for you? (y/n)"

    def __init__(self):
        self.x, self.y = self._get_plot_size()
        self.coordinates = self._get_barren_coordinates()
        self.visualizations = self._get_visualization_method()
        self._recap()

    def _get_plot_size(self) -> (int, int):
        """
        Asks user to enter the plot dimensions in
        x, y format. Checks that they are integers,
        then returns as an int tuple

        :return: (x, y)
        """
        print(self.opening_message)
        while True:
            try:
                x,y = input().strip().split(", ")
                x, y = int(x), int(y)
                break
            except ValueError:
                print("Whoops, I couldn't read that. Try again, "
                      "in form \"x, y\"")
        return x, y

    def _get_barren_coordinates(self) -> list:
        """
        Asks user to enter multiple barren land plots
        by their corner coordinates (x0 y0 x1 y1). User
        can enter multiple rectangles by hitting enter and
        typing another rectangle's coordinates. When the user
        is finished, they type "END". The plots are returns
        as a list of integers after they are validated to be
        within the range of the max dimensions and valid integers

        :return: list of integers corresponding to barren land coordinates
        """
        print(self.barren_land_message)
        coordinates = []
        while True:
            response = input()
            if response == "END":
                break
            try:
                response = response.strip()
                coords = [int(x) for x in response.split(" ")]

                if len(coords) != 4:
                    print("Only 4 numbers please!")
                    raise ValueError

                if not 0 <= coords[0] < self.x or \
                        not 0 <= coords[2] < self.x:
                    print("Make sure the x values are in bounds!")
                    raise ValueError

                if not 0 <= coords[1] < self.y or \
                        not 0 <= coords[3] < self.y:
                    print("Make sure the y values are in bounds!")
                    raise ValueError

                coordinates.append(coords)
            except ValueError:
                print("It doesn't quite line up - try again and follow "
                      "the format! \"x0 y0 x1 y1\"")
        print("COORDS", coordinates)
        return coordinates

    def _get_visualization_method(self) -> bool:
        """
        Asks user if they would like to visualize
        the plots after the calculations. They can reply
        y or n, which will return a True or False bool
        respectively.

        :return: True (y) or False (n)
        """
        print(self.visualization_message)
        return self._get_answer_y_n()

    def _get_answer_y_n(self) -> bool:
        """
        Generic method that looks for a y or n response
        from the user and if that's not recieved, prompts them
        for a retry. Returns a bool True (y) or False (n)

        :return: True (y) or False (n)
        """
        while True:
            response = input().lower()
            if response == 'y':
                result = True
                break
            if response == 'n':
                result = False
                break
            else:
                print("Not sure what that means - try again. "
                      "Type \"y\" for yes or \"n\" for no")
        return result

    def _recap(self):
        """
        After all info has been gathered from the user,
        this function reads everything back to them

        :return: None
        """
        print("Great. So to recap:")
        print("The plot size is: (" + str(self.x) + ", " + str(self.y)+")")
        print("The barren land plots are:")
        for coords in self.coordinates:
            print("\t"+" ".join([str(x) for x in coords]))
        if self.visualizations:
            print("You will be visualizing the data")
        else:
            print("You will not be visualizing the data")
        print(".\n.\n.")
        print("And awaaayyyy we go!\n")


if __name__ == "__main__":
    InputRobot()
