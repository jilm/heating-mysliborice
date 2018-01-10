# -*- coding: utf-8 -*-

import sys

class Transform:

    def __init__(self):
        self.a11 = 1.0
        self.a12 = 0.0
        self.a21 = 0.0
        self.a22 = 1.0
        self.x0 = 0.0
        self.y0 = 0.0

    def transform_points(self, points):
        return list(((self.a11 * x + self.a12 * y + self.x0
            , self.a21 * x + self.a22 * y + self.y0) for x, y in points))

    def transform_point(self, point):
        x, y = point
        return self.a11 * x + self.a12 * y + self.x0, self.a21 * x + self.a22 * y + self.y0

    def transform_vectors(self, vectors):
        return list(((self.a11 * x + self.a12 * y
            , self.a21 * x + self.a22 * y) for x, y in vectors))

    def transform_vector(self, vector):
        x, y = vector
        return self.a11 * x + self.a12 * y, self.a21 * x + self.a22 * y

    def scale(self, x_scale, y_scale = None):
        if y_scale is None: y_scale = x_scale
        result = Transform()
        result.a11 = x_scale * self.a11
        result.a12 = x_scale * self.a12
        result.x0 = x_scale * self.x0
        result.a21 = y_scale * self.a21
        result.a22 = y_scale * self.a22
        result.y0 = y_scale * self.y0
        return result

    def r_scale(self, x_scale, y_scale = None):
        if y_scale is None: y_scale = x_scale
        result = Transform()
        result.a11 = x_scale * self.a11
        result.a12 = y_scale * self.a12
        result.x0 = self.x0
        result.a21 = x_scale * self.a21
        result.a22 = y_scale * self.a22
        result.y0 = self.y0
        return result

    def move(self, vector):
        x, y = vector
        result = Transform()
        result.a11 = self.a11
        result.a12 = self.a12
        result.x0 = self.x0 + x
        result.a21 = self.a21
        result.a22 = self.a22
        result.y0 = self.y0 + y
        return result

    def r_move(self, x, y):
        result = Transform()
        result.a11 = self.a11
        result.a12 = self.a12
        result.x0 = self.a11 * x + self.a12 * y + self.x0
        result.a21 = self.a21
        result.a22 = self.a22
        result.y0 = self.a21 * x + self.a22 * y + self.y0
        return result

    def rotate_vect(self):
        result = Transform()
        result.a11 = self.a21
        result.a12 = self.a22
        result.x0 = self.x0
        result.a21 = -self.a11
        result.a22 = -self.a12
        result.y0 = self.y0
        return result

    def move_to(self, point):
        x, y = point
        result = Transform()
        result.a11 = self.a11
        result.a12 = self.a12
        result.x0 = x
        result.a21 = self.a21
        result.a22 = self.a22
        result.y0 = y
        return result

    def transform(self, tr):
        result = Transform()
        result.a11 = tr.a11 * self.a11 + tr.a12 * self.a21
        result.a12 = tr.a11 * self.a12 + tr.a12 * self.a22
        result.x0 = tr.a11 * self.x0 + tr.a12 * self.y0 + tr.x0
        result.a21 = tr.a21 * self.a11 + tr.a22 * self.a21
        result.a22 = tr.a21 * self.a12 + tr.a22 * self.a22
        result.y0 = tr.a21 * self.x0 + tr.a22 * self.y0 + tr.y0
        return result

    def get_offset(self):
        return self.x0, self.y0

    def __str__(self):
        return '\n'.join((
            '[{}  {}  {}]'.format(self.a11, self.a12, self.x0),
            '[{}  {}  {}]'.format(self.a21, self.a22, self.y0),
            '[{}  {}  {}]\n'.format(0.0, 0.0, 1.0)
        ))



I = Transform()

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
        return self.corners

    def get_path(self):

        """ Return a rectagle in the form of path to draw. """

        x1, y1 = self.corners[0]
        x2, y2 = self.corners[1]
        return [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]

