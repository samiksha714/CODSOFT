#CALCULATOR BY PYTHON

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            self.history.append(f"{num1} / {num2} = {result}")
            return result
        else:
            return "Error: Division by zero"

    def show_history(self):
        print("\nCalculator History:")
        for entry in self.history:
            print(entry)

    def run(self):
        while True:
            print("\nCalculator Menu:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Show History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice in ["1", "2", "3", "4"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"Result: {self.add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {self.subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {self.multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {self.divide(num1, num2)}")
            elif choice == "5":
                self.show_history()
            elif choice == "6":
                print("Exiting Calculator.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()