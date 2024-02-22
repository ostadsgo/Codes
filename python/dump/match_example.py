class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def gurd_exa(point):
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print("Not on the diagonal")

print("Gurd example")
gurd_exa(Point(x=0, y=0))
def get_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"




def using_match(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


def using_if(point):
    point_org = Point(x=0, y=0)
    if point.x == point_org.x and point.y == point_org.y:
        print("Origin")
