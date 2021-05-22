import random


def generate_random_bits(n):
    return [str(random.randint(0, 1)) for _ in range(n)]


def list_to_str(l):
    if isinstance(l, str):
        return l
    return "".join(l)


def str_to_list(s):
    if isinstance(s, list):
        return s
    return [c for c in s]


def interfere_data(data, n):
    if isinstance(data, str):
        data = str_to_list(data)
    random_bits = random.sample(range(len(data)), n)
    for bit in random_bits:
        data[bit] = str(int(not int(data[bit])))
    return data


def count_errors(l1, l2):
    if len(l1) != len(l2):
        return -1
    errors = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            errors += 1
    return errors
