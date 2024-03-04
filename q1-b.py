def calculate_dollars(age: int) -> int:
    dollars = -1

    if age < 3:
        dollars = 0
    elif age < 12:
        dollars = 10
    elif age < 18:
        dollars = 12
    elif age < 65:
        dollars = 15
    else:
        dollars = 8

    return dollars


if __name__ == "__main__":
    ages = [int(age) for age in input("Enter ages: ")[1:-1].split(", ")]
    dollars_list = []

    for age in ages:
        dollars_list.append(calculate_dollars(age=age))

    print(dollars_list)
