print("Welcome!")


def operations(oper, num1, num2):
    match oper:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Unsupported operation"


def get_user_value():
    try:
        num1 = int(input("Enter your first value: "))
        num2 = int(input("Enter your second value: "))
        oper = input("Enter operation (+, -, *, /): ")

        res = operations(oper, num1, num2)
        return res
    except ValueError:
        return "Invalid input: Please enter valid integers."


def main():
    print("""Perform your operations in the following way:
    1. Enter your first number
    2. Enter your second number
    3. Enter the operation (+, -, *, /)""")

    result = get_user_value()
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
