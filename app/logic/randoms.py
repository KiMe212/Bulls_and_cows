import random


def random_number() -> list:
    list_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    number = random.sample(list_num, k=4)
    return number
