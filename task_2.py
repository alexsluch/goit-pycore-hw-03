import random

def get_numbers_ticket(min:int, max:int, quantity:int)->list:
    """
    Generate unique random lottery numbers within the specified range.

    Args:
        min: Minimum value (inclusive)
        max: Maximum value (inclusive)
        quantity: Number of unique numbers to generate

    Returns:
        List of unique random integers

    Raises:
        ValueError: If parameters are invalid
    """
    if min < 0 or max < 0:
        raise ValueError("min and max must be non-negative")

    if min >= max:
        raise ValueError("min must be less than max")

    if max > 1000:
        raise ValueError("max must be less than 1000")

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

        return list(unique_numbers)

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
