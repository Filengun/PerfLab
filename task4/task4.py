import sys

def min_moves(nums: list) -> int:
    """Высчитываем наименьшее количество ходов."""
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def read_file(file_path: str) -> list:
    """Открываем файл."""
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]
    return nums

def main():
    file_path = sys.argv[1]
    nums = read_file(file_path)
    print(min_moves(nums))

if __name__ == "__main__":
    main()