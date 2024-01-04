import requests

# Виконати GET-запит до API ПриватБанку
response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')

# Перевірити, чи успішно виконаний запит
if response.status_code == 200:
    # Отримати дані з відповіді у форматі JSON
    data = response.json()

    # Перебрати курси валют і вивести їх у командному рядку
    for currency in data:
        print(f"{currency['ccy']}: {currency['buy']} - {currency['sale']}")
else:
    # Якщо запит не успішний, вивести повідомлення про помилку
    print(f"Помилка запиту: {response.status_code}")