from typing import List


def calculate_cross_product(v1: List[List[int]], v2: List[int]) -> List[int]:
    cross_product = []

    for column in v1:
        cross_product.append(sum([column[i] * v2[i] for i in range(3)]))

    return cross_product


if __name__ == "__main__":
    # v1 = [
    #     int(element)
    #     for element in input("Enter the first vector: ")[1:-1].split("; ")
    # ]
    # v2 = [
    #     int(element)
    #     for element in input("Enter the second vector: ")[1:-1].split("; ")
    # ]

    v1 = [[0, -5, 1], [5, 0, -2], [-1, 2, 0]]
    v2 = [-6, 4, 8]

    cross_product = str(calculate_cross_product(v1, v2)).replace(",", ";")

    print(f"The cross product of the two vectors is {cross_product}.")
