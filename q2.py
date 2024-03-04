import math

from typing import List


def calculate_dot_product(v1: List[int], v2: List[int]) -> int:
    return sum([v1[i] * v2[i] for i in range(len(v1))])


def calculate_vector_magnitude(v: List[int]) -> float:
    return math.sqrt(sum([v[i]**2 for i in range(len(v))]))


def calculate_angle(v1: List[int], v2: List[int]) -> float:
    return math.degrees(
        math.acos(
            calculate_dot_product(v1, v2) /
            (calculate_vector_magnitude(v1) * calculate_vector_magnitude(v2))))


def calculate_cross_product(v1: List[int], v2: List[int]) -> List[int]:
    return [
        v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


if __name__ == "__main__":
    # v1 = [
    #     int(element)
    #     for element in input("Enter the first vector: ")[1:-1].split(", ")
    # ]
    # v2 = [
    #     int(element)
    #     for element in input("Enter the second vector: ")[1:-1].split(", ")
    # ]

    v1 = [2, 1, 5]
    v2 = [-6, 4, 8]

    print(
        f"The angle between the two vectors is {calculate_angle(v1, v2)} degrees."
    )

    print(
        f"The cross product of the two vectors is {calculate_cross_product(v1, v2)}."
    )
