from typing import List


def calculate_cross_product(v1: List[int], v2: List[int]) -> List[int]:
    return [
        v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


if __name__ == "__main__":
    # v1 = [
    #     int(element)
    #     for element in input("Enter the first vector: ")[1:-1].split("; ")
    # ]
    # v2 = [
    #     int(element)
    #     for element in input("Enter the second vector: ")[1:-1].split("; ")
    # ]

    v1 = [2, 1, 5]
    v2 = [-6, 4, 8]

    cross_product = str(calculate_cross_product(v1, v2)).replace(",", ";")

    print(f"The cross product of the two vectors is {cross_product}.")
