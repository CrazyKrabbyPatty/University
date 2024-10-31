import random

def generate_random_doors():
    doors = [0, 0, 0]
    doors[random.randint(0, 2)] = 1
    return doors

def monty_hall(iterations):
    iter = 0
    dict_iter = {}
    choices = ['Yes', 'No']

    while iter != iterations:

        doors_list = generate_random_doors
        user_choice = random.randit(0,2)

        