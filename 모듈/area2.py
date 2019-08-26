#148 area2.py
def tri_area(width, height):
    return width * height * 1/2

def box_area(width, height):
    return width * height

def print_area(width, height):
    print("가로", width, "세로", height, "인 삼각형의 넓이: ", tri_area(width, height))
    print("가로", width, "세로", height, "인 사각형의 넓이: ", box_area(width, height))

if __name__ == '__main__':
    print_area(3, 5)
    print_area(6, 10)
