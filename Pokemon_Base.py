class Pokemon:
    base_stats_template = {
        "HP": 0,
        "Attack": 0,
        "Defense": 0,
        "Special Attack": 0,
        "Special Defense": 0,
        "Speed": 0
    }

    def __init__(self, name, base_stats, abilities, types):
        self.name = name
        self.base_stats = {stat: base_stats.get(stat, 0) for stat in self.base_stats_template}
        self.abilities = abilities
        self.types = types

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Base Stats:")
        for stat, value in self.base_stats.items():
            positive_value = max(value, 0)
            print(f"{stat}: {positive_value}")
        print(f"Types: {', '.join(self.types)}")
        print("Abilities:")
        for ability in self.abilities:
            print(ability)

    def get_offense_multiplier(self, opponent_types):
        multiplier = 1
        for my_type in self.types:
            multiplier *= my_type.get_offense_multiplier(opponent_types)
        return multiplier

    def get_defense_multiplier(self, opponent_types):
        multiplier = 1
        for my_type in self.types:
            multiplier *= my_type.get_defense_multiplier(opponent_types)
        return multiplier
