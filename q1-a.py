def calculate_dollars(age: int):
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

    print(f"You need to pay {dollars} dollars.")


if __name__ == "__main__":
    age = int(input("Enter your age: "))

    calculate_dollars(age=age)
