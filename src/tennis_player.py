from enum import Enum

Sex = Enum('Sex', 'Female Male')


class tennis_player:
    def __init__(self, name: str, sex: Sex, ability: int, luck: int):
        self.name = name
        self.sex = sex
        self.ability = ability
        self.luck = luck

    def __str__(self) -> str:
        return f'{self.name} {self.sex} {self.ability} {self.luck}'


class male_tennis_player(tennis_player):
    def __init__(self, name: str, sex: Sex, ability: int, luck: int, strength: int, velocity: int):
        super().__init__(name, sex, ability, luck)
        self.strength = strength
        self.velocity = velocity

    def __str__(self) -> str:
        return super().__str__() + f' {self.strength} {self.velocity}'


class female_tennis_player(tennis_player):
    def __init__(self, name: str, sex: Sex, ability: int, luck: int, reaction_time: float):
        super().__init__(name, sex, ability, luck)
        self.reaction_time = reaction_time

    def __str__(self) -> str:
        return super().__str__() + f' ${self.reaction_time}'