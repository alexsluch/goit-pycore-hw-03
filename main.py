# --- TASK 1 ---
from datetime import timedelta


def get_days_from_today(date_string):

    from datetime import date, datetime

    try:
        today = date.today()
        target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        delta = today - target_date
        return delta.days
    except ValueError:
        return "wrong date format"

print("\nTASK #1")
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
print("\nTASK #2")
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

print("\nTASK #3")
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# --- TASK 4 ---
def get_upcoming_birthdays(users):

    from datetime import datetime

    today = datetime.today().date()

    result = []

    for user in users:

        birthday = datetime.strptime(user.get("birthday"), "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:

            congratulation_date = birthday_this_year

            match congratulation_date.weekday():
                case 5:
                    congratulation_date += timedelta(days=2)
                case 6:
                    congratulation_date += timedelta(days=1)


            result.append({
                "name": user.get("name"),
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


users = [
    {"name": "John Doe", "birthday": "1985.02.01"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)

print("\nTASK #4")
print("Список привітань на цьому тижні:", upcoming_birthdays)