class Pokemon:
    
    # Template dictionary for base stats
    base_stats_template = {
        "HP": 0,
        "Attack": 0,
        "Defense": 0,
        "Special Attack": 0,
        "Special Defense": 0,
        "Speed": 0
    }
    
    def __init__(self, name, base_stats, abilities):
        self.name = name
        self.base_stats = {stat: base_stats.get(stat, 0) for stat in self.base_stats_template}
        self.abilities = abilities
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Base Stats:")
        for stat, value in self.base_stats.items():
            positive_value = max(value, 0)
            print(f"{stat}: {positive_value}")
        print("Abilities:")
        for ability in self.abilities:
            print(ability)
        
        