from interfaces import Being

class Villain(Being):
    type = 'Villain'
    def __init__(self, name: str, strenght: int, health: int):
        super().__init__(name, strenght, health)
        # weapon

    def attack(self, hero):
        print(f'I attack you, {hero.name}!')
        hero.health -= self.strenght
    

if __name__ == '__main__':
    jaime = Villain('Jaime', 30, 100)
    jaime.introduce_itself()