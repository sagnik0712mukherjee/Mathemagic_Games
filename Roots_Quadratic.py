def quad(a,b,c):
    x1 = (-b + (b**2 - 4*a*c) ** 0.5) / 2*a
    x2 = (-b - (b**2 - 4*a*c) ** 0.5) / 2*a
    s = f'the roots of the equation are ({int(x1)}, {int(x2)}).'
    return print(s)

quad(1, -7, 12)