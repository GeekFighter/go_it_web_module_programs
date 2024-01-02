import logging

# створюємо форматтер "formatter": час виведення (asctime), ім'я модуля (name), рівень журналювання (levelname) та саме повідомлення (message)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# створюємо handler "ch" для виведення в консоль та встановлюємо рівень журналювання DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)  # додаємо форматтер до handler ch

# створюємо handler "fh" для виведення в файл (лог) та встановлюємо рівень журналювання ERROR
fh = logging.FileHandler("app.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)  # додаємо форматтер до handler fh

# створюємо логер "logger", даємо йому ім'я "simple_example" та встановлюємо рівень журналювання logging.DEBUG
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)  # додаємо handler ch до логера
logger.addHandler(fh)  # додаємо handler fh до логера

# приклад виконання коду
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
