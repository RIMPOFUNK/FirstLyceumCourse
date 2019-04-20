daily_food = []


def count_food(days):
    return sum([daily_food[i - 1] for i in days if i <= len(daily_food)])
