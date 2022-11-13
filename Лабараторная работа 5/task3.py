from random import randint
def get_unique_list_numbers() -> list[int]:
    spis = []
    while len(spis) < 16:
        k = randint(-10, 10)
        if k not in spis:
            spis.append(k)
    return spis
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
