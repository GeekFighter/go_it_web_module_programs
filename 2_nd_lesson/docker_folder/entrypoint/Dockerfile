# Вказуємо базовий образ python 3.12 на основі якого створимо новий образ
FROM python:3.12

# Копіюємо файл entrypoint_command.py з локальної файлової системи (зліва) до контейнера,
# який буде створено. Шлях /entrypoint_command.py вказує, куди саме в контейнері хочемо скопіювати
COPY entrypoint_command.py /entrypoint_command.py

# Вказуємо команду, яка буде виконуватись при запуску контейнера створеного з образу.
# В даному випадку команда python3 вказує на виконання інтерпретатора Python версії 3,
# а /entrypoint_command.py вказує шлях до файлу в середині контейнера.
ENTRYPOINT ["python3", "/entrypoint_command.py"]