class Fibonacci:

    def __init__(self, num):
        self.num = num

    def recursive(self, n):

        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:
            return self.recursive(n - 1) + self.recursive(n - 2)

    def dynamic(self):

        first = 0
        second = 1

        if self.num == 0:
            return first

        elif self.num == 1:
            return second

        for i in range(2, self.num + 1):
            next = first + second
            first = second
            second = next

        return second

    def display(self):

        first = 0
        second = 1

        print("\nFibonacci Series:")

        for i in range(self.num):

            if i == 0:
                print(first, end=" ")

            elif i == 1:
                print(second, end=" ")

            else:
                next = first + second
                print(next, end=" ")
                first = second
                second = next

        print()


class MainProgram:

    def main(self):

        num = int(input("Enter Number : "))

        obj = Fibonacci(num)

        while True:

            print("\n===== MENU =====")
            print("1. Recursive Method")
            print("2. Dynamic Method")
            print("3. Display Series")
            print("4. Exit")

            choice = int(input("Enter Choice : "))

            if choice == 1:

                print("Answer :", obj.recursive(num))

            elif choice == 2:

                print("Answer :", obj.dynamic())

            elif choice == 3:

                obj.display()

            elif choice == 4:

                print("Thank You")
                break

            else:

                print("Invalid Choice")


m = MainProgram()
m.main()