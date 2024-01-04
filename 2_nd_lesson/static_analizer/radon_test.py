def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def greet(name):
    print("Hello, " + name + "!")


def main():
    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print("Average:", average)

    number = 10
    if is_prime(number):
        print(number, "is prime")
    else:
        print(number, "is not prime")

    greet("Alice")
    greet("Bob")

    
if __name_ == '__main__':
    main()
