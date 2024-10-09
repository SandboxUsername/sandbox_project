from abc import ABC

class Being(ABC):
    type = None
    def __init__(self, name: str, strenght: int, health: int):
        print('I am alive!')
        self.name = name
        self.strenght = strenght
        self.health = health

    def introduce_itself(self):
        print(f'My name is {self.name}, my strenght is {self.strenght} and my health is {self.health}.')
    
    def attack():
        pass

    def dramatically_die(self):
        print(f'I, {self.name}, dramatically die, and my enemy wins!')
    
    def inform_of_health(self):
        print(f"{self.type}'s health is {self.health}.")