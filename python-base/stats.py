def max(numbers: list):
    x = numbers[0]
    for num in numbers:
        if num > x:
            x = num
    return x


def min(numbers: list):
    x = numbers[0]
    for num in numbers:
        if num < x:
            x = num
    return x


def avg(numbers: list):
    if len(numbers) > 0:
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
    else:
        return None
