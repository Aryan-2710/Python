def ball_collide(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2

    distance_square = (x1 - x2) ** 2 + (y1 - y2) ** 2
    distance = distance_square ** 0.5

    return distance <= r1 + r2


x1, y1, r1 = map(int, input("Enter x1, y1, r1 : ").split())
x2, y2, r2 = map(int, input("Enter x2, y2, r2 : ").split())

ball1 = (x1, y1, r1)
ball2 = (x2, y2, r2)

if ball_collide(ball1, ball2):
    print("They are colliding.")
else:
    print("They are not colliding.")
