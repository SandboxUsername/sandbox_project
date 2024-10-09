from interfaces import Being

class Hero(Being):
    type = 'Hero'
    def __init__(self, name: str, strenght: int, health: int):
        super().__init__(name, strenght, health)
        # weapon
    
    def attack(self, villain):
        print(f'I attack you, {villain.name}!')
        villain.health -= self.strenght


if __name__ == '__main__':
    cesar = Hero('Cesar', 50, 200)
    cesar.introduce_itself()