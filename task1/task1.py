import sys

def interval_path(n: int, m: int) -> str:
    """Определяем путь с интервалом."""
    array = list(range(1, n + 1))
    path = []
    index = 0

    for _ in range(n):
        if array[index] not in path:
            path.append(array[index])
        index = (index + m - 1) % n

    return ''.join(map(str, path))

print(interval_path(int(sys.argv[1]), int(sys.argv[2])))
