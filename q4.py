from typing import List


def calculate_dot_product(v1: List[int], v2: List[int]) -> int:
    return sum([v1[i] * v2[i] for i in range(len(v1))])


def calculate_cross_product(v1: List[int], v2: List[int]) -> List[int]:
    return [
        v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


if __name__ == "__main__":
    v1 = [2, 1, 5]
    v2 = [-6, 4, 8]
    v3 = [4, 9, 2]

    value_1 = calculate_cross_product(v1, calculate_cross_product(v2, v3))

    temp_1 = [calculate_dot_product(v1, v3) * v2[i] for i in range(len(v2))]
    temp_2 = [calculate_dot_product(v1, v2) * v3[i] for i in range(len(v3))]
    value_2 = [temp_1[i] - temp_2[i] for i in range(len(temp_1))]

    if value_1 == value_2:
        print("The given vectors are equal.")
    else:
        print("The given vectors are not equal.")
