# --- TASK 1 ---
def get_days_from_today(date_string):

    from datetime import date, datetime

    try:
        today = date.today()
        target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        delta = today - target_date
        return delta.days
    except ValueError:
        return "wrong date format"

print(get_days_from_today("2026-10-09"))


# --- TASK 2 ---
def get_numbers_ticket(min, max, quantity):

    import random

    if min < 0 or max < 0:
        raise ValueError("min and max must be non-negative")

    if min >= max:
        raise ValueError("min must be less than max")

    if quantity <= 0:
        raise ValueError("quantity must be greater than 0")

    # increase max by 1 to make sure it's included in the range
    if quantity > max - min + 1:
        raise ValueError("quantity must be less than or equal to max - min")

    if random.randint(0, 1) == 0: # God of Randomness ;D
        return random.sample(range(min, max + 1), quantity)
    else:
        unique_numbers = set()

        while len(unique_numbers) < quantity:
            unique_numbers.add(random.randint(min, max))

        return unique_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


# --- TASK 3 ---
def normalize_phone(phone):

    import re

    phone = re.sub(r"\D", "", phone)
    return "+" + phone if phone.startswith("38") else "+38" + phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# --- TASK 4 ---
def get_upcoming_birthdays(users):

    from datetime import datetime

    today = datetime.today().date()
    today_in_next_year = today.replace(year=today.year + 1)

    print(today,today.weekday())

    for user in users:
        name = user.get("name")
        birthday = datetime.strptime(user.get("birthday"), "%Y.%m.%d").date()

        print(birthday,birthday.day)


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)