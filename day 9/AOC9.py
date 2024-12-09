from collections import deque

FILENAME = "snake.txt"


def create_disk(disk_map):
    disk = []
    current_block_id = 0
    for i, block in enumerate(disk_map):
        if i % 2 == 1:
            disk += block * [-1]
        else:
            disk += block * [current_block_id]
            current_block_id += 1
    return disk


def part_one(disk):
    updated_disk = disk.copy()
    free_space = deque([i for i, num in enumerate(disk) if num == -1])
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != -1 and free_space and free_space[0] < i:
            index_to_move = free_space.popleft()  # Get the earliest free space
            updated_disk[index_to_move], updated_disk[i] = updated_disk[i], -1
    return updated_disk


def solve(updated_disk):
    return sum(i * num for i, num in enumerate(updated_disk) if num > -1)


def find_fragments(disk):
    occupied, empty = [], []
    start = 0
    for i in range(1, len(disk)):
        if disk[i] != disk[start]:
            if disk[start] == -1:
                empty.append([start, i - 1])
            else:
                occupied.append([start, i - 1])
            start = i
    if disk[start] != -1:
        occupied.append([start, len(disk) - 1])
    return occupied, empty


def defragment(disk):
    defragmented = disk.copy()
    occupied, empty = find_fragments(disk)
    for start, end in occupied[::-1]:
        block_size = end - start + 1
        for empty_block in empty:
            empty_start, empty_end = empty_block
            if empty_start > start:
                break
            if empty_end - empty_start + 1 >= block_size:
                defragmented[empty_start : empty_start + block_size] = disk[
                    start : start + block_size
                ]
                defragmented[start : start + block_size] = [-1] * block_size
                empty_block[0] += block_size
                if empty_block[0] > empty_block[1]:
                    empty.remove(empty_block)
                break
    return defragmented


def main():
    with open(FILENAME, "r") as input_file:
        disk_map = [int(num) for num in input_file.read()]
    disk = create_disk(disk_map)
    updated_disk = part_one(disk)
    print(solve(updated_disk))
    defragmented = defragment(disk)
    print(solve(defragmented))


if __name__ == "__main__":
    main()
