from datetime import datetime

def get_days_from_today(date):
    try:
        date_in_datetime = datetime.strptime(date, '%Y-%m-%d').date()           # Перетворюємо рядок в об'єкт datetime і віднімаємо його від теперішнього часу
        date_now = datetime.today().date()
        result_in_datetime = date_in_datetime - date_now
        return result_in_datetime.days
    except ValueError:
        print(f"Wrong format, {date} is not YYYY-MM-DD")                                        # При не правильному вводі дати просимо користувача,
        return get_days_from_today(input("Please enter again date in format YYYY-MM-DD  "))     #  ввести дату в правильному форматі ще раз.


result = get_days_from_today(f"{input("Enter date in format YYYY-MM-DD  ")}")   # Просимо користувача ввести дату, одразу в функцію
print(result)
