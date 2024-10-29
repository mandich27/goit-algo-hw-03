import random

def get_numbers_ticket(min, max, quantity):
    try:
        if not (1 <= min <= 1000) or not (1 <= max <= 1000) or min >= max:   # Закладаєм перевірку по умові завдання, що діапазон не може бути менший 1 і більше 1000
            raise ValueError
        range_lottery = range(min, max + 1)                                  # до верхньої межі діапазону додаємо 1, бо метод range не включає друге число діапазону
        lottery_numbers = random.sample(range_lottery, quantity)
        lottery_numbers.sort()                                               # Сортуємо отримані лотерейні числа
        return lottery_numbers
    except (ValueError, NameError, AttributeError, TypeError, SyntaxError):  # Можливі винятки
        return []                                                            # Якщо введені дані не відповідають вимогам виводиться пустий список як вказано в завданні

lottery_numbers = get_numbers_ticket(1, 1000, 10)                            # Передаємо в функцію діапазон рандомних чисел від (1 до 1000 )і кількість унікальних чисел яку потрібно обрати

print("Ваші лотерейні числа:", lottery_numbers)
