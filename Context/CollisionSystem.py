"""
CollisionSystem.py
 *  Creates n random particles and simulates their motion according
 *  to the laws of elastic collisions.

"""
from Queues.MinPQ import MinPQ
from Context.Particle import Particle


class Event:
    _time = 0.0
    _count_a = None
    _count_b = None

    def __init__(self, t, a, b):
        self._time = t
        self._a = a
        self._b = b
        if a is not None:
            self._count_a = a.count()
        else:
            self._count_a = -1
        if b is not None:
            self._count_b = b.count()
        else:
            self._count_b = -1

    def compare_to(self, other):
        if self._time > other._time:
            return 1
        elif self._time < other._time:
            return -1
        else:
            return 0

    def is_valid(self):
        if self._a is not None and self._a.count() != self._count_a:
            return False
        if self._b is not None and self._b.count() != self._count_b:
            return False
        return True


class CollisionSystem:

    HZ = 0.5
    _pq: MinPQ
    _t = 0.0

    def __init__(self, particles: list):
        self._particles = particles.copy()

    def _predict(self, a: Particle, limit):
        if a is None:
            return
        # particle-particle collisions
        for i in range(len(self._particles)):
            dt = a.time_to_hit(self._particles[i])
            if self._t + dt <= limit:
                self._pq.insert(Event(self._t + dt, a, self._particles[i]))

        # particle-wall collisions
        dt_x = a.time_to_hit_vertical_wall()
        dt_y = a.time_to_hit_horizontal_wall()
        if self._t + dt_x <= limit:
            self._pq.insert(Event(self._t + dt_x, a, None))
        if self._t + dt_y <= limit:
            self._pq.insert(Event(self._t + dt_y, None, a))

    def _redraw(self, limit):
        pass

    def simulate(self, limit):
        self._pq = MinPQ()
        for i in range(len(self._particles)):
            self._predict(self._particles[i], limit)
        self._pq.insert(Event(0, None, None))

        while not self._pq.is_empty():
            e = self._pq.del_min()
            if not e.is_valid():
                continue
            a = e._a
            b = e._b
            for i in range(len(self._particles)):
                self._particles[i].move(e._time - self._t)
            self._t = e._time

            if a is not None and b is not None:
                a.bounce_off(b)
            elif a is not None and b is None:
                a.bounce_off_vertical_wall()
            elif a is None and b is not None:
                b.bounce_off_horizontal_wall()
            elif a is None and b is None:
                # self.redraw(limit)
                print(limit)
            self._predict(a, limit)
            self._predict(b, limit)

