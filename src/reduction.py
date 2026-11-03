def full_reduction(amount):
    """满减：满 200 减 25，满 100 减 10，否则不减。"""
    if amount < 0:
        return 0
    if amount >= 200:
        return 25
    if amount >= 100:
        return 10
    return 0
