import pytest


class Circle:

    def __init__(self, r=1):
        # if r <= 0: raise ValueError()
        self.radius = r   # wywolanie self.radius = value

    @property
    def radius(self):        # c.radius
        return self.x

    @radius.setter
    def radius(self, value):    # c.radius = 10
        if value <= 0:
            raise ValueError("Radius can not be negative")
        self.x = value


    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


def test_circle_creation():
    c = Circle()
    assert c.radius == 1
    # assert c._radius == 1
    c = Circle(r=2)
    assert c.radius == 2


def test_diameter():
    c = Circle()
    assert c.diameter == 2
    c.diameter = 4
    assert c.radius == 2


def test_change_radius_by_changing_diameter():
    c = Circle()
    assert c.diameter == 2
    c.diameter = 4
    assert c.radius == 2


def test_diameter_cant_be_negative():
    c = Circle()
    with pytest.raises(ValueError):
        c.diameter = -2


def test_radius_cant_be_negative():
    with pytest.raises(ValueError):
        c = Circle(r=-10)

    circle = Circle(r=10)
    assert circle.radius == 10
    print(circle.radius)
    with pytest.raises(ValueError):
        circle.radius = -1
