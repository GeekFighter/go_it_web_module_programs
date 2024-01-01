import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",  # Встановлення формату повідомлення
    level=logging.DEBUG,  # Встановлення рівня журналювання
    handlers=[
        logging.FileHandler("program.log"),  # Обробник для запису у файл "program.log"
        logging.StreamHandler(),  # Обробник для виведення в консоль
    ],
)

logging.warning("An example message.")  # Виведення повідомлення рівня WARNING
logging.warning("Another message")  # Виведення ще одного повідомлення рівня WARNING
