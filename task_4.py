from datetime import datetime, timedelta

def get_upcoming_birthdays(users : list) -> list:
    """
    Get list of users with birthdays in the next 7 days for congratulations.
    Weekends (Sat/Sun) are moved to Monday.

    Args:
        users: List of dicts with "name" and "birthday" (YYYY.MM.DD).

    Returns:
        List of dicts with "name" and "congratulation_date".
    """
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

if __name__ == "__main__":

    users = [
        {"name": "John Doe", "birthday": "1985.02.01"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)