from typing import Tuple, List, Set, Mapping
import numpy as np

Cart_dir = Mapping[str, Tuple[int, int]]

dir_symbols = set('> v < ^'.split())
dir_coords = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# cart symbol direction, maps symbol wth coord change in the next tick
# if no intersection is present
cart_dir = {k: v for k, v in zip(dir_symbols, dir_coords)}

# cart behaviour when finds a rail split (left, straight, rigth)
# ['\', '|', '/']
turn = [(-1, 0), (0, 1), (1, 0)]


with open('day13_data.txt') as f:
    RAW = f.readlines()


def find_carts(raw: str) -> List[Tuple[int, int]]:
    """Finds carts positions"""
    cart_positions = []
    for i, line in enumerate(RAW):
        print(len(line))
        for j, c in enumerate(line):
            if c in dir_symbols:
                cart_positions.append((i, j))
    return cart_positions


max_width = max(len(line) for line in RAW) + 1
max_heigth = len(RAW) + 1
tracks = np.empty((max_width, max_heigth), dtype=object)
print(max_width, max_heigth)
for i, line in enumerate(RAW):
        for j, c in enumerate(line):
            tracks[i, j] = c

print(tracks)