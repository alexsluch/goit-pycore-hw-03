from datetime import date, datetime

def get_days_from_today(date_string: str) -> int | ValueError:
    """
    Calculate the number of days between today and the given date.

    Args:
        date_string: Date in format YYYY-MM-DD

    Returns:
        Number of days (positive if date in past, negative if in future).
    """

    today = date.today()

    try:
        target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("Некоректна дата: очікується формат YYYY-MM-DD та валідні значення дня/місяця/року")
    delta = today - target_date
    return delta.days


if __name__ == "__main__":
    print(get_days_from_today("2026-10-09"))