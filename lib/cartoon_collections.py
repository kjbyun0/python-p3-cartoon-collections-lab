def roll_call_dwarves(l):
    for index, name in enumerate(l):
        print(f'{index+1}. {name}')

def summon_captain_planet(l):
    return [f'{item.title()}!' for item in l]

def long_planeteer_calls(l):
    for item in l:
        if (len(item) > 4):
            return True
    return False

def find_the_cheese(l):
    for item in l:
        if item in ['cheddar', 'gouda', 'camembert']:
            return item
    return None
    
