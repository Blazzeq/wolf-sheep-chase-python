import logging


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: float):
        if isinstance(x, float):
            self._x = x
        else:
            logging.error('x must be float type!')
            raise TypeError('x must be float type!')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: float):
        if isinstance(y, float):
            self._y = y
        else:
            logging.error('y must be float type!')
            raise TypeError('y must be float type!')

    def set(self, point):
        logging.debug('set() method called, point:' + str(point))
        self._x = point.x
        self._y = point.y

    def __add__(self, other):
        self._x += other.x
        self._y += other.y
        return self

    def __str__(self):
        return "(" + "%.3f" % self._x + ", " + "%.3f" % self._y + ")"
