class Ball:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.color == other.color and self.size == other.size

class Box:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.color == other.color and self.size == other.size

if __name__ == '__main__':
    ball_1 = Ball('blue', 'small')
    ball_2 = Ball('blue', 'small')
    ball_3 = Ball('green', 'small')

    print(ball_1 == ball_2)
    print(ball_1 == ball_3)

    box_1 = Box('blue', 'small')
    print(ball_1 == box_1)