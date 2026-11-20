square = lambda s: s * s
rectangle = lambda l, b: l * b
triangle = lambda b, h: b * h / 2

s = float(input("Square side: "))

l, b = map(float, input("Rectangle length and breadth: ").split())

base, h = map(float, input("Triangle base and height: ").split())

print("Square area =", square(s))
print("Rectangle area =", rectangle(l, b))
print("Triangle area =", triangle(base, h))