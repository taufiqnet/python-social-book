#If we want to generate bank account number automatically.
#otherwise we can comment out the clean function with ValidationError

import random

available_numbers = [x for x in range(10)] # number 0 to 9
size = 26 # bank account number size : 26 digits


def generate_account_number():
    new_number_list = [str(random.choice(available_numbers)) for _ in range(size)]
    new_number_str ="".join(new_number_list)
    return new_number_str
