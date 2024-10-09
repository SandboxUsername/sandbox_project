from villain import Villain
from hero import Hero

def main():
    villains_name = input('Villain, what is your name? ')
    villain = Villain(villains_name, 30, 100)
    villain.introduce_itself()

    heros_name = input('Hero, what is your name? ')
    hero = Hero(heros_name, 50, 200)
    hero.introduce_itself()
    
    fighters = (hero, villain)
    active, passive = fighters
    round = 1

    while hero.health and villain.health:
        action = input(f'{active.name}, Attack (A) or Run (R)? ')
        if action == 'A':
            active.attack(passive)
        elif action == 'R':
            pass
        else:
            print('Wrong input, type either A or R!!')
        passive.inform_of_health()
        
        if passive.health <= 0:
            passive.dramatically_die()
            print(f'{active.name} won!!')
            break
        fighters = fighters[::-1]
        active, passive = fighters  # Swap turns
        round += 1

main()