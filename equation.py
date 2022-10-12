print("ax + bx + c = 0")
print("Дано:")
a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))
if a == 0:
    print("Дано не квадратное уравнение.")

discriminant = b*b - 4*a*c

if discriminant < 0:
    print("Решений нет.")

if discriminant == 0:
    print("x1 = x2 = ", (-b) / (2*a))

if discriminant > 0:
    print("x1 = ", (-b + discriminant) / (2*a),
          "x2 = ", (-b - discriminant) / (2*a))



