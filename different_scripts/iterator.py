numbers = [1, 2, 3, 4, 5]

# Створюємо ітератор зі списку
iterator = iter(numbers)

# Використовуємо цикл for для ітерації по елементах списку
for num in numbers:
    print(num)
    if num == 3:
        break
