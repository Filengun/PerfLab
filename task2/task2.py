import sys
import math

def read_circle(file_path: str) -> tuple:
    """Функция для определения окружности."""
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        r = float(file.readline())
    return (x, y, r)

def read_points(file_path: str) -> list:
    """Функция для определения точек."""
    with open(file_path, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]
    return points

def point_position(circle: tuple, point: list, i: int) -> str:
    """Определяем местнахождение относительно окружности."""
    x, y, r = circle
    px, py = point
    distance = math.sqrt((px - x)**2 + (py - y)**2)
    if math.isclose(distance, r):
        return(f"{i} - точка лежит на окружности")
    elif distance < r:
        return(f"{i} - точка внутри")
    else:
        return(f"{i} - точка снаружи")

def main():
    circle_file_path = sys.argv[1]
    points_file_path = sys.argv[2]
    circle = read_circle(circle_file_path)
    points = read_points(points_file_path)
    for i, point in enumerate(points):
        print(point_position(circle, point, i))

if __name__ == "__main__":
    main()
