from calculator import Calculator


def main():
    expression = input("Enter your calculation: ")
    calculator = Calculator()

    print(f"Result: {calculator.solve(expression)}")


if __name__ == "__main__":
    main()
