"""
Particle.py
 *  A particle moving in the unit box with a given position, velocity,
 *  radius, and mass.
 *  The Particle class represents a particle moving in the unit box,
 *  with a given position, velocity, radius, and mass. Methods are provided
 *  for moving the particle and for predicting and resolvling elastic
 *  collisions with vertical walls, horizontal walls, and other particles.
 *  This data type is mutable because the position and velocity change.
"""
import math


class Particle:
    INFINITY = float('inf')
    _count = 0  # number of collisions so far

    def __init__(self, rx, ry, vx, vy, radius, mass, color=None):
        self._rx = rx  # position
        self._ry = ry
        self._vx = vx  # velocity
        self._vy = vy
        self._radius = radius
        self._mass = mass
        self._color = color

    def move(self, dt):
        self._rx += self._vx * dt
        self._ry += self._vy * dt

    def draw(self):
        pass

    def count(self):
        return self._count

    def time_to_hit(self, other):
        if self == other:
            return self.INFINITY
        dx = other._rx - self._rx
        dy = other._ry - self._ry
        dvx = other._vx - self._vx
        dvy = other._vy - self._vy
        dvdr = dx * dvx + dy * dvy
        if dvdr > 0:
            return self.INFINITY
        dvdv = dvx * dvx + dvy * dvy
        if dvdv == 0:
            return self.INFINITY
        drdr = dx * dx + dy * dy
        sigma = self._radius + other._radius
        d = (dvdr * dvdr) - dvdv * (drdr - sigma * sigma)
        if d < 0:
            return self.INFINITY
        return -(dvdr + math.sqrt(d)) / dvdv

    def time_to_hit_vertical_wall(self):
        if self._vx > 0:
            return (1.0 - self._rx - self._radius) / self._vx
        elif self._vx < 0:
            return (self._radius - self._rx) / self._vx
        else:
            return self.INFINITY

    def time_to_hit_horizontal_wall(self):
        if self._vy > 0:
            return (1.0 - self._ry - self._radius) / self._vy
        elif self._vy < 0:
            return (self._radius - self._ry) / self._vy
        else:
            return self.INFINITY

    def bounce_off(self, other):
        dx = other._rx - self._rx
        dy = other._ry - self._ry
        dvx = other._vx - self._vx
        dvy = other._vy - self._vy
        dvdr = dx * dvx + dy * dvy
        dist = self._radius + other._radius
        magnitude = 2 * self._mass * other._mass * dvdr / (self._mass + other._mass) \
                    * dist
        # normal force in x and y directions
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        # update velocities according to normal force
        self._vx += fx / self._mass
        self._vy += fy / self._mass
        other._vx -= fx / other._mass
        other._vy -= fy / other._mass

        # update collision counts
        self._count += 1
        other._count += 1

    def bounce_off_vertical_wall(self):
        self._vx = -self._vx
        self._count += 1

    def bounce_off_horizontal_wall(self):
        self._vy = -self._vy
        self._count += 1

    def kinetic_energy(self):
        return 0.5 * self._mass * (self._vx * self._vx + self._vy * self._vy)

