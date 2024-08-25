import random
import sys


def create_sorted_random_nums(count: int) -> None:
    numbers = [random.randint(0, count) for _ in range(count)]

    # バブルソート
    for _ in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(numbers)


args = sys.argv
try:
    count = int(args[1])
except IndexError:
    count = 100
create_sorted_random_nums(count)
