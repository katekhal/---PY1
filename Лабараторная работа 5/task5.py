from random import sample
def get_random_password() -> str:
    values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spis = ''.join(sample(values, 8))
    return spis
print(get_random_password())
