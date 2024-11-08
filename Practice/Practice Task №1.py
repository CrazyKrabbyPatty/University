import random

def generate_random_doors():
  doors = [0, 0, 0]
  doors[random.randint(0, 2)] = 1
  return doors

def monty_hall(iterations):
  
  attempts = 0
  results = {}
  choices = ['Yes', 'No']

  while attempts != iterations:
      
    doors_list = generate_random_doors()
    user_choice = random.randint(0, 2)

    if doors_list[user_choice] == 1:
        
      if random.choice(choices) == "Yes":
        results['LostByChanging'] = results.get('LostByChanging', 0) + 1
      else:
        results['WonByStaying'] = results.get('WonByStaying', 0) + 1

    else:
        
      if random.choice(choices) == "No":
        results['LostByStaying'] = results.get('LostByStaying', 0) + 1
      else:
        del doors_list[user_choice]

        if random.choice(doors_list) == 1:
          results['WonByChanging'] = results.get('WonByChanging', 0) + 1
        else:
          results['LostByChanging'] = results.get("LostByChanging", 0) + 1

    attempts += 1

    ChangingAttempts = results.get('WonByChanging', 0) + results.get('LostByChanging', 0)
    StayingAttempts = results.get('WonByStaying', 0) + results.get('LostByStaying', 0)

    ChancesChanging = results.get('WonByChanging', 0) / ChangingAttempts
    ChancesStaying = results.get('WonByStaying', 0) / StayingAttempts

    output = [
        f'Вероятность выйгрыша при смене двери: {ChancesChanging}'
        f'Вероятность выигрыша без смены двери: {ChancesStaying}'
    ]

    print(*output)

monty_hall(1000)