class Cube:
    def __init__(self, edge):
        self.edge = edge

    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        if value <= 0:
            raise ValueError("Edge must be greater than 0")
        self.__edge = value

    def calculate_surface_area(self):
        return 6 * (self.__edge ** 2)


class ErrorRate:
    def __init__(self, absolute_error, measured_value):
        self.absolute_error = absolute_error
        self.measured_value = measured_value

    @property
    def absolute_error(self):
        return self.__absolute_error

    @absolute_error.setter
    def absolute_error(self, value):
        if value <= 0:
            raise ValueError("Absolute error must be greater than 0")
        self.__absolute_error = value

    @property
    def measured_value(self):
        return self.__measured_value

    @measured_value.setter
    def measured_value(self, value):
        if value <= 0:
            raise ValueError("Measured value must be greater than 0")
        self.__measured_value = value

    def calculate_error_percentage(self):
        return (self.__absolute_error / self.__measured_value) * 100


if __name__ == "__main__":
    try:
        edge = float(input("Enter cube edge: "))
        cube = Cube(edge)
        print("Surface area of cube:", cube.calculate_surface_area())

        absolute_error = float(input("Enter absolute error: "))
        measured_value = float(input("Enter measured value: "))

        error = ErrorRate(absolute_error, measured_value)
        print("Error percentage:", error.calculate_error_percentage(), "%")

    except ValueError as e:
        print("Error:", e)

    except Exception:
        print("Invalid input")