# -*- coding: utf-8 -*-


class Transform:

    def __init__(self):
        self.scale = 1.0
        self.x_offset = 0.0
        self.y_offset = 0.0

    def transform_points(self, points):
        return list(((x * self.scale + self.x_offset, y *
                      self.scale + self.y_offset) for x, y in points))

    def transform_vectors(self, vectors):
        return list(((x * self.scale, y * self.scale) for x, y in vectors))

    def scale(self, scale):
        self.scale *= scale

    def move(self, vector):
        self.x_offset += vector[0] * self.scale
        self.y_offset += vector[1] * self.scale

    def move_to(self, point):
        self.x_offset, self.y_offset = point


class Rect:
    """ A rectangle which is parallel to coordinate axes. """

    def __init__(self, points):
        """ Creates the smallest possible rectangle that contains given points.

        It expects at least one point."""
        self.corners = (
            (
                min((x for x, y in points)),
                min((y for x, y in points))
            ), (
                max((x for x, y in points)),
                max((y for x, y in points))
            )
        )

    def union(self, points):
        self.corners = (
            (
                min((x for p in (points, self.corners) for x, y in p)),
                min((y for p in (points, self.corners) for x, y in p))
            ), (
                max((x for p in (points, self.corners) for x, y in p)),
                max((y for p in (points, self.corners) for x, y in p))
            )
        )

    def get_size(self):
        return self.corners[1][0] - \
            self.corners[0][0], self.corners[1][1] - self.corners[0][1]

    def get_points(self):
        pass

    def get_path(self):
        """ Return a rectagle in the form of path to draw. """
        x1, y1 = self.corners[0]
        x2, y2 = self.corners[1]
        return [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]

