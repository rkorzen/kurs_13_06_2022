


class Circle:
    pass

c = Circle()

c.name = "Okrąg"
c.x = 10

c.radius = lambda c: c.x

print(c.radius(c))